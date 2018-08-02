import quandl
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, svm

df = quandl.get("WIKI/AMZN")

#print(df.tail())
df = df[['Adj. Close']]
forecast_out = int(30)
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
print(df.tail())
