"""
Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
Esercizio:
Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array.
"""

import numpy as np

array = np.arange(10,49)
print(array.dtype)
print(array.shape)

array = np.arange(10,49,dtype="float")
print(array.dtype)
print(array.shape)