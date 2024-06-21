import random
def generaNumero(): #funzione genera numero casuale

    return random.randint(1, 100)   #ho trovato in internet questa funzione che genera randomicamente tramite l'import random

def gioca():    #funzione di lancio del gioco

    numero = generaNumero() #associo alla variabile il numero generato con la funzione precedente
    tentativi = 0   #counter dei tentativi
    
    while True:
        tentativo = int(input("Indovina il numero (compreso tra 1 e 100): "))
        tentativi += 1  #incremento di ogni tentativo fatto
        
        if tentativo == numero:
            print(f"Complimenti! Hai indovinato il numero {numero} in {tentativi} tentativi.")
            break
        elif tentativo < numero:
            print("Il numero da indovinare è più alto.")
        else:
            print("Il numero da indovinare è più basso.")


gioca() #lancio della funzione gioca()