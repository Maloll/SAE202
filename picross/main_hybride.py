from picross_maker import picrossMaker
from est_valide import *
from visioneuse_pic import *
from picross_certains import *
from backtracking_picross import *
import time
import numpy as np

nomFich = input("nomFich .pic : ")
indices_ligne, indices_colonne, picross = picrossMaker(f"{nomFich}")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire pour une taille donnée
print(f"\nTable picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"indices colonnes : {indices_colonne}")

print("-------------------------")
debut = time.perf_counter()

#####################


# LE MAIN 
grille = initialisation_tab_certains(indices_ligne, indices_colonne) # On initialise la grille avec les cases certaines

# Tant qu'il y a du changement, on continue de chercher de nouvelles cases certaines
changement = True
while changement: 
    changement, grille = tab_certains(grille, indices_ligne, indices_colonne)


# On cherche a savoir si il reste des cases inconnus
inconnu = 0
for ligne in grille:
    for c in ligne:
        if 0 == c :
            inconnu += 1
        


grille_valide = []
# Si il reste des inconnus dans la grille, on passe au backtracking, en calculant en avance toutes les combinaisons possibles pour lignes et colonnes
if inconnu > 0:
    print(f"Reste de {inconnu} inconnus\nBacktracking...")
    tab_valide_ligne, tab_valide_colonne = tab_valides(grille, indices_ligne, indices_colonne, binary_list)
    backtracking(0,tab_valide_ligne,tab_valide_colonne,indices_ligne,indices_colonne,grille_valide)
else:
    grille_valide = grille

print("Fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")
# On affiche le resultat
afficher_pic(grille_valide,indices_ligne,indices_colonne)