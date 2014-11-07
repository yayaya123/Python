liste=[45,67,34]
i=0
maxim=0
while i<len(liste):
    if liste[i]>maxim:
        maxim=liste[i]
    i+=1
print("Le plus grand élément de la liste est ",maxim)
