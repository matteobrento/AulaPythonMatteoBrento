"""
Esercizio 1: Analisi di Vendite Fittizie

Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.

Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". I dati
devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.

Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.
Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.
Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto.
"""

import pandas as pd
import numpy as np
import random

def generazione_valori():
    citta = ["Bari", "Milano", "Torino"]
    df_citta = []
    prodotti = ["T-Shirt", "Felpa", "Pantaloncino"]
    df_prodotti = []
    vendite = np.random.randint(50, 400, size=15)
    date = np.random.randint(1, 31, size=15)

    for i in range(15):
        citta_casuale = random.choice(citta)
        df_citta.append(citta_casuale)

    for i in range(15):
        prodotto_casuale = random.choice(prodotti)
        df_prodotti.append(prodotto_casuale)

    return date, df_citta, df_prodotti, vendite

def crea_dataframe():
    
    date, df_citta, df_prodotti, vendite = generazione_valori()
    data = {
        "Giorno del mese di Luglio": date,
        "Città": df_citta,
        "Prodotto": df_prodotti,
        "Vendite": vendite
    }

    df = pd.DataFrame(data)
    print("\nDataFrame Iniziale: \n", df, "\n")
    return df

df = crea_dataframe()

pivot_df = df.pivot_table(values="Vendite", index="Prodotto", columns="Città", aggfunc="mean")
print("Vendite medie di ciascun prodotto per città: \n", pivot_df, "\n")

""" 
grouped_df = df.groupby('Prodotto').sum()
print("Vendite totali per ogni prodotto: \n", grouped_df) 
"""

grouped_df = df.groupby('Prodotto').agg({
    'Vendite': 'sum',
})
print("Vendite totali per ogni prodotto: \n", grouped_df) 

