import requests
from datetime import datetime, timedelta
import pandas as pd
import json

# Définir les séries à importer avec leurs métadonnées
# 2020 = 100 Baseline par rapport à 2020
series_list = [
    {
        "symbol": "BBDP1",
        "key" : "M.DE.N.VPI.C.A00000.I20.A",
        "frequency": "M",
        "title": "Consumer Price Index",
        "description": "Overall Increase in Prices for a given basket of goods",
        "unit": "2020=100",
        "adjustments": "Unadjusted"
    },
    {
        "symbol": "BBDP1",
        "key":"A.DE.N.VPI.C.A00000.I20.A",
        "frequency": "A",
        "title": "Consumer Price Index",
        "description": "Overall Increase in Prices for a given basket of goods",
        "unit": "2020=100",
        "adjustments": "Unadjusted"
    },
    #...
]
# Fonction pour formater la date selon la fréquence
def format_date(timestamp, frequency):
    if frequency == 'M': # Mets la journée au 1er du mois
        return timestamp.replace(day=1)
    elif frequency == 'Q': # Mets le mois au 1er janvier avec 3 mois entre chaque observation 
        return timestamp.replace(month=1, day=1)
    elif frequency == 'A': # Mets le mois au 1er janvier avec 1 an entre chaque observartion
        return timestamp.replace(month=1, day=1)
    else:
        return timestamp

# Fonction pour faire un appel à l'API et formater les données
def fetch_and_format_data(symbol, key, frequency): 
    # Faire l'appel à l'API #mensuel api_url = "https://api.statistiken.bundesbank.de/rest/data/{flowRef}/{key}"
    #  Returns the time series from the specified dataflow (e.g. BBDY1) with the specified key (e.g. A.B10.N.G100.P0010.A).
    
    
    api_url = f"https://api.statistiken.bundesbank.de/rest/data/{symbol}/{key}"
    
    # header pour load au format json
    headers = {"accept": "application/json"}
    
    response = requests.get(api_url, headers=headers)

    
    
    # S'assurer que la data à bien été importée, voir le contenu
    if response.status_code == 200:
            print("La donnée à bien été importé")
            data = response.json()
            print(response.json())
    
    # Sinon print une erreur
    else:
         print(f"Erreur lors de la requête à l'API. Code d'état : {response.status_code}")

    # Formated la data en fonction des critères voulus
    # Ainsi qu'appliquer la fonction format_date, pour mettre la date en fonction des différentes fréquences au format voulu
    formatted_data = [
            {
                'id': symbol,
                'timestamp': format_date(entry['TIME_PERIOD'], frequency),
                'country_id': entry['country_id'],
                'value': entry['value']
            }
            for entry in data   
            ]
    return formatted_data


data_format = fetch_and_format_data("BBDP1","M.DE.N.VPI.C.A00000.I20.A","M")

# Création d'un DataFrame Pandas

df = pd.DataFrame(data_format)

# Affichage du dataframe
print(df)
        
    

