giocatori = {"1":3, 
             "2":8, 
             "3":8, 
             "4":6}

conv_ruoli = {"1": "Portiere", 
              "2": "Difensore", 
              "3": "Centrocampista", 
              "4": "Attaccante"}

def leggi_db_calcio():
    with open("28.06\\calcio.csv", "r") as file:
        db_calcio = file.read()
    return db_calcio

def scrivi_db_calcio(dato, metodo):
    with open("28.06\\calcio.csv", metodo) as file:
            file.write(dato)

def conteggio_ruolo(ruolo, matrice):
    numero = 0
    for e in matrice:
        if e[1] == ruolo:
            numero +=1
    return numero

def conv_matrice(dato):
    righe = dato.split("\n")
    if len(righe) < 1:
        print("Database Vuoto!")
    elif len(righe) > 1:
        righe_ok = []
        for riga in righe:
            righe_ok.append(riga.split(","))
    else:
        righe_ok = righe.split()
    return righe_ok

def conv_salvataggio(dato):
    if len(dato)>1:
        lista = []
        for riga in dato:
            lista.append(",".join(riga))
        stringa = "\n".join(lista)
    else:
        stringa = ",".join(dato)
    
    return stringa

""" def verifica_db():
    try:
        leggi_db_calcio()
    except:
        scrivi_db_calcio(dato, "w") """
    
def aggiungi_giocatore():
    contenuto = leggi_db_calcio()
    squadra_matrice = conv_matrice(contenuto)
    if len(squadra_matrice)>24:
        print("Hai raggiunto il numero massimo di calciatori!")
        print(squadra_matrice)

    else:
        ruolo_inserito = input("Inserisci il ruolo del giocatore (1.Portiere, 2.Difensore, 3.Centrocampista, 4.Attaccante): ")
        if ruolo_inserito in giocatori:
            num_max = giocatori[ruolo_inserito]
            num_pres = conteggio_ruolo(conv_ruoli[ruolo_inserito], squadra_matrice)
            if num_pres >= num_max:
                print("Hai raggiunto il numero massimo di calciatori per questo ruolo")
            else:
                nome = input("Inserisci nome del calciatore: ")
                squadra_matrice.append([nome, conv_ruoli[ruolo_inserito]])
                squadra_matrice_str = conv_salvataggio(squadra_matrice)
                scrivi_db_calcio(squadra_matrice_str, "w")
                print("Giocatore Inserito")
        else:
            print("Ruolo non valido!")

def rimuovi_giocatore():
    contenuto = leggi_db_calcio()
    squadra_matrice = conv_matrice(contenuto)
    
    nome = input("Inserisci nome calciatore: ")
    ruolo_inserito = input("Inserisci il ruolo del giocatore da rimuovere (1.Portiere, 2.Difensore, 3.Centrocampista, 4.Attaccante): ")
    trovato = False
    for riga in squadra_matrice:
        if riga[0] == nome and riga[1] == conv_ruoli[ruolo_inserito]:
            squadra_matrice.remove(riga) 
            trovato = True
            squadra_matrice_str = conv_salvataggio(squadra_matrice)
            scrivi_db_calcio(squadra_matrice_str, "w")
            print("Giocatore eliminato!")
        if not trovato:
            print("Giocatore non trovato!")

def visualizza(matrice):
    contenuto = leggi_db_calcio()
    squadra_matrice = conv_matrice(contenuto)
    for element in matrice:
        print(f"Nome: {element[0]}, Ruolo: {element[1]}")

    print(squadra_matrice) 
    
def menu():
    while True:
        print("Menu: ")
        print("1. Aggiungi un calciatore \n2. Rimuovi un calciatore \n3. Visualizza l'elenco dei calciatori")
        scelta = input("Seleziona un'opzione: ")
        if scelta == '1':
            aggiungi_giocatore()
        elif scelta == "2":
            rimuovi_giocatore()
        elif scelta == "3":
            visualizza()
            pass
        elif scelta == "4":
            exit()
        else:
            print("Opzione non valida.")
        break



usernameCoach = "admin"
passwordCoach = "1234"

print("Esegui il login per gestire la tua squadra: ")
user = input("Inserisci l'username: ")
psw = input("Inserisci la password: ")
if user == usernameCoach and psw == passwordCoach:
    print("Buongiorno Coach! Login effettuato con successo.")
    menu()
else:
    print("Credenziali errate.")


