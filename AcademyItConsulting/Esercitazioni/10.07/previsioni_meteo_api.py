"""
Create un programma python che permette tramite le api
https://open-meteo.com/en/docs (per le previsioni metereologiche) e
https://geocoding-api.open-meteo.com/v1/search?name=Berlin&count=1&language=it&format=json (per l’ottenimento in automatico della propria
langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione
metereologiche.
L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni.
"""

import requests
import json


def coordinate():
    citta=input("inserisci il nome della città: ")
    posizione= requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json")
    risposta=posizione.text
    conversione_dizionario=json.loads(risposta)
    if conversione_dizionario['results']:
        info = conversione_dizionario['results'][0]
        return {
            'citta': info['name'],
            'latitudine': info['latitude'],
            'longitudine': info['longitude']
        }
    else:
        print(f"Nessun risultato trovato per la città: {citta}")
        return None

dizionario=coordinate()
print(dizionario)






