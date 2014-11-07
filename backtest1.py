from pandas import *
from numpy import *
import numpy as np
import pandas as pd
import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
randn=np.random.randn
import pandas.stats.interface as sm
from scipy import stats

def aggregate(sym1="C",sym2="BAC",\
              start=datetime.datetime(2010,1,1),\
              end=datetime.datetime(2014,9,30)):
    stocks=[sym1,sym2]
    builder=web.DataReader(sym1,'yahoo',start,end).index
    mainFrame=DataFrame(np.zeros((len(builder),2)),index=builder,columns=stocks)

    for stock in stocks:
        mainFrame[stock]=web.DataReader(stock,'yahoo',start,end)['Adj Close']

    return(mainFrame)

def percentage(sym1="C",sym2="BAC",frame=aggregate()):
    frame1=frame.pct_change()
    frame1=frame1.dropna()
    return frame1

def rolling_OLS(sym1="C",sym2="BAC",\
                Frame=percentage(aggregate(sym1='C',sym2='BAC')),\
                avg=10):
    a=Frame
    print(len(a))
    a['roll_Beta']=0
    a['rolling_r2']=0
    
    
    for i in range(len(a)-avg+1):  
        x=a.iloc[i:i+avg-1][sym1] #extraction d'une sous matrice
        y=a.iloc[i:i+avg-1][sym2]
        a.iloc[i+avg-1,2]=stats.linregress(x,y)[0]
        a.iloc[i+avg-1,3]=stats.linregress(x,y)[2]

    a=a[avg:]

    a['Beta_hedged '+sym1]=a[sym1]-a['roll_Beta']*a[sym2]
    a['ZScore']=(a['Beta_hedged '+ sym1]-\
                 np.mean(a['Beta_hedged '+ sym1]))/\
                 np.std(a['Beta_hedged '+ sym1])
    print(np.mean(a['Beta_hedged '+ sym1]))
    print(np.std(a['Beta_hedged '+ sym1]))               

    return a

def mineyours(sym1='C',sym2='BAC',avg=10):
    Frame=rolling_OLS(sym1,sym2)
    Frame['Mine']=Frame['ZScore']<=-1.5
    Frame['Yours']=Frame['ZScore']>=1.5
    Frame['PNL']=Frame['Mine']*Frame['Beta_hedged '+ sym1].shift(-1)-\
                  Frame['Yours']*Frame['Beta_hedged '+ sym1].shift(-1)
    Frame['Cumul. PNL']=cumsum(Frame['PNL'])
    Frame['test']=Frame['Mine']==1
    return Frame,mean(Frame['PNL']),std(Frame['PNL']),mean(Frame['PNL'])/std(Frame['PNL'])


Frame=mineyours()
print(Frame)






