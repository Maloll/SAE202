import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from picross_maker import picrossMaker



def afficher_pic(grille,indices_ligne,indices_colonne):
    choix_couleur = 0
    for ligne in grille : 
        if 2 in ligne :
            choix_couleur = 2
            break
    
    if choix_couleur == 2:
        couleurs = ['red','black','white']
    else:
        couleurs = ['white','black']
    colorMap = ListedColormap(couleurs)
    matrice = np.array(grille)
    taille = 10
    plt.figure(figsize=(taille,taille))
    plt.imshow(matrice, cmap=colorMap, vmin=0, vmax=2)
    plt.title(f"Table picross en {len(indices_ligne)}x{len(indices_ligne)}")
    plt.tick_params(axis='x', bottom=False, labelbottom=False, top=True, labeltop=True)
    plt.xticks(range(len(indices_colonne)), [str(x) for x in indices_colonne])
    plt.yticks(range(len(indices_ligne)), [str(y) for y in indices_ligne])
    plt.show()

#indices_ligne, indices_colonne, grille = picrossMaker("picross/10x10.pic")
#afficher_pic(grille,indices_ligne,indices_colonne)