class Automobile:
    
    numero_di_ruote = 4
    def __init__(self, marca, modello): #self, me stesso, dato che una classe può avere migliaia di oggetti, self è obbligatorio perchè definisce quale oggetto sta chiamando quel metodo
        self.marca = marca
        self.modello = modello

    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello) 

auto1 = Automobile("Fiat", "500")   #il self è l'oggetto
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()