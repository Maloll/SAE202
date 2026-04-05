from picross_maker import picrossMaker
from est_valide import *
from visioneuse_pic import *
from picross_certains import *
import time
import numpy as np

taille = int(input("taille : "))
indices_ligne, indices_colonne, picross = picrossMaker(f"picross/{taille}x{taille}.pic")
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


def valide_hybride(bin, ligne, indice):
    for i, c in enumerate(ligne):
        if (c == 1 and bin[i] == 0) or (c == 2 and bin[i] == 1):
            return False
    return est_valide(bin, indice)

def cases_certaines_hybride(ligne_sur, indices,taille,binary_list):
    tab_certain = []
    tab_valide = []
    for bin in binary_list:
        if(valide_hybride(bin, ligne_sur, indices)): # si c'est valide on ajoute a la liste
            tab_valide.append(bin)
    colonnes = []
    for i in range(taille):
        colonne = []
        for ligne in tab_valide :
            colonne.append(ligne[i])
        colonnes.append(colonne)
    
    # si la somme d'une colone est égale au nombre de lignes valides, on mets un 1, sinon si = 0 alors on mets 2, sinon 0
    taille_valide = len(tab_valide)
    for i, c in enumerate(colonnes):
        if sum(c) == taille_valide and taille_valide>0:
            tab_certain.append(1)
        elif sum(c) == 0 or not sum(c):
            tab_certain.append(2)
        else:
            tab_certain.append(0)
    return tab_certain


def tab_certains(tab_sur, indices_ligne, indices_colonne):
    # Elle creer un tableau certain pour les lignes et colonnes
    # Et les fusiones pour faire un grand tableaux de cases certaines
    taille = len(indices_ligne)
    binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire pour une certaine taille données
    
    certain_ligne = []
    for i, indice in enumerate(indices_ligne):
        certain_ligne.append(cases_certaines_hybride(tab_sur[i],indice,taille,binary_list)) # On fait un tableau avec toutes les cases certaines pour les lignes

    certain_colonne_temp = []
    for i, indice in enumerate(indices_colonne):
        colonne = []
        for j in range(len(tab_sur)):
            colonne.append(tab_sur[j][i])
        certain_colonne_temp.append(cases_certaines_hybride(colonne,indice,taille,binary_list)) # On fait un tableau avec toutes les cases certaines pour les colonnes

    certain_colonne = inversion_tab(certain_colonne_temp)
    
    tab_certain = tab_fusion(certain_ligne,certain_colonne)
    return tab_certain



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
for i in range(5):
    grille_valide = tab_certains(grille_valide, indices_ligne, indices_colonne)
print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")
afficher_pic(grille_valide,indices_ligne,indices_colonne)

for l in grille_valide:
    print(l)