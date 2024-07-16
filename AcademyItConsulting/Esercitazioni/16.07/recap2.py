"""
Esercizio 2: Manipolazione di Array Multidimensionali

Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
"""

import numpy as np

""" 
matrice = np.arange(1,26).reshape(5,5)
print("Matrice: \n", matrice, "\n")

print("Stampa seconda colonna: \n", matrice[:,1:2], "\n")

print("Stampa terza riga: ", matrice[2:3,:], "\n")

diagonale = np.diag(matrice)
print("La diagonale della matrice sotto forma di array è: ", diagonale, "\n")

somma_diagonale = np.trace(matrice)
print("Somma degli elementi della Diagonale: ", somma_diagonale, "\n") 
"""

matrice = np.arange(1,26).reshape(5,5)  #arange crea un array di 25 num consecutivi, reshape l trasforma in una matrice 5x5
print("Matrice: \n", matrice, "\n")

while True:

    print("\nMenu")
    print("1. Stampa Matrice")
    print("2. Stampa Seconda Colonna")
    print("3. Stampa Terza Riga")
    print("4. Stampa della Diagonale")
    print("5. Stampa della Somma dei valori della Diagonale\n")
    scelta = int(input("Scegli un opzione: "))
    if scelta == 1:
        print("Matrice: \n", matrice, "\n") #stampa della matrice creata con arange e gestita con reshape
    elif scelta == 2:
        print("Stampa seconda colonna: \n", matrice[:,1:2], "\n")   #slicing colonna
    elif scelta == 3:
        print("Stampa terza riga: ", matrice[2:3,:], "\n")  #slicing riga
    elif scelta == 4:
        diagonale = np.diag(matrice)
        print("La diagonale della matrice sotto forma di array è: ", diagonale, "\n")   #stampa della diagonale sotto forma di array
    elif scelta == 5:
        somma_diagonale = np.trace(matrice)
        print("Somma degli elementi della Diagonale: ", somma_diagonale, "\n")  #somma dei valori della diag con np.trace()
    else:
        print("Opzione non disponibile!")

    tent = input("Vuoi eseguire un'altra operazione ? ")    #ripetibilità
    if tent != "si":
        print("\nArrivederci")
        break

