def est_valide(ligne,indices) :
    valide = True
    n = 0
    i = 0
    nb_indices = len(indices)

    if nb_indices == 0:
        return sum(ligne) == 0 # On sort direct si ya pas d'indices
    
    # c = case, n = nombre, i = nombre d'indice actuel
    # tant que c != 1 on augmente le nombre
    # si le nombre (n) depasse le premier indice ou le nombre d'indice actuel (i) dépasse le nombre d'indice total : on return false
    for c in ligne  :
        if c !=0:
            n = n + 1
        elif n > 0 :
            if i < nb_indices and n == indices[i] :
                i = i + 1
                n = 0
            else :
                return False
    if n > 0:
        if i < nb_indices and n == indices[i] :
            i = i + 1
        else :
            return False
    
    return valide and i == nb_indices


def valide_hybride(bin, ligne, indice):
    # un est_valide qui verifie les possibilités en fonction des cases certaines
    for i, c in enumerate(ligne):
        if (c == 1 and bin[i] == 0) or (c == 2 and bin[i] == 1):  # si la proposition est a 1 quand la ligne est a 0 || quand la proposition est a 1 alors que la ligne a 2 (croix): return False
            return False
    return est_valide(bin, indice)



"""indice = [1,3]
ligne = [1,0,1,1,1,1]
print(f"FAUX ? {est_valide(ligne,indice)}")

indice = [1,3]
ligne2 = [1,0,1,1,1,0]
print(f"BON ?  {est_valide(ligne2,indice)}")"""