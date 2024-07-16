class Ristorante:   #creo una classe Ristorante

    aperto = False  #imposto una variabile booleana per l'apertura a False
    menu = []   #creo una lista vuota per aggiungere piatti al menu di tipo dict

    def __init__(self, nome, tipo_cucina):  #creo il costruttore con gli attributi nome e tipo_cucina
        self.nome = nome
        self.tipo_cucina = tipo_cucina

    def descrivi_ristorante(self):  #creo un metodo che stampa una descrizione con nome del ristorante e tipo cucina
        print("Benvenuti nel ristorante:",self.nome,"e il tipo di cucina è:",self.tipo_cucina)

    def apri_ristorante(self):  #creo un metodo per l'apertura del ristorante
        global aperto   #prendo la variabile globale impostata su false e se voglio aprire il ristorante, passa a True
        aprire = input("Vuoi aprire il ristorante? ")
        if aprire == "si":
            aperto = True
        else:
            print("Il ristorante è chiuso") #se la risposta è diversa da "si", stampa che è chiuso e termina il programma
            quit()

    def chiudi_ristorante(self):    #creo un metodo per la chiusura del ristorante
        global aperto   #prendo la variabile globale che questa volta, se il ristorante sarà già stato aperto in precedenza sarà
        chiudere = input("Vuoi chiudere il ristorante? ") #impostata su True e chiedendo di chiudere, in caso di risposta affermativa
        if chiudere == "si":  #aperto ripassa a False
            aperto = False
        else:
            print("Il ristorante rimane aperto")
    
    def stato_apertura(self):   #creo un metodo per lo stato dell'apertura che si basa sui due precedenti e ritornerà un messaggio di
        global aperto           #stampa, chiuso o aperto in base all'esito di apri_ristorante() o chiudi_ristorante()
        if aperto:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")

    def aggiungi_al_menu(self): #metodo per aggiungere un piatto chiedendo nome e prezzo da input

        nome_piatto = input("Inserisci il nome del piatto: ")
        prezzo = input("Inserisci il prezzo: ")
        piatto = {"nome_piatto":nome_piatto, "prezzo":prezzo}   #creo un dizionario con il piatto inserito e faccio un append nella
        Ristorante.menu.append(piatto)  #lista, dopodichè stampo la lista per vedere il menù attuale
        print("Il piatto è stato aggiunto!")
        print(Ristorante.menu)

    def togli_dal_menu(self):   #metodo per rimuovere un piatto dal menu chiedendo il nome da input e facendo un confronto

        nome_piatto = input("Inserisci il nome del piatto che vuoi rimuovere: ")
        trovato = False
        for piatto in Ristorante.menu:
            if piatto["nome_piatto"] == nome_piatto:    #se il nome del piatto da input coincide con la il valore della chiave 
                Ristorante.menu.remove(piatto)  #"nome_piatto", faccio remove dalla lista e printo il menù aggiornato
                print(f"Prodotto {piatto['nome_piatto']} eliminato con successo!")
                trovato = True
                break
        
        if not trovato: #se non trova il piatto stampa un messaggio e poi di nuovo il menu attuale
            print("Il piatto non è nel menù!")

        print(Ristorante.menu)
    
    def stampa_menu(self):  #metodo di stampa a video del menu, se trova almeno un piatto, altrimenti messaggio di errore

        print(f"Il menù a disposizione è: {Ristorante.menu}")
        
    
""" ristorante = Ristorante("Mc Donald's", "Fast Food")
ristorante.apri_ristorante()
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.aggiungi_al_menu() """

ristorante = Ristorante("Mc Donald's", "Fast Food") #creo un oggetto Ristorante e inserisco il nome e il tipo cucina
ristorante.apri_ristorante()    #uso l'oggetto per chiamare il metodo di apertura (Chiede se voler aprire)
ristorante.stato_apertura()     #uso l'oggetto per chiamare il metodo di stato di apertura (Stampa lo stato)
ristorante.descrivi_ristorante()    #uso l'oggetto per chiamare il metodo di descrizione (Stampa la descrizione)

while True: 

    print("Menu: ") #menu
    print("1. Aggiungi un piatto al menù")
    print("2. Rimuovi un piatto dal menù")
    print("3. Stampa il menu: ")
    scelta = int(input("Scegli l'opzione che vuoi eseguire: ")) #scelta opzioni
    print("\n")

    if scelta == 1:
        ristorante.aggiungi_al_menu()   #chiamo il metodo di aggiunta
    elif scelta == 2:
        ristorante.togli_dal_menu() #chiamo il metodo di rimozione
    elif scelta == 3:
        ristorante.stampa_menu()    #chiamo il metodo di stampa
    else:
        ristorante.chiudi_ristorante()  #chiedo se chiudere e in caso affermativo stato apertura printa "chiuso", poi quit()
        ristorante.stato_apertura()
        quit()

    print("\n")
    continua = input("Vuoi effettuare un'altra operazione? ")   #nuova operazione ?
    if continua != "si":
        print("\nArrivederci!")
        break



    

    