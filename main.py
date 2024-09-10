import requests
from bs4 import BeautifulSoup
import os
from creation_csv import load_data_books
import infos_livres

url = "http://books.toscrape.com"


def main(url):
    category_links = []
    category_names = []
    """
    La fonction crée le dossier "livres" et le dossier "images" à l'intérieur de celui-ci.
    Ensuite, elle récupère les liens de toutes les catégories, qui va servir à nomé les fichiers csv.
    Elle appelle la fonction "extract_data_books" pour récupérer toutes les informations des différents livres.
    puis, elle appelle la fonction "transform_data_books" pour transformer ces données.
    Elle utilise ensuite la fonction "load_data_books" pour les enregistrer dans des fichiers CSV.
    Elle appelle également la fonction "load_images" pour télécharger et renommer les images des livres.
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Créer le dossier "dossier livres" s'il n'existe pas déjà
    dossier_livres = "dossier livres"
    if not os.path.exists(dossier_livres):
        os.mkdir(dossier_livres)

    # Créer le dossier "images" à l'intérieur du dossier "dossier livres" s'il n'existe pas déjà
    dossier_images = os.path.join(dossier_livres, "images")
    if not os.path.exists(dossier_images):
        os.mkdir(dossier_images)
    
    pages = soup.find("div", class_="side_categories")
    infos_categories = pages.find("ul").find("li").find("ul")

    # Récupération des noms des catégories
    for name_categorys in infos_categories.children :
        if name_categorys.name :
            category_names.append(name_categorys.text.strip())

    # Récupération des liens des catégories
    for link_category in infos_categories.find_all("a") :
        category_links.append("https://books.toscrape.com/" + link_category.get("href"))

    # Enregistrement des données dans un fichier CSV nommé en fonction de la catégorie.
    # #Téléchargement de l'image dans le dossier "images"
    #L'image est également renomé en fonction du nom du livre.    
    for i,j in zip(category_names,category_links) :
        data_books = infos_livres.transformed_data_books(infos_livres.extract_data_books(j), dossier_images)
        load_data_books(i , dossier_livres, dossier_images, data_books)


main(url)

