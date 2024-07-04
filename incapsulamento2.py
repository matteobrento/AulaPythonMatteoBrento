class Posto:

    def __init__(self, numero, fila, occupato=False):
        self.__numero = int(numero)
        self.__fila = fila
        self.__occupato = occupato

    def prenota(self):
        if self.__occupato:
            print("Il posto è già occupato!")
        else:
            self.__occupato = True
            print("Posto prenotato!")

    def libera(self):
        if not self.__occupato:
            print("Il posto è già libero!")
        else:
            self.__occupato = False
            print("Posto liberato!")

    def get_numero(self):
        return self.__numero
    
    def get_fila(self):
        return self.__fila
    
    def get_stato(self):
        return self.__occupato


class PostoVIP(Posto):

    def __init__(self, numero, fila, servizi_extra, occupato=False):
        super().__init__(numero, fila, occupato)
        self.__servizi_extra = servizi_extra
    
    def prenota(self):
        if self.__occupato:
            print("Il posto è già occupato!")
        else:
            self.__occupato = True
            print("Posto VIP prenotato!")
            print(f"Servizi extra inclusi: {self.__servizi_extra}")
            while True:
                vip = int(input("Desideri ordinare qualcosa da bere (1) o da mangiare (2)? (0 per terminare): "))
                if vip == 1:
                    print("Hai ordinato un kit di spumanti!")
                elif vip == 2:
                    print("Hai ordinato una cena privata!")
                elif vip == 0:
                    print("Goditi lo spettacolo!")
                    break
                else:
                    print("Scelta non valida, riprova.")


class PostoStandard(Posto):

    def __init__(self, numero, fila, costo_aggiuntivo, occupato=False):
        super().__init__(numero, fila, occupato)
        self.__costo_aggiuntivo = costo_aggiuntivo

    def prenota(self):
        if self.__occupato:
            print("Il posto è già occupato!")
        else:
            self.__occupato = True
            print(f"Posto standard prenotato! Costo aggiuntivo: {self.__costo_aggiuntivo} euro")


class Teatro(Posto):

    def __init__(self):
        self.__numero_posti = []

    def aggiungi_posto(self, posto):
        self.__numero_posti.append(posto)

    def prenota_posto(self, numero, fila):
        for posto in self.__numero_posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
            else:
                print("Posto non trovato! ")

    def stampa_posti(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.get_stato():
                print(f"Fila {posto.get_fila()}, Numero {posto.get_numero()}")



teatro = Teatro()
teatro.aggiungi_posto(Posto(1, 'A'))
teatro.aggiungi_posto(PostoVIP(2, 'A', 'Accesso al lounge'))
teatro.aggiungi_posto(PostoStandard(3, 'B', 5))

teatro.prenota_posto(1, 'A')
teatro.prenota_posto(2, 'A')
teatro.prenota_posto(3, 'B')

teatro.stampa_posti()



    

    