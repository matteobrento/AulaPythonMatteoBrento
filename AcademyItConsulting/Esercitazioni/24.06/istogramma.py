"""
Scrivete un programma che richiede una lista di numeri all’utente e fornisce in output un istogramma basato su questi numeri, 
usando asterischi per disegnarlo. Data ad esempio la lista [3, 7, 9, 5], il programma dovrà produrre questa sequenza:
***
*******
*********
*****
"""
controllo = True
while controllo:

    lista = input("Inserisci una lista di numeri: ")
    listaSplittata = lista.split(" ")
    print(lista.split(" "))

    lista2 = [] 

    for n in listaSplittata:
        lista2.append(int(n))

    print(lista2)

    for num in lista2:
        print("*" * num)

    continua = input("Vuoi creare un altro istogramma ? ")
    if(continua == "si"):
        controllo = True
    
    else:
        print("Arrivederci")
        controllo = False

