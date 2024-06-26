from random import randint

numeri=[]
for i in range(5):
    numeri.append(str(randint(0,50)))

spazio= " "
stringa=spazio.join(numeri)
#print(stringa)

with open("file.txt","w") as file:
    file.write(stringa)

with open("file.txt","r") as file:
    stringa=(file.read())
print("La stringa del file è: ",stringa)

lista_da_ind=stringa.split(" ")
#print("La lista è:",lista_da_ind)

tent=0
ind=0

while tent<4 and ind<2:

    print("Numero tentativo: ",tent+1)
    turno = 2
    while turno > 0:
        num1=input("\ninserisci un numero: ")
        if num1 in lista_da_ind:
            ind+=1
            print("Hai indovinato!")

        else:
            print("Non hai indovinato!")

        turno -= 1
    tent += 1

if ind==2:
    print("\nHai indovinato 2 numeri.")

elif tent==4:
    print("\nHai finito i tentativi.")

print("\nProgramma Terminato")

