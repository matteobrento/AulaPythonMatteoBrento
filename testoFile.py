stringa = """Il passaggio standard del Lorem Ipsum, utilizzato sin dal sedicesimo secolo
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
La sezione 1.10.32 del "de Finibus Bonorum et Malorum", scritto da Cicerone nel 45 AC
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"""

with open("file1.txt", "w") as file:    #crea il file1.txt e ci scrive dentro la stringa
    file.write(stringa) 

with open("file1.txt", "r") as file:    #legge e salva file1.txt
    stringa = file.read()


with open("file1.txt", "r") as file:    #mi restituisce il numero di righe della stringa nel file1.txt
    lista_righe = file.readlines()


#conto parole
stringa2 = stringa.replace("\n", " ")   #ad una variabile stringa2 associo la stringa rimpiazzando l'andare a capo con uno spazio
lista = stringa2.split(" ")             #alla variabile lista associo la stringa senza "andare a capo" e me la splitta in parole singole
numero_parole = len(lista)              #alla variabile numero_parole associo la lunghezza
print("Il numero di parole è: ", numero_parole) #print


#conto numero righe
numero_righe = len(lista_righe)         #len righe e print
print("Il numero di righe é:" , numero_righe)


#conto caratteri                        #len caratteri e print
print("Il numero di caratteri è: " , len(stringa2))



