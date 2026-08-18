# Section 1 : Imports de module
import json
import requests
from pprint import pprint

# Section 2 : Définition de fonctions

# Bus de la STAR
def api_position_bus(url):
    reponse = requests.get(url)
    reponse.raise_for_status()
    return reponse.json()

def bus_en_service():
    url = "https://data.explore.star.fr/api/explore/v2.1/catalog/datasets/tco-bus-vehicules-position-tr/records?limit=-1&refine=etat%3AEn%20ligne"
    les_bus = api_position_bus(url)
    liste_pos = []
    for bus in les_bus["results"]:
        d = {}
        for cle in ["numerobus", "nomcourtligne", "destination", "ecartsecondes"]:
            d[cle] = bus[cle]
        d["position"] = bus["coordonnees"]
        liste_pos.append(d)
    return liste_pos

def nb_bus_en_avance(bus_en_ligne):
    nombre_bus_en_avance = 0
    for bus in bus_en_ligne:
        if bus["ecartsecondes"] > 0:
            nombre_bus_en_avance += 1
    return nombre_bus_en_avance

def ligne_de_bus_ecartensecondes(les_bus):
    dico_ligne_de_bus_ecartensecondes = {}
    for bus in les_bus:
        nomcourtligne = bus["nomcourtligne"]
        ecartensecondes = bus["ecartsecondes"]
        if nomcourtligne not in dico_ligne_de_bus_ecartensecondes:
            dico_ligne_de_bus_ecartensecondes[nomcourtligne] = [ecartensecondes]
        else:
            dico_ligne_de_bus_ecartensecondes[nomcourtligne].append(ecartensecondes)
    return dico_ligne_de_bus_ecartensecondes

# Enrichissement des données restaurants via l'API Open Data NYC
URL_API_NYC = "https://data.cityofnewyork.us/resource/43nn-pn8j.json"

def fetch_restaurants_par_type(cuisine):
    reponse = requests.get(URL_API_NYC, params={"cuisine_description": cuisine, "$limit": 50})
    reponse.raise_for_status()
    donnees = reponse.json()
    return [{"camis": r["camis"], "dba": r["dba"], "zipcode": r.get("zipcode")} for r in donnees]

def fetch_score_moyen_par_cuisine(liste_cuisines):
    scores_moyens = {}
    for cuisine in liste_cuisines:
        reponse = requests.get(URL_API_NYC, params={"cuisine_description": cuisine, "$limit": 50})
        reponse.raise_for_status()
        donnees = reponse.json()
        scores = [float(r["score"]) for r in donnees if r.get("score")]
        if scores:
            scores_moyens[cuisine] = sum(scores) / len(scores)
    return scores_moyens

def lecture_json(dossier, nom_fichier, encodage="utf-8"):
    with open(f"{dossier}/{nom_fichier}", "r", encoding=encodage) as fp:
        return json.load(fp)

def compte_par_cuisine(restaurants):
    compte = {}
    for restaurant in restaurants:
        cuisine = restaurant["cuisine"]
        compte[cuisine] = compte.get(cuisine, 0) + 1
    return compte

def compare_local_api(restaurants_locaux):
    compte_local = compte_par_cuisine(restaurants_locaux)
    for cuisine, n_local in compte_local.items():
        n_api = len(fetch_restaurants_par_type(cuisine))
        print(f"{cuisine} : {n_local} restaurants locaux, {n_api} restaurants API")

# Section 3 : Tests de fonctions définies et manipulations en mode "script"
if __name__ == "__main__":
    # 1-2. Position des bus de la STAR
    url = "https://data.explore.star.fr/api/explore/v2.1/catalog/datasets/tco-bus-vehicules-position-tr/records"
    bus_defaut = api_position_bus(url)
    print(len(bus_defaut["results"]))
    print(bus_defaut["total_count"])

    # 3.
    bus_en_ligne = bus_en_service()
    pprint(bus_en_ligne)

    # 4.
    print(nb_bus_en_avance(bus_en_ligne))

    # 5.
    pprint(ligne_de_bus_ecartensecondes(bus_en_ligne))

    # 6.
    print(fetch_restaurants_par_type("Italian"))

    # 7.
    print(fetch_score_moyen_par_cuisine(["Italian", "Chinese", "French"]))

    # 8.
    restaurants_locaux = lecture_json("data", "NYfood.json")
    compare_local_api(restaurants_locaux)
