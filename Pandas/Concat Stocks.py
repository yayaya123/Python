#import several closes

from pandas import *
from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
randn=np.random.randn
import pandas as pd
import pandas.io.data as web
import datetime


#Import d'AAPL

start=datetime.datetime(2014,1,1)
end=datetime.datetime(2014,9,29)

liste=["AAPL","YHOO"]# liste de tickers
First=web.DataReader('AAPL','yahoo',start,end) #recuperation d'une serie pour avoir les index etc

DF=DataFrame(np.zeros((len(First.index),0)),index=First.index)
  # crétaion d'une dataFrame vide avec 
  #uniquement l'index et pas de colonne

print(DF)

for elements in liste:  #remplissage avec les données du WEB
    df=web.DataReader(elements,'yahoo',start,end)['Adj Close']
    df1=df.pct_change()
    DF[elements]=df
    DF[elements+ '(%)']=df1

print(DF)
DF=DF.fillna(value=0)
print(DF)
DF=asarray(DF)
print(DF)
