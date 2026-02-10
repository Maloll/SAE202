import numpy as np
print("\nLE SUPER PROGRAMME DE MORTY\n\n")

global taille
taille = 5

def estValide(x,y) :
    valide = True
    if plateau[x][y] != 1:
        if x > taille - 1 or y > taille - 1:
            valide = False
        if x < 1 or y < 1:
            valide = False
    else:
        valide = False
        
    return valide


def backtracking():
    plateau[1][1] = 1

plateau = [[0 for _ in range(taille)]for _ in range(taille)]
global positions
positions = []
backtracking()
print(np.matrix(plateau))
print(f"1, 1 = {estValide(1, 1)}")
print(f"4, 2 = {estValide(4, 2)}")
print(f"1, 1 = {estValide(1, 1)}")