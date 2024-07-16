num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

print("1) Addizione\n2) Sottrazione\n3) Moltiplicazione\n4) Divisione\n") 
print("\n")
cod = int(input("Scegli l'operazione che vuoi eseguire: "))
print("\n")

if(cod == 1):
    
    print(num1 + num2)
    print("\n")

elif(cod == 2):

    print(num1 - num2)
    print("\n")

elif(cod == 3):

    print(num1 * num2)
    print("\n")

elif(cod == 4):
    if(num1 == 0 or num2 == 0):
        print("Errore: Divisione per Zero")
        print("\n")
    else:
        print(num1 / num2)
        print("\n")

else:
    print("Operazione non riconosciuta")
    print("\n")