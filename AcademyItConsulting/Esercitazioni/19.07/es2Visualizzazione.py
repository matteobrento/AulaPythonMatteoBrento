"""
Esercizio Medio: Normalizzazione dei Dati

Testo dell'esercizio:

Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 

Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.

Fornisci un codice che:

Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
Applichi la normalizzazione min-max alle colonne altezza e peso.
Stampa sia il DataFrame originale sia quello modificato per compararli.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def genera_valori():

    altezza = np.random.randint(140, 200, 10)   #cm
    peso = np.random.randint(40, 100, 10)   #kg
    eta = np.random.randint(10, 70, 10)

    return altezza, peso, eta

def crea_dataframe():

    altezza, peso, eta = genera_valori()

    data = {
        "Altezza":altezza,
        "Peso":peso,
        "Età":eta
    }

    df = pd.DataFrame(data)
    print("DataFrame Iniziale: \n", df.to_string(index=False), "\n")
    return df

df = crea_dataframe()

def normalizzazione(df):

    colonne = ["Altezza", "Peso"]
        
    for colonna in colonne:
        min_value = df[colonna].min()
        max_value = df[colonna].max()
        df[colonna] = (df[colonna] - min_value) / (max_value - min_value)
        
    print("DataFrame con Altezza e Peso normalizzate: \n", df[colonne].to_string(index=False), "\n")

def grafici(df):
    
    plt.figure(figsize=(15, 5))
    x = df["Età"]
    y = df["Peso"]

    plt.bar(x, y, color="red")
    plt.title('Grafico a Barre')
    plt.xlabel('Età')
    plt.ylabel('Peso')
    plt.show()

    plt.figure(figsize=(15, 5))
    x = df["Età"]
    y = df["Altezza"]

    plt.bar(x, y, color="red")
    plt.title('Grafico a Barre')
    plt.xlabel('Età')
    plt.ylabel('Altezza')
    plt.show()

    plt.figure(figsize=(15, 5))
    x = df["Altezza"]
    y = df["Peso"]

    plt.bar(x, y, color="red")
    plt.title('Grafico a Barre')
    plt.xlabel('Altezza')
    plt.ylabel('Peso')
    plt.show()

grafici(df)

    
        