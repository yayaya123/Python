#conversion secondes en année mois jour

sec=int(input("nombre de secondes ? "))
jour=60*60*24
heure=60*60
minute=60

NbJours=sec//jour
Reste1=sec%jour
#NbJours=(sec-NbJours*jour)//heure
NbHeures=Reste1//heure
Reste2=Reste1%heure
NbMinutes=Reste2//minute
NbSecondes=Reste2%minute

print(sec, " secondes equivalent à ",NbJours," jours ", NbHeures, " heures ", NbMinutes, " minutes et ",NbSecondes, " secondes.") 
