import numpy as np
import matplotlib.pyplot as plt
print("\nLe problemme du cavalier\n\n")


taille = 5
plateau = [[0 for _ in range(taille)]for _ in range(taille)]

def estValide(x,y) :
    if x < taille and y < taille and x >= 0 and y >= 0 and plateau[x][y] == 0:
        return True
    return False


def backtracking(x,y,compteur):
    plateau[x][y] = compteur
    if compteur == taille * taille: # si on a deja fais toutes les cases, on arrete
        return True

    deplacements = [
        (x + 2, y +1), (x + 1, y + 2), (x -1, y +2), (x - 2, y + 1), (x - 2, y -1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)
    ]
    for depX, depY in deplacements:
        if estValide(depX, depY): # verifie si la case determiner par le deplacement est libre
            if(backtracking(depX,depY,compteur+1)): # on teste toutes les possibilités depuis cette nouvelle case
                return True

    plateau[x][y] = 0 # si aucun deplacement na fonctionner, on remets la case a 0
    return False 

def afficherPlateau(plateau):
    plt.figure(figsize=(8, 8))
    
    plt.imshow(plateau, cmap='binary')

    for i in range(taille):
        for j in range(taille):
            chiffre = plateau[i][j]
            plt.text(j, i, int(chiffre), ha='center', va='center', color='red', fontsize=12)
            

    plt.title("Parcours du Cavalier")
    plt.show()


if(backtracking(0,0,1)):
    afficherPlateau(plateau)
else:
    print("Pas de solution")