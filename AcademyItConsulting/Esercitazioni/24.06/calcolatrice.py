"""
create una calcolatrice semplificata che fa operazione solo su 2 numeri, 
l'utente inserisce primo numero, secondo numero e operazione matematica e il programma ci restituisce il risultato
"""

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

print("Menu")
print("1) Somma \n2) Differenza \n3) Prodotto \n4) Divisione \n")
cod = int(input("Scegli l'operazione che vuoi effettuare "))

if(cod == 1):
    print("La somma dei due numeri è", num1 + num2)

elif(cod == 2):
    print("La differenza tra i due numeri è", num1 - num2)

elif(cod == 3):
    print("Il prodotto tra i due numeri è", num1 * num2)

elif(cod == 4):
    print("La divisione tra i due numeri è", num1 / num2)

else:
    print("Esci dalla calcolatrice")
    