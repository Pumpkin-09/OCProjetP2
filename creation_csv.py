import csv
import requests
import os

def load_data_books(nom, dossier_livres, dossier_images, donnees) :
    # Enregistrement des données dans un fichier CSV nommé en fonction de la catégorie.
    en_tete = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating","image_url","nom_image", "chemin_image"]
    name = os.path.join(dossier_livres, nom +".csv")
    try :
        with open(name, "w", newline = "", encoding = "utf-8") as f :
            writer = csv.DictWriter(f, fieldnames=en_tete, delimiter = ",")
            writer.writeheader()
            for i in donnees :
                writer.writerow(i)

    except OSError as e :
        with open("ERROR_NAME", "w", newline = "", encoding = "utf-8") as f :
            writer = csv.DictWriter(f, fieldnames=en_tete, delimiter = ",")
            writer.writeheader()
            for i in donnees :
                writer.writerow(i)
        print(f"OS error : {e}")

    #Téléchargement de l'image dans le dossier "images"
    #L'image est également renomé en fonction du nom du livre.
    for image in donnees :
        nom_du_fichier = image["nom_image"] + ".jpg"
        nom_image = nom_du_fichier
        chemin_image = os.path.join(dossier_images, nom_image)
        try :
            f = open(chemin_image, "wb")
        except OSError as e :
            f = open("ERROR_MANE.jpg", "wb")
            print(f"OS error : {e}")
        
        response = requests.get(image["image_url"])
        f.write(response.content)
        f.close()
