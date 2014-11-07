#recuperation des data excel

import xlrd
from numpy import *
from pandas import *
import matplotlib.pyplot as plt

# Ouverture du classeur
path='/Users/Yann/Desktop/Python/DB/histo vix.xlsx'
classeur = xlrd.open_workbook(path)

# Récupération du nom de toutes les feuilles sous forme de liste
nom_des_feuilles = classeur.sheet_names()

# Récupération de la première feuille
feuille = classeur.sheet_by_name(nom_des_feuilles[0])

#liste de dates
liste=[]
for i in range(6,1262):
    liste.append((feuille.cell_value(i, 1),feuille.cell_value(i, 2),feuille.cell_value(i, 5),feuille.cell_value(i, 8),feuille.cell_value(i, 11)))
#print(liste)
    
#on essaie de stocker dans une matrice now

#A=ones((1257,4))
#print(A[1])
#for i in range(1257):
    #print(1262-i)
    #print(feuille.cell_value(1262, 5))
#    A[i,:]=[feuille.cell_value(1261-i, 2),feuille.cell_value(1261-i, 5),feuille.cell_value(1261-i, 8),feuille.cell_value(1261-i, 11)]
#print(A[0,:])
#for i in range(4):
#    print(mean(A[:,i]))

print(sin(0))
#A=random().randint(2)
print(array([[1,2],[2],[3]]))
print(size(array(([1,2],[2],[3]))))

df=DataFrame(liste,columns=['Date','VIX','UX1','UX2','UX3'])
print(df)

df['UX2-UX1']=df['UX2']-df['UX1']
print(df)

graph=plt.plot(df['VIX'],df['UX2-UX1'],'o')
plt.show()



