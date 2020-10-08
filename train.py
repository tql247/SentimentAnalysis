import math
import os
import sys
from time import strftime, localtime
import random
import numpy
import logging


from sklearn import metrics
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split

from data_utils import build_tokenizer, build_embedding_matrix, SADataset

from models.lstm import LSTM
from models.rnn import RNN
from models.char_base_cnn import CharCNNTextClassifier
from models.dynamic_lstm import DynamicLSTM

from collections import defaultdict
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))




class Instructor:
    def __init__(self, model_name='lstm', dataset='train', optimizer='adam',initializer='xavier_uniform_',
                learning_rate=2e-5, dropout=0.1, l2reg=0.01, num_epoch=10, batch_size=16, log_step=5, embed_dim=300,
                hidden_dim=300, max_seq_len=80, polarities_dim=3, device=None, valset_ratio=0):
        self.model_name = model_name
        self.dataset = dataset
        self.optimizer = optimizer
        self.initializer = initializer
        self.learning_rate = learning_rate
        self.dropout = dropout
        self.l2reg = l2reg
        self.num_epoch = num_epoch
        self.batch_size = batch_size
        self.log_step = log_step
        self.embed_dim = embed_dim
        self.hidden_dim = hidden_dim
        self.max_seq_len = max_seq_len
        self.polarities_dim = polarities_dim
        self.device = device
        self.valset_ratio = valset_ratio
       
        log_file = '{}-{}-{}.log'.format(self.model_name, self.dataset, strftime("%y%m%d-%H%M", localtime()))
        logger.addHandler(logging.FileHandler(log_file))
        
        model_classes = {
            'lstm': LSTM,
            'rnn' : RNN
        }
        dataset_files = {
            'train': {
                'train': './Preprocess/train.csv',
                'test': './Preprocess/test.csv'
            }
        }
        input_colses = {
            'lstm': ['text_raw_indices'],
            'rnn': ['text_raw_indices']
        }
        initializers = {
            'xavier_uniform_': torch.nn.init.xavier_uniform_,
            'xavier_normal_': torch.nn.init.xavier_normal,
            'orthogonal_': torch.nn.init.orthogonal_,
        }
        optimizers = {
            'adadelta': torch.optim.Adadelta,  # default lr=1.0
            'adagrad': torch.optim.Adagrad,  # default lr=0.01
            'adam': torch.optim.Adam,  # default lr=0.001
            'adamax': torch.optim.Adamax,  # default lr=0.002
            'asgd': torch.optim.ASGD,  # default lr=0.01
            'rmsprop': torch.optim.RMSprop,  # default lr=0.01
            'sgd': torch.optim.SGD,
        }

        
        
        self.model_class = model_classes[self.model_name]
        self.dataset_file = dataset_files[self.dataset]
        self.inputs_cols = input_colses[self.model_name]
        self.initializer = initializers[self.initializer]
        self.optimizer = optimizers[self.optimizer]
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') \
            if self.device is None else torch.device(self.device)
        
        
        
        tokenizer = build_tokenizer(
            fnames=[self.dataset_file['train'], self.dataset_file['test']],
            max_seq_len=self.max_seq_len,
            dat_fname='{0}_tokenizer.dat'.format(self.dataset))
        embedding_matrix = build_embedding_matrix(
            word2idx=tokenizer.word2idx,
            embed_dim=self.embed_dim,
            dat_fname='{0}_{1}_embedding_matrix.dat'.format(str(self.embed_dim), self.dataset))
        self.model = self.model_class(embedding_matrix, self).to(self.device)

        self.trainset = SADataset(self.dataset_file['train'], tokenizer)
        self.testset = SADataset(self.dataset_file['test'], tokenizer)
        assert 0 <= self.valset_ratio < 1
        if self.valset_ratio > 0:
            valset_len = int(len(self.trainset) * self.valset_ratio)
            self.trainset, self.valset = random_split(self.trainset, (len(self.trainset) - valset_len, valset_len))
        else:
            self.valset = self.testset
        logger.info('Model selected: {}'.format(self.model_name))
        if self.device.type == 'cuda':
            logger.info('cuda memory allocated: {}'.format(torch.cuda.memory_allocated(device=self.device.index)))

    # def predict(self, text):
        # predict = self.model(
    def _train(self, criterion, optimizer, train_data_loader, val_data_loader):
        max_val_acc = 0
        max_val_f1 = 0
        global_step = 0
        path = None
        history = defaultdict(list)
        for epoch in range(self.num_epoch):
            #logger.info('>' * 100)
            logger.info('epoch: {}'.format(epoch))
            n_correct, n_total, loss_total = 0, 0, 0
            # switch model to training mode
            self.model.train()
            for i_batch, sample_batched in enumerate(train_data_loader):
                global_step += 1
                # clear gradient accumulators
                optimizer.zero_grad()

                inputs = [sample_batched[col].to(self.device) for col in self.inputs_cols]
                outputs = self.model(inputs)
                targets = sample_batched['polarity'].to(self.device)

                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()

                n_correct += (torch.argmax(outputs, -1) == targets).sum().item()
                n_total += len(outputs)
                loss_total += loss.item() * len(outputs)
                if global_step % self.log_step == 0:
                    train_acc = n_correct / n_total
                    train_loss = loss_total / n_total
            logger.info('loss: {:.4f}, acc: {:.4f}'.format(train_loss, train_acc))
            
            history['train_loss'].append(train_loss)
            history['train_acc'].append(train_acc)

            val_acc, val_f1 = self._evaluate_acc_f1(val_data_loader)
            history['val_acc'].append(val_acc)
            history['val_f1'].append(val_f1)
            logger.info('> val_acc: {:.4f}, val_f1: {:.4f}'.format(val_acc, val_f1))
            if val_acc > max_val_acc:
                max_val_acc = val_acc
                if not os.path.exists('state_dict'):
                    os.mkdir('state_dict')
                path = 'state_dict/{0}_{1}_val_acc{2}'.format(self.model_name, self.dataset, round(val_acc, 4))
                torch.save(self.model.state_dict(), path)
                logger.info('>> saved: {}'.format(path))
            if val_f1 > max_val_f1:
                max_val_f1 = val_f1
        plt.plot(history['train_loss'])
        plt.plot(history['train_acc'])
        plt.plot(history['val_acc'])
        plt.plot(history['val_f1'])
        plt.legend(['training loss', 'training accuracy', 'validation accuracy', 'validation f1'])
        plt.savefig('lstm.png')
        return path

    def _reset_params(self):
        for child in self.model.children():
            for p in child.parameters():
                if p.requires_grad:
                    if len(p.shape) > 1:
                        self.initializer(p)
                    else:
                        stdv = 1. / math.sqrt(p.shape[0])
                        torch.nn.init.uniform_(p, a=-stdv, b=stdv)

    def _evaluate_acc_f1(self, data_loader):
        n_correct, n_total = 0, 0
        t_targets_all, t_outputs_all = None, None
        # switch model to evaluation mode
        history = defaultdict(list)
        self.model.eval()
        with torch.no_grad():
            for t_batch, t_sample_batched in enumerate(data_loader):
                t_inputs = [t_sample_batched[col].to(self.device) for col in self.inputs_cols]
                t_targets = t_sample_batched['polarity'].to(self.device)
                t_outputs = self.model(t_inputs)

                n_correct += (torch.argmax(t_outputs, -1) == t_targets).sum().item()
                n_total += len(t_outputs)

                if t_targets_all is None:
                    t_targets_all = t_targets
                    t_outputs_all = t_outputs
                else:
                    t_targets_all = torch.cat((t_targets_all, t_targets), dim=0)
                    t_outputs_all = torch.cat((t_outputs_all, t_outputs), dim=0)

        acc = n_correct / n_total
        f1 = metrics.f1_score(t_targets_all.cpu(), torch.argmax(t_outputs_all, -1).cpu(), labels=[0, 1, 2],
                              average='macro')
        return acc, f1

    def run(self):
        # Loss and Optimizer
        criterion = nn.CrossEntropyLoss()
        _params = filter(lambda p: p.requires_grad, self.model.parameters())
        optimizer = self.optimizer(_params, lr=self.learning_rate, weight_decay=self.l2reg)

        train_data_loader = DataLoader(dataset=self.trainset, batch_size=self.batch_size, shuffle=True)
        test_data_loader = DataLoader(dataset=self.testset, batch_size=self.batch_size, shuffle=False)
        val_data_loader = DataLoader(dataset=self.valset, batch_size=self.batch_size, shuffle=False)

        self._reset_params()
        best_model_path = self._train(criterion, optimizer, train_data_loader, val_data_loader)
        self.model.load_state_dict(torch.load(best_model_path))
        self.model.eval()
        test_acc, test_f1 = self._evaluate_acc_f1(test_data_loader)
        logger.info('>> test_acc: {:.4f}, test_f1: {:.4f}'.format(test_acc, test_f1))    

# def main():
    # # Hyper Parameters
    # ins = Instructor(model_name='rnn')
    # ins.run()


# if __name__ == '__main__':
    # main()
