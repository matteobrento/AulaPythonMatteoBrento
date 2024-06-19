#ESEMPIO DI PROPRIETARIETA
x = 2
if(x>1):
    print("Condizione Esatta \n" )

#INPUT DEL NOME DA TASTIERA
nome = input("Inserisci il tuo nome: ")
print("ciao, " + nome + "! Benvenuto in Python! \n")

nome = "Matteo"
eta = "23"
print(nome)
print(eta + "\n")
print("Il mio nome è: " + nome + " e la mia eta è: " + eta) #CONCATENAZIONE DI STRINGHE

print(1+2)
print(5+2)
print(1*2)
print(5/2) #DIVISIONE COL RESTO
print(2**2)
print("\n")


# *****I PROF VOGLIONO SEMPRE I CODICI*****

nome = "Ignazio"
print(nome[0]) #STAMPA IL VALORE IN POSIZIONE 0 POICHE UN ARRAY DI n CHAR PARTE DA 0 FINO a n-1 CARATTERI
print(nome[1])
print(nome[2] + "\n")

s = "Ciao, Mondo!"
print(len(s))           #STAMPA LA LUNGHEZZA
print(s.upper())        #STAMPA IL TESTO IN MAIUSCOLO
print(s.split(', '))    #DIVIDE LA STRINGA IN UNA LISTA DI SOTTOSTRINGHE SUDDIVISE DA UN CARATTERE (,)
print(s.replace('Mondo', 'Universo') + "\n")



x = 5
y = 10
z = 7 

print(x<y and y<z)
print(x<y or z>y)
print(not(x<y))
print("\n")

numero = 10
if (numero > 0):
    print("Il numero è positivo")
    if (numero == 100):
        print("wow")
elif (numero < 0):
    print("Il numero è negativo")

else: 
        print("Il numero è 0")






