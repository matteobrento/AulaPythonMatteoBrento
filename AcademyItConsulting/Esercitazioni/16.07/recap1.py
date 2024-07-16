import numpy as np

""" array = np.random.randint(0,100,15)
print("Array: ", array, "\n")
print("La somma degli elementi dell'array è: ", array.sum(), "\n")
print("La media degli elementi dell'array è: ", array.mean()) """

array = np.random.randint(0,100,15) #array di 15 valori casuali tra 0 e 100
print("Array: ", array, "\n")

while True:

    print("\nMenu")
    print("1. Somma")
    print("2. Media\n")
    scelta = int(input("Scegli un opzione: "))
    if scelta == 1:
        print("La somma degli elementi dell'array è: ", array.sum(), "\n")  #somma con array.sum()
    elif scelta == 2:
        print("La media degli elementi dell'array è: ", array.mean(), "\n") #media con array.mean()
    else:
        print("Opzione non disponibile!")

    tent = input("Vuoi eseguire un'altra operazione ? ")    #ripetibilità
    if tent != "si":
        print("\nArrivederci")
        break

