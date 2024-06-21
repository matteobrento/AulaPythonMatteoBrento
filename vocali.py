stringa = input("Inserisci una stringa: ")  #inserisco in input una stringa che ha x vocali

vocali = "aeiouAEIOU"   #in questa stringa sono contenute tutte le vocali maiuscole e minuscole

contatore = 0   
for i in stringa:   #faccio interare la stringa inserita in input tramite l'elemento i
    if i in vocali: #a questo punto se i si trova nella stringa vocali il contatore incrementa
        contatore += 1
    
print(f"Numero di vocali trovate nella stringa: {contatore}")   #stampa