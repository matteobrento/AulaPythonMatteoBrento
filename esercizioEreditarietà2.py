class MembroSquadra:

    x = ""

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = int(eta)

    def descrivi(self):
        print(f"Nome: {self.nome}, Eta: {self.eta}")

class Giocatore(MembroSquadra):

    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = int(numero_maglia)

    def descrivi(self):
        super().descrivi()
        print(f"Ruolo: {self.ruolo}, Numero di Maglia: {self.numero_maglia}")

    def gioca_partita(self):
        if self.ruolo == "Portiere":
            print("Esegui Parata")
        elif self.ruolo == "Difensore":
            print("Esegui Scivolata")
        elif self.ruolo == "Centrocampista":
            print("Esegui Cross")
        elif self.ruolo == "Attaccante":
            print("Fai Goal")
        else:
            print("Riserva")



class Allenatore(MembroSquadra):

    global x

    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = int(anni_di_esperienza)

    def descrivi(self):
        super().descrivi()
        print(f"Anni di Esperienza: {self.anni_di_esperienza}")

    def dirige_allenamento(self):
        tipo = int(input("Scegli il tipo di allenamento 1)Corsa 2)Tattica 3)Partita: "))
        if tipo == 1:
            x = "Allenamento d'intensità"
            print(x)
        elif tipo == 2:
            x = "Allenamento su schemi di gioco"
            print(x)
        elif tipo == 3:
            x = "Partita finale 11 vs 11"

    

membro = MembroSquadra("Marco", 18)
membro.descrivi()
print("\n")
giocatore = Giocatore("Matteo", 23, "Difensore", 3)
giocatore.descrivi()
giocatore.gioca_partita()
print("\n")
allenatore = Allenatore("Giulio", 45, 15)
allenatore.descrivi()
allenatore.dirige_allenamento()
print("\n")
    