controllo = True
utilizzo = input("Vuoi utilizzare il sistema ? ")

lista_prodotti = ["CD", "Vinile", "Cassetta"]   #liste di prodotti, prezzi, quantita, acquisti 
lista_prezzi = ["5", "15", "7"]
lista_quantita = ["10", "12", "7"]
lista_acquisti = []
acquisto = True

inventario = {                              #l'ho cominciato ad utilizzare nel secondo punto
            "nome" : lista_prodotti,
            "prezzo" : lista_prezzi,
            "quantità" : lista_quantita
        }

if (utilizzo == "si"):

    while controllo:

        visualizzazione_prodotti = input("Vuoi vedere i prodotti disponibili ? ")
        if(visualizzazione_prodotti == "si"):
            print("I prodotti disponibili sono: ")
            print(lista_prodotti)

        
            acquisto_prodotti = input("Tra i prodotti disponibili, desideri effettuare un acquisto ? ")

            if(acquisto_prodotti == "si"):
                print(lista_prodotti)
                print("1) CD\n2) Vinile\n3) Cassetta\n") 
                print("\n")
                cod = int(input("Scegli il prodotto che vuoi acquistare: "))
                print("\n")
                

            if(cod == 1):
                lista_acquisti.insert(0, "CD")
                print("Hai acquistato un CD")
                print(lista_acquisti)
                print("\n")
                

            elif(cod == 2):
                lista_acquisti.insert(0, "Vinile")
                print("Hai acquistato un Vinile")
                print(lista_acquisti)
                print("\n")
                
            
            elif(cod == 3):
                lista_acquisti.insert(0, "Cassetta")
                print("Hai acquistato una Cassetta")
                print(lista_acquisti)
                print("\n")
                

        else:
            print("Non desidero fare acquisti ") #Devo aggiungere la possibilità di fare altri acquisti e conteggiarli


        tracciamento = input("Si desidera visualizzare il tracciamento degli acquisti? ")
        if(tracciamento == "si"):
            print("La lista degli acquisti effettuati è: ")
            print(lista_acquisti)

        else:
            print("Non voglio visualizzare il tracciamento \n")

        break



    while controllo:

        inventario = {
            "nome" : lista_prodotti,
            "prezzo" : lista_prezzi,
            "quantità" : lista_quantita
        }

        stampaInventario = input("Vuoi visualizzare le caratteristiche del tuo Inventario? ")
        if(stampaInventario == "si"):
            print(inventario.items())

        else:
            print("Non voglio visualizzare") #Ho perso tempo qui perchè non avevo concatenato le liste con il dizionario e avevo fatto una struttura differente

        #Devo continuare, quindi se ad un certo punto del run si blocca è per questo

else:
    print("Arrivederci")