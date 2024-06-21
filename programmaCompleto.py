controllo = True   #variabile per conteggiare i tentativi
somma = 0   #variabile somma

while controllo:    #inizio del ciclo
    numPos = int(input("Inserisci un numero intero positivo: "))    #inserimento
    
    if(numPos > 0):    #condizione numero positivo

        for i in range(1,numPos+1,1):
            if(i%2 == 0):
                somma += i
        print("La somma dei numeri pari è: ", somma)
        
        for i in range(1,numPos+1,1):
            if(i%2 != 0):
                print(f"Numeri dispari: {i}")

    elif(numPos == 0):
        break
        
    else:        
        print("Il numero non è positivo ")
        

