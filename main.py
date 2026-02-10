import numpy as np
print("\nLE SUPER PROGRAMME DE MORTY\n\n")

global taille
taille = 5


def estValide(x,y) :
    valide = True
    
    if x > taille - 1 or y > taille - 1 or x < 0 or y < 0:
        valide = False
    else:
        if plateau[x][y] == 1: 
            valide = False
        
    return valide


def backtracking(x,y,i):
    plateau[x][y] = i
    if i == taille * taille:
        return True

    deplacements = [
        (x + 2, y +1), (x + 1, y + 2), (x -1, y +2), (x - 2, y + 1), (x - 2, y -1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)
    ]
    for depX, depY in deplacements:
        if estValide(depX, depY):
            if(backtracking(depX,depY,i+1)):
                return True

    plateau[x][y] = 0
    return False


global plateau
plateau = [[0 for _ in range(taille)]for _ in range(taille)]

x,y,i = 0,0,1
backtracking(x,y,i)
print(np.matrix(plateau))