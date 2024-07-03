class ContoBancario:

    def __init__(self):

        self.__titolare = "Matteo"
        self.__saldo = 1000

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def deposita(self):
        
        importo = int(input("Inserisci un importo che vuoi depositare: "))
        if importo > 0:
            ContoBancario.set_saldo = self.__saldo + importo
            print(f"Deposito avvenuto con successo! Il tuo saldo è: {ContoBancario.set_saldo} euro")
        else:
            print("Importo negativo.")

    def preleva(self):

        importo = int(input("Inserisci un importo che vuoi prelevare: "))
        if ContoBancario.set_saldo > 0 and importo > 0:
            ContoBancario.set_saldo = self.__saldo - importo
            print(f"Prelievo avvenuto con successo! Il tuo saldo è: {ContoBancario.set_saldo} euro")
        else:
            print("Importo negativo.")

    def visualizza_saldo(self):

        print(f"Il tuo saldo è: {ContoBancario.set_saldo} euro")


conto = ContoBancario()
conto.deposita()
conto.preleva()