import csv
import requests
import os

def impression(infos, nom, chemin_livres) :
    en_tete = ["product_page_url", "universal_ product_code(upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating","image_url", "image"]

    """
    Fonction qui permet de créer un fichier csv. Nécessite trois paramètres: 
    les données, qui seront integrées au fichier csv. 
    le nom, qui servira à nommer le fichier
    le chemin d'accès, pour decider où créer le fichier.
    A chaque appel de cette fonction, si le nom du fichier est identique, les données déjà présentes seront écrasées.
    Le délimiteur des données est ' , ' 
    """

    chemin_fichier = chemin_livres + "/" + nom + ".csv"
    with open(chemin_fichier, "w") as f :
        writer = csv.writer(f, delimiter = ",")
        writer.writerow(en_tete)
        for info in infos :
            writer.writerow(info)


def telechargement(titre_livre, image_couverture, chemin_images) :

    #Téléchargement de l'image dans le dossier "images"
    #L'image est également renomé en fonction du nom du livre.
    nom_du_fichier = titre_livre + ".jpg"
    chemin_image = os.path.join(chemin_images, nom_du_fichier)
    f = open(chemin_image, "wb")
    response = requests.get(image_couverture)
    f.write(response.content)
    f.close()
    return chemin_image