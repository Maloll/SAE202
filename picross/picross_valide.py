def est_valide(ligne,indices) :
    valide = True
    n = 0
    i = 0
    for c in ligne + [0] :
        if c !=0:
            n = n + 1
        elif n > 0 :
            if n == indices[i] :
                i = i + 1
                n = 0
            else :
                valide = False
                break
            
    return valide


"""indice = [1,3]
ligne = [1,0,1,1,1,1]
print(f"FAUX ? {est_valide(ligne,indice)}")

indice = [1,3]
ligne = [1,0,0,1,1,1]
print(f"BON ?  {est_valide(ligne,indice)}")"""