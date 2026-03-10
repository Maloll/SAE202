from picross_maker import picrossMaker
from picross_valide import est_valide
import numpy as np


indices_ligne, indices_colonne, picross = picrossMaker("picross/10x10.pic")
taille = len(indices_ligne)
print(len(indices_ligne))
binary_list = np.unpackbits(np.expand_dims(np.arange(2 ** taille, dtype=np.uint8), -1), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille

grille = []

def backtraking_du_futur(compteur) :
    if compteur == taille:
        grilleTest = grille
        for i in range(taille) :
            colonne = []
            for ligne in grilleTest :
                colonne.append(ligne[i])
            if not est_valide(colonne, indices_colonne[i]) :
                return False
        return True

    for bin in binary_list :
        if est_valide(bin, indices_ligne[compteur]) :
            grille.append(bin)
            if(backtraking_du_futur(compteur+1)) :
                return True
            grille.pop()
    return False


print(backtraking_du_futur(0))
for ligne in grille:
    print(f"{ligne}")