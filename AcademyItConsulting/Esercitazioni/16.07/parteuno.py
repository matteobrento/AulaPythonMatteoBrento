"""
Parte UNO: 
Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
Il programma deve presentare un menu interattivo che consente all'utente
di eseguire varie operazioni sulla matrice. Le operazioni disponibili includono:
Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma.
"""

import numpy as np

#creazione della matrice
def crea_matrice():
    while True:     #inserimento righe e colonne con un while finchè non viene inserito un valore accettabile
        try:        
            righe=int(input("Inserisci il numero di righe: "))
            break
        except ValueError as e:
            print("\nErrore nel valore passato:", e, "\nInserisci un valore intero valido! \n")   #except con ValueError nel caso in cui si inserisce un valore non intero
    while True:
        try:
            col=int(input("Inserisci il numero di colonne: "))
            break
        except ValueError as e:
            print("\nErrore nel valore passato:", e, "\nInserisci un valore intero valido! \n")   #except con ValueError nel caso in cui si inserisce un valore non intero

    variabile = input("Vuoi inserire un numero casuale(1) o inserirli da input(2) ? ")
    if variabile == "1":
        matrice = np.random.randint(0,100,size=(righe,col))
    elif variabile == "2":
        v=np.zeros(righe*col)
        for i in range(righe*col):
            inp=int(input("Inserisci il valore: "))
            v[i]=inp

        matrice = v.reshape(righe, col)

    print(f"\nLa matrice 2D di partenza è:\n {matrice}")

    return matrice,righe,col    #return della matrice creata, delle righe e delle colonne

#calcolo sottomatrice dalla prima riga alla penultima, e dalla prima colonna alla penultima
def sotto_matrice(matrice,righe,col):
    print(f"\nSotto-Matrice centrale:\n {matrice[1:righe-1,1:col-1]}")    #sotto-matrice tramite Slicing

#calcolo matrice trasposta
def trasp_matrice(matrice):
    trasposta=matrice.T     #metodo numpy per il calcolo della trasposta
    print("\nMatrice Trasposta: \n", trasposta)

#somma degli elementi della matrice
def somma_elem(matrice):
    print(f"\nLa somma degli elementi della matrice è: {np.sum(matrice)}")

#calcolo determinante della matrice se righe==col
def det_mat(matrice,righe,col):
    if righe==col:
        print(f"\nIl determinante della matrice è: {np.linalg.det(matrice)}") #calcolo determinante tramite linalg.det solo se righe e colonne sono uguali
    else:
        print("\nNumero di righe e colonne diverso. Non si può calcolare il determinante. ")

#moltiplicazione element-wise
def molt_elem_wise(matrice,righe,col):
    matrice2=np.random.randint(0,100,size=(righe,col))
    prodotto_matrici=matrice*matrice2   #prodotto elemento per elemento
    print(f"\nSeconda matrice generata:\n{matrice2}\n")
    print(f"Prodotto delle due matrici:\n {prodotto_matrici}")

#calcolo media della matrice
def media_mat(matrice):
    print(f"\nLa media degli elementi della matrice è: {np.mean(matrice)}")

#matrice inversa
def matrice_inversa(matrice,righe,col): # funzione che calcola la matrice inversa
    det = np.linalg.det(matrice)
    if righe == col and det != 0: # la matrice è invertibile solo se è quadrata ed il suo determinante è diverso da 0
        mat_inv = np.linalg.inv(matrice)
        print(f"La matrice inversa è:\n{mat_inv}")
    else:
        print(f"La matrice non è invertibile!") 

#Filtro
def filtro_mat(matrice):
    f = int(input("Inserire filtro: "))
    while True:
        bol = input("1: Minore di\n2: Maggiore di\n")
        if bol == "1":
            mat_filtr = matrice[matrice<f]
            break
        elif bol == "2":
            matr_filtr = matrice[matrice>f]
            break
        else:
            print("Indicare scelta valida")

    print(f"Elementi della matrice con filtro eseguito:\n{matr_filtr}")

def funzione_matematica(matrice):

    scelta = input("1. Sin - 2. Cos - 3. Exp: ")
    if scelta == "1":
        seno = np.sin(matrice)
        print("Seno dei valori: \n", seno)
    elif scelta == "2":
        coseno = np.cos(matrice)
        print("Coseno dei valori: \n", coseno)
    elif scelta == "3":
        esponenziale = np.exp(matrice)
        print("Esponenziale dei valori: \n", esponenziale)
    