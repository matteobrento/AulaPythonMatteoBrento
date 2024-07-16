"""
Scrivete un programma che chiede un numero all’utente e restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }
"""
controllo = True
dict = {}

while controllo:

    print("Menu")
    print("1) Quadrato del numero \n2) Pari o Dispari \n3) Conteggio Cifre")
    cod = int(input("Seleziona un opzione: "))

    numero = int(input("Inserisci un numero: "))

    if(cod == 1):

        dict[numero] = numero**2
        print(dict)

    elif(cod == 2):

        if(numero % 2 == 0):
            print(f"{numero} è pari")
        
        else:
            print(f"{numero} è dispari")
    
    elif(cod == 3):

        dict[numero] = len(str(numero))
        print(dict)
    
    else:
        print("Errore")

   
    continua = input("Vuoi eseguire un'altra operazione ? ")
    if(continua == "si"):
        controllo = True
    
    else:
        print("Arrivederci!")
        controllo = False