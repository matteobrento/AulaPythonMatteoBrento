"""
Scrivere un programma Python che scarica l’xml della home page ANSA e stampa tutte le informazioni della prima notizia.
"""

import requests
import xml.etree.ElementTree as ET

def get_root():
    
    contenuto = requests.get("https://www.ansa.it/sito/ansait_rss.xml").text
    #print(contenuto.text)
    root = ET.fromstring(contenuto)
    return root


def informazioni(root):

    channel = root.find('channel')
    item = channel.find('item')

    if item is not None:

        titolo = item.find('title').text
        descrizione = item.find('description').text
        link = item.find('link').text
        data = item.find('pubDate').text
        print("Titolo:", titolo)
        print("Descrizione:", descrizione)
        print("Link:", link)
        print("Data di pubblicazione:", data)

    else:
        print("Nessuna notizia trovata.")


root = get_root()
informazioni(root)








