"""
Consegna:

Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
Somma i due array elemento per elemento per ottenere un nuovo array.
Calcola la somma totale degli elementi del nuovo array.
Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.

Obiettivo:

Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per creare array di numeri casuali, 
e sum per eseguire operazioni di somma sugli array, incluso l'uso di condizioni per la somma parziale.
"""

import numpy as np

""" 
array = np.linspace(0,10,50)
print(array, "\n")

array2 = np.random.random(50)
print(array2, "\n")

nuovo_array = array + array2
print(nuovo_array, "\n")

s = nuovo_array.sum()
print("Somma Totale del nuovo Array: ", s, "\n") 
"""

""" 
somma = np.where(somma_array>5, somma_array.sum(), somma_array.mean())
print(somma) 
"""

""" 
somma = 0
for valore in nuovo_array:
    if valore > 5:
        somma += valore

print(f"La somma dei valori maggiori di 5 è: {somma} \n") 
"""


def array50():

    try:
        int1 = int(input("\nInserisci il primo valore del range: "))
        int2 = int(input("Inserisci il secondo valore del range: "))
        dimensione = int(input("Inserisci la dimensione del tuo array: "))
        array = np.linspace(int1, int2, dimensione)
        print(f"\nArray di {dimensione} valori equidistanti tra {int1} e {int2}: \n", array, "\n")
        return array
    except ValueError as e:
        print("\nErrore nei valori passati:", e)

def array50_casuali():

    try:
        dimensione = int(input("\nInserisci la dimensione del tuo array: "))
        array2 = np.random.random(dimensione)
        print(f"\nArray di {dimensione} valori casuali tra 0 e 1 con random.random: \n", array2, "\n")
        return array2
    except ValueError as e:
        print("\nErrore nel passare la dimensione:", e)

def somma_due_array():
    
    array = array50()
    array2 = array50_casuali()
    nuovo_array = array + array2
    print("\nSomma dei due array valore per valore: \n", nuovo_array, "\n")
    return nuovo_array

def somma_totale():

    nuovo_array = somma_due_array()
    s = nuovo_array.sum()
    print("\nSomma Totale del nuovo Array: ", s, "\n")

def somma_maggiore_di_5():

    nuovo_array = somma_due_array()
    somma = 0
    for valore in nuovo_array:
        if valore > 5:
            somma += valore

    print(f"\nLa somma dei valori maggiori di 5 è: {somma} \n")

def menu_numpy():

    print("\nMenu")
    print("1. Array di 50 numeri equidistanti tra 0 e 10")
    print("2. Array di 50 numeri casuali compresi tra 0 e 1")
    print("3. Somma dei due Array elemento per elemento")
    print("4. Somma totale degli elementi del nuovo Array")
    print("5. Somma degli elementi del nuovo array che sono maggiori di 5")

while True:

    menu = menu_numpy()
    opzione = int(input("\nScegli l'operazione che desideri effettuare: ")) #scelta opzione
    if opzione == 1:
        array50()
    elif opzione == 2:
        array50_casuali()
    elif opzione == 3:
        somma_due_array()
    elif opzione == 4: 
        somma_totale()
    elif opzione == 5:
        somma_maggiore_di_5()
    else:
        print("\nOpzione selezionata non disponibile.")

    continua = input("\nVuoi effettuare un'altra operazione? ")
    if continua.lower() != "si":
        print("\nArrivederci")
        break





    
      



