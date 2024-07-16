import mysql.connector

def connessione_server():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
        )

        #print(mydb)
        print("Connessione avvenuta! ")
        return mydb
    
    except:
        print("Connessione non avvenuta! ")


def connessione_database():
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "testpython"
        )

        #print(mydb)
        print("Connessione avvenuta! ")    
        return mydb
    
    except:
        print("Connessione non avvenuta! ")

mydb = connessione_database()
mycursor = mydb.cursor()  #si connette al database specificato

#mycursor.execute("CREATE DATABASE testPython") #commento perche ho già creato
""" mycursor.execute("SHOW DATABASES")
for database in mycursor:
    print(database) """

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
""" mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table) """

def inserimento_valori(query, val):
    """ 
    query = "INSERT INTO customers (nome, cognome, italiano, matematica, storia) VALUES (%s, %s)" #i segnaposto evitano problemi di sql inception(?)
    val = [("Matteo", "Bari 21"), ("Giulio", "Milano 12")]    #un singolo valore ("valore",) seno la tupla non funziona 
    """
    mycursor.executemany(query, val)

    mydb.commit()   #il commit carica i valori nel database

    print(mycursor.rowcount, "record inserted.")    #conta le righe inserite




