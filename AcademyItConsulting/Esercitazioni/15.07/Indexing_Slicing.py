import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])  # Output: 1

# Slicing
print(arr[1:3])  # Output: [2 3]    dalla posizione 1 alla 3 esclusa

# Boolean Indexing
print(arr[arr > 2])  # Output: [3 4 5]  stampa valori dove val>2
print("\n")


arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
# Slicing sulle righe
print(arr_2d[1:3], "\n")  # Output: [[ 5  6  7  8]  slicing solo sulle righe, stampa dalla riga in pos 1 a quella in pos 3, poichè non c'è nessuna riga in pos 3 e la pos 3 è esclusa, mi stampa 1 e 2
                   #          [ 9 10 11 12]]
# Slicing sulle colonne
print(arr_2d[:, 1:3], "\n")  # Output: [[ 2  3] nessuna indicazione per le righe ma slicing solo su colonne da 1 a 3 (escluso)
                       #          [ 6  7]
                       #          [10 11]]
# Slicing misto
print(arr_2d[1:, 1:3], "\n")  # Output: [[ 6  7]   si parte dalla riga 1 (seconda) e si stampano solo le colonne nel range 1-3(escluso) 
                        #          [10 11]]


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7])  # Output: [2 3 4 5 6]

# Slicing con passo
print(arr[1:8:2])  # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5])  # Output: [0 1 2 3 4]
print(arr[5:])  # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:])  # Output: [5 6 7 8 9]  parte dalla fine in poi
print(arr[:-5])  # Output: [0 1 2 3 4]  parte dalla fine verso l'inizio