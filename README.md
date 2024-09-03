# OpenClassrooms projet 2: BOOKS TO SCRAPE
*version Beta*

## Description
Ce code permet de recuperer divers informations des livres du site http://books.toscrape.com ainsi que les images des differants livres.
les informatios en question sont :
- l'URL du livre
- l'Universal Product Code (UPC)
- le titre du livre
- le prix, taxe incluse
- le prix, taxe exclue
- la quantitédisponible
- la description du produit
- la catégorie
- le rating
- l'URL de l'image
- le chemin d'acces local de l'image téléchargée

les informations récuperé sont regroupé par categorie, et chacune d'entre elles, sont stocké dans des fichiers csv distincte.
Les images quant à elles, sont renomé puis stocker dans un dossier à part.
Les données, sont générées à la racines du projet, dans un dossier nomé "dossier livres" pour les categories et dans un dossier nomé "images" pour les images.

## Instalation
### Python
Commencer par verifier si python est installé. Pour ce faire, ouvré l'invite de commande et saisisé :

' python --version '

si python n'est pas installe, suivier la documentation suivante en fonction de votre environement :
[windows](https://docs.python.org/fr/3/using/windows.html)
[linux](https://docs.python.org/fr/3/using/unix.html)
[mac](https://docs.python.org/fr/3/using/mac.html)

### le projet
lancé votre invite de commande, placévous dans le dossier de votre choix avec la commande cd puis cloné le repository :
' git clone https://github.com/Pumpkin-09/OCProjetP2.git '

Placez vous ensuite dans le dossier OCProjetP2, toujours avec la commande cd, ,ous allez créé puis activé notre environement virtuel. 
Sous linux tapé les commandes suivante :

' python3 -m venv env '
pour la création de l'environement, puis :

' source env/bin/activate '
pour l'activé

Sous windows :

' python -m venv env '
pour la création de l'environement, puis :
' env\scripts\activate.bat '
pour l'activé.

il ne reste plus qu'a installer les packages :
' pip install -r requirements.txt '

Et voila, vous pouvez maintenant lancer le script grace a la commande qui suit
sous linux :
' python3 main.py '

Sous windows :
' python main.py '
