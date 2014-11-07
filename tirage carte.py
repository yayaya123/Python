# tirage de cartes

from random import *



num=randrange(1,53)
print(num)
if num<=13:
    a='trefle'
elif num>13 and num<=26:
    a='carreau'
elif num>26 and num<=39:
    a='coeur'
else:
    a='pique'

reste=num%13
if reste ==11:
    print("vous avez tiré le valet de ", a)
elif reste ==12:
    print("vous avez tiré la dame de ", a)
elif reste ==13:
    print("vous avez tiré le roi de ", a)
elif reste ==1:
    print("vous avez tiré l'As de ", a)
else:
    print("vous avez tiré le ", reste, " de ", a)
    
