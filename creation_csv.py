import csv

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
