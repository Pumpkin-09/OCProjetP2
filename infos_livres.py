from genericpath import exists
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def Soup(url) :
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

def all_infos_livre(url) :

    """
    Fonction qui prend en paramètre un lien url.
    Elle va scrap des données via le lien.
    Elle renvoit une liste de 11 éléments
    """

    new_link = []
    link_book = []
    new_link.append(url)
    pages = Soup(url).find("li", class_="next")
    while pages != None :
        next_page = pages.a.get("href")
        url_modif = url.replace("index.html", next_page)
        new_link.append(url_modif)
        page_modif = requests.get(url_modif)
        soup = BeautifulSoup(page_modif.content, "html.parser")
        pages = soup.find("li", class_="next")
    
    for next_page in new_link :
        links = Soup(next_page).find_all("article")
        for i in links :
            link_book.append(i.h3.a.get("href").replace("../../..", "http://books.toscrape.com/catalogue"))

    donnees_livre = []
    for j in link_book :
        #Récupération de la description du livre
        descriptions = Soup(j).find("div", class_="sub-header")
        description_livre = descriptions.find_next("p").text
        
        #Récupération du UPC, des prix, du nombre en stock et du range
        info_livre = []
        infos = Soup(j).find_all("td")
        for info in infos :
            info_livre.append(info.string)

        #Récupération et si besoin, modification du titre
        titre = Soup(j).find("h1")
        t_l = titre.string
        titre_livre = t_l.replace("/", " ")

        #Récupération du nom de la catégorie du livre
        category = Soup(j).find("ul", class_="breadcrumb")
        cat = category.find_all("li")
        catagory_livre = cat[2].text.strip()

        #Récupération de l'URL de l'image du livre
        image = Soup(j).find("img")
        image_couverture = urljoin("http://books.toscrape.com/", image.get("src"))

        #Création d'un dossier image et téléchargement de l'image dans le dossier
        #L'image est également renomé en fonction du nom du livre.
        if not exists("images"):
            os.mkdir("images")
        nom_du_fichier = titre_livre + ".jpg"
        chemin_image = os.path.join("images", nom_du_fichier)

        f = open(chemin_image, "wb")
        response = requests.get(image_couverture)
        f.write(response.content)
        f.close()

        desc_livre = [j, info_livre[0],titre_livre, info_livre[3], info_livre[2], info_livre[5], description_livre, catagory_livre, info_livre[6], image_couverture, chemin_image]
        donnees_livre.append(desc_livre)
    return donnees_livre
