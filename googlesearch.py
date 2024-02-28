import time
import random
from googlesearch import *

# Paramètres
mot_cle = "Transformation Numérique"  # Votre mot-clé de recherche
nombre_de_pages = 2  # Nombre de pages de résultats à extraire
# Initialisation du fichier de sortie
fichier_sortie = open("contacts_google.txt", "wb")

# Parcours des pages de résultats
for i in range(nombre_de_pages):
    # Attente aléatoire pour éviter de surcharger Google
    attente = random.uniform(2, 5)
    time.sleep(attente)

    # Recherche Google
    recherche = googlesearch.googlesearch(mot_cle)
    recherche.results_per_page = 10
    recherche.page = i
    resultats = recherche.get_results()

    # Extraction des liens
    for res in resultats:
        fichier_sortie.write(res.url.encode("utf8"))
        fichier_sortie.write("\n")

fichier_sortie.close()
print("Extraction terminée. Les liens sont enregistrés dans contacts_google.txt.")
