from picross_maker import picrossMaker
from est_valide import *
from visioneuse_pic import afficher_pic
import time
import numpy as np
import matplotlib.pyplot as plt

"""indices_ligne, indices_colonne, picross = picrossMaker("picross/15x15.pic")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille
print(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"indices colonnes : {indices_colonne}")
debut = time.perf_counter()"""

def cases_certaines_ligne(indices,taille,binary_list):
    tab_certain = []
    tab_valide = []
    for bin in binary_list:
        if(est_valide(bin, indices)): # si c'est valide on ajoute a la liste
            tab_valide.append(bin)
    colonnes = []
    for i in range(taille):
        colonne = []
        for ligne in tab_valide :
            colonne.append(ligne[i])
        colonnes.append(colonne)
    
    # si la somme d'une colone est égale au nombre de lignes valides, on mets un 1, sinon un 0
    taille_valide = len(tab_valide) 
    for i, c in enumerate(colonnes) :
        if sum(c) == taille_valide and taille_valide>0:
            tab_certain.append(1)
        elif sum(c) == 0 or not sum(c):
            tab_certain.append(2)
        else:
            tab_certain.append(0)
    return tab_certain


def tab_fusion(ligne,colonne):
    # Une fonction qui fusione 2 tableaux
    tab_certain = []
    for i in range(len(ligne)):
        ligne_certaine = []
        for j in range(len(ligne[i])):
            if (ligne[i][j] == 1 or colonne[i][j] == 1) : # si 1 dans un 1 deux on mets 1, sinon 0
                case = 1
            elif (ligne[i][j] == 2 or colonne[i][j] == 2):
                case = 2
            else : 
                case = 0
            ligne_certaine.append(case)
        tab_certain.append(ligne_certaine)
    return tab_certain


def inversion_tab(tab):
    # Une double boucle pour remmettre le tableaux des colonnes dans le bon sens
    tab_inverse = []
    taille = len(tab[0])
    for j in range(taille): 
        nouvelle_ligne = []
        for i in range(len(tab)):
            nouvelle_ligne.append(tab[i][j])
        tab_inverse.append(nouvelle_ligne)
    return tab_inverse


def initialisation_tab_certains(indices_ligne, indices_colonne):
    # Fonction qui orchestre les 2 fonctions au dessus
    # Elle creer un tableau certain pour les lignes et colonnes
    # Et les fusiones pour faire un grand tableaux de cases certaines
    taille = len(indices_ligne)
    binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire pour une certaine taille données
    
    certain_ligne = []
    for indice in indices_ligne:
        certain_ligne.append(cases_certaines_ligne(indice,taille,binary_list)) # On fait un tableau avec toutes les cases certaines pour les lignes

    certain_colonne_temp = []
    for indice in indices_colonne:
        certain_colonne_temp.append(cases_certaines_ligne(indice,taille,binary_list)) # On fait un tableau avec toutes les cases certaines pour les colonnes

    certain_colonne = inversion_tab(certain_colonne_temp)
    
    tab_certain = tab_fusion(certain_ligne,certain_colonne)
    return tab_certain



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
    # Fonction qui renvoie un tableau de cases certaines
    # Elle creer un tableau certain pour les lignes et colonnes
    # Et les fusiones pour faire un grand tableau de cases certaines
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
    return (tab_certain != tab_sur), tab_certain


"""
#####################
certain_ligne, certain_colonne = cases_certaines_tab(indices_ligne, indices_colonne)
tab_certain = tab_fusion(certain_ligne,certain_colonne)
afficher_pic(tab_certain,indices_ligne,indices_colonne)

print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")

#####################
"""


