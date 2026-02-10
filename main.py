import numpy as np
print("\nLE SUPER PROGRAMME DE MORTY\n\n")

global taille
taille = 5
global x,y
x,y = 0, 0

def estValide(x,y) :
    valide = True
    
    if x > taille - 1 or y > taille - 1 or x < 1 or y < 1:
        valide = False
    else:
        if plateau[x][y] == 1: 
            valide = False
        
    return valide


def backtracking():
    if estValide(x + 1 , y + 2) == True:
        x = x + 1
        y = y + 2
    elif estValide(x + 1 , y - 2) == True:
        x = x + 1
        y = y - 2
    elif estValide(x + 2 , y + 1) == True:
        x = x + 2
        y = y + 1
    elif estValide(x + 2 , y - 2) == True:
        x = x + 2
        y = y - 2
    elif estValide(x - 1 , y + 2) == True:
        x = x - 1
        y = y + 2
    elif estValide(x - 1 , y - 2) == True:
        x = x - 1
        y = y - 2
    elif estValide(x - 2 , y + 1) == True:
        x = x - 2
        y = y + 1
    elif estValide(x - 2 , y - 1) == True:
        x = x - 2
        y = y - 1
    plateau[x][y] = 1
    


plateau = [[0 for _ in range(taille)]for _ in range(taille)]
global positions
positions = []
backtracking()
print(np.matrix(plateau))
print(f"1, 1 = {estValide(1, 1)}")
print(f"4, 2 = {estValide(4, 2)}")
print(f"1, 1 = {estValide(1, 1)}")