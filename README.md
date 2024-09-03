# OpenClassrooms projet 2: BOOKS TO SCRAPE
*version Beta*

## Description
<<<<<<< HEAD
Ce code permet de recuperer divers informations des livres du site http://books.toscrape.com ainsi que les images des differants livres.
les informatios en question sont :
=======
Ce code permet de récuperer divers informations des livres du site http://books.toscrape.com ainsi que les images des différents livres.
les informations en question sont :
>>>>>>> 6e256f8 (corrections)
- l'URL du livre
- l'Universal Product Code (UPC)
- le titre du livre
- le prix, taxe incluse
- le prix, taxe exclue
- la quantité disponible
- la description du produit
- la catégorie
- le rating
- l'URL de l'image
- le chemin d'accès local de l'image téléchargée

Les informations récuperées sont regroupées par catégorie, et chacune d'entre elles est stockée dans des fichiers csv distincts.
Les images quant à elles, sont renommées puis stockées dans un dossier à part.
Les données sont générées à la racine du projet, dans un dossier nommé "dossier livres" pour les catégories et dans un dossier nommé "images" pour les images.

<<<<<<< HEAD
## Instalation
### Python
Commencer par verifier si python est installé. Pour ce faire, ouvré l'invite de commande et saisisé :

`python --version`

si python n'est pas installé, suivier la documentation suivante en fonction de votre environement :
=======
## Installation
### Python
Commencer par vérifier si Python est installé. Pour ce faire, ouvrez l'invite de commande et saisisser :

`python --version`

Si Python n'est pas installé, suivez la documentation suivante en fonction de votre environnement :
>>>>>>> 6e256f8 (corrections)

[windows](https://docs.python.org/fr/3/using/windows.html)

[linux](https://docs.python.org/fr/3/using/unix.html) 

[mac](https://docs.python.org/fr/3/using/mac.html)

<<<<<<< HEAD
### le projet
lancé votre invite de commande, placez vous dans le dossier de votre choix avec la commande cd puis cloné le repository :

`git clone https://github.com/Pumpkin-09/OCProjetP2.git`

Placez vous ensuite dans le dossier OCProjetP2, toujours avec la commande cd, vous allez créé puis activez notre environement virtuel. 
#### Utilisé les commandes suivante :
##### Sous linux :

`python3 -m venv env`

pour la création de l'environement, puis :

`source env/bin/activate`

pour l'activé

##### Sous windows :

`python -m venv env`

pour la création de l'environement, puis :

`env\scripts\activate.bat`

pour l'activé.

il ne reste plus qu'a installer les packages :

`pip install -r requirements.txt`


Et voila, vous pouvez maintenant lancer le script grace a la commande qui suit
##### sous linux :

`python3 main.py`


##### Sous windows :

`python main.py`

=======
### Le projet
Lancez votre invite de commande, placez-vous dans le dossier de votre choix avec la commande cd puis clonez le repository :

`git clone https://github.com/Pumpkin-09/OCProjetP2.git`

Placez vous ensuite dans le dossier OCProjetP2, toujours avec la commande cd, vous allez créer puis activer votre environnement virtuel. 
#### Utilisez les commandes suivantes :
##### Sous linux :

`python3 -m venv env`

pour la création de l'environnement, puis :

`source env/bin/activate`

pour l'activer.

##### Sous windows :

`python -m venv env`

pour la création de l'environnement, puis :

`env\scripts\activate.bat`

pour l'activer.

Il ne reste plus qu'à installer les packages :

`pip install -r requirements.txt`


Et voilà, vous pouvez maintenant lancer le script grâce à la commande qui suit:
##### Sous linux :

`python3 main.py`


##### Sous windows :

`python main.py`

>>>>>>> 6e256f8 (corrections)
