"""
L'obiettivo di questo esercizio è generare un set di dati di serie temporali
utilizzando NumPy, analizzarli con pandas e visualizzare i risultati usando
Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:

Generazione dei Dati: Utilizzare NumPy per generare una serie temporale
di 365 giorni di dati, simulando il numero di visitatori giornalieri in
un parco. Assumere che il numero medio di visitatori sia 2000 con una
deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
tempo per simulare l'aumento della popolarità del parco.

Creazione del DataFrame: Creare un DataFrame pandas con le date come
indice e il numero di visitatori come colonna.

Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la
deviazione standard.

Visualizzazione dei Dati:
Creare un grafico a linee del numero di visitatori giornalieri.
Aggiungere al grafico la media mobile a 7 giorni per mostrare la
tendenza settimanale.
Creare un secondo grafico che mostri la media mensile dei visitatori.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def genera_valori():

    date = pd.date_range(start='2023-01-01', periods=365, freq='D')

    media = 2000
    dev_standard = 500

    visitatori = np.random.normal(loc=media, scale=dev_standard, size=365)
    trend = np.linspace(0, 50, 365)
    visitatori+=trend

    return date, visitatori

def crea_dataset():

    date, visitatori = genera_valori()

    data = {
        "Data":date,
        "Visitatori":visitatori
    }

    df = pd.DataFrame(data)
    df.set_index("Data", inplace=True)
    print("DataFrame Iniziale con il Trend di 0.2 applicato: \n", df, "\n")
    
    return df

df = crea_dataset()

def media_e_std(df):

    media = df.resample("M").mean()
    print("La media di visitatori mensili è: \n", media, "\n")
    deviazione_standard = df.resample("M").std()
    print("La deviazione standard di visitatori mensili è: \n", deviazione_standard, "\n")

    return media, deviazione_standard

def grafico_a_linee_visitatori_giornalieri(df, media):

    sns.set(style="whitegrid")
    #Grafico a linee dei visitatori giornalieri
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df, x=df.index, y='Visitatori', label='Visitatori Giornalieri')
    plt.show()

    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 7))
    df['Media Mobile 7 Giorni'] = df['Visitatori'].rolling(window=7).mean()
    sns.lineplot(data=df, x=df.index, y='Media Mobile 7 Giorni', label='Media Mobile 7 Giorni', linestyle='--')
    plt.show()

    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=media, x=media.index, y='Visitatori', marker='o', linestyle='-')
    plt.show()

media, deviazione_standard = media_e_std(df)
grafico_a_linee_visitatori_giornalieri(df, media)

