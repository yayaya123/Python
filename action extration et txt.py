#import several cpacks

from pandas import *
from numpy import *
import numpy as np
randn=np.random.randn
#path='/Users/Yann/Desktop/Python/DB/Bikes.csv'
import pandas as pd
import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt


#Import d'AAPL

start=datetime.datetime(2010,9,1)
end=datetime.datetime(2014,9,30)

liste=["AAPL"] # liste de tickers
df=web.DataReader("AAPL",'yahoo',start,end)['Adj Close']

#DF=DataFrame(np.zeros((len(df.index),len(liste))),\
#             index=df.index,columns=liste)

#df_rets=df.pct_change()

tab=asarray(df) 
tab[-4]=101.  #pour faire des tests sur les returns
#tab[-1]=100.


tab_rets=np.zeros(len(tab))
for i in range(1,len(tab)):  # construction des returns, tableau qui fait len(tab)-1 elements
    tab_rets[i]=tab[i]/tab[i-1]-1

print(tab)
print(tab_rets)

def getdatelist(array, lag):
    datelist=[]
    cpt=0
    for i in range(len(array)):
        if array[i]<0:
            cpt+=1
            if cpt >= lag:
                datelist.append(i)
                #cpt=0
        else:
            cpt=0

    return datelist

#datelist=getdatelist(tab_rets,3)
#print(datelist, len(datelist))

def returns_NextDay(liste_days,nb_Days):   #que se passe t-il les nb_Days suivant les jours de X baisses
    output=[]
    for jour in liste_days:
        if jour<len(tab)-nb_Days:
            #print(jour)
            output.append(tab[jour+nb_Days]/tab[jour]-1)
    return output

#utilisation de la fonction

def AAPL(lag,nb_Days):  #la fonction qui dit, quand on lui dit combien de returns neg ce qi se passe les NbDays suivant. Retoure la liste
    #lag= int(input("Combien de jours de rendements négatifs ? "))
    #nb_Days=int(input("le rendement des combiens de jours suivants ? "))

    return (getdatelist(tab_rets,lag),returns_NextDay(getdatelist(tab_rets,lag),nb_Days),
            cumsum((returns_NextDay(getdatelist(tab_rets,lag),nb_Days))),
                   len(returns_NextDay(getdatelist(tab_rets,lag),nb_Days)),
                mean(returns_NextDay(getdatelist(tab_rets,lag),nb_Days)))

def return_matrix(size=2):  #retourne la perf de la strategie sous forme de tableau
    returnStrat=np.zeros([size+1,size+1])
    #print(returnStrat)
    for i in range(1,size+1):
        for j in range(1,size+1):
            returnStrat[i,j]=(AAPL(i,j)[2][-1])

    return returnStrat[1:,1:]

#print(return_matrix())
#print(AAPL(2,1)[0],AAPL(2,1)[1], end='\n')

#la strategie 3 baisses, on porte 1 jour depuis 15 ans.
y=AAPL(3,1)[2]
print(y)
x=range(len(y))

plt.plot(x,y)
plt.show()
