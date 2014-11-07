#tuple

def funk(e):
    return (e,)+(e,)


a=(1,'deux', 3)
for e in a:
    b=funk(e)
    print(b)
    
