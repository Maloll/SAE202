from est_valide import est_valide
import time

debut = time.perf_counter()

indice = [1,3]
ligne2 = [1,0,1,1,1,0]
for i in range(100000):
    {est_valide(ligne2,indice)}


print("fini")
fin = time.perf_counter()
print(f"Exécuté en : {(fin - debut) * 1000:.4f} ms")