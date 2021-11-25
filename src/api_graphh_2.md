---
title : API web d'accès aux données
subtitle: Planche de TD pour un cours dispensé à l'université de Rennes 2
language: fr
rights: Creative Commons CC BY-NC-SA
---


# Principe

Cet énoncé de TD va vous amener à effectuer des requêtes aux APIs que vous avez déjà manipulées dans les TD précédents, sous la forme de quelques mini-projets.

## Quel covoiturage ?

Dans cette partie, on suppose que l'on cherche à déterminer, parmi plusieurs choix possibles, un trajet optimal avec les contraintes suivantes :
* les points de départ et d'arrivée sont fixés
* on doit récupérer, sur le trajet, une personne en covoiturage et l'on peut choisir entre plusieurs personnes situées à des positions différentes.

La question peut par exemple être posée sous la forme suivante :

> Lors d'un trajet Rennes - Marseille, vaut-il mieux (en termes de temps de trajet) prendre quelqu'un à Paris, Lyon ou Marseille ?

1. Écrivez une fonction qui prend en entrée :
    * un lieu d'origine (sous la forme d'une chaîne de caractères)
    * une destination (sous la forme d'une chaîne de caractères)
    * une liste d'options sur le trajet (sous la forme d'une liste de chaînes de caractères)
    * un client d'API GraphHopper
    
   et retourne l'option correspondant au trajet le plus court (en temps).
