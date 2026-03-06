from picross_maker import picrossMaker
from picross_valide import est_valide
import time
indices_ligne, indices_colonne, picross = picrossMaker("picross/table.pic")

print(indices_ligne)
print(indices_colonne)
debut = time.perf_counter()

for _ in range(1000000) : 
    est_valide([1,0,0,1,1,1],indices_ligne[0])
print("fini")

fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")