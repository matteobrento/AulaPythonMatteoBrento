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

""" 
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
"""

def menu_numpy():

    print("\nMenu")
    print("1. Stampa Array di 12 numeri equidistanti tra 0 e 1")
    print("2. Cambia Forma Array")
    print("3. Stampa Matrice di valori casuali tra 0 e 1 3x4")
    print("4. Somma dei valori del primo Array")
    print("5. Somma dei valori della Matrice 3x4")


array = np.linspace(0,1,12)
print("Array di 12 numeri equidistanti tra 0 e 1: \n", array, "\n") #uso linspace per creare array con valori equidistanti nel range definito

matrice = np.random.rand(3,4)
print("Matrice 3x4 di numeri casuali tra 0 e 1: \n", matrice, "\n") #uso range per creare matrice di valori casuali tra 0 e 1 3x4

while True:

    menu = menu_numpy()
    opzione = int(input("\nScegli l'operazione che desideri effettuare: ")) #scelta opzione
    if opzione == 1:
        print("Array di 12 numeri equidistanti tra 0 e 1: \n", array, "\n")
    elif opzione == 2:
        r = array.reshape(3,4)      #uso reshape per cambiare la forma dell'array in una matrice 3x4
        print("Cambio forma dell'array a una matrice 3x4: \n", r, "\n")
    elif opzione == 3:
        print("Matrice 3x4 di numeri casuali tra 0 e 1: \n", matrice, "\n")
    elif opzione == 4: 
        somma1 = array.sum()    #uso sum() per la somma
        print("Somma Array: ", somma1, "\n")
    elif opzione == 5:
        somma2 = matrice.sum()
        print("Somma Matrice: ", somma2, "\n")
    else:
        print("Opzione selezionata non disponibile.")

    continua = input("Vuoi effettuare un'altra operazione? ")
    if continua.lower() != "si":
        print("\nArrivederci")
        break

