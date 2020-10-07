import math
import os
import sys
from time import strftime, localtime
import random
import numpy

from sklearn import metrics
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split

from data_utils import build_tokenizer, build_embedding_matrix, Tokenizer4Bert, ABSADataset

from models import CharCNNTextClassifier, DynamicLSTM, LSTM

class SentimentAnalysis:
    def __init__(self, param, text):
