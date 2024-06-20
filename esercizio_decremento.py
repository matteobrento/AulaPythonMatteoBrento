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
    inserimento = int(input("Inserisci un numero per controllare se è primo o no: "))

    if(inserimento%2 != 0):
        print("Il numero è primo ")
    elif(inserimento == 2):
        print("Il numero è primo, in quanto 2 è il primo dei numeri primi ")
    elif(inserimento < 2) :
        print("Il numero non è primo")

    else:
        print("Il numero non è primo")
    
    scelta = input("Vuoi inserire un altro numero? ")
    if (scelta != "si"):
        break
    

