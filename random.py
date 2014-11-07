# test de fonctions random

from math import *
from random import *

#print(int(10*random())+1)
#print(gauss(0,1))

def unTirage(S,Sigm,T1,K):
    return max(S*exp(Sigm*gauss(0,sqrt(T1)))-K,0)
#print(unTirage(100,0.2,1))

def pxBSMC(S_0,Sigma,T,K,NbTirages):
    i=0
    Sum=0
    while i<NbTirages:
        Sum+=unTirage(S_0,Sigma,T,K)
        i+=1      
    Sum=Sum/NbTirages
    return(Sum)    

print(pxBSMC(100,0.2,1,100,500))
for i in range(10):
    print(i)

      

