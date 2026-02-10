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


def backtracking():
    global x,y,i
    impasse = True
    if estValide(x + 1 , y + 2) == True:
        impasse = False
        x = x + 1
        y = y + 2
    elif estValide(x + 1 , y - 2) == True:
        impasse = False
        x = x + 1
        y = y - 2
    elif estValide(x + 2 , y + 1) == True:
        impasse = False
        x = x + 2
        y = y + 1
    elif estValide(x + 2 , y - 2) == True:
        impasse = False
        x = x + 2
        y = y - 2
    elif estValide(x - 1 , y + 2) == True:
        impasse = False
        x = x - 1
        y = y + 2
    elif estValide(x - 1 , y - 2) == True:
        impasse = False
        x = x - 1
        y = y - 2
    elif estValide(x - 2 , y + 1) == True:
        impasse = False
        x = x - 2
        y = y + 1
    elif estValide(x - 2 , y - 1) == True:
        impasse = False
        x = x - 2
        y = y - 1
    if impasse != True:
        i = i + 1
        plateau[x][y] = 1
    else:
        i = i - 1

plateau = [[0 for _ in range(taille)]for _ in range(taille)]
global positions
positions = []
global x,y,i
x,y,i = 0,0,1

backtracking()
print(np.matrix(plateau))
print(f"1, 1 = {estValide(1, 1)}")
print(f"4, 2 = {estValide(4, 2)}")
print(f"1, 1 = {estValide(1, 1)}")