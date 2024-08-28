import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
from infos_livres import all_infos_livre
from creation_csv import impression
url = "http://books.toscrape.com"

def Soup(url) :
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

def main(url):
    cat_links = []
    cat_name = []

    categorys_scrap = Soup(url).find("div", class_="side_categories")
    categories = categorys_scrap.find("ul").find("li").find("ul")

    for category in categories.children :
        if category.name :
            cat_name.append(category.text.strip())

    for cat in categories.find_all("a") :
        cat_links.append("https://books.toscrape.com/" + cat.get("href"))

    for i,j in zip(cat_name,cat_links) :
        impression(all_infos_livre(j), i)

        

main(url)

