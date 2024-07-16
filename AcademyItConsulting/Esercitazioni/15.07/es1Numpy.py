"""
Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
Esercizio:
Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array.
"""

import numpy as np

controllo = True

def crea_array():
    int1 = int(input("Inserisci un valore: "))  #primo valore dell'intervallo
    int2 = int(input("Inserisci un valore: "))  #secondo valore dell'intervallo
    s = "int64" 
    s1 = "float64"
    scelta = int(input("1) dType INT, 2)dType FLOAT: "))    #decide se vuole un dtype intero o float
    if scelta == 1:
        array = np.arange(int1,int2,dtype=s)    #int
        print(array, "\n")
    elif scelta == 2:
        array = np.arange(int1,int2,dtype=s1)   #float
        print(array, "\n")
    else:
        print("Opzione non valida!")

    return array

def tipo():

    array = crea_array()    #prende l'operazione di creazione da crea_array e stampa il tipo
    print("dType: ", array.dtype, "\n")

def struttura():

    array = crea_array()    #prende l'operazione di creazione da crea_array e stampa la shape
    print("Shape: ", array.shape, "\n")


while controllo:

    print("Benvenuto!")
    print("1)Crea Array ")
    print("2)Visualizza Tipo Array ")
    print("3)Visualizza Struttura Array ")
    opzione = int(input("\nScegli l'operazione che desideri effettuare: "))

    if opzione == 1:
        crea_array()
    elif opzione == 2:
        tipo()
    elif opzione == 3:
        struttura()
    else:
        print("Opzione non valida!")
        quit()

    scelta = input("\nVuoi effettuare un altra operazione ? ")
    if scelta.lower() != "si":
        print("\nSistema in chiusura. Arrivederci! ")
        break
