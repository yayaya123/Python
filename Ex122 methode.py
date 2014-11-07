#Ex122, comte bancaire

class CompteBancaire(object):
    def __init__(self,a='Dupont',b='1000'):
        self.nom=a
        self.solde=b

    def depot(self, somme=0):
        self.solde+=somme

    def retrait(self, somme):
        self.solde-=somme

    def affiche(self):
        print("Mr {0} a {1} euro sur son compte".format(self.nom, self.solde))
    
    
#utilisation

compte1=CompteBancaire()
compte1.affiche()

compte1=CompteBancaire('Yann', 500000)
compte1.depot(50000)
compte1.affiche()
