controllo = True   #variabile per conteggiare i tentativi
somma = 0   #variabile somma

while controllo:    #inizio del ciclo
    numPos = int(input("Inserisci un numero intero positivo: "))    #inserimento
    
    if(numPos > 0):    #condizione numero positivo

        for i in range(1,numPos+1,1):   #ciclo for che parte da 1 (lo 0 è escluso perchè permette di uscire dal programma)
            if(i%2 == 0):               #e arriva al numero positivo inserito incluso, con step di 1, stampando la somma dei numeri pari
                somma += i
        print("La somma dei numeri pari è: ", somma)    #print della somma
        
        for i in range(1,numPos+1,1):   #ciclo for che parte da 1 (lo 0 è escluso perchè permette di uscire dal programma)
            if(i%2 != 0):               #e arriva al numero positivo inserito incluso, con step di 1, stampando i numeri dispari
                print(f"Numeri dispari: {i}")

    elif(numPos == 0):  #condizione di break, schiacciando 0 il programma termina
        #break
        controllo = False
        
    else:        
        print("Il numero non è positivo ")  #numero non positivo, inserire di nuovo
        

