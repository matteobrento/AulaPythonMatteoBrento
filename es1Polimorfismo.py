class MetodoPagamento:

    def effettua_pagamento(self):
        print("Questo metodo non fa nulla!")

class CartaDiCredito(MetodoPagamento):

    def effettua_pagamento(self):
        print("Questo metodo permette di pagare tramite Carta di Credito.")

class BonificoBancario(MetodoPagamento):

    def effettua_pagamento(self):
        counter = 0
        val = int(input("Inserisci una somma di denaro: "))
        counter += val
        print(f"Hai effettuato un bonifico di: {counter} euro")

class PayPal(MetodoPagamento):

    def effettua_pagamento(self):
        pagamento = False
        if pagamento:
            print("Sto pagando con PayPal!")
        else:
            print("Non pago e scappo via")

class GestorePagamenti(MetodoPagamento):

    def pagamento(self, metodo : MetodoPagamento):
        metodo.effettua_pagamento()


while True:
    print("Menu")
    print("Scegli il metodo di pagamento: 1) Carta di Credito, 2) PayPal, 3) Bonifico Bancario ")
    cod = int(input("Scegli un opzione di pagamento: "))
    print("\n")
    if cod == 1:
        carta = CartaDiCredito()
        gestore = GestorePagamenti()
        gestore.pagamento(carta)
    elif cod == 2:
        pay = PayPal()
        gestore = GestorePagamenti()
        gestore.pagamento(pay)
    elif cod == 3:
        bonifico = BonificoBancario()
        gestore = GestorePagamenti()
        gestore.pagamento(bonifico)
    else:
        print("Hai selezionato un'opzione non supportata. ")

    print("\n")
    continua = input("Desideri effettuare un altro pagamento ? ")
    if continua.lower() != "si":
        print("Arrivederci!")
        break






