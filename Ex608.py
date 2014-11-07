a=input('borne basse')
b=input('borne haute')
a=int(a)
b=int(b)
                
addition=0
i=a

while i<=b:
    if (not i%3) or (not i%5):
        addition=addition+i
    i+=1
print(addition)
        
        
        
        
        
