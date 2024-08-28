import csv

def impression(infos, nom) :
    en_tete = ["product_page_url", "universal_ product_code(upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]

    with open(nom, "a") as f :
        writer = csv.writer(f, delimiter = ",")
        writer.writerow(en_tete)
        for info in infos :
            writer.writerow(info)
