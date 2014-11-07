#manipulation de fichier

import os
a=os.getcwd()
print(a)
texte=input('quel texte voulez-vous ajouter au fichier ? ')
File=open('monFichier', 'a') #File est l'objet générique
File.write(texte)
File.close()
