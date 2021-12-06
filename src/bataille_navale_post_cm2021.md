---
title : Bataille navale
subtitle: Planche de TD pour un cours dispensé à l'université de Rennes 2
language: fr
author: Aurélie Lemaitre, Romain Tavenard
rights: Creative Commons CC BY-NC-SA
---
# Travail effectué en CM

1. Vérifier que vous connaissez les règles du jeu de bataille navale ([lien](https://fr.wikipedia.org/wiki/Bataille_navale_(jeu))).

2. En lisant soigneuseument les traces d'exécution ci-dessous, répondez aux questions suivantes :
* Que joue le joueur ?
* Quelles sont les différentes réponses possibles du système ?

3. Réfléchir aux structures de données à utiliser pour mémoriser la position des bateaux ainsi que les différents coups du joueur.

4. Réfléchir à une méthode permettant de traduire les coordonnées sous forme lettre/chiffre vers un numéro de ligne et de colonne.
Exemple : `"B2"`{.haskell} donne "2ème ligne, 2ème colonne".

# Fruit des réflexions de CM

![fullwidth](img/cm2021_1.jpg)&nbsp;
![fullwidth](img/cm2021_2.jpg)&nbsp;

En plus de ces deux tableaux qui présentent un pseudo-code gros grain et une ébauche de prototype des fonctions à créer, nous avons étudié les structures de données à utiliser.

Pour stocker les positions de tous les bateaux, un consensus est apparu sur la structure suivante : un dictionnaire ayant pour clés des noms de bateaux et pour valeurs des listes de positions.

Pour coder une position de bateau, deux options sont apparues : soit on conserve le codage sous forme de chaîne de caractères (`"A3"`), soit on code une position comme un tuple d'entiers correspondant aux indices de lignes et colonnes (`"A3"` devient alors `(0, 2)` ou `(1, 3)` selon que l'on indice à partir de 0 ou de 1).
**Chaque groupe de TD doit choisir comment il souhaite coder une position.**

Pour coder la grille, plusieurs options sont apparues :

* un dictionnaire ayant pour clés les noms de colonnes et pour valeurs des listes indiquant le contenu de chacune des cases de la colonne en question (`{"A": ["", "X", ..., "O", ""], "B": ...}`)
* une liste de listes similaire à ce qui avait été utilisé pour le TD TicTacToe (`[["", "X", ..., "O", ""], [...]]`)
* un dictionnaire ayant pour clés `"X"` et `"O"` et pour valeurs associées la listes des positions où l'on trouve ces symboles dans la grille (`{"X": [pos1, pos2, ...], "O": [pos6, pos7, ...` où `posN` est une position -- cf discussion sur le codage des positions plus haut)
* un dictionnaire ayant pour clés des positions et pour valeurs l'état de ces cases (`{pos1: "X", pos5: "O", ...}`)

**Chaque groupe de TD doit choisir comment il souhaite coder une grille.**


# Énoncé

5. Programmez (en Python) un jeu de bataille navale pour lequel la position des navires sera lue dans un fichier annexe dont voici un exemple contenant 2 navires nommés respectivement `1` et `2` :
```
1,D1,D2,D3
2,E4,F4
```
Le programme demandera au joueur de rentrer une case dans laquelle jouer jusqu'à ce qu'il ait coulé tous les bateaux.
Votre programme devra fournir une sortie du type :
```
Entrez une position pour jouer A1
À l'eau
   ABCDEFGHIJ
01:X         
02:          
03:          
04:          
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer C2
À l'eau
   ABCDEFGHIJ
01:X         
02:  X       
03:          
04:          
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer C4
À l'eau
   ABCDEFGHIJ
01:X         
02:  X       
03:          
04:  X       
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer D4
À l'eau
   ABCDEFGHIJ
01:X         
02:  X       
03:          
04:  XX      
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer F4
Touché
   ABCDEFGHIJ
01:X         
02:  X       
03:          
04:  XX O    
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer E4
Bateau 2 coulé
   ABCDEFGHIJ
01:X         
02:  X       
03:          
04:  XXOO    
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer D1
Touché
   ABCDEFGHIJ
01:X  O      
02:  X       
03:          
04:  XXOO    
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer D2
Touché
   ABCDEFGHIJ
01:X  O      
02:  XO      
03:          
04:  XXOO    
05:          
06:          
07:          
08:          
09:          
10:          
Entrez une position pour jouer D3
Bateau 1 coulé
   ABCDEFGHIJ
01:X  O      
02:  XO      
03:   O      
04:  XXOO    
05:          
06:          
07:          
08:          
09:          
10:          
Partie gagnée en 9 tours
```
