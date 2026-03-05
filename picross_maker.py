picross = []

with open('table.picross', 'r') as fich :
    for ligne in fich :
        ligne = ligne.strip()
        
        ligne_int = [int(case) for case in ligne]
        picross.append(ligne_int)
        
for ligne in picross :
    print(ligne)


grille_indice_ligne = []
for ligne in picross :
    n = 0
    indices_ligne = []
    longueur = len(ligne) - 1
    for i, c in enumerate(ligne) :
        if c != 0:
            n = n + 1
            if i == longueur:
                indices_ligne.append(n)

        elif n > 0:
            indices_ligne.append(n)
            n = 0
    print(indices_ligne)
    grille_indice_ligne.append(indices_ligne)


grille_indice_colonne = []
for j in range(len(picross)) :
    colonne = []
    for ligne in picross :
        colonne.append(ligne[j])
    n = 0
    indices_colonne = []
    longueur = len(colonne) - 1
    for i, c in enumerate(colonne) :
        if c != 0:
            n = n + 1
            if i == longueur:
                indices_colonne.append(n)

        elif n > 0:
            indices_colonne.append(n)
            n = 0
    grille_indice_colonne.append(indices_colonne)

print(f"Indices lignes : {grille_indice_ligne}")
print(f"Indices colonnes : {grille_indice_colonne}")