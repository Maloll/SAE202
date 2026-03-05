def est_valide(ligne,indices) :
    valide = True
    n = 0
    i = 0
    nb_indices = len(indices)
    for c in ligne  :
        if c !=0:
            n = n + 1
        elif n > 0 :
            if i > nb_indices and n == indices[i] :
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



"""indice = [1,3]
ligne = [1,0,1,1,1,1]
print(f"FAUX ? {est_valide(ligne,indice)}")

indice = [1,3]
ligne = [1,0,0,1,1,1]
print(f"BON ?  {est_valide(ligne,indice)}")"""