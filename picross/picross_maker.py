def picrossMaker(Nomfich) :

    picross = []
    with open(Nomfich, 'r') as fich :
        for ligne in fich :
            ligne = ligne.strip()
            
            ligne_int = [int(case) for case in ligne]
            picross.append(ligne_int)

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
        
    return grille_indice_ligne, grille_indice_colonne, picross


"""ligne, colonne, picross = picrossMaker("picross/10x10.pic")
print(f"Indices lignes : {ligne}")
print(f"Indices colonnes : {colonne}")"""