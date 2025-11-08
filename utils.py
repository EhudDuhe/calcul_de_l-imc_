#from main import nom


#from imc import arrondir_imc


def valider_entree(poids,taille):
    while poids<10 or poids>300 :
        print(" Veillez inserer le poids dans le bon plage, le min est de 10kg et le max a 300kg")
        poids = input("veillez saisir votre poids")
        poids = float(poids)
        if 10<=poids <=300 :
            break
    while taille<0.6 or taille>2.70 :
        print(" Veillez inserer la taille dans le bon plage, le min est de o,6 metres et le max a 2,70 metres")
        taille = input("veillez saisir votre taille")
        taille = float(taille)
        if 0.6<=taille<=2.70 :
            break
    return poids,taille



def interpretation_resultat(imc_arrondit,nom) :
    imc_arrondit=round(imc_arrondit,2)
    if 0 <= imc_arrondit <18.5:
        print(" votre imc est de :", imc_arrondit ," vous etes en insuffisance ponderale")
    elif 18.5 <= imc_arrondit <=24.9 :
        print("salut",nom, "votre imc est de :",  imc_arrondit , " votre poids est normal")
    elif 24.9 < imc_arrondit <=29.9 :
        print("salut",nom, "votre imc est de :",  imc_arrondit , " vous etes en surpoids")
    elif 29.9 < imc_arrondit <=34.9 :
        print("salut",nom, "votre imc est de :",  imc_arrondit , " votre IMC indique l'obesite moderee ( GRADE 1 )")
    elif 34.9 < imc_arrondit <=39.9 :
        print("salut",nom, "votre imc est de :",  imc_arrondit , " votre IMC indique l'obesite severe ( GRADE 2")
    elif  imc_arrondit >39.9 :
        print("salut",nom, "votre imc est de :",  imc_arrondit , " votre IMC indique l'obesite massive ( GRADE 3")
    #else :
        #return none''1`
    return  imc_arrondit

