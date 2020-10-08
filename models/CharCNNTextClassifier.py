import torch
from torch import nn
import time
import torchtext

from collections import defaultdict

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
        n_in = 256 * 34
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
