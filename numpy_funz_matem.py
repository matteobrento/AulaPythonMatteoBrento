"""
Descrizione: 
Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.

Esercizio:
Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
Cambia la forma dell'array a una matrice 3x4.
Genera una matrice 3x4 di numeri casuali tra 0 e 1.
Calcola e stampa la somma degli elementi di entrambe le matrici.
"""

import numpy as np

array = np.linspace(0,1,12)
print("Array di 12 numeri equidistanti tra 0 e 1: \n", array, "\n")

r = array.reshape(3,4)
print("Cambio forma dell'array a una matrice 3x4: \n", r, "\n")

matrice = np.random.rand(3,4)
print("Matrice 3x4 di numeri casuali tra 0 e 1: \n", matrice, "\n")

somma1 = array.sum()
print("Somma Array: ", somma1, "\n")

somma2 = matrice.sum()
print("Somma Matrice: ", somma2, "\n")