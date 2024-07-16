import random

class Pokemon:

    def __init__(self, nome):
        self.nome = nome
        self.hp = 0
        self.livello = 0
        self.mosse = []
        self.tipo = ""

    def __str__(self):
        return f"{self.nome} è un Pokémon di tipo: {self.tipo}, con mosse: {self.mosse} e possiede i seguenti punti vita: {self.hp}"

class Pikachu(Pokemon):

    classe = "Pikachu"

    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.hp = 0
        self.livello = 0
        self.tipo = tipo="Electric"
        lista_mosse_pikachu = ["Tuono Shock", "Attacco Rapido", "Ruggito", "Colpo Coda"]
        self.mossa = random.choice(lista_mosse_pikachu)


class Bulbasaur(Pokemon):

    classe = "Bulbasaur"

    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.hp = 0
        self.livello = 0
        self.tipo = tipo="Erba-Veleno"
        lista_mosse_bulbasaur = ["Azione", "Frustata", "Ruggito"]
        self.mossa = random.choice(lista_mosse_bulbasaur)


class Charmander(Pokemon):

    classe = "Charmander"

    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.hp = 0
        self.livello = 0
        self.tipo = tipo="Fuoco"
        lista_mosse_charmander = ["Graffio", "Colpo Coda", "Braciere"]
        self.mossa = random.choice(lista_mosse_charmander)


class Squirtle(Pokemon):

    classe = "Squirtle"

    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome
        self.hp = 0
        self.livello = 0
        self.tipo = tipo="Acqua"
        lista_mosse_squirtle = ["Azione", "Colpo Coda", "Pistolacqua"]
        self.mossa = random.choice(lista_mosse_squirtle)


class Pokedex:

    def __init__(self):
        self.lista_pokemon = []

    def aggiungi_pokemon(self, pokemon):
        self.lista_pokemon.append(pokemon)

    def mostra_pokemon(self):
        for pokemon in self.lista_pokemon:
            print(pokemon)

class GestorePokemon:

    def __init__(self):
        self.lista_pokemon = []
        self.tipo_pokemon = {"Pikachu": 0, "Bulbasaur": 0, "Charmander": 0, "Squirtle": 0}

    def cattura_pokemon(self, pokemon):
        self.lista_pokemon.append(pokemon)
        tipo = pokemon.classe
        self.tipo_pokemon[tipo] += 1

    def mostra_pokemon(self):
        print("Pokémon nel gestore:")
        for pokemon in self.lista_pokemon:
            print(pokemon)

    def mostra_statistiche(self):
        print(f"Statistiche Pokémon: {self.tipo_pokemon}")

# Esempio di utilizzo
""" 
pikachu = Pikachu("Pikachu1", 1, 100, ["Fulmine", "Attacco Rapido", "Coda di Ferro"])
bulbasaur = Bulbasaur("Bulbasaur1", 1, 120, ["Frustata", "Raggio Solare"])
charmander = Charmander("Charmander1", 1, 110, ["Lanciafiamme", "Graffio"])
squirtle = Squirtle("Squirtle1", 1, 130, ["Idropompa", "Pistolacqua"])

gestore = GestorePokemon()
gestore.cattura_pokemon(pikachu)
gestore.cattura_pokemon(bulbasaur)
gestore.cattura_pokemon(charmander)
gestore.cattura_pokemon(squirtle)

gestore.mostra_pokemon()
gestore.mostra_statistiche()

pikachu.scegli_mossa()
bulbasaur.scegli_mossa()
charmander.scegli_mossa()
squirtle.scegli_mossa() 
"""