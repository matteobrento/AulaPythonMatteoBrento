studente = {
    "nome" : "Matteo",
    "eta" : 23,
    "sesso": "Maschio"
}

print(studente)
print("\n")

studente["eta"] = 24
print(studente)
print("\n")

studente["eta"] = 23
print(studente)
print("\n")

studente["città"] = "Bari"
print(studente)
print("\n")

print(studente.keys())
print(studente.values())
print(studente.items())
print(studente.get("nome"))
print(studente.get("eta"))
print("\n")


lista = [True, 12, "Ciao"]  #lista con booleano, intero, stringa
dizionario = {
    "tipididato" : lista    #associo la lista come valore ad una chiave denominata "tipididato"
}

print(dizionario)   #stampa