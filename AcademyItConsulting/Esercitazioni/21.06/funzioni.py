def saluto(nome):
    print("ciao", nome)
    print("Benvenuto nel nostro programma! ")

saluto("Matteo")



a = int(input("Inserisci a: "))
b = int(input("Inserisci b: "))
def somma(a, b):
    print("La somma di a e b è:", a+b)

somma(a, b)


numero = int(input("Inserisci un numero: "))
def quadrato (numero):
    return numero*numero    #return fa tornare un valore nel punto in cui è chiamata la funzione

risultato = quadrato(numero)
print(risultato)


def somma(**argomenti): #se metto il secondo parametro = 0 vuol dire che è opzionale, sarà 0, qualora prenderà un altro valore si usera quello
                    #se uso *argomento mi passa una serie di argomenti, un numero indefinito 
    print(argomenti)
    print(argomenti["Italiano"])   #se usiamo 2 asterischi ** possiamo chiamare gli argomenti come parametri di un dizionario
    
somma(Italiano = 5, Matematica = 6)

