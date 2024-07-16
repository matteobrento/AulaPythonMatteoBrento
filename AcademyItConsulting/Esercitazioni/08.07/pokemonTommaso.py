from random import randint, choice

class Pokemon:
    def __init__(self, nome,livello):
        self.nome = nome
        self.livello = livello
        self.mosse = {}
        self.punti_vita = 0
        self.tipo = ""
    def __str__(self):
        return f"Nome: {self.nome}, Mosse: {self.mosse}, Punti vita: {self.punti_vita}, Tipo: {self.tipo}, Livello: {self.livello}"


class Bulbasaur(Pokemon):
    def __init__(self, nome, livello):
        super().__init__(nome, livello)
        coefficiente=livello*0.5
        self.mosse = {"Foglielama":30*coefficiente,"Frustata":50*coefficiente,"Parassiseme":20*coefficiente}
        self.punti_vita =  45*coefficiente
        self.tipo = "Erba/Veleno"
    
    def cambia_livello(self, livello):
        self.livello = livello
        coefficiente=livello*0.5
        self.mosse = {"Foglielama":30*coefficiente,"Frustata":50*coefficiente,"Parassiseme":20*coefficiente}
        self.punti_vita =  45*coefficiente


class Charmender(Pokemon):
    def __init__(self, nome,livello):
        super().__init__(nome, livello)
        coefficiente=livello*0.5
        self.mosse = {"Braciere":50*coefficiente,"Lanciafiamme":40*coefficiente,"Ruggito":10*coefficiente}
        self.punti_vita = 50 *coefficiente
        self.tipo = "Fuoco"
    
    def cambia_livello(self, livello):
        self.livello = livello
        coefficiente=livello*0.5
        self.mosse = {"Foglielama":30*coefficiente,"Frustata":50*coefficiente,"Parassiseme":20*coefficiente}
        self.punti_vita =  45*coefficiente


class Squirtle(Pokemon):
    def __init__(self, nome,livello):
        super().__init__(nome, livello)
        coefficiente=livello*0.5
        self.mosse = {"Pistola_acqua":10*coefficiente,"Idropompa":20*coefficiente,"Colpo_coda":20*coefficiente}
        self.punti_vita = 55 *coefficiente
        self.tipo = "Acqua"
    
    def cambia_livello(self, livello):
        self.livello = livello
        coefficiente=livello*0.5
        self.mosse = {"Foglielama":30*coefficiente,"Frustata":50*coefficiente,"Parassiseme":20*coefficiente}
        self.punti_vita =  45*coefficiente

class Pikachu(Pokemon):
    def __init__(self, nome,livello):
        super().__init__(nome, livello)
        coefficiente=livello*0.5
        self.mosse = {"Fulmine":50*coefficiente,"Tuono":50*coefficiente,"Elettro_palla":50*coefficiente}
        self.punti_vita = 70 *coefficiente
        self.tipo = "Elettro"
    
    def cambia_livello(self, livello):
        self.livello = livello
        coefficiente=livello*0.5
        self.mosse = {"Foglielama":30*coefficiente,"Frustata":50*coefficiente,"Parassiseme":20*coefficiente}
        self.punti_vita =  45*coefficiente


tipi_pokemon= {"1":Bulbasaur, "2":Charmender, "3":Squirtle, "4":Pikachu}

class Pokedex:
    
    def __init__(self,nome):
        self.nome = nome
        self.dizionario = {}

    def aggiungi_pokemon(self, pokemon):
        self.dizionario[pokemon.nome] = pokemon
    
    def visualizza_pokemon(self):
        for chiave, pokemon in self.dizionario.items():
            print(pokemon)
    
    def scelta_primo_pokemon(self):
        while True:
            scelta_pokemon = input("Inserisci:\n1 per Bulbasaur\n2 per Charmender\n3 per Squirtle\n4 per Pikachu\n: ")
            if scelta_pokemon in tipi_pokemon:
                nome = input("Inserisci il nome del tuo pokemon: ")
                pokemon = tipi_pokemon[scelta_pokemon](nome, 1)
                self.aggiungi_pokemon(pokemon)
                self.visualizza_pokemon()
                break
            else:
                print("Scelta non valida!")

    def restituisci_livello_nuovo(self):
        pokemon = list(self.dizionario.values())
        somma_livelli = 0
        for elemento in pokemon:
            somma_livelli += elemento.livello

        media_livello = somma_livelli//len(pokemon)
        if media_livello  <=3:
            differenza = 0
        else:
            differenza = randint(-2,2)
        
        return media_livello+differenza
    
    def trova_pokemon(self):
        nuovo_pokemon = choice(list(tipi_pokemon.values()))
        livello = self.restituisci_livello_nuovo()
        nuovo_pokemon = nuovo_pokemon("selvatico", livello)
        return nuovo_pokemon
    
    def lotta(self, pokemon_avversario):
        self.visualizza_pokemon()
        scegli_pokemon = input("Inserisci il nome del pokemon che vuoi usare: ")
        while True:
            if scegli_pokemon in self.dizionario:
                pokemon_mio = self.dizionario[scegli_pokemon]
                break
            else:
                print("pokemon non presente")
            
        
        mosse_sue = list(pokemon_avversario.mosse.keys())
        print(f"Le tue mosse sono: {pokemon_mio.mosse}")
        inizio = randint(0,1)
        if inizio == 1:
            noi = True
        else:
            noi = False
        punti_vita_miei = pokemon_mio.punti_vita
        punti_vita_avversario = pokemon_avversario.punti_vita
        while punti_vita_miei > 0 and punti_vita_avversario > 0:
            if noi:
                mossa = input("Scegli una mossa: ")
                if mossa in pokemon_mio.mosse:
                    punti_vita_miei -= pokemon_mio.mosse[mossa]
                else:
                    print("mossa non valida!")
                if punti_vita_avversario < 1:
                    break
                mossa_avversario = choice(mosse_sue)
                punti_vita_avversario -= pokemon_avversario.mosse[mossa_avversario]
            
            else:
                mossa_avversario = choice(mosse_sue)
                punti_vita_miei -= pokemon_avversario.mosse[mossa_avversario]
                if punti_vita_miei < 1:
                    break
                mossa = input("Scegli una mossa: ")
                if mossa in pokemon_mio.mosse:
                    punti_vita_avversario -= pokemon_mio.mosse[mossa]
                else:
                    print("mossa non valida!")
            

            print(f"Punti vita mio pokemon: {pokemon_mio.punti_vita}, Punti vita avversario: {pokemon_avversario.punti_vita}")
        
        if punti_vita_avversario <= 0:
            cattura = input("Vuoi catturare il pokemon: ")
            if cattura.lower() == "si":
                nome = input("Inserisci il nome del nuovo pokemon: ")
                pokemon_avversario.nome = nome
                self.aggiungi_pokemon(pokemon_avversario)
                print(f"Hai catturato il pokemon: {pokemon_avversario}")

                pokemon_mio.cambia_livello(pokemon_mio.livello+1)
                self.visualizza_pokemon()
        else:
            print("Hai perso il combattimento!")

                        
mio_pokedex = Pokedex("mio")

mio_pokedex.scelta_primo_pokemon()

pokemon_trovato = mio_pokedex.trova_pokemon()

print(pokemon_trovato)

combattimento = input("Vuoi combattere: ")

if combattimento.lower() == "si":
    mio_pokedex.lotta(pokemon_trovato)





            


