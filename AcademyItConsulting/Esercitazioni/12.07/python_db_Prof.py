import mysql.connector

def connessione_server():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port ="8889"
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
        port ="8889",
        database = 'testpython'
        )
        print("connessione ok")
        
        return mydb
    except:
        print("Connessione non avvenuta!")



def inserimento(query, val):
    mycursor.executemany(query, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def seleziona(query):

    mycursor.execute(query)
    risultati = mycursor.fetchall()

    for risultato in risultati:
        print(risultato)

def eliminazione(query):
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")

def aggiorna(query):
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record aggiornati.")




"""query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [("marco", "roma 31"),("antonio", "milano 31")]"""

mydb =connessione_database()
mycursor = mydb.cursor()

#query = "select * from customers"

#seleziona(query)

"""query = "delete from customers where address = 'milano 31'"

eliminazione(query)"""

query = "update customers set address= 'catanzaro 10' where address = 'roma 31'"
aggiorna(query)

query = "select * from customers"

seleziona(query)