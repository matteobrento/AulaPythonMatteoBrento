class ContoBancario:

    def __init__(self):

        self.__titolare = "Matteo"
        self.__saldo = 1000

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, titolare):
        self.__titolare = titolare

    def deposita(self):
        
        importo = int(input("Inserisci un importo che vuoi depositare: "))
        if importo > 0:
            ContoBancario.set_saldo = self.__saldo + importo
            saldo_corrente = ContoBancario.set_saldo
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

while True:

    print("Menu: ")
    print("1) Deposita")
    print("2) Preleva")
    print("3) Visualizza Saldo")
    print("4) Visualizza Titolare")
    print("5) Modifica Titolare\n")
    cod = int(input("Inserisci l'opzione che vuoi effettuare: "))
    if cod == 1:
        conto = ContoBancario()
        conto.deposita()
    elif cod == 2:
        conto = ContoBancario()
        conto.preleva()
    elif cod == 3:
        conto = ContoBancario()
        conto.visualizza_saldo()
    elif cod == 4:
        conto = ContoBancario()
        print(f"Il titolare è: {conto.get_titolare()}")
    elif cod == 5:
        conto = ContoBancario()
        conto.set_titolare("Luca")
        print(f"Ora invece il titolare è: {conto.get_titolare()}")
    else:
        quit()

    continua = input("Vuoi effettuare un'altra operazione ? ")
    if continua != "si":
        break



""" conto = ContoBancario()
conto.deposita()
print("\n")
print(f"Il titolare è: {conto.get_titolare()}")
conto.set_titolare("Luca")
print(f"Ora invece il titolare è: {conto.get_titolare()}") """


