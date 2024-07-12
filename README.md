# L1_Sokoban
(2020) Sokoban en Python. Découverte de la programmation objet et de pygame.

Le principe du jeu est qu'un personnage doit pousser des caisses à des
cases spécifiques pour pouvoir passer au niveau suivant. Le personnage ne
peut se déplacer que dans les quatre directions et pousser une seule caisse à
la fois.Comme le personnage ne peut pas tirer de caisse, il est possible de se
retrouver bloqué après un mouvement mal choisi.

Un niveau est constitué de Murs, de Caisses, d'endroits où pousser les
caisses que l'on a renommé "Objectifs" et du Personnage.

Il nous fallait donc placer ces objets sur une interface graphique (pygame)
et les faire réagir lorsqu'ils rentrent en contact les une avec les autres : par
exemple si un personnage veut pousser une caisse il ne le peut que si derrière
celle ci il n'y a pas un mur ou une autre caisse, celui ci fonctionne de la même
manière, il ne peut pas traverser les murs ou les caisses.

Pas terminé (premier confinement) : Créer une fonctionnalité de résolution automatique de
niveau grâce a l'algorithme A*.
