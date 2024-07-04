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




carta = CartaDiCredito()
gestore = GestorePagamenti()
gestore.pagamento(carta)
