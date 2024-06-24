"""
Scrivete un programma che chiede una stringa all’utente e restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
"""
controllo = True

while controllo:
    stringa = input("Inserisci una stringa: ")

    dict = {}

    for carattere in stringa:   #controllo del carattere nella stringa

        if carattere in dict:   #se il carattere si trova nel dizionario, viene incrementato
            dict[carattere] += 1
        
        else:                   #altrimenti viene impostato ad 1
            dict[carattere] = 1

    print(dict)
    print("\n")

    continua = input("Vuoi inserire un'altra stringa ?")
    if(continua == "si"):
        controllo = True
    
    else:
        print("Arrivederci!")
        controllo = False

        
        