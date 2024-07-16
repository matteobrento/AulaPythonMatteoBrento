class ContoBancario:

    def __init__(self, titolare, saldo):
        self.__titolare=titolare
        self.__saldo=saldo
    
    def deposita(self,importo):
        if importo>0:
            self.__saldo=self.__saldo+importo
        else:
            return f"Importo insufficiente"
        
    def preleva(self,importo):
        if self.__saldo>=importo and importo>0:
            self.__saldo=self.__saldo-importo
        else:
            return f"Saldo insufficiente"
        
    def visualizza_saldo(self):
        print(f"Saldo disponibile: {self.__saldo}")

    def get_titolare(self):
        return self.__titolare
    
    def get_saldo(self):
        return self.__saldo
              


conto=ContoBancario("Cristiano Malgioglio",3000)
conto.deposita(39)  
conto.visualizza_saldo()
conto.preleva(200)
conto.visualizza_saldo()
x=conto.get_saldo()
y=conto.get_titolare()
print(x)
print(y)
    
#TESTING 