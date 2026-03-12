from picross_maker import picrossMaker
from est_valide import est_valide
from visioneuse_pic import afficher_pic
import time
import numpy as np
import matplotlib.pyplot as plt

indices_ligne, indices_colonne, picross = picrossMaker("picross/5x5.pic")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille
print(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"indices colonnes : {indices_colonne}")
debut = time.perf_counter()

#####################

def cases_certaines_ligne(indices):
    tab_certain = []
    tab_valide = []
    for bin in binary_list:
        if(est_valide(bin, indices)):
            tab_valide.append(bin)
    colonnes = []
    for i in range(taille):
        colonne = []
        for ligne in tab_valide :
            colonne.append(ligne[i])
        colonnes.append(colonne)
    
    taille_valide = len(tab_valide)
    for i, c in enumerate(colonnes) :
        if sum(c) == taille_valide:
            tab_certain.append(1)
        else:
            tab_certain.append(0)
    return tab_certain

def cases_certaines_tab(indices_ligne, indices_colonne):
    certain_ligne = []
    for indice in indices_ligne:
        certain_ligne.append(cases_certaines_ligne(indice))

    certain_colonne_temp = []
    for indice in indices_colonne:
        certain_colonne_temp.append(cases_certaines_ligne(indice))

    certain_colonne = []
    taille_certain_col = len(certain_colonne_temp[0])
    for j in range(taille_certain_col): 
        nouvelle_ligne = []
        for i in range(len(certain_colonne_temp)):
            nouvelle_ligne.append(certain_colonne_temp[i][j])
        certain_colonne.append(nouvelle_ligne)
        
    return certain_ligne, certain_colonne


def tab_fusion(ligne,colonne):
    tab_certain = []
    for i in range(len(ligne)):
        ligne_certaine = []
        for j in range(len(ligne[i])):
            if (ligne[i][j] == 1 or colonne[i][j] == 1) :
                case = 1
            else : 
                case = 0
            ligne_certaine.append(case)
        tab_certain.append(ligne_certaine)
    return tab_certain

#####################
certain_ligne, certain_colonne = cases_certaines_tab(indices_ligne, indices_colonne)
tab_certain = tab_fusion(certain_ligne,certain_colonne)
afficher_pic(tab_certain,indices_ligne,indices_colonne)

print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")

#####################
