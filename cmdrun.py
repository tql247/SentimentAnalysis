from sentiment_analysis import SentimentAnalysis as sa

param = {'model' : 'lstm',
         'textprocessor' : 'character',
         'activation' : 'linear',
         'loss' : 'crossEntropy'}
         
text = ['chưa mua nhưng nhân viên bên tgdđ tư vấn làm mình hoang mang quá họ nói đồng hồ này có thể đo huyết áp nhưng phải vơi samsung s9 đúng k mọi người']
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
