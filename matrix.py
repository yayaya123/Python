from numpy import *
#from random import *

A=ones((3,4))
B=2*ones((4,3))
C=array((1,2,3,4))
D=array([[1,2,3,4],[3,4,5,6],[1,4,2,3]])

print(A)
print(B)
print(A.dot(B))
print(B.transpose())
print(C)
print(D)
print(A*D)
print(B.dot(D))
E=D[1:3,1:4]
print(E,size(E))



G=random.randint(-1,2,(2,2))
print(G)
