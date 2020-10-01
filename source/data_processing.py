import os
import json

from torchtext.data import *
from torchtext.vocab import Vocab, FastText
from underthesea import sent_tokenize

def load_data(train_file, test_file):
    