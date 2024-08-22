import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from pprint import pprint

url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")


def scrap_livre(url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    description_livre = []
    descriptions = soup.find_all("p")
    for desc in descriptions:
       description_livre.append(desc.string)
    description = description_livre[3]


    info_livre = []
    infos = soup.find_all("td")
    for info in infos :
        info_livre.append(info.string)

    upc = info_livre[0]
    price_excl_taxe = info_livre[2]
    price_incl_taxe = info_livre[3]
    in_stock = info_livre[5]
    reviews_rating = info_livre[6]

    titre = soup.find("h1")
    titre_livre = titre.string

    categorys = []
    category = soup.find_all("a")
    for cat in category :
      categorys.append(cat.string)
    catagory_livre = categorys[3]

    image = soup.find("img")
    image_couverture = urljoin("http://books.toscrape.com/", image.get("src"))


    tab_info_livre = {
        "product_page_url" : url,
        "universal_product_code (upc)" : upc,
        "title" : titre_livre,
        "price_including_tax" : price_incl_taxe,
        "price_excluding_tax" : price_excl_taxe,
        "number_available" : in_stock,
        "product_description" : description,
        "category" : catagory_livre,
        "review_rating" : reviews_rating,
        "image_url" : image_couverture
    }

    with open("donnees_livres.csv", "a") as f:
        writer = csv.writer(f)
        for k, v in tab_info_livre.items():
            writer.writerow([k,v])


def scrap_category(url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    link_book = []
    links = soup.find_all("article")
    for i in links :
        link_book.append(i.h3.a.get("href").replace("../../..", "http://books.toscrape.com/catalogue"))

    for links_books in link_book :
        scrap_livre(links_books)
 

def Categorys(url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    new_link = []
    new_link.append(url)
    pages = soup.find("li", class_="next")
    while pages != None :
        next_page = pages.a.get("href")
        url_modif = url.replace("index.html", next_page)
        new_link.append(url_modif)
        page_modif = requests.get(url_modif)
        soup = BeautifulSoup(page_modif.content, "html.parser")
        pages = soup.find("li", class_="next")

    for categorys_links in new_link :
        scrap_category(categorys_links)

   

Categorys(url)
