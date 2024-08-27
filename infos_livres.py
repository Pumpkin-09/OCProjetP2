import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def Soup(url) :
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

def all_infos_livre(url) :
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

    description_livre = []
    donnees_livre = []
    for j in link_book :
        descriptions = Soup(j).find_all("p")
        for desc in descriptions:
           description_livre.append(desc.string)
        description = description_livre[3]

        info_livre = []
        infos = Soup(j).find_all("td")
        for info in infos :
            info_livre.append(info.string)

        titre = Soup(j).find("h1")
        titre_livre = titre.string

        categorys = []
        category = Soup(j).find_all("a")
        for cat in category :
          categorys.append(cat.string)
        catagory_livre = categorys[3]

        image = Soup(j).find("img")
        image_couverture = urljoin("http://books.toscrape.com/", image.get("src"))

        desc_livre = [j, description_livre[3], info_livre[0], info_livre[2], info_livre[3], info_livre[5], info_livre[6], titre_livre, catagory_livre, image_couverture]
        donnees_livre.append(desc_livre)
    return donnees_livre