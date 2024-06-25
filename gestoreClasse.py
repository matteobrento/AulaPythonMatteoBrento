"""
Scrivete un programma che prenda i nomi degli alunni di una classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10
"""
controllo = True

listaNomi = []
#listaVoti = []
dict = {}

while controllo:

    nome = input("Inserisci il nome di uno studente: ")
    
    if nome not in listaNomi:
        listaNomi.append(nome)
        dict[nome] = []

    while controllo:
        voto = int(input(f"Inserisci un voto per {nome}: "))
        dict[nome].append(voto)
        print("\n")

        continua = input("Vuoi inserire un altro voto? ")
        if continua == "no":
            break

    continua = input("Vuoi inserire un altro studente ? ")
    if continua == "no":
        controllo = False

    print(dict)
    print("\n")

for nome in listaNomi:

    voti = dict[nome]
    media = sum(voti)/len(voti)

    print(f"Nome: {nome}, Media: {media}")

    



    