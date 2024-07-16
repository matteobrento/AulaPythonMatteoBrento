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

    def scegli_mossa(self):
        mossa_scelta = random.choice(self.mosse)
        print(f"{self.nome} usa {mossa_scelta}!")
        return mossa_scelta

    def ricevi_danno(self, danno):
        self.hp -= danno
        print(f"{self.nome} ha subito {danno} danni! Punti vita rimanenti: {self.hp}")
        if self.hp <= 0:
            print(f"{self.nome} è stato sconfitto!")
            return True
        return False

class Pikachu(Pokemon):
    classe = "Pikachu"
    def __init__(self, nome):
        super().__init__(nome)
        self.hp = 100
        self.livello = 5
        self.tipo = "Elettrico"
        self.mosse = ["Tuono Shock", "Attacco Rapido", "Ruggito", "Colpo Coda"]

class Bulbasaur(Pokemon):
    classe = "Bulbasaur"
    def __init__(self, nome):
        super().__init__(nome)
        self.hp = 120
        self.livello = 5
        self.tipo = "Erba-Veleno"
        self.mosse = ["Azione", "Frustata", "Ruggito"]

class Charmander(Pokemon):
    classe = "Charmander"
    def __init__(self, nome):
        super().__init__(nome)
        self.hp = 110
        self.livello = 5
        self.tipo = "Fuoco"
        self.mosse = ["Graffio", "Colpo Coda", "Braciere"]

class Squirtle(Pokemon):
    classe = "Squirtle"
    def __init__(self, nome):
        super().__init__(nome)
        self.hp = 130
        self.livello = 5
        self.tipo = "Acqua"
        self.mosse = ["Azione", "Colpo Coda", "Pistolacqua"]

class Pokedex:
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

class GestorePokemon:
    def __init__(self):
        self.pokedex = Pokedex()
        self.pokemon_catturati = []

    def cattura_pokemon(self, pokemon):
        self.pokedex.cattura_pokemon(pokemon)
        self.pokemon_catturati.append(pokemon)

    def mostra_pokemon(self):
        self.pokedex.mostra_pokemon()

    def combatti(self, mio_pokemon, pokemon_selvatico):
        print(f"Combattimento tra {mio_pokemon.nome} e {pokemon_selvatico.nome} iniziato!")
        while mio_pokemon.hp > 0 and pokemon_selvatico.hp > 0:
            danno_mio_pokemon = random.randint(10, 30)
            danno_pokemon_selvatico = random.randint(10, 30)
            
            print(f"{mio_pokemon.nome} attacca {pokemon_selvatico.nome}")
            sconfitto = pokemon_selvatico.ricevi_danno(danno_mio_pokemon)
            if sconfitto:
                print(f"Hai sconfitto {pokemon_selvatico.nome} e lo hai catturato!")
                self.cattura_pokemon(pokemon_selvatico)
                return True

            print(f"{pokemon_selvatico.nome} attacca {mio_pokemon.nome}")
            mio_pokemon.ricevi_danno(danno_pokemon_selvatico)
            if mio_pokemon.hp <= 0:
                print(f"{mio_pokemon.nome} è stato sconfitto!")
                return False
        return False

def scegli_pokemon_iniziale():
    print("Scegli il tuo Pokémon iniziale:")
    print("1. Pikachu")
    print("2. Bulbasaur")
    print("3. Charmander")
    print("4. Squirtle")
    scelta = int(input("Inserisci il numero del Pokémon scelto: "))
    if scelta == 1:
        return Pikachu("Pikachu")
    elif scelta == 2:
        return Bulbasaur("Bulbasaur")
    elif scelta == 3:
        return Charmander("Charmander")
    elif scelta == 4:
        return Squirtle("Squirtle")
    else:
        print("Scelta non valida.")
        return scegli_pokemon_iniziale()

def trova_pokemon():
    pokemon_possibili = [
        Pikachu("Pikachu Selvatico"),
        Bulbasaur("Bulbasaur Selvatico"),
        Charmander("Charmander Selvatico"),
        Squirtle("Squirtle Selvatico")
    ]
    return random.choice(pokemon_possibili)

def main():
    gestore = GestorePokemon()
    mio_pokemon = scegli_pokemon_iniziale()
    gestore.cattura_pokemon(mio_pokemon)
    print(f"Hai scelto {mio_pokemon.nome} come tuo Pokémon iniziale!")
    gestore.mostra_pokemon()

    while True:
        comando = input("Vuoi cercare un Pokémon? (s/n): ").lower()
        if comando == 's':
            pokemon_selvatico = trova_pokemon()
            pokemon_selvatico.livello = random.randint(1, 5)
            pokemon_selvatico.hp = random.randint(50, 100)
            print(f"Hai trovato un {pokemon_selvatico.nome} di livello {pokemon_selvatico.livello} con {pokemon_selvatico.hp} HP!")
            combatti = input("Vuoi combattere? (s/n): ").lower()
            if combatti == 's':
                successo = gestore.combatti(mio_pokemon, pokemon_selvatico)
                if not successo:
                    print("Il Pokémon è scappato!")
            else:
                print("Hai deciso di non combattere.")
        elif comando == 'n':
            break
        else:
            print("Comando non valido.")
        gestore.mostra_pokemon()

if __name__ == "__main__":
    main()
