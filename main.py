import numpy as np
print("\nLE SUPER PROGRAMME DE MORTY\n\n")

class Position:
    x, y = 0, 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

def estValide(x,y) :
    posVerif = Position(x,y)
    dejaVu = False
    for pos in positions:
        if pos == posVerif:
            dejaVu = True
            valide = False
            break

    if not(dejaVu):
        valide = True
        if x > 7 or y > 7:
            valide = False
        if x < 1 or y < 1:
            valide = False

    if valide:
        pos = Position(x,y)
        positions.append(pos)
    
    return valide

       
plateau = [[0 for _ in range(8)]for _ in range(8)]
global positions
positions = []
print(np.matrix(plateau))
print(f"2, 6 = {estValide(2, 6)}")
print(f"5, 4 = {estValide(5, 4)}")
print(f"2, 6 = {estValide(2, 6)}")