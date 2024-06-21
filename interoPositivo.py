conteggio = 0   #variabile per conteggiare i tentativi
somma = 0   #variabile somma

while conteggio < 3:    #inizio del ciclo
    numPos = int(input("Inserisci un numero intero positivo: "))    #inserimento
    
    if(numPos >= 0):    #condizione numero positivo

        print("I numeri positivi pari nel range sono: ")
        for i in range(0,numPos+1,1):
            if(i%2 == 0):
                print(i)
        
        for i in range(0,numPos+1,1):
            if(i%2 != 0):
                somma += i
        print("La somma dei numeri dispari è: ", somma)

        if(somma > 250):
            print("Hai vinto!")
            break
        
    else:        
        conteggio += 1
        print("Il numero non è positivo ")
        if(conteggio == 3):

            print("Hai finito i tentativi")



        


        