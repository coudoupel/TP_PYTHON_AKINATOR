# TP_PYTHON_AKINATOR
## Mise en place de la solution
Pour réaliser ce projet, l'environnement devra être réalisé comme tel:

- Création d'une VM Debian 12
- Installation de poetry et python

Pour ce projet, j'ai voulu reproduire le jeu akinator grâce à un script python.

Je vais créer différents scripts pour ma solution:

- Un script python pour le fonctionnement global du projet
- Des scripts html/css pour l'interface web
- Un script json pour stocker les questions et réponses
### Schéma simplifié :
[![Image](https://i.goopics.net/18fa3j.png)](https://goopics.net/i/18fa3j)

## Description détaillée des scripts :

## `app.py` (Python/Flask) :  

#### Ce script contient l'application Flask qui gère la logique du jeu.  Il charge la base de données depuis le fichier `base_de_donnees.json`.

* Il gère les sessions utilisateur pour stocker l'état du jeu en cours.

* Il définit les différentes actions du jeu (page d'accueil, réponse à une question, recommencer).

-  Il interagit avec les templates HTML pour afficher l'interface utilisateur.

 

## `base_de_donnees.json` (JSON) :

#### Ce fichier contient l'arbre de décision du jeu.

* Chaque nœud de l'arbre représente une question et possède deux réponses (oui/non) menant à d'autres questions ou à des personnages.

* **`index.html` (HTML/CSS) :**  Ce template HTML affiche la question courante à l'utilisateur et permet de soumettre une réponse (oui/non).
 
* **`resultat.html` (HTML/CSS) :**  Ce template HTML affiche le résultat final du jeu, c'est-à-dire le personnage trouvé.

* Il inclut également des styles CSS pour la présentation comme des images ou des fonds
