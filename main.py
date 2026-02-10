import numpy as np
print("\nLE SUPER PROGRAMME DE MORTY\n\n")

global taille
taille = 5

def estValide(x,y) :
    valide = False
    
    if x > taille - 1 or y > taille - 1 or x < 1 or y < 1:
        valide = True
        print("hors plateau")
    else:
        if plateau[x][y] == 1: 
            valide = True
            print("Deja vu")
        
    return valide


def backtracking():
    x,y = 0, 0
    print(estValide(x + 1 , y + 2))
    print(estValide(x + 1 , y - 2))
    print(estValide(x + 2 , y + 1))
    print(estValide(x + 2 , y - 2))
    print(estValide(x - 1 , y + 2))
    print(estValide(x - 1 , y - 2))
    print(estValide(x - 2 , y + 1))
    print(estValide(x - 2 , y - 1))


plateau = [[0 for _ in range(taille)]for _ in range(taille)]
global positions
positions = []
backtracking()
print(np.matrix(plateau))
print(f"1, 1 = {estValide(1, 1)}")
print(f"4, 2 = {estValide(4, 2)}")
print(f"1, 1 = {estValide(1, 1)}")