print("\nLE SUPER PROGRAMME DE MORTY\n\n")

class Position:
    x, y = 0, 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

def estValide(x,y) :
    if not hasattr(estValide, "positions"):
        estValide.positions = []

    posVerif = Position(x,y)
    dejaVu = False
    for pos in estValide.positions:
        if pos == posVerif:
            dejaVu = True
            valide = False
            break
        
    if not(dejaVu):
        valide = True
        if x > 8 or y > 8:
            valide = False
        if x < 1 or y < 1:
            valide = False

    if valide:
        pos = Position(x,y)
        estValide.positions.append(pos)
    
    return valide


print(f"2, 6 = {estValide(2, 6)}")
print(f"5, 4 = {estValide(5, 4)}")
print(f"2, 6 = {estValide(2, 6)}")