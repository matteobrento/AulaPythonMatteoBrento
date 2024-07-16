"""with open("test.txt", "w") as file: #with è una parola chiave crea un contesto d'uso
    print(file.write(" Matteo"))    #read legge solo il file e se non esiste da errore ("r")
                                    #x crea un file se non esiste, se esiste da errore
                                    #w write lo crea e sovrascrive il contenuto
                                    #a append aggiunge un elemento al file se esiste, altrimenti se il file non esiste lo crea e aggiunge
                                    #se aggiungiamo una b accanto al valore tra "" crea il file e permette di scrivere in formato binario ad esempio "wb" permette di scrivere in binario, "rb" ecc
"""

with open("26.06/file.csv", "r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")
print(righe)

elementi = []
for elem in righe:
    elementi.append(elem.split(","))
print(elementi)
print(elementi [1][1])

'''
for e in righe:
    print(e.split(",") [0])
'''