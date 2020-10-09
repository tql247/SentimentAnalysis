from sentiment_analysis import SentimentAnalysis as sa

param = {'model' : 'cnn',
         'textprocessor' : 'character',
         'activation' : 'linear',
         'loss' : 'crossEntropy'}
         
text = ['tệ']
out = sa(param, text)
#{'Positive': 0, 'Negative': 1, 'Normal': 2}
if out == 0:
    print("Text: {}".format(text[0]))
    print("Predict: Positive")
if out == 1:
    print("Text: {}".format(text[0]))
    print("Predict: Negative")
if out == 2:
    print("Text: {}".format(text[0]))
    print("Predict: Normal")
