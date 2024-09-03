import requests
from bs4 import BeautifulSoup
import csv
from genericpath import exists
from pathlib import Path
import os
from urllib.parse import urljoin
from infos_livres import all_infos_livre
from creation_csv import impression
url = "http://books.toscrape.com"

def Soup(url) :
    #fonction qui permet, via une URL, de récuperer le code HTML grace à requests
    # et de parser ces données, via BeautifulSoup 
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

def main(url):
    cat_links = []
    cat_name = []
    """
    Fonction qui va récuperer les liens de toutes les catégories.
    Appeler la fonction all_infos_livres afin de récuperer toutes les informations des différents livres.
    Appeler la fonction impression pour les enregistrer dans des fichiers csv.
    Elle profite de la récuperation des liens pour extraire le nom des catégories,
    et la fonction impression va les utiliser pour nommer les fichiers csv.
    """

    if not exists("dossier livres") :
        os.mkdir("dossier livres")
    chemin = "dossier livres"

    categorys_scrap = Soup(url).find("div", class_="side_categories")
    categories = categorys_scrap.find("ul").find("li").find("ul")

    for category in categories.children :
        if category.name :
            cat_name.append(category.text.strip())

    for cat in categories.find_all("a") :
        cat_links.append("https://books.toscrape.com/" + cat.get("href"))

    for i,j in zip(cat_name,cat_links) :
        impression(all_infos_livre(j), i, chemin)

        

main(url)

