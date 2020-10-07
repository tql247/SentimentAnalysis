import torch
from torch import nn
import time
import torchtext

from collections import defaultdict

import matplotlib.pyplot as plt

plt.style.use('seaborn')

class CharCNNTextClassifier(nn.Module):
    def __init__(self, text_field, class_field):
        super().__init__()
        self.voc_size = len(text_field.vocab)
        n_classes = len(class_field.vocab)
        
        n_channels = 256
        dropout_prob = 0.5
        fc_size = 1024
        
        # The model by Zhang et al. is applied to one-hot encoded characters. Character-based
        # models that have been proposed more recently have used an embedding layer to represent
        # the characters, but we'll just stick with the one-hot encoding here.
        
        # We first define the stack of convolutional and pooling layers, following the
        # description by Zhang exactly.
        # We use a Sequential, which is a container for objects of the type nn.Module.
        # They will be applied serially, where the output of one step will be fed as the
        # input to the next step in the sequence.
        self.conv_stack = nn.Sequential(
            nn.Conv1d(in_channels=self.voc_size, out_channels=n_channels, kernel_size=7),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3),
            nn.Conv1d(in_channels=n_channels, out_channels=n_channels, kernel_size=7),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3),
            nn.Conv1d(in_channels=n_channels, out_channels=n_channels, kernel_size=3),
            nn.ReLU(),
            nn.Conv1d(in_channels=n_channels, out_channels=n_channels, kernel_size=3),
            nn.ReLU(),
            nn.Conv1d(in_channels=n_channels, out_channels=n_channels, kernel_size=3),
            nn.ReLU(),
            nn.Conv1d(in_channels=n_channels, out_channels=n_channels, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=3),
        )
        
        # We define another Sequential stack for the fully connected (fc) part of the network.        
        # The size of the input will be 256*34 = 8704 because of the structure of the conv_stack
        # network, and because the input to conv_stack has a fixed size of 1014 characters.        
        n_in = 256*34
        self.fc = nn.Sequential(
            nn.Linear(in_features=n_in, out_features=fc_size),
            nn.ReLU(),
            nn.Dropout(dropout_prob),
            nn.Linear(in_features=fc_size, out_features=fc_size),
            nn.ReLU(),
            nn.Dropout(dropout_prob),
            nn.Linear(in_features=fc_size, out_features=n_classes)
        )
        
        
    def onehot_encode(self, texts):
        # A helper function to do the one-hot encoding of characters.
        sen_len, batch_size = texts.shape
        out = torch.zeros(size=(sen_len, batch_size, self.voc_size), device=texts.device)
        out.scatter_(2, texts.view(sen_len, batch_size, 1), 1)
        return out.permute(1, 2, 0)
        
        
    def forward(self, texts):
        # One-hot-encode the sequences of characters.
        onehot = self.onehot_encode(texts)

        # Apply the convolution stack. Because the size of the input is fixed to 1014 characters,
        # and because we set the number of output channels to 256, 
        # the shape will now be (batch size, 256, 34)
        conv = self.conv_stack(onehot)

        # We view the result as a tensor of shape (batch_size, 256*34)
        # so that it fits the input shape of the fully connected layer.
        conv = conv.view(conv.shape[0], -1)

        # Finally apply the fully connected layer, and then return the output.
        scores = self.fc(conv)
        return scores

def read_data(corpus_file, datafields, label_column, doc_start):
    with open(corpus_file, encoding='utf-8') as f:
        examples = []
        for line in f:
            columns = line.strip().split(',')
            doc = columns[1]      
            label = columns[-1]
            examples.append(torchtext.data.Example.fromlist([doc, label], datafields))
    return torchtext.data.Dataset(examples, datafields)
    
def evaluate_validation(scores, loss_function, gold):
    guesses = scores.argmax(dim=1)
    n_correct = (guesses == gold).sum().item()
    return n_correct, loss_function(scores, gold).item()

def main():
    # NOTE that the tokenization is done differently here compared to the previous examples.
    # The output of this tokenization will be a sequence of 1014 characters.
    TEXT = torchtext.data.Field(sequential=True, tokenize=list, fix_length=1014)
    LABEL = torchtext.data.LabelField(is_target=True)
    datafields = [('text', TEXT), ('label', LABEL)]
    
    data = read_data('Preprocess/clear.csv', datafields, label_column=1, doc_start=3)
    train, valid = data.split([0.85, 0.15])

        
    TEXT.build_vocab(train, max_size=10000)
    LABEL.build_vocab(train)
    
    model = CharCNNTextClassifier(TEXT, LABEL)

    device = 'cuda'
    model.to(device)
    
    train_iterator = torchtext.data.BucketIterator(
        train,
        device=device,
        batch_size=128,
        sort_key=lambda x: len(x.text),
        repeat=False,
        train=True)
    
    valid_iterator = torchtext.data.Iterator(
        valid,
        device=device,
        batch_size=128,
        repeat=False,
        train=False,
        sort=False)

    loss_function = torch.nn.CrossEntropyLoss()
    learning_rate = 0.0005
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    print(f'Setting the learning rate to {learning_rate}.')
    
    train_batches = list(train_iterator)
    valid_batches = list(valid_iterator)
    
    history = defaultdict(list)
    
    for i in range(1, 31):
        
        t0 = time.time()
        
        loss_sum = 0
        n_batches = 0

        model.train()
        
        for batch in train_batches:
            scores = model(batch.text)
            loss = loss_function(scores, batch.label)

            optimizer.zero_grad()            
            loss.backward()
            optimizer.step()
    
            loss_sum += loss.item()
            n_batches += 1
        
        train_loss = loss_sum / n_batches
        history['train_loss'].append(train_loss)
        
        n_correct = 0
        n_valid = len(valid)
        loss_sum = 0
        n_batches = 0

        model.eval()
        
        for batch in valid_batches:
            scores = model(batch.text)
            n_corr_batch, loss_batch = evaluate_validation(scores, loss_function, batch.label)
            loss_sum += loss_batch
            n_correct += n_corr_batch
            n_batches += 1
        val_acc = n_correct / n_valid
        val_loss = loss_sum / n_batches

        history['val_loss'].append(val_loss)
        history['val_acc'].append(val_acc)        
        
        t1 = time.time()
        print(f'Epoch {i}: train loss = {train_loss:.4f}, val loss = {val_loss:.4f}, val acc: {val_acc:.4f}, time = {t1-t0:.4f}')

        if i % 5 == 0:
            learning_rate *= 0.5
            print(f'Setting the learning rate to {learning_rate}.')
            for g in optimizer.param_groups:
                g['lr'] = learning_rate            
            
    plt.plot(history['train_loss'])
    plt.plot(history['val_loss'])
    plt.plot(history['val_acc'])
    plt.legend(['training loss', 'validation loss', 'validation accuracy'])
    plt.savefig('cnn.png')
    
    
main()
