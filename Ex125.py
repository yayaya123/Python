#EX125

class Cercle(object):
    def __init__(self,r=0):
        self.rayon=r

    def surface(self):
        return self.rayon*self.rayon*3.14159

New=Cercle(2)
print(New.surface())
    
    
class Cylindre(Cercle):

    def __init__(self,r=0,h=0):
        Cercle.__init__(self,r)
        self.hauteur=h

    def volume(self):
        return self.surface()*self.hauteur

test=Cylindre(2,4)
print(test.surface())
print(test.volume())

class Cone(Cylindre):
    def __init__(self, r=0,h=0):
        Cylindre.__init__(self,r,h)

    def volume(self):
        return Cylindre.volume(self)/3

test=Cone(2,4).volume()
print(test)

