class MembroSquadra:    #classe genitore

    x = ""

    def __init__(self, nome, eta):  #creazione del costruttore 
        self.nome = nome
        self.eta = int(eta)

    def descrivi(self): #metodo che stampa gli attributi a video
        print(f"Nome: {self.nome}, Eta: {self.eta}")

class Giocatore(MembroSquadra): #classe figlio che eredita da MembroSquadra

    def __init__(self, nome, eta, ruolo, numero_maglia):    #definisce il costruttore erenditando da quello del genitore
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = int(numero_maglia)

    def descrivi(self): #descrizione
        super().descrivi()
        print(f"Ruolo: {self.ruolo}, Numero di Maglia: {self.numero_maglia}")

    def gioca_partita(self):    #metodo che in base al ruolo del giocatore inserito effettua un azione associata al ruolo
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


class Allenatore(MembroSquadra):    #classe figlio che eredita da MembroSquadra

    global x

    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = int(anni_di_esperienza)

    def descrivi(self):
        super().descrivi()
        print(f"Anni di Esperienza: {self.anni_di_esperienza}")

    def dirige_allenamento(self):   #chiede il tipo di allenamento in input e aggiorna una variabile globale importata con l'esito
        tipo = int(input("Scegli il tipo di allenamento 1)Corsa 2)Tattica 3)Partita: "))
        if tipo == 1:
            x = "Allenamento d'intensità"
            print(x)
        elif tipo == 2:
            x = "Allenamento su schemi di gioco"
            print(x)
        elif tipo == 3:
            x = "Partita finale 11 vs 11"
            print(x)
        else:
            x = "Allenamento non programmato"
            print(x)



class Assistente(MembroSquadra):    #classe figlio che eredita da MembroSquadra

    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def descrivi(self):
        super().descrivi()
        print(f"Specializzazione: {self.specializzazione}")

    def supporta_team(self):    #metodo dove in base alla specializzazione dell'assistente si effetua un supporto specifico
        if self.specializzazione == "Medico":
            print("Fornisce supporto tramite assistenza medica ai giocatori")
        elif self.specializzazione == "Fisioterapista":
            print("Fornisce supporto per il recupero fisico dei giocatori")
        elif self.specializzazione == "Analista":
            print("Fornisce supporto analizzando le partite e le prestazioni dei giocatori")
        else:
            print("Tipologia di assistente non disponibile")
    
#test delle classi e dei metodi

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
assistente = Assistente("Luca", 38, "Analista")
assistente1 = Assistente("Barbara", 28, "Fisioterapista")
assistente.descrivi()
assistente.supporta_team()
print("\n")
assistente1.descrivi()
assistente1.supporta_team()
    