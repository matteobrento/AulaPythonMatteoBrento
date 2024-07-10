"""
Scaricare l’RSS di ANSA Ultime Notizie e convertirlo in un file CSV e un file html.
"""

import requests
import pandas as pd
import xml.etree.ElementTree as ET

df_col = ["titolo", "descrizione", "link", "data", "guid"]
df_row = []

def get_root():
    
    contenuto = requests.get("https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml").text
    #print(contenuto)
    root = ET.fromstring(contenuto)
    return root

root = get_root()
channel = root.find('channel')
item = channel.findall('item')

for info in item:
    titolo = info.find('title').text    if item is not None else None
    descrizione = info.find('description').text  if item is not None else None
    link = info.find('link').text   if item is not None else None
    data = info.find('pubDate').text    if item is not None else None
    guid = info.find('guid').text   if item is not None else None

    df_row.append({"titolo":titolo, "descrizione":descrizione, "link":link, "data":data, "guid":guid})

df = pd.DataFrame(df_row, columns=df_col)
print(df)

df.to_csv("notizie.csv", index=False)
df.to_html("notizie.html", index=False)

