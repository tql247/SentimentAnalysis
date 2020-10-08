import pandas as pd 

data = pd.read_csv("./clear.csv") 
from sklearn.model_selection import train_test_split
train, test = train_test_split(data, test_size=0.2)

train.to_csv('./train.csv', index=False, columns = ['Comment', 'Rating'])
test.to_csv('./test.csv', index=False, columns = ['Comment', 'Rating'])