utilizzo = input("Vuoi utilizzare il sistema ? ")
controllo = True

if (utilizzo == "si"):

    while controllo:

        print("1) Inserisci un numero\n2) Inserisci una stringa\n") 
        print("\n")
        cod = int(input("Scegli l'operazione che vuoi eseguire: "))
        print("\n")

        if(cod == 1):
            numero = int(input("Inserisci il numero: "))
            if(numero%2 == 0):
                print("Il numero inserito è pari ")
                print("\n")
            else:
                print("Il numero inserito è dispari")
                print("\n")
        elif(cod == 2):
            stringa = input("Inserisci la stringa: ")
            if(len(stringa)%2 == 0):
                print("La lunghezza della stringa è pari")
                print("\n")
            else:
                print("La lunghezza della stringa è dispari")
                print("\n")
        else:
            print("Opzione selezionata non disponibile")
            controllo = False

else:
    print("Arrivederci")