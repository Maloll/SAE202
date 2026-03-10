from picross_maker import picrossMaker
from est_valide import est_valide
import time
import numpy as np

indices_ligne, indices_colonne, picross = picrossMaker("picross/10x10.pic")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille
print(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"ibndices colonnes : {indices_colonne}")
debut = time.perf_counter()

#####################

grille = []

def backtraking(compteur) :
    if compteur == taille:
        for i in range(taille) :
            colonne = []
            for ligne in grille :
                colonne.append(ligne[i])
            if not est_valide(colonne, indices_colonne[i]) :
                return False
        return True

    for bin in binary_list :
        if est_valide(bin, indices_ligne[compteur]) :
            grille.append(bin)
            if(backtraking(compteur+1)) :
                return True
            grille.pop()
    return False


# main
backtraking(0)
for ligne in grille:
    print(f"{ligne}")

#####################
print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")