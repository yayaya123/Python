# class perso qui communte les elements d une liste de deux

class liste(object):
    def __init__(self,a=['','']):
        self.element1=a[0]
        self.element2=a[1]
        

    def commut(self):
        self.element1,self.element2=self.element2,self.element1
        print(self)

test=liste(['a','b'])
print(test)
print(test.element1)
print(test.element2)
test.commut()
