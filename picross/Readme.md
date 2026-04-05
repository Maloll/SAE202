## Manuel solveur picross

**PicrossMaker & fichier .pic** : 
* La fonction `picrossMaker` prend un fichier .pic et renvoie les indices des lignes et colonnes.
* Les fichiers .pic sont des fichiers composés uniquement de 0 et de 1 : les 0 sont les cases vides et les 1 sont les cases pleines.

**main_bourrin.py** :
* On choisit le fichier .pic au début (ex : `nomFich .pic : 10x10.pic`).
* Backtracking bourrin : rapide sur les picross tout petits, très lent à partir de 10x10.
* Dans le main bourrin : les cases pleines sont des 1 et les cases vides des 0.

**main_hybride.py** :
* On choisit le fichier .pic au début (ex : `nomFich .pic : 10x10.pic`).
* Propagation : on cherche toutes les cases certaines jusqu'à ce qu'on ne puisse plus. On note 1 les cases certaines, 2 les cases vides à 100% et 0 les cases inconnues.
* Backtracking hybride : grâce au travail de la propagation, on crée une liste des possibilités (on réduit la liste binaire de 32 000 à moins de 500) puis on fait du backtracking classique.
* Dans le main hybride, les cases pleines sont des 1, les cases inconnus des 0, et les cases vides des 2.