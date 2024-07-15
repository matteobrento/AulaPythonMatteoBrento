"""
Esercizio su NumPy Slicing

Consegna:
Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.
"""

import numpy as np

array = np.random.randint(10,50,20)
print(array, "\n")

print("Primi 10 valori: ", array[:10], "\n")
print("Ultimi 5 valori: ", array[-5:], "\n")
print("Valori dall'indice 5 all'indice 15 (escluso): ", array[5:15], "\n")
print("Stampa ogni 3: ", array[::3], "\n")

array[5:10] = 99
print("Array con 99 da 5 a 10 escluso: ", array)
