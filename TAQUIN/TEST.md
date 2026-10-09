# RESOLUTION DU JEU DU TAQUIN AVEC L'ALGORITHME A*


### TAQUIN.py :
---Permet de modeliser un jeu du taquin qui a une solution, les coups valides

### plusCourtChemin.py :
---Implementation des ALGORITHME BFS,Dijkstra et A*

### heuristique.py :
--- Implementation de plusieurs heuristiques : Hingram, Manhattan, Linear Conflict et Corner Conflict
--- Implementation d'heuristiques efficaces : 1.4*Manhattan + 2.8*Linear Conflict + 2.8*Corner Conflict

## Prenons l'exemple d'un jeu 4*4 difficile
Exemple d'un jeu difficile:
5  13 8 9
4  12 7 3
10 11 1 15
6  14 2 

### Chemin Optimal avec heuristique sous-optimale -

Running A* with Manhattan heuristic
36
Nombre de nœuds visités : 4807321
Temps d'exécution : 354.8157193660736 secondes # Tres long
A* Manhattan path length: 52 # La distance optimale
['up', 'up', 'up', 'left', 'down', 'left', 'down', 'right', 'up', 'right', 'down', 'left', 'down', 'left', 'left', 'up', 'right', 'up', 'right', 'down', 'left', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'down', 'left', 'up', 'up', 'right', 'right', 'up', 'left', 'down', 'right', 'right', 'up', 'left', 'down', 'left', 'down', 'down', 'right', 'right']

### Chemin Optimal avec combinaisons d'heuritique optimale

Running A* with combined heuristic (Manhattan + Linear Conflict + Corner Conflict)
36 
Nombre de nœuds visités : 1286400
Temps d'exécution : 168.9850513935089 secondes
A* (Combined) path length: 52 # La distance optimale
['up', 'up', 'up', 'left', 'down', 'left', 'down', 'right', 'up', 'right', 'down', 'left', 'down', 'left', 'left', 'up', 'right', 'up', 'right', 'down', 'left', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'up', 'left', 'down', 'down', 'right', 'down', 'left', 'up', 'up', 'right', 'right', 'up', 'left', 'down', 'right', 'right', 'up', 'left', 'down', 'left', 'down', 'down', 'right', 'right']

### SUPERIORITE DE A* PONDERE

Running A* with combined heuristic (1.4 * Manhattan + 2.8 * Linear Conflict + 2.8 * Corner Conflict)
50.4
Nombre de nœuds visités : 15357 # 83 fois moins de memoire
Temps d'exécution : 1.9919261932373047 secondes # 85 fois plus rapide
A* (Combined) path length: 54 # Une longueur sous-optimale +2
['up', 'up', 'up', 'left', 'down', 'left', 'up', 'left', 'down', 'right', 'down', 'right', 'up', 'right', 'down', 'left', 'up', 'left', 'down', 'left', 'up', 'right', 'down', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'up', 'left', 'up', 'left', 'down', 'right', 'down', 'down', 'right', 'up', 'up', 'up', 'left', 'down', 'down', 'right', 'up', 'right', 'up', 'left', 'down', 'down', 'down', 'right']

## CEPENDENT! :
--- La superioritee de A* Pondere cede face a un simple 5*5 :

Running A* with combined heuristic (1.4 * Manhattan + 2.8 * Linear Conflict + 2.8 * Corner Conflict)
113.39999999999999
Nombre de nœuds visités : 1809386
Temps d'exécution : 361.73110365867615 secondes # plus de 6 minutes
A* (Combined) path length: 105                  # qui n'est meme pas necessairement optimal
['up', 'up', 'left', 'down', 'right', 'right', 'right', 'right', 'down', 'down', 'left', 'left', 'left', 'up', 'up', 'right', 'up', 'left', 'left', 'down', 'right', 'right', 'right', 'down', 'left', 'down', 'down', 'left', 'up', 'up', 'up', 'right', 'up', 'right', 'right', 'down', 'left', 'left', 'down', 'down', 'down', 'right', 'right', 'up', 'left', 'left', 'left', 'up', 'left', 'down', 'right', 'up', 'left', 'up', 'up', 'right', 'right', 'down', 'down', 'right', 'down', 'left', 'left', 'down', 'right', 'up', 'right', 'down', 'left', 'left', 'left', 'up', 'up', 'up', 'right', 'down', 'right', 'up', 'left', 'up', 'right', 'right', 'right', 'down', 'left', 'down', 'right', 'up', 'left', 'left', 'up', 'left', 'left', 'down', 'right', 'right', 'right', 'up', 'left', 'down', 'down', 'right', 'right', 'down', 'down']

#   Comment trouver une presque solution a un jeu insoluble ?
--- Trouver une presque solution pour un jeu non resoluble revient a minimiser le nombre de tuiles mal placees,
exactement comme pour un jeu resoluble. Donc il suffit de s'arreter lorsque 2 tuiles ou 1 tuile et la case vide sont mal placees.

7 5 4
8 2 6
3   1

Running A* with combined heuristic (1.4 * Manhattan + 2.8 * Linear Conflict + 2.8 * Corner Conflict...
26.599999999999998
Nombre de nœuds visités : 2947
Temps d'exécution : 0.21793031692504883 secondes
A* (Combined) path length: 25
['right', 'up', 'left', 'up', 'right', 'down', 'left', 'down', 'left', 'up', 'up', 'right', 'down', 'down', 'right', 'up', 'left', 'down', 'left', 'up', 'up', 'right', 'right', 'down', 'left']

1 2 3
4   6
7 8 5

11 5 8 3
15 14 9 1
6 2   7
4 13 12 10

1 2 3 4
5 6 7 8
9 10   12
13 14 15 11

#   (MHA*) Multi-Heuristique A* :
...

#   (IDA*) Iterative Deepening A* :
...