"""
Scrivete un programma che chiede un numero all’utente e restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }
"""
controllo = True

def quadrato(numero):
    return numero**2

def pari_o_dispari(numero):

    if numero%2 == 0:
        return"Pari"
    
    else:
        return"Dispari"
    
def cifre(numero):
    return len(str(numero))

while controllo:

    numero = int(input("Inserisci un numero: "))

    dict = {
        "quadrato" : quadrato(numero),
        "pari_o_dispari" : pari_o_dispari(numero),
        "numero_cifre" : cifre(numero)
    }

    print(dict)

    continua = input("Vuoi inserire un altro numero ? ")
    if continua == "no":
    
        print("Programma Terminato")
        controllo = False
    