#Ex 10.11
#conversion phrase en une liste de mots

def convert(phrase):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    mot=''
    liste=[]
    for e in phrase:
        if e in alphabet:
            mot=mot+e
        else:
            liste.append(mot)
            mot=''
    liste.append(mot)
    print(liste)
            
convert(input("saisissez votre phrase : "))
