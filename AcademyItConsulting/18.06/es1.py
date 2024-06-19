#Creare una serie di condizioni una dentro l'altra che a fronte di un input per ogni if decidano se farti passare o no (3 livelli, ==)

cod = int(input("Inserisci cod: "))

if (cod >  0):
    print("primo livello superato")
   
    cod = int(input("Inserisci cod: "))
    if (cod >= 5 and cod <= 10):
        print("secondo livello superato")
      
        cod = int(input("Inserisci cod: "))
        if (cod == 7):
            print("terzo livello superato")
        else:
            print("Accesso negato")
    else:
        print("Accesso negato")
else:
    print("Accesso negato")

