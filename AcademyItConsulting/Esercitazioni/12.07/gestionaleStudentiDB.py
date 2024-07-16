"""
create un gestionale scolastico basato su un database mysql, 
l'utente può inserire per ogni studente, nome, cognome, 
e 3 voti, uno per italiano, uno per matematica e uno per storia.
Se esistono già studenti si possono modificare le informazioni o eliminare.
"""

import mysql.connector

def connessione_server():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        print(mydb)
        print("connessione ok")
    except:
        print("Connessione non avvenuta!")

    mycursor = mydb.cursor()

def connessione_database():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = 'gestionale_scolastico'
        )
        print("connessione ok")
        
        return mydb
    except:
        print("Connessione non avvenuta!")

def crea_tabella():
    mycursor.execute("CREATE TABLE studenti (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),cognome VARCHAR(255), italiano INT, matematica INT, storia INT)")

def inserimento_valori():
    query = "INSERT INTO studenti (name, cognome, italiano, matematica, storia) VALUES (%s, %s, %s, %s, %s)" 
    nome = input("Inserisci nome: ")
    cognome = input("Inserisci cognome: ")
    italiano = input("Inserisci italiano: ")
    matematica = input("Inserisci matematica: ")
    storia = input("Inserisci storia: ")
    val = (nome, cognome, italiano, matematica, storia)
    
    mycursor.execute(query, val)
    mydb.commit()   #il commit carica i valori nel database
    
    print(mycursor.rowcount, "record inserted.")    #conta le righe inserite

def stampa_tabella():
    query = "SELECT * FROM studenti"
    mycursor.execute(query)
    lista = []
    for tabella in mycursor:
        lista.append(tabella)
        print(tabella)
    return lista

def aggiorna(query):
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record aggiornati.")

def modifica_studente():
    tabella =stampa_tabella()
    if len(tabella)<1:
        print("la tabella è vuota")
    else:
        selezione = int(input("Inserire l'id dello studente che si vuole modificare: "))
        trovato = False
        for riga in tabella:
            if riga[0] == selezione:
                trovato = True
        if not trovato:
            print("Studente non presente")
        else: 
            dizionario ={"1":"name","2":"cognome","3":"italiano","4":"matematica","5":"storia"}
            scelta = input("""Cosa vuoi modificare:
            1. nome
            2. cognome
            3. voto italiano
            4. voto matematica
            5. voto storia
            """)
            modifica = input("Digitare modifica: ")
            query = f"UPDATE studenti SET {dizionario[scelta]} = '{modifica}' WHERE ID = {selezione}"
            aggiorna(query)

def eliminazione(query):
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")


def elimina_studente():
    tabella = stampa_tabella()
    if len(tabella)<1:
        print("la tabella è vuota")
    else:
        selezione = int(input("Inserire l'id dello studente che si vuole eliminare: "))
        trovato = False
        for riga in tabella:
            if riga[0] == selezione:
                trovato = True
        if not trovato:
            print("Studente non presente")
        else: 
            query = f"DELETE FROM studenti WHERE ID = {selezione} "
            eliminazione(query)


def menù():
    info_menù = """ 
    1: aggiungi studente
    2: modifica studente
    3: elimina studente
    4: visualizza tabella
    5: exit
    """
    scelta_menu= input(info_menù)
    return scelta_menu


while True:

    mydb = connessione_database()
    mycursor = mydb.cursor()

    scelta_menu = menù()
    if scelta_menu == "1":
        inserimento_valori()
    elif scelta_menu == "2":
        modifica_studente()
    elif scelta_menu == "3":
        elimina_studente()
    elif scelta_menu == "4":
        t = stampa_tabella()
    elif scelta_menu == "5":
        break
    else:
        print("Scelta non valida")