utilizzo = input("Vuoi utilizzare il sistema ? ")
controllo = True
intervallo = 0

lista_pari = []
lista_dispari = []


if (utilizzo == "si"):

    while controllo:

        num1 = int(input("Inserisci il primo intervallo: "))
        num2 = int(input("Inserisci il secondo intervallo: "))
        input = int(input("Indicare con 0 i numeri primi, 1 altrimenti: "))

        if(input == 0):
            for i in range(num1, num2+1):
                if(i%2 != 0):
                    print(i)
        elif(input == 1):
            for i in range(num1, num2+1):
                if(i%2 == 0):
                    print(i)
        else:
            print("Operazione non valida")



else:
    print("Arrivederci")