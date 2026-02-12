import numpy as np
import matplotlib.pyplot as plt
print("\nLe problemme du cavalier\n\n")


taille = 5
plateau = [[0 for _ in range(taille)]for _ in range(taille)]


def estValide(x,y) :
    if x < taille and y < taille and x >= 0 and y >= 0 and plateau[x][y] == 0:
        return True
    return False



def backtracking(x,y,compteur):
    plateau[x][y] = compteur
    if compteur == taille * taille: # si on a deja fais toutes les cases, on arrete
        return True

    deplacements = [
        (x + 2, y +1), (x + 1, y + 2), (x -1, y +2), (x - 2, y + 1), (x - 2, y -1), (x - 1, y - 2), (x + 1, y - 2), (x + 2, y - 1)
    ]
    for depX, depY in deplacements:
        if estValide(depX, depY): # verifie si la case determiner par le deplacement est libre
            if(backtracking(depX,depY,compteur+1)): # on teste toutes les possibilités depuis cette nouvelle case jusqua la victoire
                return True

    plateau[x][y] = 0 # si aucun deplacement na fonctionner, on remets la case a 0 et on reviens en arriere
    return False 



def afficherPlateau(plateau):
    plt.figure(figsize=(7, 7))
    
    plateauJeu = [[0 for _ in range(taille)] for _ in range(taille)]
    for i in range(taille):
        for j in range(taille):
            if i % 2 == 0 and j % 2 ==0:
                plateauJeu[i][j] = 1
            elif j % 2 != 0 and i % 2 !=0:
                plateauJeu[i][j] = 1


    plt.imshow(plateauJeu, cmap='binary')

    liste_x = [0 for _ in range(taille * taille + 1)]
    liste_y = [0 for _ in range(taille * taille + 1)]

    for i in range(taille):
        for j in range(taille):
            chiffre = plateau[i][j]
            liste_x[chiffre] = j
            liste_y[chiffre] = i
    
    for i in range(1,taille*taille):
        plt.annotate('', xy=(liste_x[i+1], liste_y[i+1]), xytext=(liste_x[i], liste_y[i]), arrowprops=dict(arrowstyle='->', color='darkturquoise', lw=3))

    for i in range(taille):
        for j in range(taille):
            nombre = plateau[i][j]
            plt.text(j, i, int(nombre), ha='center', va='bottom', color='red', fontsize=16, fontweight='bold')
    #plt.plot(liste_x, liste_y, marker='o', color='darkturquoise', linestyle='-', linewidth=2)
    plt.title("Parcours du Cavalier")
    plt.show()



# prog
x = int(input("x : "))
y = int(input("y : "))
if(backtracking(x-1,y-1,1)):
    afficherPlateau(plateau)
else:
    print("Pas de solution")