# Lista dei prodotti
prodottiDict = []

# Funzione per aggiungere un prodotto
def aggiungiProdotto():
    id = input("Inserisci l'id del prodotto: ")
    nome = input("Inserisci il nome del prodotto: ")
    nuovo_prodotto = {"id": id, "nome": nome}
    prodottiDict.append(nuovo_prodotto)
    print("Prodotto aggiunto correttamente")
    mod_file(prodottiDict)

# Funzione per eliminare un prodotto
def eliminaProdotto():
    id = input("Inserisci l'id del prodotto che vuoi eliminare: ")
    trovato = False
    for prodotto in prodottiDict:
        if prodotto["id"] == id:
            prodottiDict.remove(prodotto)
            print(f"Prodotto {prodotto['nome']} eliminato con successo!")
            trovato = True
            break
    if not trovato:
        print("Prodotto non trovato!")
    mod_file(prodottiDict)

# Funzione per visualizzare il menu
def menu():
    print("1. Aggiungi Prodotto")
    print("2. Elimina Prodotto")
    print("3. Esci dal programma")

# Funzione per salvare i prodotti su file
def mod_file(dizionario):
    with open("01.07\\prodotti_aggiornati.txt", "w") as file:
        file.write(str(dizionario))
    print("Prodotti salvati su file con successo!")

# Funzione per caricare i prodotti dal file (se esiste)
def carica_da_file():
    try:
        with open('01.07\\prodotti_aggiornati.txt', 'r') as file:
            contenuto = file.read()
            global prodottiDict
            prodottiDict = eval(contenuto)
            print("Prodotti caricati dal file con successo!")
    except FileNotFoundError:
        print("Nessun file di prodotti trovato, inizializzo una lista vuota.")
        prodottiDict = []
    except SyntaxError:
        print("Errore di sintassi nel file, inizializzo una lista vuota.")
        prodottiDict = []

# Credenziali
username = "matteo"
password = "12345"

# Login utente
user = input("Inserisci l'username: ")
psw = input("Inserisci la password: ")

if user == username and psw == password:
    print("Login effettuato con successo! Benvenuto in un gestionale di prodotti!")
    print("\n")

    # Carica i prodotti dal file all'avvio
    carica_da_file()

    while True:
        print("Menù: ")
        menu()
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            aggiungiProdotto()
        elif scelta == "2":
            eliminaProdotto()
        elif scelta == "3":
            mod_file(prodottiDict)
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova!")
        print("\nProdotti attuali:", prodottiDict)
else:
    print("Credenziali errate, riprova!")

        