controllo = True
somma = 0

while controllo:
    intero = int(input("Inserisci un numero intero, 0 per terminare: "))

    if(intero == 0):
         controllo = False
    somma = somma + intero

    print("La somma è: ", somma)

controllo = False
print("\n")



parola = input("Inserisci una parola: ")
for p in parola:
     print(p)
print("\n")


N = int(input("Inserisci un massimo N: "))
step = int(input("Inserisci un valore di step: "))
for p in range(0, N, step):
     print(p)
print("\n")




    
    

  