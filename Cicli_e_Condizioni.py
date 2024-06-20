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


#Esercizio 3: creo un input con lista e utilizzo un ciclo for sulla lista per iterare tutti gli elementi stampandone in quadrato

lista = [1, 2, 5, 10, 50]
controllo = True

while controllo == True:

    for i in lista:
        print(i*i)

    scelta = input("Vuoi eseguire di nuovo l'operazione? ")
    if (scelta != "si"):
        controllo = False


#Esercizio 4: If, While e For



