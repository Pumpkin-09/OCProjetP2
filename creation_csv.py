import csv

def impression(infos, nom, chemin) :
    en_tete = ["product_page_url", "universal_ product_code(upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating","image_url", "image"]

    """
    fonction qui permet de crée un fichier csv. necessite trois parametres: 
    les données, qui seront integré au fichier csv. 
    le nom, qui serviras à nomé le fichier
    le chemin d'acces, pour decider d'ou crée le fichier.
    à chaque appel de cette fonction, si le nom du fichier est identique les données deja présente seront écrasé.
    le delimiteur des donnees est ' , ' 
    """
    chemin_fichier = chemin + "/" + nom + ".csv"
    with open(chemin_fichier, "w") as f :
        writer = csv.writer(f, delimiter = ",")
        writer.writerow(en_tete)
        for info in infos :
            writer.writerow(info)
