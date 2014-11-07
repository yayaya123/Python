#methode

class Time(object):
    "Objet et méthode permettant d'aficher l'heure lorsqu'un instantnous est fourni"

    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure,format(self.minute,'02d'),format(self.seconde,'02d')))

now=Time()
now.heure=int(input("entrez les heures : "))
now.minute=int(input("entrez les minutes : "))
now.seconde=int(input("entrez les secondes : "))

now.affiche_heure()

#autre version avec la methode constructeur

class Time(object):
    "Objet et méthode permettant d'aficher l'heure lorsqu'un instantnous est fourni"

    def __init__(self):
        self.heure=0
        self.minute=0
        self.seconde=0
    
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(format(self.heure,'02d'),format(self.minute,'02d'),format(self.seconde,'02d')))

now=Time()
now.affiche_heure()

#definition et création de l'objet en meme temps

class Time(object):
    "Objet et méthode permettant d'aficher l'heure lorsqu'un instantnous est fourni"

    def __init__(self,a=0,b=0,c=0): #valeur par défaut
        self.heure=a
        self.minute=b
        self.seconde=c
    
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(format(self.heure,'02d'),format(self.minute,'02d'),format(self.seconde,'02d')))
