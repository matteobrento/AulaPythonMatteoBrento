#super() è un metodo che  si scrive nelle classi figlie per richiamare pezzi della classe padre
#sovrascrittura dei metodi (overriding): serve a far comportare una classe figlia in modo diverso dalla classe padre, aggiorno il comportamento
#ereditarietà multipla: una classe figlia che ha pià classe padri, avviene principalmente solo in python

#esempio basic
class Veicolo:

    def __init__(self, marca, modello): 
        self.marca = marca
        self.modello = modello

    def mostra(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}")


class Auto(Veicolo):
    def __init__(self, marca, modello, tipo_carburante):
        super().__init__(marca, modello)    #prende il costruttore della classe da cui eredita
        self.tipo_carburante = tipo_carburante

    def mostra(self):
        self.mostra()
        print(f"Tipo Carburante: {self.tipo_carburante}")



