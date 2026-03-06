from picross_maker import picrossMaker
from picross_valide import est_valide
import numpy as np


indices_ligne, indices_colonne, picross = picrossMaker("picross/table.pic")
taille = len(indices_ligne)
""" commande numpy trouvé sur internet permetant la creation d'un tableau avec toutes 
    les combinaisons binaires possible pour une taille donné"""
binary_list = np.unpackbits(np.expand_dims(np.arange(2 ** taille, dtype=np.uint8), -1), axis=1, bitorder='little', count=taille).tolist()

grille = []

def backtraking_du_futur(compteur) :
    plateau = []
    if compteur == taille * 2 :
        return True
    
    if compteur <= taille :
        for bin in binary_list :
            if est_valide(bin, indices_ligne[compteur]) :
                if(backtraking_du_futur(compteur+1)) :
                    grille.append(bin)
                    return True
    
    elif compteur > taille :
        colonne = []
        for ligne in picross :
            colonne.append(ligne[compteur - 5])
        if est_valide(colonne, indices_colonne[compteur - 5]) :
            if backtraking_du_futur(compteur+1) :
                return True
    grille.pop
    return False
        


print(backtraking_du_futur(0))
print(grille[::-1])