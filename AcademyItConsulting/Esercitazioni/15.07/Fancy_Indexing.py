import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices])  # Output: [20 40]

# Utilizzo di una lista di indici
indices = [4, 2, 3]
print(arr[indices])  # Output: [50 30 40]

