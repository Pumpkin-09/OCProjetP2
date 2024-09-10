import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


def extract_data_books(url) :
    """
    Fonction qui prend en paramètre un lien url.
    Elle va scrap des données via le lien.
    """
    donnees_livre = []
    list_link = []
    link_book = []

    list_link.append(url)
    page = requests.get(url)
    soupe = BeautifulSoup(page.content, "html.parser")

    # Vérification du nombre de pages de la catégorie.
    pages = soupe.find("li", class_="next")
    while pages != None :
        next_page = pages.a.get("href")
        url_modif = url.replace("index.html", next_page)
        list_link.append(url_modif)
        page_modif = requests.get(url_modif)
        soupe = BeautifulSoup(page_modif.content, "html.parser")
        pages = soupe.find("li", class_="next")
    
    # Création d'une boucle sur les liens pour récupérer les données.
    for next_page in list_link :
        page = requests.get(next_page)
        link = BeautifulSoup(page.content, "html.parser")
        links = link.find_all("article")
        for i in links :
            link_book = (i.h3.a.get("href").replace("../../..", "http://books.toscrape.com/catalogue"))
            page = requests.get(link_book)
            soup = BeautifulSoup(page.content, "html.parser")

            # Récupération de la description du livre
            descriptions = soup.find("div", class_="sub-header")
            description_livre = verification_donnees(descriptions.find_next("p").string)
        
            # Récupération du UPC, des prix et du nombre en stock
            info_livre = []
            infos = soup.find_all("td")
            for info in infos :
                info_livre.append(info.string)

            # Récupération du titre
            titre = soup.find("h1")
            titre_livre = verification_donnees(titre.string)

            # Récuperation de la note du livre
            rating = soup.find("p", class_="star-rating")
            book_rating = verification_donnees(rating["class"][-1])

            # Récupération du nom de la catégorie du livre
            category = soup.find("ul", class_="breadcrumb")
            cat = category.find_all("li")
            catagory_livre = verification_donnees(cat[2].text.strip())

            # Récupération de l'URL de l'image du livre
            image = soup.find("img")
            image_couverture = urljoin("http://books.toscrape.com/", image.get("src"))
        
            # Regroupement des données dans un dictionaire
            donnees_livre.append({
                "product_page_url" : link_book,
                "universal_product_code (upc)" : info_livre[0],
                "title" : titre_livre,
                "price_including_tax" : info_livre[3],
                "price_excluding_tax" : info_livre[2],
                "number_available" : info_livre[5],
                "product_description" : description_livre,
                "category" : catagory_livre,
                "review_rating" : book_rating,
                "image_url" : image_couverture
            })    

    return donnees_livre



def transformed_data_books(data,chemin_image) :

    # Fonction qui va transformer les données.
    transformed_data = []
    for book in data :
        product_page_url = book["product_page_url"]
        universal_product_code = book["universal_product_code (upc)"]
        title = book["title"]
        price_including_tax = book["price_including_tax"]
        price_excluding_tax = book["price_excluding_tax"]
        number_available = book["number_available"]
        product_description = book["product_description"]
        category = book["category"]
        review_rating = remplacement_note(book["review_rating"])
        image_url = book["image_url"]
        nom_image = re.sub(r"\W", "_", book["title"])
        image = chemin_image
    
        transformed_data.append({
            "product_page_url" : product_page_url,
            "universal_product_code (upc)" : universal_product_code,
            "title" : title,
            "price_including_tax" : price_including_tax,
            "price_excluding_tax" : price_excluding_tax,
            "number_available" : number_available,
            "product_description" : product_description,
            "category" : category,
            "review_rating" : review_rating,
            "image_url" : image_url,
            "nom_image" : nom_image,
            "chemin_image" : image
        })
    return transformed_data



def remplacement_note(note) :

    # Fonction qui va transformer les notes qui on été récupérées en toutes lettres, en chiffres.
    remplacement = {
        "One" : "1 sur 5",
        "Two" : "2 sur 5",
        "Three" : "3 sur 5",
        "Four" : "4 sur 5",
        "Five" : "5 sur 5"
    }

    if note in remplacement :
        note_chiffre = remplacement[note]
    else :
        note_chiffre = "note non valide"
    
    return(note_chiffre)

def verification_donnees(variable) :
    # Fonction qui verifie la présence de données dans "variable"
    # si "variable" est nul, la fonction lui attribu la valeur "donnée non trouvée"
    # la fonction revoie "variable" modifier ou non
    if variable is None :
        variable = "donnée non trouvée"
    return variable

