"""
Esercizio 1: Analisi Esplorativa dei Dati

Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.

Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 

Caricare i dati in un DataFrame autogenerandoli casualmente .
Visualizzare le prime e le ultime cinque righe del DataFrame.
Visualizzare il tipo di dati di ciascuna colonna.
Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
Identificare e rimuovere eventuali duplicati.
Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
Salvare il DataFrame pulito in un nuovo file CSV.
"""

import pandas as pd
import numpy as np
import random


""" nomi = ["Matteo", "Amalia", "Danilo", "Davide", "Antonio", "Valentina"]
nomi_df = []
for i in range(10):
    nome_casuale = random.choice(nomi)
    nomi_df.append(nome_casuale)

citta = ["Roma", "Milano", "Napoli", "Torino", "Palermo", "Bologna"]
citta_df = []
for i in range(10):
    citta_casuale = random.choice(citta)
    citta_df.append(citta_casuale)


eta = np.random.randint(10, 80, size=10)
salari = np.random.randint(1500, 3000, size=10)

data = {
        "Nome": nomi_df,
        "Età": eta,
        "Città": citta_df,
        "Salario": salari
    }

df = pd.DataFrame(data)
print(df, "\n") """


def generazione_valori():   #funzione per generare i valori con cui riempire il df

    nomi = ["Matteo", "Amalia", "Danilo", "Davide", "Antonio", "Valentina"]
    nomi_df = []    #per nomi e città ho usato due liste con un for 
    for i in range(10):
        nome_casuale = random.choice(nomi)
        nomi_df.append(nome_casuale)

    citta = ["Roma", "Milano", "Napoli", "Torino", "Palermo", "Bologna"]
    citta_df = []
    for i in range(10):
        citta_casuale = random.choice(citta)
        citta_df.append(citta_casuale)


    eta = np.random.randint(18, 50, size=10)    #per età e salario ho creato due array con numpy usando random
    salari = np.random.randint(1500, 3000, size=10)

    return nomi_df, eta, citta_df, salari   #return dei valori

def crea_dataframe():

    nomi_df, eta, citta_df, salari = generazione_valori()   #richiamo i valori ritornati

    data = {    #creazione del df tramite dict
        "Nome": nomi_df,
        "Età": eta,
        "Città": citta_df,
        "Salario": salari
    }

    df = pd.DataFrame(data) #creo il dict
    print("DataFrame iniziale: \n", df, "\n")   #stampo il dict iniziale
    return df   #ritorno il dict


def stampa_prime_e_ultime_5_righe(df):

    print("Prime 5 Righe: \n", df.head(5), "\n")    #df.head e df.tail per le prime e le ultime 5 righe
    print("Ultime 5 Righe: \n", df.tail(5), "\n")

def stampa_tipi(df):

    print("Nome di tipo: ", np.dtype(df["Nome"]))   #np.dtype per il tipo della colonna
    print("Età di tipo: ",np.dtype(df["Età"]))
    print("Città di tipo: ",np.dtype(df["Città"]))
    print("Salario di tipo: ",np.dtype(df["Salario"]), "\n")

def media_mediana_deviazione(df):

    print("Media dei valori di età: ", df["Età"].mean())    #mean median e std per le function matematiche
    print("Mediana dei valori di età: ", df["Età"].median())
    print("Deviazione Standard dei valori di età: ", df["Età"].std(), "\n")

    print("Media dei valori di età: ", df["Salario"].mean())
    print("Mediana dei valori di età: ", df["Salario"].median())
    print("Deviazione Standard dei valori di età: ", df["Salario"].std(), "\n")

def elimina_duplicati(df):  #rimuove duplicati e stampa il df senza duplicati

    df.drop_duplicates()
    print("Dataframe senza duplicati: \n", df, "\n")
    return df

""" 
df['Età'].fillna(df['Età'].mean(), inplace=True)
df['Salario'].fillna(df['Salario'].mean(), inplace=True)
print(df) 
"""

def aggiungi_categoria_eta(df): #aggiungo categoria al df usando il metodo apply per passare una funzione al df

    def categoria(eta):
        if eta <= 18:
            return "Giovane"
        elif 19 <= eta <= 65:
            return "Adulto"
        else:
            return "Senior"
    
    df['Categoria Età'] = df['Età'].apply(categoria)
    print("DataFrame con Categoria Età: \n", df, "\n")
    return df

def salva_dataframe(df):    #salvo su csv con df.to_csv
    df.to_csv('C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\17.07\\dataframe.csv', index=False)
    print("DataFrame salvato")


def menu_pandas():  #menu

    print("\nMenu:")
    print("1. Visualizzare le prime e le ultime 5 righe")
    print("2. Visualizzare il tipo di dati di ciascuna colonna")
    print("3. Calcolo Media, Mediana e Deviazione Standard delle colonne numeriche")
    print("4. Stampa DataFrame senza duplicati")
    print("5. DataFrame con la Categoria Età")
    print("6. Salva su CSV\n")


df = crea_dataframe()   #creo il df iniziale

while True:

    menu = menu_pandas()
    opzione = int(input("\nScegli l'operazione che desideri effettuare: ")) #scelta opzione
    if opzione == 1:
        stampa_prime_e_ultime_5_righe(df)
    elif opzione == 2:
        stampa_tipi(df)
    elif opzione == 3:
        media_mediana_deviazione(df)
    elif opzione == 4: 
        elimina_duplicati(df)
    elif opzione == 5:
        aggiungi_categoria_eta(df)
    elif opzione == 6:
        salva_dataframe(df)
    else:
        print("Scelta non disponibile")

    continua = input("Vuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break















