class Point():
    "création d'une classe"

premierPoint=Point()
premierPoint.x=3
premierPoint.y=9


print(premierPoint.x,premierPoint.y)
    
class Rectangle():
    "cette classe utilisera un point"
monRect=Rectangle()
monRect.longueur=2
monRect.largeur=1
 #   monRect.coin=premierPoint
monRect.coin=Point()
monRect.coin.x=4
monRect.coin.y=2

print(monRect.coin.y)
      
