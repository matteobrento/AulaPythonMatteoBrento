class MetodoPagamento:

    def __init__(self, nome, numero_carta, data_scadenza, cvc):
        self.__nome = nome
        self.__numero_carta = numero_carta
        self.__data_scadenza = data_scadenza
        self.__cvc = int(cvc)

    def metodo_pagamento(self):
        print("Metodo di pagamento generico")


class CartaDiCredito(MetodoPagamento):

    classe = "CartaDiCredito"

    def __init__(self, nome, numero_carta, data_scadenza, cvc, saldo=1000):
        super().__init__(nome, numero_carta, data_scadenza, cvc)
        self.__saldo = saldo

    def metodo_pagamento(self):
        
        nome1 = input("Inserisci il nome del titolare della carta: ")
        numero_carta1 = input("Inserisci il numero di carta: ")
        data1 = input("Inserisci la data di scadenza: ")
        cvc1 = int(input("Inserisci il cvc della carta: "))
        if self._MetodoPagamento__nome == nome1 and self._MetodoPagamento__numero_carta == numero_carta1 and self._MetodoPagamento__data_scadenza == data1 and self._MetodoPagamento__cvc == cvc1:
            print("La carta corrisponde ai dati inseriti, perciò puoi effettuare il pagamento! \n")

            importo = int(input("Inserisci l'importo da pagare tramite Carta di Credito: "))
            if importo > self.__saldo:
                print("Pagamento rifiutato! Non ci sono abbastanza soldi. ")
            else:
                print("Pagamento effettuato!")
                self.__saldo -= importo
            print(f"Il saldo attuale è: {self.__saldo}")

        else:
            print("I dati non corrispondono, non puoi utilizzare questa carta! ")


class PayPal(MetodoPagamento):

    classe = "PayPal"

    def __init__(self, nome, numero_carta, data_scadenza, cvc, username, password, saldo = 1000):
        super().__init__(nome, numero_carta, data_scadenza, cvc)
        self.__user = username
        self.__password = password
        self.__saldo = saldo

    def metodo_pagamento(self):

        user = input("Inserisci un username: ")
        psw = input("Inserisci una password: ")
        if user == self.__user and psw == self.__password:
            print("I tuoi dati sono corretti, Benvenuto nel tuo account PayPal \n")

            nome2 = input("Inserisci il nome del titolare della carta: ")
            numero_carta2 = input("Inserisci il numero di carta: ")
            data2 = input("Inserisci la data di scadenza: ")
            cvc2 = int(input("Inserisci il cvc della carta: "))
            if self._MetodoPagamento__nome == nome2 and self._MetodoPagamento__numero_carta == numero_carta2 and self._MetodoPagamento__data_scadenza == data2 and self._MetodoPagamento__cvc == cvc2:
                print("La carta corrisponde ai dati registrati nel tuo account PayPal, perciò puoi effettuare il pagamento! ")
            
                importo = int(input("Inserisci l'importo da pagare tramite PayPal: "))
                if importo > self.__saldo:
                    print("Pagamento rifiutato! Non ci sono abbastanza soldi. ")
                else:
                    print("Pagamento effettuato!")
                    self.__saldo -= importo
                    print(f"Il saldo attuale è: {self.__saldo}")

            else:
                print("I dati non corrispondono, non puoi utilizzare questa carta! ")
        else:
            print("Login Fallito! I tuoi dati sono errati! ")


class BonificoBancario(MetodoPagamento):

    classe = "BonificoBancario"

    def __init__(self, nome, iban, saldo = 1000):
        super().__init__(nome, None, None, None)
        self.__iban = iban 
        self.__saldo = saldo

    def metodo_pagamento(self):

        iban1 = "1234-5678-9000-0000"
        if self.__iban == iban1:
            print("Il Conto Bancario è presente nel database. Puoi effettuare un bonifico. ")

            counter = 0
            val = int(input("Inserisci la somma di denaro per effettuare il bonifico: "))

            if val < self.__saldo:
                counter += val
                self.__saldo -= counter
                print(f"Hai effettuato un bonifico di: {counter} euro e il tuo saldo attuale è: {self.__saldo} euro")
            else:
                print("Stai cercando di inviare una somma maggiore al tuo saldo. Errore!")
        else:
            print("Il Conto Bancario non è presente nel database")


class GestorePagamenti(MetodoPagamento):

    def __init__(self):
        
        self.listaPagamentiUsati = []
        self.tipoPagamento = {"CartaDiCredito":0, "PayPal":0, "BonificoBancario":0}

    def registraPagamento(self, pagamento):
        self.listaPagamentiUsati.append(pagamento)
        tipo = pagamento.classe
        self.tipoPagamento[tipo] += 1

    def mostraElencoMetodi(self):
        print(f"Il numero di metodi di pagamento utilizzati è: {self.tipoPagamento}")


    def pagamento(self, metodo : MetodoPagamento):
        metodo.metodo_pagamento()


while True:
    print("Menu")
    print("\nScegli il metodo di pagamento:")
    print("1. Carta di Credito")
    print("2. Account PayPal")
    print("3. Bonifico Bancario")
    print("4. Mostra Pagamenti effettuati \n")

    scelta = int(input("Scegli l'opzione che vuoi eseguire: "))
    if scelta == 1:
        carta = CartaDiCredito("Matteo", "1234", "12-24", 659)
        gestore = GestorePagamenti()
        gestore.registraPagamento(carta)
        gestore.pagamento(carta)
    elif scelta == 2:
        paypal = PayPal("Matteo", "1234", "12-24", 659, "matteobrento", "12345")
        gestore = GestorePagamenti()
        gestore.registraPagamento(paypal)
        gestore.pagamento(paypal)
    elif scelta == 3:
        bonifico = PayPal("Matteo", "1234-5678-9000-0000")
        gestore = GestorePagamenti()
        gestore.registraPagamento(bonifico)
        gestore.pagamento(bonifico)
    elif scelta == 4:
        gestore.mostraElencoMetodi()
    else:
        print("Il metodo di pagamento scelto non è valido. ")
        quit()

    print("\n")
    continua = input("Vuoi effettuare un'altra operazione ?")
    if continua.lower() != "si":
        print("Arrivederci!")
        break


    

        

