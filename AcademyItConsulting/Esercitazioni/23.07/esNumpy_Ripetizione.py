"""
Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti operazioni:
- calcolo della media;
- calcolo della deviazione standard;
- trasformarlo in un array 5x10
"""

import numpy as np

array = np.random.randint(1, 1001, 50)

media = array.mean()
dev_standard = array.std()

array_reshape = array.reshape(5,10)

print("Array Iniziale con 50 valori compresi tra 1 e 1000: \n",array, "\n")
print(f"Media dei valori dell'array: {media:.2f}\n")
print(f"Deviazione Standard dei valori dell'array: {dev_standard:.2f}\n")
print("Array con Reshape 5x10: \n",array_reshape, "\n")