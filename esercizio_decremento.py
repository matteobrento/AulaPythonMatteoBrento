controllo = True
controllo1 = True

while controllo == True:
    inserimento = int(input("Inserisci un numero da decrementare: "))

    for i in range(inserimento, -1, -1):
        print(i)

    scelta = input("Vuoi inserire un altro numero? ")
    if (scelta != "si"):
        controllo = False

while controllo1 == True:
    inserimento = int(input("Inserisci un numero >= 2 per controllare se è primo o no: "))

    if(inserimento/1 and inserimento/inserimento):
        print("Il numero è primo ")
    elif(inserimento < 2):
        print("Errore")
    else:
        print("Il numero non è primo")
        controllo = False

