#retourne une liste avec la table de nombre

def table(n):
    
    result=[]
    i=1
    while i<=10:
        result.append(i*n)
        i+=1

    return result      

nombre=input("entrez votre nombre ")
print('voici la table : ',table(int(nombre)))

