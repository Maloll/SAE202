## Manuelle solveur picross

**PicrossMaker & fichier .pic** : 
* La fonction picrossMaker prend un fichier .pic, et renvoie les indices des lignes et colonnes
* Les fichiers.pic sont des fichiers composés uniquement de 0 et de 1, les 0 sont les cases vides et les 1 sont les cases pleines.

**main_debile.py** :
* On choisi le fichier .pic au début (ex : `nomFich .pic : 10x10.pic`)
* Backtracking bourrin, rapide sur picross tout petits, tres lent a partir de 10x10

**main_hybride.py**
* On choisi le fichier .pic au début (ex : `nomFich .pic : 10x10.pic`)
* Propagation : On cherche toutes les cases certaines jusqu'a ce qu'on ne puisse plus, on note 1 les cases certaines, 2 les cases vide a 100% et 0 les cases inconnus
* Backtracking hybride : Grace au travail de la propagation on creer une liste des possibilités (on reduit la liste binaire de 32000 a moins de 500) puis on fais du backtracking classique.