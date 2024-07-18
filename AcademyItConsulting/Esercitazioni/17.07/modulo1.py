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

def crea_dataframe():   #dataframe iniziale con i valori della slide
    data = {
        "Prodotto":["Computer", "Smartphone", "Tastiera", "Mouse", "Computer"],
        "Quantità":[30, 50, 70, 90, 20],
        "Prezzo_Unitario":[800, 400, 100, 50, 800],
        "Città":["Roma", "Milano", "Roma", "Napoli", "Milano"]
    }

    df = pd.DataFrame(data)
    print("DataFrame Iniziale: \n", df, "\n")

    return df   #ritorno il df

def totale_vendite(df): #aggiungo la colonna totale vendite come prodotto di quantità e prezzo unitario

    df["Totale_Vendite"] = df["Quantità"]*df["Prezzo_Unitario"]
    print("\nDataFrame con Totale_Vendite: \n", df, "\n")
    return df

def totale_vendite_per_prodotto(df):    #ho utilizzato groupby e agg trovati in internet per raggruppare per una colonna ed effettuare un operazione matematica

    raggruppamento = df.groupby("Prodotto").agg({
        "Totale_Vendite": "sum" #qui effettua la somma e la mette come valore 
    })
    print("\nProdotto con Totale Vendite: \n", raggruppamento, "\n")

def prodotto_piu_venduto(df):   #ho utilizzato idmax() per cercare l'id del valore più alto della colonna specificata

    prodotto_piu_venduto = df["Quantità"].idxmax()
    print("\nIl prodotto più venduto è l'ID in posizione: ", prodotto_piu_venduto, "\n")

def citta_piu_vendite(df):  #ho utilizzato idmax() per cercare l'id del valore più alto della colonna specificata

    citta_piu_vendite = df["Città"].idxmax()
    print("\nLa città con il maggior numero di vendite è l'ID in posizione: ", citta_piu_vendite, "\n")

def filtro_vendite(df): #try-except per il valore da input e creo un filtro che mi fa stampare un nuovo df con totale vendite maggiore del valore passatovi
    try:
        while True:
            val = int(input("\nInserisci il valore totale di vendite da usare come filtro del DataFrame: "))
            break
    except ValueError as e:
            print("\nErrore nel valore passato:", e, "\nInserisci un valore intero valido! \n")
    df = totale_vendite(df)
    df_filtro = df[df["Totale_Vendite"]>val]
    print("\nNuovo DataFrame con Totale Vendite > di un valore: \n", df_filtro, "\n")

def ordinamento_decrescente(df):    #utilizzo il metodo sort_values con ascending a false per ordinamento decrescente

    df_ordinato = df.sort_values(by="Totale_Vendite", ascending=False)
    print("\nDataFrame ordinato in modo decrescente: \n", df_ordinato, "\n")

def visualizza_numero_vendite_per_citta(df):    #uso groupby per raggruppare per città e poi size per contare le righe di vendita per ogni città

    vendite_per_citta = df.groupby("Città").size()
    print("Numero di vendite per città:\n", vendite_per_citta, "\n")

def menu_pandas():  #menu

    print("\nMenu:")
    print("1. Stampa DataFrame con Totale_Vendite (Quantità*Prezzo_Unitario)")
    print("2. Totale delle vendite per prodotto")
    print("3. Prodotto più venduto")
    print("4. Città con maggior numero di vendite")
    print("5. Totale vendite maggiore di un valore scelto da input")
    print("6. Ordinamento decrescente per Totale_Vendite")
    print("7. Visualizza numero vendite per città\n")










