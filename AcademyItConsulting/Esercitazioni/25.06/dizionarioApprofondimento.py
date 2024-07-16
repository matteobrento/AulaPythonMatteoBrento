utenti = {

    "id1" : {"nome" : "Matteo", "cognome" : "Brento", "indirizzo" : "Via Marcisi"},
    "id2" : {"nome" : "Pietro", "cognome" : "Rossi"}
}

for id in utenti:
    #print(utenti[id]["nome"])

    print(f"nome utente '{utenti[id].get('nome', 'nome non presente')}', indirizzo '{utenti[id].get('indirizzo', 'indirizzo non presente')}'")
    #questa operazione è fondamentale nei database non relazionali, ovvero dove non tutti gli id hanno gli stessi valori 

