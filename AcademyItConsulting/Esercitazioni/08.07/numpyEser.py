import numpy as np


""" arr = np.array([1, 2, 3, 4, 5]) #monodimensionale
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) #bidimensionale

print(arr[0])   #indexing
print(arr[::-1])    #slicing (array al contrario)

print(arr)
print(arr2)

print(arr.dtype)    #tipo di dati dell'array

print(np.shape(arr))    #restituisce la dimensione di arr (in questo caso riga di 5 valori)


b = np.arange(0, 20).reshape((2,10))    #arange crea un array di quel range specificato con l'ultimo valore escluso, 
print(b)                                #reshape suddivide l'array nel numero di righe specificato come primo valore, fino al secondo 
print(np.sum(b))    #da la somma
print(np.mean(b))   #da la media
print(np.std(b))    #da la dev standard

c = np.linspace(0, 1, 8)
print(c)

random = np.random.rand(3,3)
print(random)   #array multidimensionale con valori casuali tra 0 e 1 3x3

f = np.zeros((2,3)) #crea una matrice 2x3 inizializzando tutti i valori a 0
f = np.ones((2,3))  #passando la shape inizializza tutti i valori a 1
f = np.eye(4)   #matrice d'identità (stesso numero righe e colonne), si mette un solo valore come parametro, 1 nella diagonale """



""" 
array = np.arange(10,49)
print(array.dtype)
print(array)
print("\n")
array = np.arange(10,49).reshape((3,13))
print(array) 
"""


""" 
array = np.linspace(0,1,12) #12 valori equidistanti tra 0 e 1
print(array)
print("\n")
array = np.linspace(0,1,12).reshape(3,4)    #reshape in 3x4
print(array)
print("\n")
print("Somma: ", np.sum(array)) #somma
print("Media: ", np.mean(array))    #media
print("Deviazione Standard: ", np.std(array))   #dev standard
print("\n")
matriceCasuale = np.random.rand(3,4)    #matrice 3x4 random
print("\n")
print("Somma: ", np.sum(matriceCasuale))
print("Media: ", np.mean(matriceCasuale))
print("Deviazione Standard: ", np.std(matriceCasuale))
print("\n")
print(np.shape(matriceCasuale)) 
"""

