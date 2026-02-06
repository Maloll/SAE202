print("\nLE SUPER PROGRAMME DE MALO LUCAS ET GATO\n\n")

def estValide(x,y) :
    valide = True
    if x > 8 or y > 8:
        valide = False
    if x < 1 or y < 1:
        valide = False

    pos = Position(x,y)
    return valide, pos

tabVisit = []

class Position:
    x, y = 0, 0 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y


pos = Position()

valide, pos = estValide