class UnitaMilitare:

    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = int(numero_soldati)

    def muovi(self):
        print(f"L'unità {self.nome} con {self.numero_soldati} unità effettua un movimento!")

    def attacco(self):
        print(f"L'unità {self.nome} con {self.numero_soldati} unità esegue un attacco!")
    
    def ritira(self):
        print(f"L'unità {self.nome} con {self.numero_soldati} unità effettua una ritirata!")


class Fanteria(UnitaMilitare):

    classe = "Fanteria"

    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        #self.listaFanteria = []

    def muovi(self):
        return super().muovi()

    def costruisci_trincea(self):
        difesa = 0
        trincea = int(input("Inserisci il numero di trincee che vuoi costruire: "))
        for t in range(0,trincea):
            difesa +=1
        print(f"La difesa è incrementata a: {difesa} poichè hai costruito {trincea} trincee!" )

    """ def aggiungi_fanteria(self):

        self.listaFanteria.append(Fanteria)
        print(f"Numero di unità Fanteria: {len(self.listaFanteria)}") """


class Artiglieria(UnitaMilitare):

    classe = "Artiglieria"

    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        #self.listaArtiglieria = []

    def muovi(self):
        return super().muovi()
    
    def calibra_artiglieria(self):
        precisione = 0
        pezzi = int(input("Inserisci il numero di pezzi da cui è composta la tua artiglieria: "))
        for p in range(0, pezzi):
            precisione += 1
        print(f"Hai aggiunto {pezzi} pezzi e la tua precisione è incrementata a: {precisione/2}")

    """ def aggiungi_artiglieria(self):

        self.listaArtiglieria.append(Artiglieria)
        print(f"Numero di unità Artiglieria: {len(self.listaArtiglieria)}") """


class Cavalleria(UnitaMilitare):

    classe = "Cavalleria"

    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()
    
    def esplora_terreno(self):
        terreno = int(input("Inserisci il numero di Km che vuoi esplorare: "))
        if terreno%2 == 0:
            print("Sei nel territorio amico!")
        else:
            print("Sei nel territorio nemico!")


class SupportoLogistico(UnitaMilitare):

    classe = "SupportoLogistico"

    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()

    def rifornisci_unita(self):

        numero_alimenti = 0
        alimenti = int(input("Inserisci il numero di alimenti che vuoi rifornire: "))
        for a in range(0, alimenti):
            numero_alimenti += 1

        print(f"Hai aggiunto {numero_alimenti} alimenti alle tue unità! ")


class Ricognizione(UnitaMilitare):

    classe = "Ricognizione"

    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def muovi(self):
        return super().muovi()
    
    def conduci_ricognizione():
        print("Effettua una ricognizione")


class ControlloMilitare(UnitaMilitare):

    def __init__(self):
        
        self.unita_registrate = []
        self.tipo_unita = {"Fanteria":0, "Artiglieria":0, "Cavalleria":0, "SupportoLogistico":0, "Ricognizione":0}

    def registraUnità(self,unita):
        self.unita_registrate.append(unita)
        tipo = unita.classe
        self.tipo_unita[tipo] += 1

    def mostra_unita(self):
        print(f"Il numero di unità aggiornate è: {self.tipo_unita}")

    def dettagli(self,nome):
        
        for unita in self.unita_registrate:
            if unita.nome == nome:
                print(f"Nome: {unita.nome}")
                print(f"Numero Soldati: {unita.numero_soldati}")


""" unita = UnitaMilitare("Unita1", 50)
unita.muovi()
print("\n") """

fanteria = Fanteria("Fanteria", 100)
fanteria.muovi()
fanteria.costruisci_trincea()
controllo = ControlloMilitare()
controllo.registraUnità(fanteria)
controllo.mostra_unita()
print("\n")

artiglieria = Artiglieria("Artiglieria", 80)
artiglieria.muovi()
artiglieria.calibra_artiglieria()
controllo.registraUnità(artiglieria)
controllo.mostra_unita()
print("\n")

cavalleria1 = Cavalleria("Cavalleria1", 30)
cavalleria1.esplora_terreno()
controllo.registraUnità(cavalleria1)
controllo.mostra_unita()
print("\n")
cavalleria2 = Cavalleria("Cavalleria2", 50)
cavalleria2.esplora_terreno()
controllo.registraUnità(cavalleria2)
controllo.mostra_unita()
print("\n")

supporto = SupportoLogistico("Supporto", 20)
supporto.rifornisci_unita()
controllo.registraUnità(supporto)
controllo.mostra_unita()
print("\n")

controllo.dettagli("Fanteria")
controllo.dettagli("Artiglieria")
controllo.dettagli("Cavalleria2")
controllo.dettagli("Supporto")







