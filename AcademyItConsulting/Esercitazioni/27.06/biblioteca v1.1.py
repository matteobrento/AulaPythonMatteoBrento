"""
Dobbiamo creare un programma per la gestione di una biblioteca,
all'avvio del programma ci viene chiesto se siamo amministratori o utenti,
se siamo amministratori possiamo vedere i libri, aggiungere un libro
eliminare un libro.
il libro ha le seguenti caratteristiche:
- titolo
- autore
- anno
- stato prestito
"""
import pickle

def conversione_salvataggio_libro(dato):
    if len(dato) >1:
        righe = []
        for riga in dato:
            righe.append(",".join(riga))
        righe = "\n".join(righe)
    else:
        righe = ",".join(dato)
    
    return righe

def leggi_db_libri():
    with open("27.06\\db_libri.csv", "r") as file:
        db_libri = file.read()
    return db_libri

def leggi_db_utenti():
    with open("db_untenti.bin", "rb") as file:
        db_utenti = pickle.loads(file.read())
    return db_utenti

def verifica_db():
    try:
        db_utenti = leggi_db_utenti()
    except:
        user = input("Inserisci un nome utente: ")
        psw = input("Inserisci un nome utente: ")
        dizionario = {"amministratori":{user:psw},"utenti":{}}
        scrivi_utenti(dizionario)
        db_utenti = leggi_db_utenti()   
    libr_vuoti = True
    try:
        db_libri = leggi_db_libri()
    except:
        scrivi_libri("")
        db_libri = leggi_db_libri()
    
    if len(db_libri) >0:
        libr_vuoti = False

    return db_utenti , db_libri, libr_vuoti

def scrivi_libri(dato, metodo):
    with open("27.06\\db_libri.csv", metodo) as file:
            file.write(dato)

def scrivi_utenti(dato):
    dato_b = pickle.dumps(dato)
    with open("db_untenti.bin", "wb") as file:
            file.write(dato_b)

def aggiungi_utente_a():
    ruolo = input("1 per ruolo amministratore\n2 per ruolo 'utente': ")
    ruolo_ok = True
    if ruolo == "1":
        chiave = "amministratori"
    elif ruolo == "2":
        chiave = "utenti"
    else:
        print("Ruolo non valido!")
        ruolo_ok = False
    
    if ruolo_ok:
        user = input("Inserisci l'user: ")
        if user in db_utenti[chiave]:
            print("Utente già presente! ")
        else:
            psw = input("Inserisci la password: ")
            db_utenti[chiave][user] = psw
            scrivi_utenti(db_utenti)
            print("Utente aggiunto! ")

def inserisci_libro():
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci il autore del libro: ")
    anno = input("Inserisci anno del libro: ")
    stato = "libero"
    nuovo_libro =titolo+","+autore+","+anno+","+stato
    if libr_vuoti:
        scrivi_libri(nuovo_libro, "a")
        
    else:
        scrivi_libri("\n"+nuovo_libro,"a")
    
    print("Libro inserito correttamente!")

def elimina_libro():
    if libr_vuoti:
        print("Nessun libro da eliminare!")
    else:
        titolo = input("Inserisci il titolo del libro: ")
        righe = db_libri.split("\n")
        for riga in righe:
            if titolo == riga.split(",")[0]:
                righe.remove(riga)
                print("Libro eliminato!")
                if len(righe) >1:
                    righe = "\n".join(righe)
                else:
                    righe = "".join(righe)

                scrivi_libri(righe, "w")
            
            else:
                print("Libro non trovato!")
    
def visualizza_libri():
    if libr_vuoti:
        print("Nessun libro!")
    else:
        if len(db_libri) >1:
            righe = db_libri.split("\n")
            righe_convertite = []
            for riga in righe:
                riga = riga.split(",")
                righe_convertite.append(riga)
                print(f"Titolo: {riga[0]}, Autore: {riga[1]}, Anno: {riga[2]}, Stato: {riga[3]}")

        else:
            riga = db_libri.split(",")
            print(f"Titolo: {riga[0]}, Autore: {riga[1]}, Anno: {riga[2]}, Stato: {riga[3]}")
            righe_convertite = riga

        return righe_convertite
        
