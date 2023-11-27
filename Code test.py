import requests
from datetime import datetime, timedelta
import pandas as pd
import json


def fetch_and_format_data(symbol, key, frequency): 
    # Faire l'appel à l'API #mensuel api_url = "https://api.statistiken.bundesbank.de/rest/data/{flowRef}/{key}"
    #  Returns the time series from the specified dataflow (e.g. BBDY1) with the specified key (e.g. A.B10.N.G100.P0010.A).
    
    
    api_url = f"https://api.statistiken.bundesbank.de/rest/data/{symbol}/{key}"
    
    
    headers = {"Content-Type": "application/json"}
    
    response = requests.get(api_url, headers=headers)

     # print(response.text)


    if response.status_code == 200:
            print("La donnée à bien été importé")
            print(response.json())

    else:
         print(f"Erreur lors de la requête à l'API. Code d'état : {response.status_code}")

fetch_and_format_data("BBEX3","A.AED.DEM.CA.AA.A04","A")
