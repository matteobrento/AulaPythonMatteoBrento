import modulo1 as mod1

df = mod1.crea_dataframe()   #creo il df iniziale

while True:

    menu = mod1.menu_pandas()
    opzione = int(input("\nScegli l'operazione che desideri effettuare: ")) #scelta opzione
    if opzione == 1:
        mod1.totale_vendite(df)
    elif opzione == 2:
        mod1.totale_vendite_per_prodotto(df)
    elif opzione == 3:
        mod1.prodotto_piu_venduto(df)
    elif opzione == 4: 
        mod1.citta_piu_vendite(df)
    elif opzione == 5:
        mod1.filtro_vendite(df)
    elif opzione == 6:
        mod1.ordinamento_decrescente(df)
    elif opzione == 7:
        mod1.visualizza_numero_vendite_per_citta(df)
    else:
        print("Scelta non disponibile")

    continua = input("Vuoi effettuare un'altra operazione? ")   #ripetibilità
    if continua.lower() != "si":
        print("\nArrivederci")
        break