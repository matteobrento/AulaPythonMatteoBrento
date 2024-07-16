"""
Consegna:
Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.


Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, 
applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi.
"""

import numpy as np

matrice = np.random.randint(1,100,size=(6,6))   #matrice 6x6 random
print("Matrice 6x6 di partenza: \n", matrice, "\n")

matrice_ridotta = matrice[1:5,1:5]  #slicing
print("Matrice 4x4 Centrale: \n", matrice_ridotta, "\n")

""" 
matrice_swap = np.swapaxes(matrice, axis1=0,axis2=1)
print(matrice_swap) 
"""

matrice_invertita = matrice_ridotta[::-1]   #step di -1 per invertire
print("Matrice con righe invertite: \n", matrice_invertita, "\n")

diagonale = np.diag(matrice_invertita)
print("Diagonale: \n", diagonale, "\n")

for i in range(matrice_invertita.shape[0]):
    for j in range(matrice_invertita.shape[1]):
        if matrice_invertita[i,j]%3 == 0:
            matrice_invertita[i,j] = -1

print("Matrice Invertita Aggiornata con -1 per i multipli di 3: \n", matrice_invertita, "\n")