def login():
    tipo_utente = input("Inserisci 1 per amministratore\n2 per utente: ")
    return tipo_utente

def menu_amministratore():
    info_menu="""Inserisci 1 per inserire un libro\n
Inserisci 2 per eliminare libro\n
Inserisci 3 per visualizzare i libri\n
Inserisci 4 per aggiungere un utente\n
Inserisci 5 per uscire: """

    scelta_menu = input(info_menu)
    return scelta_menu

def menu_utente():
    info_menu="""Inserisci 1 per prendere in prestito un libro\n
Inserisci 2 per restituire un libro\n
Inserisci 3 per visualizzare i libri\n
Inserisci 5 per uscire: """
    scelta_menu = input(info_menu)
    return scelta_menu

db_utenti , db_libri, libr_vuoti =verifica_db()

print("Benvenuto nella biblioteca\n")

tipo_utente = login()
if tipo_utente == "1":
    user = input("Inserisci il tuo user: ")
    amministratori = db_utenti["amministratori"]
    for amministratore in amministratori:
        if user == amministratore:
            print("user corretto!")
            password = input("Inserisci la password: ")
            if amministratori[user] == password :
                print("Password corretta!")
                scelta_menu = menu_amministratore()
                if scelta_menu == "1":
                    inserisci_libro()
                elif scelta_menu == "2":
                    elimina_libro()
                elif scelta_menu == "3":
                    visualizza_libri()
                elif scelta_menu == "4":
                    aggiungi_utente_a()
                elif scelta_menu == "5":
                    print("Grazie per aver usato il programma!")
                    exit()
            else:
                print("Opzione non valida!")

elif tipo_utente == "2":
    utente_log = False
    iscrizione = input("Sei già iscritto? ")
    if iscrizione == "si":
        user = input("Inserisci il tuo user: ")
        tipo_ut = db_utenti["utenti"]
        for utenti in tipo_ut:
            if utenti == user:
                password = input("Inserisci la password: ")
                if tipo_ut[user] == password :
                    utente_log = True
    else:
        user = input("Inserisci il tuo user: ")
        if user in db_utenti["utenti"]:
            print("Utente già presente! ")
        else:
            psw = input("Inserisci la password: ")
            db_utenti["utenti"][user] = psw
            scrivi_utenti(db_utenti)
            print("Utente registrato! ")
    
    if utente_log:
        scelta_menu = menu_utente()
        if scelta_menu == "1":
            libri_in_biblio = visualizza_libri()
            titolo_libro = input("Inserisci il titolo del libro: ")
            libro_trovato = False
            for libro in libri_in_biblio:
                if titolo_libro == libro[0]:
                    libro_trovato = True
                    if libro[3] == "libero":
                        index = libri_in_biblio.index(libro)
                        libri_in_biblio[index][3] = "prestito"
                        print("Libro preso in prestito!")
                        dati = conversione_salvataggio_libro(libri_in_biblio)
                        scrivi_libri(dati, "w")
                    else:
                        print("Libro non disponibile preso in prestito!")
            
            if not libro_trovato:
                print("Libro non in biblioteca!")

        elif scelta_menu == "2":
            libri_in_biblio = visualizza_libri()
            titolo_libro = input("Inserisci il titolo del libro: ")
            libro_trovato = False
            for libro in libri_in_biblio:
                if titolo_libro == libro[0]:
                    libro_trovato = True
                    if libro[3] == "prestito":
                        index = libri_in_biblio.index(libro)
                        libri_in_biblio[index][3] = "libero"
                        print("Libro restituito!")
                        dati = conversione_salvataggio_libro(libri_in_biblio)
                        scrivi_libri(dati, "w")
                    else:
                        print("Libro non disponibile già restituito!")
            
            if not libro_trovato:
                print("Libro non in biblioteca!")

        elif scelta_menu == "3":
            visualizza_libri()
        elif scelta_menu == "4":
            print("Grazie per aver usato il programma!")
            exit
        else:
            print("Comando non valido")
    else:
        exit()
else:
    print("Comando non valido")

        




    