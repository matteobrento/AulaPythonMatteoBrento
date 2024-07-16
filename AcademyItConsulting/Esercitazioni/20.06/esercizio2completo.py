utilizzo = input("Vuoi utilizzare il sistema ? ")   #richiesta di utilizzo del sistema
controllo = True

if (utilizzo == "si"):

    while controllo:

        print("1) Inserisci un numero\n2) Inserisci una stringa\n3) Calcola numeri primi o non primi in un intervallo") #opzioni da selezionare
        print("\n")
        cod = int(input("Scegli l'operazione che vuoi eseguire: "))
        print("\n")

        if(cod == 1):
            numero = int(input("Inserisci il numero: "))
            if(numero%2 == 0):
                print("Il numero inserito è pari ") #calcolo numero pari tramite resto
                print("\n")
            else:
                print("Il numero inserito è dispari")   #altrimenti dispari
                print("\n")
        elif(cod == 2):
            stringa = input("Inserisci la stringa: ")   #calcolo lunghezza stringa
            if(len(stringa)%2 == 0):
                print("La lunghezza della stringa è pari")
                print("\n")
            else:
                print("La lunghezza della stringa è dispari")
                print("\n")
        elif(cod == 3):
            e1 = int(input("Indicare estremo sinistro: "))      #estremo destro
            e2 = int(input("Indicare estremo destro: "))        #estremo sinistro
            n = int(input("Indicare con 0 i numeri pari, 1 dispari: "))  #scegliere opzione
            if n == 0:
                for i in range(e1,e2+1):    #scelta 0, numeri pari
                    if i%2 == 0:
                        print(i)         
            elif n == 1:
                for i in range(e1,e2+1):    #scelta 1, numeri dispari
                    if i%2 != 0:
                        print(i)
            else:
                print("L'opzione scelta non è valida")
        else:
            print("Opzione selezionata non disponibile")
            controllo = False

else:
    print("Arrivederci")