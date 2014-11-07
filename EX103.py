#ex10.3

def trouve(chaine, lettre, indexDeb):
    i=indexDeb
    while i<len(chaine):
        if chaine[i]==lettre:
            return i
        else:
            i+=1
    return -1

        
print(trouve('vbhjtby','b',2))


