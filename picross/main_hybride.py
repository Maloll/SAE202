from picross_maker import picrossMaker
from est_valide import *
from visioneuse_pic import *
from picross_certains import *
import time
import numpy as np

nomFich = input("nomFich .pic : ")
indices_ligne, indices_colonne, picross = picrossMaker(f"picross/{nomFich}")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille
print(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"indices colonnes : {indices_colonne}")
debut = time.perf_counter()

#####################

""" 
    [0,1,1,1,0]
    [0,0,1,0,0]
"""


def trakbacking(bl, ligne, indice):
    tab_valide = []
    for bin in bl:
        if valide_hybride(bin, ligne, indice):
            tab_valide.append(bin)
    return tab_valide


def tab_valides(grille, il, ic, bl):
    for i, ligne in enumerate(grille):
        tab_valide_ligne.append(trakbacking(bl, ligne, il[i]))
    for i in range(len(grille)):
        colonne = []
        for ligne in grille:
            colonne.append(ligne[i])
        tab_valide_colonne.append(trakbacking(bl,colonne,ic[i]))

    return tab_valide_ligne, tab_valide_colonne


def backtracking(compteur, tab_l, tab_c, il, ic, grille_valide):
    if compteur == len(il):
        for i in range(compteur):
            colonne = []
            for ligne in grille_valide:
                colonne.append(ligne[i])
            if not est_valide(colonne, ic[i]):
                return False
        return True

    for ligne in tab_l[compteur]:
        if est_valide(ligne,il[compteur]):
            grille_valide.append(ligne)
            if backtracking(compteur+1, tab_l, tab_c, il, ic,grille_valide):
                return True
    grille_valide.pop()
    return False


ligne_test = [0,1,0,0,0,1,0,0,0,0]
indice_test = [3,2]
#print(trakbacking(binary_list, ligne_test, indice_test))
grille_valide = []
tab_valide_ligne = []
tab_valide_colonne = []
#afficher_pic(cases_certaines_tab(indices_ligne,indices_colonne),indices_ligne,indices_colonne)
#tab_valide_ligne, tab_valide_colonne = tab_valides(grille, indices_ligne, indices_colonne, binary_list)
#print(f"lignes_valides_lignes : {tab_valide_ligne}\nlignes_valides_colonnes : {tab_valide_colonne}")
#backtracking(0,tab_valide_ligne,tab_valide_colonne,indices_ligne,indices_colonne,grille_valide)


#affichage
#afficher_pic(grille_valide,indices_ligne,indices_colonne)


# LE MAIN DE TEST
grille_valide = initialisation_tab_certains(indices_ligne, indices_colonne)
changement = True
while changement:
    changement, grille_valide = tab_certains(grille_valide, indices_ligne, indices_colonne)


print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")


afficher_pic(grille_valide,indices_ligne,indices_colonne)

for l in grille_valide:
    print(l)