#requeste SQL

import sqlite3
BDD="/Users/Yann/Desktop/Python/DB/musique.sq3"
conn=sqlite3.connect(BDD)
cur=conn.cursor()

#cur.execute("CREATE TABLE Oeuvres2(Comp STRING, titre STRING, Durée INTEGER, Interpr STRING)")
#cur.execute("CREATE TABLE Compositeurs(Comp STRING, a_naiss INTEGER, a_mort INTEGER)")

liste1=('Mozart','Beethoven','Hendel','Schubert','Vivaldi','Monteverdi','Chopin','Bach','Shostakovich')
liste2=(1756,1770,1685,1797,1678,1567,1810,1685,1906)
liste3=(1791,1827,1759,1828,1741,1643,1849,1750,1975)

liste_complete=[]
for i in range(9):
    #print(i)
    liste_complete.append((liste1[i],liste2[i],liste3[i]))

#print(liste_complete)

liste4=('Vivaldi','Mozart','Brahms','Beethoven','Beethoven','Schubert','Haydn','Chopin','Bach','Beethoven','Mozart','Mozart','Beethoven',)
liste5=('Les Quattre Saisons','Concerto piano No12','Concerto violon No2','Sonate au clair de lune', 'Sonate pathétique','Quintette la truite','La création','Concerto Piano No1','Tocatta et Fugue', 'Concerto Piano No4','Symphonie No40','Concerto Piano No22','Concerto Piano No3')
liste6=(20,25,40,14,17,39,109,42,9,33,29,35,37)
liste7=('T. Pinnock','M. Parahia','A. Grumiaux','W. Kempf','W. Kempf','SE of London','H. Von Karajan','M.J. Pires','P. Burmester','M. Pollini','F. Bruggen','S. Richter','S. Richter')

#print(len(liste4),len(liste5),len(liste6),len(liste7))
liste_oeuvres=[]

for i in range(len(liste4)):
    liste_oeuvres.append((liste4[i],liste5[i],liste6[i],liste7[i]))

#print(liste_oeuvres)


#utilisation de la base

while 1:
    print("Veuillez entrer une requete SQL : ")
    requete = input()
    if requete=="":
        break
    try:
        cur.execute(requete)
    except:
        print("requete incorrecte")
    else:
        for enreg in cur:
            print(enreg)
    print()

choix = input("Confirmez-vous l'enregistrement de l'etat actuel (o/n) ? ")
if choix ==0 or choix==o:
    conn.commit()
else:
    conn.close

    
