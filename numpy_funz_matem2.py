"""
Consegna:

Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
Somma i due array elemento per elemento per ottenere un nuovo array.
Calcola la somma totale degli elementi del nuovo array.
Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.


Obiettivo:

Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per creare array di numeri casuali, 
e sum per eseguire operazioni di somma sugli array, incluso l'uso di condizioni per la somma parziale.
"""

import numpy as np

array = np.linspace(0,10,50)
print(array, "\n")

array2 = np.random.random(50)
print(array2, "\n")

nuovo_array = array + array2
print(nuovo_array, "\n")

s = nuovo_array.sum()
print("Somma Totale del nuovo Array: ", s, "\n")

""" 
somma = np.where(somma_array>5, somma_array.sum(), somma_array.mean())
print(somma) 
"""

somma = 0
for valore in nuovo_array:
    if valore > 5:
        somma += valore

print(f"La somma dei valori maggiori di 5 è: {somma} \n")

    
      



