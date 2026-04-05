from picross_maker import picrossMaker
from est_valide import *
import numpy as np

def liste_valide(bl, ligne, indice):
    # Fonction qui renvoie la liste des lignes valides pour une ligne
    tab_valide = []
    for bin in bl:
        if valide_hybride(bin, ligne, indice):
            tab_valide.append(bin)
    return tab_valide


def tab_valides(grille, il, ic, bl):
    # Fonction qui renvoie une liste des listes des lignes valides
    tab_valide_ligne = []
    for i, ligne in enumerate(grille):
        tab_valide_ligne.append(liste_valide(bl, ligne, il[i]))
    
    tab_valide_colonne = []
    for i in range(len(grille)):
        colonne = []
        for ligne in grille:
            colonne.append(ligne[i])
        tab_valide_colonne.append(liste_valide(bl,colonne,ic[i]))

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
        grille_valide.append(ligne)
        if backtracking(compteur+1, tab_l, tab_c, il, ic,grille_valide):
            return True
        grille_valide.pop()
    return False