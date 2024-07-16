"""
Scrivete un programma che chiede all'utente una lista di parole e restituisce la lunghezza di ogni parola.
"""

#Lista con valori preimpostati
lista = ["ciao", "mi", "chiamo", "Matteo"]

for parola in lista:
    print(f"La lunghezza della stringa {parola} è: ", len(parola))

print("\n")


#Lista richiesta all'utente con uno spazio tra ogni parola
lista = ("Inserisci una lista di parole separate da uno spazio: ")
listaSplittata = lista.split(" ")
for parola in listaSplittata:
    print(f"La lunghezza della stringa {parola} è: ", len(parola))