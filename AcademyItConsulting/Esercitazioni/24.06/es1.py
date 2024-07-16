""" Create un programma che richiede all’utente Nome, anno di nascita e giorno della settimana (a numero) e stampa in
maniere formattata oltre al nome, l’età e i giorni che mancano al prossimo weekend (sabato):
Esempio: ’Il tuo nome è Tommaso, hai 37 anni e mancano 5 giorni al weekend’ """

nome = input("Inserisci il tuo nome: ")
anno = input("Inserisci il tuo anno di nascita: ")
giorno = int(input("Inserisci il giorno della settimana: "))

print(f"Il tuo nome è: {nome}, hai {2024-int(anno)} anni e mancano {6 - giorno} giorni al weekend")

