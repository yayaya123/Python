#import several closes

from pandas import *
from numpy import *
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
randn=np.random.randn
#path='/Users/Yann/Desktop/Python/DB/Bikes.csv'
import pandas as pd
import pandas.io.data as web
import datetime


#Import d'AAPL

start=datetime.datetime(2014,1,1)
end=datetime.datetime(2014,9,29)

liste=["AAPL","YHOO","MSFT","C","GOOG"] # liste de tickers
First=web.DataReader('AAPL','yahoo',start,end) #recuperation d'une serie pour avoir les index etc

DF=DataFrame(np.zeros((len(First.index),len(liste))),index=First.index,columns=liste)
  # crétaion d'une dataFrame vide

for elements in liste:  #remplissage avec les données du WEB
    df=web.DataReader(elements,'yahoo',start,end)['Adj Close']
    DF[elements]=df

print(DF)

#DF["bille"]=5

#print(DF.loc['2014-03-12':])
#DF.plot()
#plt.show()
DF_rets1=DF/DF.shift()-1
DF_returns=DF.pct_change()
print(DF_rets1)
print(DF_returns)
corr=DF_returns.corr()
print(corr)

#fonction movingaverage


def movingaverage(NbDays):
    DFMA=DF
    for i in range(NbDays):
        DFMA+=DF.shift(1)
    return DFMA/NbDays
    
    
