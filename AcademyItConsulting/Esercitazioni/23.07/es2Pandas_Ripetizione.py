"""
- analizzate il tipo di dati,
- sistemate gli elementi mancanti 
- verificate se ci sono correlazioni 
- create un grafico a mappa di calore.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

class Netflix:

    def __init__(self,nome_file):
        self.df = pd.read_csv(nome_file)

    def verifica_valori_nulli(self):
        print(f"Elenco valori nulli:\n{self.df.isnull().sum()}")

    def scrivi_df(self):
        self.df.to_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\23.07\\netflix_titles_pulito.csv")
        print("\nFile salvato con successo!")

    def pulizia(self):
        self.df["rating"].fillna("G",inplace=True)
        self.df["duration"].fillna("Not Defined",inplace=True)
        self.df.dropna(inplace=True)
        print("\nIl Dataset è stato pulito con successo!")

    def visualizza_df(self):
        print(f"DataSet:\n{self.df}")

    def preprazione_correlazione(self):
        self.df['type'] = self.df['type'].apply(lambda x: 1 if x == 'Movie' else 0)
        type = self.df["type"]
        anno_uscita = self.df["release_year"]
        data = {"type":type,"release_year":anno_uscita}
        df_corr = pd.DataFrame(data)
        df_corr = df_corr.corr()
        return df_corr
    
    def visualizza_correlazione(self):
        df_corr = self.preprazione_correlazione()
        plt.figure()
        sns.heatmap(df_corr,annot=True)
        plt.title('Heatmap correlazione')
        plt.show()

def menu():
    info = """\n1  Visualizza anteprima DataSet
2: Visualizza Elenco Valori nulli
3: Pulisci DataSet
4: Visualizza possibili Correlazioni
5: Salva in un altro CSV
0: Exit
Indicare la scelta: """
    s = input(info)
    return s

def main():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    a = Netflix("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\23.07\\netflix_titles.csv")
    while True:
        s = menu()
        if s == "1":
            a.visualizza_df()
        elif s == "2":
            a.verifica_valori_nulli()
        elif s == "3":
            a.pulizia()
        elif s == "4":
            a.visualizza_correlazione()
        elif s == "5":
            a.scrivi_df()
        elif s == "0":
            break
        else:
            print("\nScelta non valida!")

main()

