import numpy as np
print("\nLe problemme du cavalier\n\n")


taille = 8
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

backtracking(0,0,1)
print(np.matrix(plateau))