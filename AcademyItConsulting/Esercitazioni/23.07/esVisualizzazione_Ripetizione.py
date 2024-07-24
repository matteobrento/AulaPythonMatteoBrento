"""
Create un programma che crea un dataframe sulla base dell'input dell'utente contenente 4 studenti e i loro voti mensili 
per sei mesi di studio in 4 materie.
Il programma ci restituirà:
-Un grafico contenente 4 grafici più piccoli, uno per ogni studente, con andamento delle medie dei voti per ogni mese;
-Un altro grafico che racchiude tutti gli andamenti di tutti gli studenti
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

def genera_valori():

    studenti = ["Matteo", "Daniele", "Valentina", "Giovanni"]
    materie = ["Italiano", "Matematica", "Geografia", "Storia"]
    voti = {studente: {materia: np.random.randint(2, 11, 6) for materia in materie} for studente in studenti}
    return voti

def crea_dataset(voti):

    mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno"]
    data = []
    for studente, materie in voti.items():
        for materia, voti_mensili in materie.items():
            data.append([studente, materia] + list(voti_mensili))
    colonne = ["Studente", "Materia"] + mesi
    df = pd.DataFrame(data, columns=colonne)
    print("DataFrame Iniziale: \n", df, "\n")
    return df

def grafici(df):

    mesi = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno"]
    studenti = df["Studente"].unique()

    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    for i, studente in enumerate(studenti):
        ax = axs[i // 2, i % 2]
        dati_studente = df[df["Studente"] == studente].iloc[:, 2:].mean()
        ax.plot(mesi, dati_studente, marker='o')
        ax.set_title(f'Andamento delle medie dei voti per {studente}')
        ax.set_xlabel('Mese')
        ax.set_ylabel('Media dei voti')
        ax.grid(True)

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    for studente in studenti:
        dati_studente = df[df["Studente"] == studente].iloc[:, 2:].mean()
        plt.plot(mesi, dati_studente, marker='o', label=studente)

    plt.title('Andamento delle medie dei voti per tutti gli studenti')
    plt.xlabel('Mese')
    plt.ylabel('Media dei voti')
    plt.legend()
    plt.grid(True)
    plt.show()


voti = genera_valori()
df = crea_dataset(voti)
grafici(df)


    
