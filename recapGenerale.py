prodottiDict = []   #lista prodotti vuota

# Funzione per aggiungere un prodotto
def aggiungiProdotto():
    id = input("Inserisci l'id del prodotto: ")
    nome = input("Inserisci il nome del prodotto: ")
    nuovo_prodotto = {"id": id, "nome": nome}   #creo un dizionario con i valori
    prodottiDict.append(nuovo_prodotto) #aggiungo il nuovo prodotto alla lista
    print("Prodotto aggiunto correttamente")
    mod_file(prodottiDict)  #scrivo su file l'aggiunta di un prodotto

# Funzione per eliminare un prodotto
def eliminaProdotto():
    id = input("Inserisci l'id del prodotto che vuoi eliminare: ")  #ricerco in base all'id
    trovato = False
    for prodotto in prodottiDict:
        if prodotto["id"] == id:    #se l'id inserito è uguale all'id del prodotto, elimina
            prodottiDict.remove(prodotto)   #metodo remove per rimuovere
            print(f"Prodotto {prodotto['nome']} eliminato con successo!")
            trovato = True
            break
    if not trovato:
        print("Prodotto non trovato!")
    mod_file(prodottiDict)  #riscrittura del file

# Funzione per visualizzare il menu
def menu():
    print("1. Aggiungi Prodotto")
    print("2. Elimina Prodotto")
    print("3. Esci dal programma")

# Funzione per salvare i prodotti su file
def mod_file(dizionario):
    with open("01.07\\prodotti_aggiornati.txt", "w") as file:   #funzione di scrittura su file "w"
        for prodotto in dizionario: #itero il dizionario 
            file.write(f"{prodotto['id']}:{prodotto['nome']}\n")    #formattazione dell'output
    print("Prodotti salvati su file con successo!")

# Funzione per caricare i prodotti dal file (se esiste)
def carica_da_file():
    try:    #blocco try-except
        with open('01.07\\prodotti_aggiornati.txt', 'r') as file:   #funzione di lettura da file "r"
            global prodottiDict #uso global per prendere la lista che fa parte dello spazio globale
            prodottiDict = []   #lista vuota
            for riga in file:   #itero le righe nel file, usando strip per rimozione di spazi e splittando tramite i ":"
                id, nome = riga.strip().split(':')
                prodottiDict.append({"id": id, "nome": nome})   #aggiunta del dict prodotto alla lista prodotti
            print("Prodotti caricati dal file con successo!")
    except FileNotFoundError:   #nel caso in cui non mi trova il file, printa
        print("Nessun file di prodotti trovato")


username = "matteo"
password = "12345"


while True: #while per ripetere le credenziali finche non sono giuste
    user = input("Inserisci l'username: ")
    psw = input("Inserisci la password: ")

    if user == username and psw == password:    #if che controlla se le credenziali di login coincidono
        print("Login effettuato con successo! Benvenuto in un gestionale di prodotti!")
        print("\n")

        carica_da_file()    #carica il file all'avvio per i prodotti

        while True:
            print("Menù: ")
            menu()
            scelta = input("Scegli un'opzione: ")

            if scelta == "1":
                aggiungiProdotto()
            elif scelta == "2":
                eliminaProdotto()
            elif scelta == "3":
                mod_file(prodottiDict)  #salva i prodotti sul file ed esce
                print("Uscita dal programma.")
                break
            else:
                print("Opzione non valida, riprova!")
            print("\nProdotti attuali:", prodottiDict)  #se scelgo un'opzione che non rientra nel menu mi dice non valida e stampa 
        break                                           #la lista attuale di prodotti
    else:
        print("Credenziali errate, riprova!")



        