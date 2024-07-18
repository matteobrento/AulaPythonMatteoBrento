"""
Esempio Pratico finale: Unione e Risistemazione

Supponiamo di avere due dataset: uno con le vendite
giornaliere di prodotti in varie città e l'altro con le
informazioni sul costo dei prodotti. Utilizzeremo pandas
per unire questi dataset e creare una tabella pivot per
analizzare le vendite totali per prodotto e città.

Dataset di esempio:

Vendite: Prodotto, Quantità, Città, Data
Costi: Prodotto, Costo per unità

Operazioni:

Unire i due dataset su "Prodotto".
Creare una tabella pivot con le vendite totali per
prodotto per città.
"""

import pandas as pd
import numpy as np
import random

def generazione_valori_df1():
    citta = ["Bari", "Milano", "Torino"]
    df_citta = []
    prodotti = ["T-Shirt", "Felpa", "Pantaloncino"]
    df_prodotti = []
    quantita = np.random.randint(50, 200, size=15)
    date = np.random.randint(1, 31, size=15)

    for i in range(15):
        citta_casuale = random.choice(citta)
        df_citta.append(citta_casuale)

    for i in range(15):
        prodotto_casuale = random.choice(prodotti)
        df_prodotti.append(prodotto_casuale)

    return date, df_citta, df_prodotti, quantita

def generazione_valori_df2():

    #df_prodotti = generazione_valori_df1()
    
    prodotti = ["T-Shirt", "Felpa", "Pantaloncino"]
    df_prodotti = []
    costo = np.random.randint(15, 150, size=15)

    for i in range(15):
        prodotto_casuale = random.choice(prodotti)
        df_prodotti.append(prodotto_casuale)

    return df_prodotti, costo

def crea_dataframe_vendite():
    
    date, df_citta, df_prodotti, quantita = generazione_valori_df1()
    data = {
        "Giorno del mese di Luglio": date,
        "Città": df_citta,
        "Prodotto": df_prodotti,
        "Quantità": quantita
    }

    df_vendite = pd.DataFrame(data)
    return df_vendite

def crea_dataframe_costi():
    
    df_prodotti, costo = generazione_valori_df2()

    data = {
        "Prodotto": df_prodotti,
        "Costo_Unità": costo
    }

    df_costi = pd.DataFrame(data)
    return df_costi

df_vendite = crea_dataframe_vendite()
df_costi = crea_dataframe_costi()

print("DataFrame Vendite: \n", df_vendite, "\n")
print("DataFrame Costi: \n", df_costi, "\n")

df_merge = pd.merge(df_vendite, df_costi, on = "Prodotto")
print("Merge dei due DataFrame: \n", df_merge, "\n")

pivot_table = df_merge.pivot_table(index='Prodotto', columns='Città', values='Quantità', aggfunc='sum')
print("Tabella pivot con le vendite totali per prodotto per città: \n", pivot_table)

