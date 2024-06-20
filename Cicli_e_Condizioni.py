#Esercizio1: If

intero = int(input("Inserire un numero: "))
if(intero%2 == 0):
    print("Il numero è pari")

else:
    print("Il numero è dispari")


#Esercizio2: While e Range, lo faccio utilizzando il range come stamattina, deve potersi ripetere all'infinito

controllo = True

while controllo == True:
    inserimento = int(input("Inserisci un numero da decrementare: "))

    for i in range(inserimento, -1, -1):
        print(i)

    scelta = input("Vuoi inserire un altro numero? ")
    if (scelta != "si"):
        controllo = False


#Esercizio 3: creo un input con lista e utilizzo un ciclo for sulla lista per iterare tutti gli elementi stampandone il quadrato

controllo = True
lista = []

while(controllo == True):
    #inserimentoValore = int(input("Inserisci un valore: "))
    #lista.append(inserimentoValore)

    scelta = input("Vuoi inserire un numero? ")
    if (scelta == "si"):
        inserimentoValore = int(input("Inserisci un valore: "))
        lista.append(inserimentoValore)

        for i in lista:
            print(i*i)
    
    else:
        controllo = False



#Esercizio 4: If, While e For

lista = [1, 6, 5, 8, 50]
max = lista[0]

controllo = True
while controllo == True:

    for elemento in lista:
        if elemento > max:
            max = elemento  

        controllo = True

    print("L'elemento massimo è: ")
    print(max)
    break


controllo = True
sommaElementi = 0
while controllo == True:

    for elemento in lista:
        sommaElementi += elemento

    controllo = True

    print("La somma degli elementi è: ")
    print(sommaElementi)
    break



lista = [1, 6, 5, 8, 50]
max = lista[0]

controllo = True
while controllo == True:

    if not lista:
        print("Lista Vuota")
    else:
        for elemento in lista:
            if elemento > max:
                max = elemento  

            controllo = True

    print("L'elemento massimo è: ")
    print(max)
    print("Il numero di elementi della lista è: ")
    print(len(lista))
    break
















        


          







