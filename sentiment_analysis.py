import os

from models.char_base_cnn import CharCNNTextClassifier, cnn_predict
from train import Instructor

def SentimentAnalysis(param, text):
    if param['model'] == 'cnn':
        out = cnn_predict(text)
        return out
    else:
        ins = Instructor(model_name = param['model'])
        out = ins.run(text)
        return out
        
        