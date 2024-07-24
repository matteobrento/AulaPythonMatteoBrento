"""
- analizzate il tipo di dati,
- sistemate gli elementi mancanti 
- verificate se ci sono correlazioni 
- create un grafico a mappa di calore.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def carica():
    colonne = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    df = pd.read_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\23.07\\housing.csv", header=None, names=colonne, delimiter=r"\s+")  #qualsiasi spazio vuoto (\s), 1 o più volte (+)
    print("Dataframe importato: \n",df, "\n")
    return df

def tipi(df):
    print("Tipi di dati: \n",df.dtypes, "\n")

def elementi_mancanti(df):
    print("Sistemare elementi mancanti: \n",df.isnull().sum(), "\n")

def correlazione(df):
    correlazione = df.corr()
    print("Verificare correlazioni : \n",correlazione, "\n")
    return correlazione

def heatmap(df):

    corr = correlazione(df)
    plt.figure()
    sns.heatmap(corr, annot = True)
    plt.title('Mappa di calore della matrice di correlazione')
    plt.show()

df = carica()
tipi(df)
elementi_mancanti(df)
heatmap(df)


