import numpy as np
import matplotlib.pyplot as plt
print("\nLe problemme du cavalier\n\n")


taille = 6
nbMov = 0
plateau = [[0 for _ in range(taille)]for _ in range(taille)]


def estValide(x,y) :
    if x < taille and y < taille and x >= 0 and y >= 0 and plateau[x][y] == 0:
        return True
    return False

def estValideBis(x,y) :
    if x < taille and y < taille and x >= 0 and y >= 0:
        return True
    return False


def backtracking(x,y,compteur):
    global nbMov
    nbMov = nbMov + 1
    
    deplacements = [
        (x + 2, y +1), (x + 1, y + 2), (x -1, y +2), (x - 2, y + 1), (x - 2, y -1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)
    ]

    plateau[x][y] = compteur
    

    if compteur == taille * taille:
        for depX, depY in deplacements:
            if depX == xDebut and depY == yDebut: # on verifie si la derniere case peut acceder a la premiere case
                return True
        plateau[x][y] = 0 # si on ne peut pas acceder a la premiere case, on remets la case a 0 et on reviens en arriere
        return False
    
    for depX, depY in deplacements:
        if estValide(depX, depY): # verifie si la case determiner par le deplacement est libre
            if(backtracking(depX,depY,compteur+1)): # on teste toutes les possibilités depuis cette nouvelle case jusqua la victoire
                return True
        
    plateau[x][y] = 0 # si aucun deplacement na fonctionner, on remets la case a 0 et on reviens en arriere
    return False 

   

def afficherPlateau(plateau):
    plt.figure(figsize=(7, 7))
    
    plateauJeu = [[0 for _ in range(taille)] for _ in range(taille)] # on creer un tableau en taille² avec des 0 partout
    for i in range(taille): # on mets des 1 une case sur 2 et en diagonal (comme un plateau d'echec)
        for j in range(taille):
            if i % 2 == 0 and j % 2 ==0:
                plateauJeu[i][j] = 1
            elif j % 2 != 0 and i % 2 !=0:
                plateauJeu[i][j] = 1


    plt.imshow(plateauJeu, cmap='binary') # on affiche en mode binary pour mettre les 0 en blanc et les 1 en noir

    # on liste les x et les y
    liste_x = [0 for _ in range(taille * taille + 1)] 
    liste_y = [0 for _ in range(taille * taille + 1)]

    for i in range(taille):
        for j in range(taille): # on mets les coordonées dans l'odre
            chiffre = plateau[i][j]
            liste_x[chiffre] = j 
            liste_y[chiffre] = i
    
    for i in range(1,taille*taille):
        plt.annotate('', xy=(liste_x[i+1], liste_y[i+1]), xytext=(liste_x[i], liste_y[i]), arrowprops=dict(arrowstyle='->', color='darkturquoise', lw=3)) # on creer les fleches a partir des liste de coordonnées et un arrow style

    for i in range(taille):
        for j in range(taille):
            nombre = plateau[i][j]
            if nombre == 1:
                plt.text(j, i, int(nombre), ha='center', va='bottom', color='chartreuse', fontsize=10, fontweight='bold')
            else:
                plt.text(j, i, int(nombre), ha='center', va='bottom', color='red', fontsize=10, fontweight='bold') # on ajoute les chiffres de l'ordre des deplacements en rouge sur chaque case
    #plt.plot(liste_x, liste_y, marker='o', color='darkturquoise', linestyle='-', linewidth=2)
    plt.title("Parcours du Cavalier")
    plt.show()



# prog
global xDebut,yDebut
x = int(input("x : "))
y = int(input("y : "))
xDebut = x - 1 #on sauvegarde les coordonnées de x
yDebut = y - 1 #on sauvegarde les coordonnées de y
if(backtracking(x-1,y-1,1)):
    afficherPlateau(plateau)
else:
    print("Pas de solution")
print(f"Nombre de mouvements : {nbMov}")