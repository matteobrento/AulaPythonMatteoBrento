"""
Scrivete un programma che utilizza una funzione che accetta come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ai rimpianti rimediamo Maria’ è palindroma
‘Ciao’ non è palindroma
"""
stringa = input("Inserisci una stringa: ")

def palindroma(stringa):

    punteggiatura = [" ", ".", ",", ";", ":"]
    for p in punteggiatura:
        stringa = stringa.lower().replace(p,"")
        
    stringa1 = stringa[::-1]
    print(stringa1)

    if(stringa == stringa1):
        print("La stringa è palindroma")
    
    else:
        print("La stringa non è palindroma")

palindroma(stringa)


