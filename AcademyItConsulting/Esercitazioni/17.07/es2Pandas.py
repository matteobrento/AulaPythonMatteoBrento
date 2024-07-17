"""
Esercizio 2: Manipolazione e Aggregazione dei Dati

Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.

Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

Caricare i dati in un DataFrame.
Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
Trovare il prodotto più venduto in termini di Quantità.
Identificare la città con il maggior volume di vendite totali.
Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
Visualizzare il numero di vendite per ogni città.
"""

import pandas as pd
import numpy as np


data = {
    "Prodotto":["Computer", "Smartphone", "Tastiera", "Mouse", "Computer"],
    "Quantità":[30, 50, 70, 90, 20],
    "Prezzo_Unitario":[800, 400, 100, 50, 800],
    "Città":["Roma", "Milano", "Roma", "Napoli", "Milano"]
}

df = pd.DataFrame(data)
print("DataFrame Iniziale: \n", df, "\n")

df["Totale_Vendite"] = df["Quantità"]*df["Prezzo_Unitario"]
print("DataFrame con Totale_Vendite: \n", df, "\n")

raggruppamento = df.groupby("Prodotto").agg({
    "Totale_Vendite": "sum"
})
print("Prodotto con Totale Vendite: \n", raggruppamento, "\n")

""" 
prodotto_piu_venduto = df.groupby("Prodotto").agg({
    "Quantità": "max"
})
print("Prodotto più venduto: \n", prodotto_piu_venduto, "\n")

colonna_quantita = df["Quantità"]
valore_massimo = colonna_quantita.max()
print("Quantità maggiore: ", valore_massimo) 
"""

prodotto_piu_venduto = df["Quantità"].idxmax()
print("Il prodotto più venduto è l'ID in posizione: ", prodotto_piu_venduto, "\n")

citta_piu_vendite = df["Città"].idxmax()
print("La città con il maggior numero di vendite è l'ID in posizione: ", citta_piu_vendite, "\n")








