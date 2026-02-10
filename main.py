import numpy as np
print("\nLE SUPER PROGRAMME DE MORTY\n\n")

global taille
taille = 5


def estValide(x,y) :
    if x <= taille - 1 and y <= taille - 1 and x >= 0 and y >= 0 and plateau[x][y] == 0:
        return False
    else:
        return True


def backtracking(x,y,compteur):
    plateau[x][y] = compteur
    if compteur == taille * taille:
        return True

    deplacements = [
        (x + 2, y +1), (x + 1, y + 2), (x -1, y +2), (x - 2, y + 1), (x - 2, y -1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)
    ]
    for depX, depY in deplacements:
        if estValide(depX, depY):
            if(backtracking(depX,depY,compteur+1)):
                return True

    plateau[x][y] = 0
    return False


global plateau
plateau = [[0 for _ in range(taille)]for _ in range(taille)]

backtracking(0,0,1)
print(np.matrix(plateau))