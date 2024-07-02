class Dato:

    def __init__(self):

        self.importi = []

    def aggiungi_importi(self):
   
        try:
            valori = input("Inserisci valori separati da spazi: ").split()
            for valore in valori:
                self.importi.append(int(valore))
            print(self.importi)
                
        except ValueError:
            print("Devi inserire solo numeri separati da spazi")
            quit()


    def calcolo_totale_e_media(self):
        
        if self.importi:
            somma = 0
            for importo in self.importi:
                somma = somma + importo
            print(f"La somma è: {somma}")

            for importo in self.importi:
                media = somma/len(self.importi)
            print(f"La media delle vendite è: {media}")
        else:
            print("La lista è vuota, non sono presenti dati di vendita")


    def vendite_sopra_la_media(self):

        listaSopraMedia = []
        if self.importi:
            somma = 0
            for importo in self.importi:
                somma = somma + importo
                media = somma/len(self.importi)
            for numVendite in self.importi:
                if numVendite > media:
                    listaSopraMedia.append(self.importi.index(numVendite))
            print(f"I giorni in cui la media è maggiore del numero di vendite è: {listaSopraMedia}")
        else:
            print("Non si può effettuare una stima perchè non ci sono dati disponibili.")


dato = Dato()
dato.aggiungi_importi()
dato.calcolo_totale_e_media()
dato.vendite_sopra_la_media()