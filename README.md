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



##  Principe du jeu  
L'objectif du jeu est de **deviner un personnage** en posant une série de questions auxquelles le joueur doit répondre par **"oui"** ou **"non"**.  

Le jeu suit un **arbre de décision**, où chaque question mène à une autre question ou directement à un personnage.  



##  Fonctionnement pas à pas  

### Début du jeu  
- Lorsqu'un utilisateur arrive sur la page d'accueil, il reçoit **la première question** de l'arbre de décision.  
- Cette question est extraite du fichier `base_de_donnees.json` et affichée via `index.html`.  
- Exemple de première question affichée :  
  > **"Votre personnage a-t-il les cheveux bouclés ?"**  



### Réponse de l’utilisateur  
- L’utilisateur clique sur **"Oui"** ou **"Non"**, puis valide.  
- La réponse est envoyée via un formulaire en **POST** à l’URL `/reponse`.  
- Flask récupère cette réponse et **met à jour l’arbre dans la session utilisateur**.  
- Selon la réponse, l’application :  
  - Charge **une nouvelle question** (si d’autres questions existent).  
  - Ou affiche **le personnage deviné** (si c’est la fin de l’arbre).  



### Exemple d’un parcours dans l’arbre  
Prenons un extrait du fichier `base_de_donnees.json` :  

```json
{
    "question": "Votre personnage a-t-il les cheveux bouclés ?",
    "oui": "Norman",
    "non": {
        "question": "Porte-t-il des lunettes ?",
        "oui": "Angelo",
        "non": "Matteo"
    }
}
```

**Exemple de parcours :**  
1. L’utilisateur répond **"oui"** à la question _"A-t-il les cheveux bouclés ?"_  
   -  L’application répond immédiatement **"Norman"** 
2. Si l’utilisateur répond **"non"**, l’application pose une autre question :  
   - _"Porte-t-il des lunettes ?"_
3. Si **"oui"** → L’application affiche **"Angelo"**  
4. Si **"non"** → L’application affiche **"Matteo"**  

Chaque réponse **rétrécit le nombre de possibilités** jusqu’à arriver à **une seule réponse possible**.



### Fin du jeu  
- Une fois qu’un personnage est trouvé, il est affiché sur `resultat.html` :  

```html
<h1>Le personnage que j'ai deviné est : {{ personnage }}!</h1>
<img src="{{ url_for('static', filename='images/' + personnage + '.jpg') }}" alt="{{ personnage }}">
```

- L’utilisateur peut cliquer sur **"Recommencer"**, ce qui **réinitialise la session** et relance le jeu avec la première question.



## Résumé du fonctionnement global  
 **Affichage de la première question**  
 **L’utilisateur répond (oui/non)**  
 **L’application avance dans l’arbre de décision**  
 **Si une nouvelle question existe, elle est affichée**  
 **Si un personnage est trouvé, il est affiché**  
 **L’utilisateur peut recommencer le jeu**  


 ### Conclusion
Le projet Akinator en Python m'a permis de mettre en place un jeu interactif en ligne basé sur un arbre de décision. En utilisant Flask pour gérer la logique serveur et l'interface web.

À travers ce projet, nous avons abordé plusieurs aspects essentiels du développement web, comme la gestion des sessions, l’interaction avec des fichiers de données en format JSON, et l’intégration d’une interface utilisateur avec des templates HTML/CSS.

Le système de questions et réponses m'a permis de reproduire le principe du jeu Akinator, où chaque réponse de l'utilisateur affine progressivement les options jusqu'à deviner un personnage.

Le projet peut encore être amélioré en termes d'expérience utilisateur, de sécurisation, et de performance, mais il fournit une base solide pour explorer d'autres évolutions comme l’optimisation du code pour un usage en production.
