import pandas as pd
from scikit_learn import preprocessing
from scikit_learn.model_selection import train_test_split


hp = pd.read_csv('housepricedata.csv')

dataset = df.values
x - dataset[:, 0:10] # rows and cols of array
Y = dataset[:, 10] 

#scaling
min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)

#weighting of variables
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3) #30% of overall dataset
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size = 0.5)
