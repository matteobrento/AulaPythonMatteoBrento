username_predef = "matteo"  #username predefinito
password_predef = "12345"   #password predefinita
esito = False

username = input("Inserisci il tuo Username: ") #chiedo all'utente di inserire l'username
password = input("Inserisci la tua Password: ") #chiedo all'utente di inserire la password

if(username == username_predef and password_predef == password):    #condizione di and per verificare username e password
    print("Credenziali Corrette, Benvenuto \n")
    esito = True

elif(username == "matteobrento" and password == "12345"):   #condizione di and per verificare username diverso e password
    print("Le credenziali sono corrette, ti ho permesso di accedere con un username differente da quello predefinito! \n")
    esito = True

else: 
    print("Username o Password errati, Login non riuscito \n")  #stampa del messaggio di errore

if(esito == True):

    print("Il login è stato effettuato con successo, ora scegli una di queste due domande di sicurezza: \n")
    print("1) Colore Preferito\n2) Animale Preferito\n")    #scelta della domanda di sicurezza
    print("\n")

    cod = int(input("Digita un opzione: "))
    print("\n")

    if(cod == 1):
        colore = input("Seleziona il tuo colore preferito: ")
        print("La tua risposta di sicurezza è: " + colore)
        print("\n")
        print("Procedura completata correttamente")

    else:
        animale = input("Seleziona il tuo animale preferito: ")
        print("La tua risposta di sicurezza è: " + animale)
        print("\n")
        print("Procedura completata correttamente")








