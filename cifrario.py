alfabeto = ["a","b","c","d","e","f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v" , "z"]

scelta = input("Scegli l'operazione da effettuare: cripta (c) o decripta (d): ")
chiave = int(input("Inserisci la chiave numerica: "))
stringa = input("Inserisci la stringa: ")

if scelta.lower() == "c":
    stringa_criptata = ""
    for carattere in stringa:
        if carattere in alfabeto:
            indice = alfabeto.index(carattere.lower())
            nuovo_indice = (indice + chiave) % 21 # calcoliamo il nuovo indice a cui corrisponde la lettera cifrata
            stringa_criptata += alfabeto[nuovo_indice]
    else:
        stringa_criptata+=carattere
        print(stringa_criptata)

elif scelta.lower() == "d":
    stringa_criptata = ""
    for carattere in stringa:
        if carattere in alfabeto:
            indice = alfabeto.index(carattere.lower())
            nuovo_indice = (indice - chiave) % 21 # calcoliamo il nuovo indice a cui corrisponde la lettera cifrata
            stringa_criptata += alfabeto[nuovo_indice]
        else:
            stringa_criptata+=carattere
            print(stringa_criptata)
else:
    print("scelta non valida")

        




    
    

