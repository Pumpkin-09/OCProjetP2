import csv
import requests
import os
import logging

def load_data_books(nom, dossier_livres, dossier_images, donnees) :
    # Enregistrement des données dans un fichier CSV nommé en fonction de la catégorie.
    en_tete = ["product_page_url", "universal_product_code (upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating","image_url","nom_image", "chemin_image"]
    
    try :
        logging.info(f"Création du fichier .csv de la catégorie {nom} et téléchargement des images des livres")
        name = os.path.join(dossier_livres, nom +".csv")
        with open(name, "w", encoding = "utf-8") as f :
            writer = csv.DictWriter(f, fieldnames=en_tete, delimiter = ",")
            writer.writeheader()
            for i in donnees :
                writer.writerow(i)

    except OSError as e :
        name = os.path.join(dossier_livres, "ERROR_NAME.csv")
        with open(name, "w", encoding = "utf-8") as f :
            writer = csv.DictWriter(f, fieldnames=en_tete, delimiter = ",")
            writer.writeheader()
            for i in donnees :
                writer.writerow(i)
        print(f"OS error : {e}")

    #Téléchargement de l'image dans le dossier "images"
    #L'image est également renomé en fonction du nom du livre.
    for image in donnees :
        nom_image = image["nom_image"]
                
        try :
            chemin_image = os.path.join(dossier_images, nom_image)
            f = open(chemin_image, "wb")
        except OSError as e :
            chemin_image = os.path.join(dossier_images, "ERROR_NAME.jpg")
            f = open(chemin_image, "wb")
            print(f"OS error : {e}")
        
        response = requests.get(image["image_url"])
        f.write(response.content)
        f.close()
