from sentiment_analysis import SentimentAnalysis as sa


param = {'model' : 'lstm',
         'textprocessor' : 'word',
         'activation' : 'linear',
         'loss' : 'crossEntropy'}
         
text = 'phim hay vcl'
sa(param, text)