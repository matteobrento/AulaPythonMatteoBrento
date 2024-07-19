"""
Calcolo di Statistiche di Base

Testo dell'esercizio:

Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese. 

Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:

La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature
"""
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

def genera_valori():

    temperature = [18.0,18.5,19.0,19.5,20.0,20.5,21.0,21.5,22.0,22.5,23.0,23.5,24.0,24.5,25.0,25.5,26.0,26.5,27.0,27.5,28.0,28.5,29.0,29.5,30.0,30.5,31.0,31.5,32.0,32.5,33.0,33.5,34.0,34.5,35.0]
    temperature_df = []
    mesi_df = []
    citta = ["Bari", "Milano", "Torino", "Roma"]
    citta_df = []
    #giorni = np.arange(1,31)

    for i in range(30):
        temp = random.choice(temperature)
        temperature_df.append(temp)
    
    for i in range(30):
        cit = random.choice(citta)
        citta_df.append(cit)

    return temperature_df, citta_df, #giorni


def crea_dataframe():

    temperature_df, citta_df = genera_valori()

    data = {
        "Temperatura_Giornaliera":temperature_df,
        "Città":citta_df,
    }

    df = pd.DataFrame(data)
    print("DataFrame Iniziale: \n", df, "\n")
    return df

df = crea_dataframe()

def temperature(df):

    temp_max = df["Temperatura_Giornaliera"].max()
    temp_min = df["Temperatura_Giornaliera"].min()
    temp_media = df["Temperatura_Giornaliera"].mean()
    temp_mediana = df["Temperatura_Giornaliera"].median()
    print(f"Temperatura massima: {temp_max}°")
    print(f"Temperatura minima: {temp_min}°")
    print(f"Media delle temperature: {temp_media}°")
    print(f"Mediana delle temperature: {temp_mediana}°")

    return temp_max, temp_min, temp_media, temp_mediana

def plot_dati(df):
    plt.figure(figsize=(15, 5))

    
    plt.subplot(1, 3, 1)
    sns.histplot(df["Temperatura_Giornaliera"], bins=10, kde=True)
    plt.title("Distribuzione delle Temperature")
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Frequenza")

    
    plt.subplot(1, 3, 3)
    sns.scatterplot(x=df.index, y=df["Temperatura_Giornaliera"])
    plt.title("Temperatura Giornaliera")
    plt.xlabel("Giorni")
    plt.ylabel("Temperatura (°C)")

    plt.tight_layout()
    plt.show()

plot_dati(df)
