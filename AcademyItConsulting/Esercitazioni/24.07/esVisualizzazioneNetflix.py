"""
Sulla base del dataframe scaricato in precedenza con i dati Netflix:
- Grafico a Torta con le percentuali di prodotti Film o Serie TV;
- Grafico con da distribuzione dei prodotti per paese;
- Grafico con andamento dell'aggiunta dei prodotti nel corso del tempo.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def carica_da_csv():

    df = pd.read_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\24.07\\netflix_titles.csv")
    print("DataFrame Iniziale: \n", df, "\n")
    return df

df = carica_da_csv()

def controlla_valori_nulli(df):

    print(f"Elenco valori nulli:\n{df.isnull().sum()}")

def pulizia_country(df):

    stati = ["United States", "India", "Australia", "United Kingdom", "France", "Italy", "Russia"]

    df["country"] = df["country"].fillna(random.choice(stati))
    print("DataFrame con Colonna Country Ripulita: \n", df, "\n")
    #df['country'] = df['country'].str.split(', ')
    return df

df_pulito = pulizia_country(df)
#controlla_valori_nulli(df_pulito)

def grafico_a_torta(df_pulito):

    conteggio_type = df_pulito['type'].value_counts()   #conta il numero di serie tv e film che ci sono nel dataset

    plt.figure(figsize=(8, 8))   #grandezza del grafico 8x8 pollici

    #Crea un grafico a torta
    #conteggio_type sono i dati che vedremo sul grafico
    #autopct serve per specificare sulle varie fette la percentuale (1.1 sta per un numero con la virgola)
    #colors sono i colori delle fette 
    plt.pie(conteggio_type, labels=conteggio_type.index, autopct='%1.1f%%', colors=['#FFFF00','#FF0000'])
    plt.title('Percentuali di prodotti Film o Serie TV su Netflix')
    plt.show()

def grafico_distribuzione(df_pulito):

    conteggio_paesi = df_pulito['country'].value_counts().head(20) 
    plt.figure(figsize=(12, 8))
    plt.barh(conteggio_paesi.index, conteggio_paesi.values, color='skyblue')
    plt.title('Distribuzione dei Prodotti per Paese su Netflix')
    plt.xlabel('Numero di Prodotti')
    plt.ylabel('Paese')
    plt.show()

def raggruppa_e_crea(df):

    new = df_pulito['release_year'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.plot(new.index, new.values)
    plt.title("Aggiunta dei prodotti nel corso del tempo")
    plt.xlabel('Anno')
    plt.ylabel('Numero di prodotti aggiunti') 
    plt.grid(True)
    plt.show()

grafico_a_torta(df_pulito)
grafico_distribuzione(df_pulito)
raggruppa_e_crea(df_pulito)





