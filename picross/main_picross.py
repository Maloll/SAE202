from picross_maker import picrossMaker
from picross_valide import est_valide

indices_ligne, indices_colonne = picrossMaker("picross/table.pic")

print(f"indices : {indices_ligne[0]} - Ligne : 100111 - {est_valide([1,0,0,1,1,1],indices_ligne[0])}")