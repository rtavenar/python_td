import requests
import pprint

URL_ADRESSES = "https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis"
URL_HOTELS = "https://tabular-api.data.gouv.fr/api/resources/3ce290bf-07ec-4d63-b12b-d0496193a535/data/"


def fetch_all_data(base_url, **params):
    all_rows = []
    page = 1

    while True:
        reponse = requests.get(base_url, params={**params, "page_size": 200, "page": page})
        reponse.raise_for_status()
        data = reponse.json()

        rows = data.get("data", [])
        if not rows:
            break

        all_rows.extend(rows)

        # Si moins de 200 lignes : dernière page
        if len(rows) < 200:
            break

        page += 1

    return all_rows


def villes_amis():
    reponse = requests.get(URL_ADRESSES)
    reponse.raise_for_status()
    amis = reponse.json()
    return sorted({ami["adresse"]["ville"] for ami in amis})


def hotels_par_ville(ville):
    cle_commune = ville.upper()
    donnees = fetch_all_data(URL_HOTELS, COMMUNE__exact=cle_commune)
    if not donnees:
        # Certaines communes composées sont enregistrées avec des tirets
        # (ex. "Château Gontier" -> "CHÂTEAU-GONTIER")
        donnees = fetch_all_data(URL_HOTELS, COMMUNE__exact=cle_commune.replace(" ", "-"))
    return [
        {
            "nom": hotel["NOM COMMERCIAL"],
            "adresse": hotel["ADRESSE"],
            "etoiles": hotel["CLASSEMENT"],
        }
        for hotel in donnees
    ]


def affiche_hotels_amis():
    for ville in villes_amis():
        print(f"Hôtels à {ville} :")
        for hotel in hotels_par_ville(ville):
            print(f"  * {hotel['nom']} - {hotel['adresse']} - {hotel['etoiles']}")


pprint.pprint(villes_amis())
affiche_hotels_amis()
