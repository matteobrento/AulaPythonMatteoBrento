stringa = input("Inserisci una stringa: ")

punteggiatura = [".", ",", ";", ":"]
for p in punteggiatura:
    stringa = stringa.lower().replace(p, "")

lista_parole = stringa.split(" ")

parole_incontrate = {}
for parola in lista_parole:
    parole_incontrate[parola] = lista_parole.count(parola)
lista_ripetizioni = list(parole_incontrate.values())

if max(lista_ripetizioni) > 1:
    print(parole_incontrate)
else:
    print("Non ci sono ripetizioni")



        
          
                

