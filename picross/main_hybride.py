from picross_maker import picrossMaker
from est_valide import est_valide
from visioneuse_pic import afficher_pic
from picross_certains import cases_certaines_tab, tab_fusion
import time
import numpy as np

indices_ligne, indices_colonne, picross = picrossMaker("picross/5x5.pic")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille
print(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"indices colonnes : {indices_colonne}")
debut = time.perf_counter()

#####################

grille = cases_certaines_tab(indices_ligne, indices_colonne)

""" 
    [0,1,1,1,0]
    [0,0,1,0,0]
"""


def valide_hybride(bin, ligne, indice):
    for i, c in enumerate(ligne):
        if c != 0 and bin[i] == 0:
            return False
    return est_valide(bin, indice)


def trakbacking(bl, ligne, indice):
    tab_valide = []
    for bin in bl:
        if valide_hybride(bin, ligne, indice):
            tab_valide.append(bin)
            print()
    return tab_valide

def backtraking(grille, il, ic, bl):
    tab_valide = []
    grille_valide = []
    for i, ligne in enumerate(grille):
        tab_valide.append(trakbacking(bl, ligne, il[i]))
    print(tab_valide)


ligne_test = [0,0,1,0,0]
indice_test = [3]
print(trakbacking(binary_list, ligne_test, indice_test))
# backtraking(grille, indices_ligne, indices_colonne, binary_list)

print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")

# affichage
# afficher_pic(grille,indices_ligne,indices_colonne)
