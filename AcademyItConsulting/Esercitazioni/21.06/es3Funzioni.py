lista = []  #lista vuota in cui caricare i risultati

def area_triangolo(base, altezza):  #funzione area triangolo base*altezza
    areaTriangolo = base * altezza
    return areaTriangolo

def area_quadrato(lato):    #funzione area quadrato l*l
    areaQuadrato = lato * lato
    return areaQuadrato

def area_rettangolo(baser, altezzar):   #funzione area rettangolo b*h
    areaRettangolo = baser * altezzar
    return areaRettangolo

base = int(input("Inserisci la base del triangolo: "))     #inserimento degli input e appoggio in una variabile di area calcolata
altezza = int(input("Inserisci l'altezza del triangolo: "))#per tutte e 3 le forme geometriche
area_triangolo_calcolata = area_triangolo(base, altezza)
print("L'area del triangolo è: ", area_triangolo_calcolata)

lato = int(input("Inserisci il lato del quadrato: "))
area_quadrato_calcolata = area_quadrato(lato)
print("L'area del quadrato è: ", area_quadrato_calcolata)

baser = int(input("Inserisci la base del rettangolo: "))
altezzar = int(input("Inserisci l'altezza del rettangolo: "))
area_rettangolo_calcolata = area_rettangolo(baser, altezzar)
print("L'area del rettangolo è: ", area_rettangolo_calcolata)

def inserisci_in_lista(area_triangolo, area_quadrato, area_rettangolo): #funzione di inserimento in lista
    lista.append(area_triangolo)
    lista.append(area_quadrato)
    lista.append(area_rettangolo)
    print(lista)

inserisci_in_lista(area_triangolo_calcolata, area_quadrato_calcolata, area_rettangolo_calcolata)    #lancio della funzione di inserimento dei risultati

    




