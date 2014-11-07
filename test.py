#table de multiplication

nombre=input("quelle table voulez-vous afficher ? ")
nombre=int(nombre)  #sinon il recopie la chaine de caractère a fois
a=1
while a<=10:
    print(a," * ",nombre," = ", a*nombre)
    a+=1
    
    

