controllo = True   #variabile per conteggiare i tentativi
controllo1 = True
somma = 0   #variabile somma


print("1) Numero Positivo\n2) Lista\n3) Somma numeri pari della Lista\n4) Numeri dispari della Lista\n5) ") 
print("\n")
cod = int(input("Scegli l'operazione che vuoi eseguire: "))
print("\n")
if(cod==1):
    while controllo:    #inizio del ciclo
        
        numPos = int(input("Inserisci un numero intero positivo: "))

        if(numPos > 0):    #condizione numero positivo

            for i in range(1,numPos+1,1):   #ciclo for che parte da 1 (lo 0 è escluso perchè permette di uscire dal programma)
                if(i%2 == 0):               #e arriva al numero positivo inserito incluso, con step di 1, stampando la somma dei numeri pari
                    somma += i
                    print("La somma dei numeri pari è: ", somma)    #print della somma
                    controllo = False
        
            for i in range(1,numPos+1,1):   #ciclo for che parte da 1 (lo 0 è escluso perchè permette di uscire dal programma)
                if(i%2 != 0):               #e arriva al numero positivo inserito incluso, con step di 1, stampando i numeri dispari
                    print(f"Numeri dispari: {i}")

    

        else:        
            print("Il numero non è positivo ")  #numero non positivo, inserire di nuovo

if(cod == 2):

    lista = []
    n = int(input("Inserisci n: "))
    for i in range(0, n, 1):
        numero_casuale = ((i * 37) % n) + 1
        lista.append(numero_casuale)
    print("Lista casuale:", lista)

if(cod == 3):

    lista = []
    n = int(input("Inserisci n: "))
    for i in range(0, n, 1):
        numero_casuale = ((i * 37) % n) + 1
        lista.append(numero_casuale)
    print("Lista casuale:", lista)

    somma = 0
    for i in lista:
        if(i%2 == 0):
            somma += i
    print("La somma dei numeri pari è: ", somma)

if(cod == 4):

    lista = []
    n = int(input("Inserisci n: "))
    for i in range(0, n, 1):
        numero_casuale = ((i * 37) % n) + 1
        lista.append(numero_casuale)
    print("Lista casuale:", lista)

    for i in range(0, n, 1):   
        if(i%2 != 0):               
            print(f"Numeri dispari: {i}")

if(cod == 5):

    lista = []
    n = int(input("Inserisci n: "))
    for i in range(0, n, 1):
        numero_casuale = ((i * 37) % n) + 1
        lista.append(numero_casuale)
    print("Lista casuale:", lista)

    Primo = True

    for i in lista:   #calcolo numero primo
        if(i > 1):
            Primo = True

        if(i == 0):
            Primo = False
            break
                
        if Primo:
            print(f"{i} è un numero primo.")

        else:
            print(f"{i} non è un numero primo.")





       