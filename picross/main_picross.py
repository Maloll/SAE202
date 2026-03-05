from picross_maker import picrossMaker
from picross_valide import est_valide
import time
indices_ligne, indices_colonne = picrossMaker("picross/table.pic")


debut = time.perf_counter()

for _ in range(10000000) : 
    est_valide([1,0,0,1,1,1],indices_ligne[0])
print("fini")

est_valide([1,0,0,1,1,1],indices_ligne[0])

fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")