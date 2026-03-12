from picross_maker import picrossMaker
from est_valide import est_valide
from visioneuse_pic import afficher_pic
from picross_certains import cases_certaines_tab, tab_fusion
import time
import numpy as np

indices_ligne, indices_colonne, picross = picrossMaker("picross/10x10.pic")
taille = len(indices_ligne)
binary_list = np.unpackbits(np.arange(2 ** taille, dtype=np.uint32).astype('<u4').view(np.uint8).reshape(-1, 4), axis=1, bitorder='little', count=taille).tolist() #cette ligne permet la creation de toutes les combinaisons binaire données pour une certaine taille
print(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
print(f"indices ligne : {indices_ligne}")
print(f"indices colonnes : {indices_colonne}")
debut = time.perf_counter()

#####################

grille = cases_certaines_tab(indices_ligne, indices_colonne)


# main

print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")

# affichage
afficher_pic(grille,indices_ligne,indices_colonne)
