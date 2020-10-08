import os

from models.char_base_cnn import CharCNNTextClassifier, cnn_predict
from train import Instructor

def SentimentAnalysis(param, text):
    if param['model'] == 'cnn':
        cnn_predict(text)
    else:
        ins = Instructor(model_name = param['model'])
        ins.run()
        
        