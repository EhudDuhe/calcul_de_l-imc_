from imc import calculer_imc
from utils import valider_entree
#from imc import arrondir_imc
from utils import interpretation_resultat

nom=input("veillez inserez votre nom")
poids = input("veillez saisir votre poids")
poids = float(poids)
taille = input("veillez saisir votre taille")
taille = float(taille)
poids, taille = valider_entree(poids, taille)

resultat = calculer_imc(poids, taille)
interpretation_resultat(resultat,nom)
