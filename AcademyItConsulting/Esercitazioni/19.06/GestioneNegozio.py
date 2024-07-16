controllo = True
controllo1 = True
utilizzo = input("Vuoi utilizzare il sistema ? ")

lista_prodotti = ["CD", "Vinile", "Cassetta"]   #liste di prodotti, prezzi, quantita, acquisti 
lista_prezzi = ["5", "15", "7"]
lista_quantita = ["10", "12", "7"]
lista_acquisti = []

if (utilizzo == "si"):

    while controllo:

        visualizzazione_prodotti = input("Vuoi vedere i prodotti disponibili ? ")
        if(visualizzazione_prodotti == "si"):
            print("I prodotti disponibili sono: ")
            print(lista_prodotti)

        
        acquisto_prodotti = input("Tra i prodotti disponibili, desideri effettuare un acquisto ? ")

        if(acquisto_prodotti == "si"):
            while True:
                print("0) Esci\n1) CD\n2) Vinile\n3) Cassetta\n") 
                print("\n")
                cod = int(input("Scegli il prodotto che vuoi acquistare: "))
                print("\n")

                if(cod == 0):
                     break
                

                elif(1 <= cod <= len(lista_prodotti)):
                        lista_acquisti.append(lista_prodotti[cod - 1])
                        print("Hai acquistato un/una: ")
                        print(lista_acquisti)
                        print("\n")
                else:
                    print("Codice non valido, riprova")


        nuovo_acquisto = input("Desideri effettuare un nuovo acquisto? ") 
        if(nuovo_acquisto == "si"):
            while True:
                print("0) Esci\n1) CD\n2) Vinile\n3) Cassetta\n") 
                print("\n")
                cod = int(input("Scegli il prodotto che vuoi acquistare: "))
                print("\n")

                if(cod == 0):
                    break
                

                elif(1 <= cod <= len(lista_prodotti)):
                    lista_acquisti.append(lista_prodotti[cod - 1])
                    print("Hai acquistato un/una: ")
                    print(lista_acquisti)
                    print("\n")
                else:
                    print("Codice non valido, riprova")  #non so se metterlo, ripeterei il ciclo precedente
        elif(nuovo_acquisto != "si"):                                        #al momento evito, poi magari potrei implementarlo
            controllo = False   #se l'utente non vuole fare un nuovo acquisto esce dal ciclo e si va al tracciamento


        tracciamento = input("Si desidera visualizzare il tracciamento degli acquisti? ")
        if(tracciamento == "si"):
            print("La lista degli acquisti effettuati è: \n")
            print(lista_acquisti)

        else:
            print("Non voglio visualizzare il tracciamento \n")


        continuare = input("Si desidera continuare ad utilizzare il sistema di acquisto ? Digitare 'no' per accedere all'Inventario. \n") #sono indeciso se inserirla o meno
        if(continuare == "si"):
            controllo
        
        else:
            controllo = False


    while controllo1:

        lista_inventario = [lista_prodotti, lista_prezzi, lista_quantita]

        stampaInventario = input("Vuoi visualizzare le caratteristiche del tuo Inventario? ")
        if(stampaInventario == "si"):
            print(lista_inventario)

        else:
            print("Non voglio visualizzare") 

        aggiungereArticolo = input("Si desidera aggiungere un nuovo articolo all'inventario ?") #ho aggiunto un elemento standard, col tempo vorrei implementare un'aggiunta dinamica
        if(aggiungereArticolo == "si"):
            lista_prodotti.append("Cuffie")
            lista_prezzi.append(50)
            lista_quantita.append(8)
            print(lista_inventario)
        
        else:
            print("Non voglio aggiungere nessun articolo")  #ho rimosso un elemento standard, col tempo vorrei implementare un'aggiunta dinamica
        
        rimuovereArticolo = input("Vuoi rimuovere un articolo? ")
        if(rimuovereArticolo == "si"):
            print(lista_inventario)
            lista_prodotti.remove("Cuffie")
            lista_prezzi.remove(50)
            lista_quantita.remove(8)
            print(lista_inventario)
        

        aggiornareArticolo = input("Vuoi aggiornare un articolo ?") ##ho aggiornato un elemento standard
        if(aggiornareArticolo == "si"):
            print(lista_inventario)
            lista_prodotti.insert(0, "Disco")
            lista_prezzi.insert(0, 9)
            lista_quantita.insert(0, 23)
            print(lista_inventario)
        
        else:
            print("Non voglio aggiornare")
       
        break
else:
    print("Arrivederci")