"""
Supponiamo di avere un dataset che registra le vendite giornaliere di diversi prodotti in varie città. 
Potremmo voler analizzare le vendite medie per prodotto in ciascuna città.
"""

import pandas as pd

# Dati di esempio
data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]
}

df = pd.DataFrame(data)

# Creazione della tabella pivot
pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
#in values cosa vogliamo analizzare, in index l'indice di raggruppamento, columns la colonna che vogliamo restituire e aggfunc per la funzione 

print(pivot_df)

