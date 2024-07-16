"""
Esercizio 3: Operazioni con Fancy Indexing

Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array 
(considerando la numerazione delle righe che parte da 0).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
"""

import numpy as np


""" 
indici = [(0, 1), (1, 3), (2, 2), (3, 0)]
righe_indici = np.array([index[0] for index in indici])
colonne_indici = np.array([index[1] for index in indici]) 

#Altro modo per poter fare il fancy in un array bidimensionale
"""

""" 
righe = np.array([0, 1, 2, 3])
colonne = np.array([1, 3, 2, 0])
print("Indici: ", matrice[righe, colonne], "\n")

indici_dispari = [0, 2]
print("Righe dispari della matrice (righe 0 e 2): \n", matrice[indici_dispari], "\n")

valore = 10
matrice_modificata = matrice+10
print("Matrice modificata: \n", matrice_modificata, "\n") 
"""


matrice = np.random.randint(10,50,size=(4,4))   #matrice 4x4 con valori casuali tra 10 e 50 con random.randint
print("Matrice: \n", matrice, "\n")

while True:

    print("\nMenu")
    print("1. Stampa Matrice")
    print("2. Fancy Indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0)")
    print("3. Fancy Indexing per selezionare e stampare tutte le righe dispari dell'array")
    print("4. Modifica elementi aggiungendo 10 alla matrice iniziale\n")
    
    scelta = int(input("Scegli un opzione: "))
    if scelta == 1:
        print("Matrice: \n", matrice, "\n") #stampa matrice
    elif scelta == 2:
        righe = np.array([0, 1, 2, 3])  #indici righe
        colonne = np.array([1, 3, 2, 0])    #indici colonne
        print("Indici: ", matrice[righe, colonne], "\n")    #indici righe e colonne nella matrice (associazione [0]righe e [1]colonne)
    elif scelta == 3:
        indici_dispari = [0, 2] #indici righe dispari
        print("Righe dispari della matrice (righe 0 e 2): \n", matrice[indici_dispari], "\n")   #stampa
    elif scelta == 4:
        valore = int(input("Inserisci il valore da aggiungere: "))  #valore da input
        matrice_modificata = matrice+valore #modifica matrice (broadcasting)
        print("Matrice modificata: \n", matrice_modificata, "\n")   #stampa
    else:
        print("Opzione non disponibile!")

    tent = input("Vuoi eseguire un'altra operazione ? ")    #ripetibilità
    if tent != "si":
        print("\nArrivederci")
        break