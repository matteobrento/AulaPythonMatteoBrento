import random as r

numeri_casuali = []

for i in range(5):
    numeri_casuali.append(str(r.randint(0,50)))

#print(f"Lista prima di usare il join : {numeri_casuali}")
separatore = " "
stringa_da_inserire = separatore.join(numeri_casuali)
#print(f"Lista trasformata in stringa suddividendo i valori con spazi: {stringa_da_inserire}")


with open("numeri.txt", "w") as file:
    file.write(stringa_da_inserire)


with open("numeri.txt", "r") as file:
    stringa = file.read()
    print(f"La stringa di valori tra cui indovinare è: {stringa}")


lista_da_indovinare = stringa.split(" ")
#print(lista_da_indovinare)

tentativi = 0

while tentativi < 3:

    num1 = input("Inserisci un numero intero tra 0 e 50: ")
    if num1 in lista_da_indovinare:
        print("Numero indovinato!")
    else:
        print("Numero non indovinato!")

    tentativi+=1

print("Hai terminato i tentativi!")