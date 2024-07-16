def generaNumero():     #funzione di generazione del numero
    numero = int(input("Inserisci un numero: "))
    return numero

def fibonacci(n):       #prof qui mi sono aiutato con internet perchè ho avuto difficolta con i calcoli matematici per la serie :(

    sequenza = [0, 1]

    if(n <= 0):
        print("Inserire un numero maggiore di 0")
        return
    
    if n == 1:
        return [0]
    
    while len(sequenza) < n:
        sequenza.append(sequenza[-1] + sequenza[-2])
    
    return sequenza


numero = generaNumero()
fibonacci(numero)
print("La sequenza di Fibonacci è la seguente:", fibonacci(numero))
