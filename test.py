"""
Ereditarietà:
L'ereditarietà permette il riutilizzo del codice in modo efficace permettendo ad una o più classi, dette sottoclassi o classi figlie, di ereditare da una classe chiamata Superclasse o Classe Genitore. 
Si parte creando la superclasse e definendo il suo costruttore (__init__) che contiene gli attributi della Superclasse. 
Il costruttore serve a creare l'oggetto, ovvero l'istanza della Classe. Nella classe definiamo attributi e metodi. 
Gli attributi corrispondo alle caratteristiche della classe, mentre i metodi al suo comportamento.
A livello tecnico, si definisce la sottoclasse con tra parentesi tonde () il nome della Superclasse da cui eredita 
e si utilizza il metodo super() per richiamare all'interno della sottoclasse il costruttore della superclasse ereditando in questo modo 
tutti gli attributi della superclasse. Stessa cosa si può fare con i metodi della Superclasse. 
Una funzionalità è la sovrascrittura dei metodi, ovvero si possono ereditare metodi dalla superclasse con la funzionalità di poterli 
sovrascrivere, ovvero modificare in funzione dell'azione che vogliamo svolgere nella sottoclasse, 
che sarà differente da quella della superclasse.
Infine Python supporta anche l'ereditarietà multipla, 
ovvero la possibilità di una classe di ereditare da più classi che andranno passate tra parentesi tonde () nel momento della creazione 
della classe.


Incapsulamento: 
L'incapsulamento è la capacita del codice di nascondere codice, persino a se stesso, come ad esempio una password. 
Permette di nascondere i dettagli di un'implementazione esponendo all'esterno solo ciò che si vuole mostrare. 
Un attributo privato è scritto con due underscore (__) antecedenti il nome dell'attributo e ciò permette all'attributo di essere 
utilizzato solo all'interno della propria classe, ma non all'esterno. Per poter ottenere e modificare il valore di un attributo privato,
principalmente all'esterno, si utilizzano i metodi getter e setter, getter per ottenere il valore e setter per modificarlo. 
Gli attributi Protetti sono indicati da un solo underscore(_) ed è una convenzione che indica che l'attributo dovrebbe poter essere 
utilizzato solo nella classe e nelle sue sottoclassi.


Polimorfismo:
Il polimorfismo è la capacità di cambiare forma ma non comportamento, è un concetto chiave dell'OOP che permette di trattare oggetti 
di classi diverse tramite un'interfaccia comune. 
Si manifesta tramite l'Overriding, ovvero la sovrascrittura dei metodi, che come detto precedentemente, 
permette la funzionalità di poterli sovrascrivere, ovvero modificare in funzione dell'azione che vogliamo svolgere. 
L'overloading non è supportato, ovvero la possibilità di avere più metodi con lo stesso nome ma con differenti parametri. 
Questo in python è gestibile tramite l'utilizzo di argomenti opzionali e variadici.
"""




#esempio di Ereditarietà

class Mezzo:    #superclasse

    def __init__(self, nome, targa):
        self.nome = nome
        self.targa = targa

    def __str__(self):
        return f"Nome: {self.nome}, Targa: {self.targa}"
    

class Moto(Mezzo):  #classe figlia

    def __init__(self, nome, targa, modello):
        super().__init__(nome, targa)
        self.modello = modello

    def __str__(self):
        return super().__str__()+f", Ruolo: {self.modello}"
    
class Auto(Mezzo):  #classe figlia
    
    def __init__(self, nome, targa, cilindrata):
        super().__init__(nome, targa)
        self.cilindrata = cilindrata

    def __str__(self):
        return super().__str__()+f", Ruolo: {self.cilindrata}"




#esempio di Incapsulamento

class ContoBancario:

    def __init__(self):

        self.__titolare = "Matteo"  #attrobuti privati
        self.__saldo = 1000         #attributi privati

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, titolare):
        self.__titolare = titolare

    def deposita(self):
        
        importo = int(input("Inserisci un importo che vuoi depositare: "))  #qui è stato gestito coi metodi get e set ma si potevano usare direttamente gli attributi perchè fanno parte della classe.
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



#esempio di Polimorfismo

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

    def pagamento(self, metodo : MetodoPagamento):  #questo metodo dimostra come il polimorfismo ci permette di utilizzare "effettua_pagamento"  
        metodo.effettua_pagamento()                 #indipendentemente da tipo di metodo che scegliamo