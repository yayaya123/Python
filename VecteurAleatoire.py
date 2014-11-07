#generer une liste de nbaléatoires et évolution dynamique de tableaux

from random import *
def RandomGenerator(NbColumns):
    tab=NbColumns*[0]
    i=0
    while i<NbColumns:
        tab[i]=gauss(0,1)
        #print(tab[i])
        i+=1
    return tab

def RandomGenerator2(NbColumns):
    tab=[]
    i=0
    while i<NbColumns:
        tab.append(gauss(0,1))
        print(tab)
        i+=1
    return tab

print(RandomGenerator(3))
print(RandomGenerator2(3))


