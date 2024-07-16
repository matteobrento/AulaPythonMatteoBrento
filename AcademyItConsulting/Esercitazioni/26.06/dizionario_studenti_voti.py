"""
Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All'avvio il programma chiede se si vuole leggere l'elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto, se si vuole eliminare un alunno o un
voto.

nome_cognome, 3,7,2,4
nome_cognome2, 5,7,9,1,2
"""

import os

if os.path.exists("26.06\\voti_aggiornati.txt"):
    pass
else:
    print("Il file non esiste")
    exit()

#{"tommaso":[7,6,8],"giuseppe":[7,5,10]}

with open("26.06\\voti_aggiornati.txt","r") as file:
    contenuto=file.read()

print(f"Contenuto attuale del file: {contenuto}\n")
#bisogna pulire i dati

inutili="[]\"\"\'{} "
#print(inutili)

contenuto_pulito=""
for element in inutili:
    contenuto=contenuto.replace(element,"")

contenuto=contenuto.replace(":",",")
lista=contenuto.split(",")
#print(contenuto)
#print(lista)
dizionario={}

for elemento in lista:
    if elemento.isalpha():
        dizionario[elemento]=[]
        nome=elemento
    else:
        dizionario[nome].append(int(elemento))

#print(dizionario)

def menu():
    print("Visualizzazione menù: ")
    print("1. Aggiungi voto")       
    print("2. Aggiungi studente")
    print("3. Rimuovi voto")
    print("4. Rimuovi studente")
    print("5. Media\n")

def aggiungi_alunno(dizionario):
    nome = input("Inserisci il nome dello studente: ").strip()  # Chiede il nome dello studente
    if nome in dizionario:
        print("Studente già presente.")  # Verifica se lo studente è già presente
    else:
        dizionario[nome] = []  # Aggiunge il nuovo studente con una lista vuota di voti

def aggiungi_voto(dizionario):
    nome = input("Inserisci il nome dello studente: ").strip()  # Chiede il nome dello studente
    if nome not in dizionario:
        print("Studente inesistente.")
    else:
        while True:
            voto=input(f"Inserisci voto di {nome}: " )
            if voto.isdecimal():
                break
            else:
                print("Inserisci un numero.")
        dizionario[nome].append(int(voto))

def mod_file(dizionario):
    with open("26.06\\voti_aggiornati.txt","w") as file:
        file.write(str(dizionario))
        
def rimuovi_voto(dizionario):
    nome = input("Inserisci il nome dello studente: ").strip()  # Chiede il nome dello studente
    if nome not in dizionario:
        print("Studente inesistente.")
    else:
        print(f"voti studente {nome}: {dizionario[nome]}")
        while True:
            voto_rim=input("Inserisci il voto che vuoi eliminare: ")
            if voto_rim.isdecimal():
                break
            else:
                print("Inserisci un numero")
        if int(voto_rim) in dizionario[nome]:
            dizionario[nome].remove(int(voto_rim))
        else:
            print("Voto non presente.")

def rimuovi_studente(dizionario):
    nome = input("Inserisci il nome dello studente: ").strip()  # Chiede il nome dello studente
    if nome not in dizionario:
        print("Studente inesistente.")
    else:
        scelta = input("La accendiamo ?")
        if scelta == "si":
            #dizionario.pop(nome)
            del dizionario[nome]

def media(dizionario):

    for nome in dizionario:
        media = sum(dizionario[nome])/len(dizionario[nome])
        print(f"Nome: {nome}, Media: {media}")


while True:
    menu()
    scelta=input("Scegli, e veloce anche: ")
    if scelta=="1":
        aggiungi_voto(dizionario)
        mod_file(dizionario)
        print("Dizionario aggiornato:",dizionario)
    elif scelta=="2":
        aggiungi_alunno(dizionario)
        mod_file(dizionario)
        print("Dizionario aggiornato:",dizionario)
    elif scelta=="3":
        rimuovi_voto(dizionario)
        mod_file(dizionario)
        print("Dizionario aggiornato:",dizionario)
    elif scelta=="4":
        rimuovi_studente(dizionario)
        mod_file(dizionario)
        print("Dizionario aggiornato:",dizionario)
    elif scelta=="5":
        media(dizionario)
        mod_file(dizionario)
        print("Dizionario aggiornato:",dizionario)
    else:
        print("Hai sbagliato")

    scelta=input("Continuare? ").lower()
    if scelta!="si":      
        print("Programma terminato!")
        break
