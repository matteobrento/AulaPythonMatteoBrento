import random

class Pokemon:

    def __init__(self, nome):
        self.nome = nome
        self.hp = random.randint(50, 100)
        self.livello = random.randint(1, 10)
        self.mosse = []
        self.tipo = ""

    def __str__(self):
        return f"{self.nome} è un Pokémon di tipo: {self.tipo}, con mosse: {self.mosse} e possiede i seguenti punti vita: {self.hp}"

    def scegli_mossa(self):
        if self.mosse:
            mossa_scelta = random.choice(self.mosse)
            print(f"{self.nome} usa {mossa_scelta}!")
            return mossa_scelta
        else:
            return None

    def ricevi_danno(self, danno):
        self.hp -= danno
        if self.hp <= 0:
            print(f"{self.nome} è stato sconfitto!")
            return True
        return False

class Pikachu(Pokemon):

    classe = "Pikachu"

    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Electric"
        self.mosse = ["Tuono Shock", "Attacco Rapido", "Ruggito", "Colpo Coda"]

class Bulbasaur(Pokemon):

    classe = "Bulbasaur"

    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Erba-Veleno"
        self.mosse = ["Azione", "Frustata", "Ruggito"]

class Charmander(Pokemon):

    classe = "Charmander"

    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Fuoco"
        self.mosse = ["Graffio", "Colpo Coda", "Braciere"]

class Squirtle(Pokemon):

    classe = "Squirtle"

    def __init__(self, nome):
        super().__init__(nome)
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
        print("Pokémon nel Pokedex:")
        for pokemon in self.lista_pokemon:
            print(pokemon)

    def mostra_statistiche(self):
        print(f"Statistiche Pokémon: {self.tipo_pokemon}")


def scegli_pokemon_iniziale():
    print("Scegli il tuo Pokémon iniziale:")
    print("1. Pikachu")
    print("2. Bulbasaur")
    print("3. Charmander")
    print("4. Squirtle")
    scelta = input("Inserisci il numero del Pokémon scelto: ")

    if scelta == "1":
        return Pikachu("Pikachu")
    elif scelta == "2":
        return Bulbasaur("Bulbasaur")
    elif scelta == "3":
        return Charmander("Charmander")
    elif scelta == "4":
        return Squirtle("Squirtle")
    else:
        print("Scelta non valida. Riprova.")
        return scegli_pokemon_iniziale()

def trova_pokemon():
    pokemon_selvatico = random.choice([Pikachu("Pikachu Selvatico"), Bulbasaur("Bulbasaur Selvatico"), Charmander("Charmander Selvatico"), Squirtle("Squirtle Selvatico")])
    pokemon_selvatico.livello = random.randint(1, 10)
    pokemon_selvatico.hp = random.randint(50, 100)
    return pokemon_selvatico

def main():
    pokedex = Pokedex()
    pokemon_iniziale = scegli_pokemon_iniziale()
    pokedex.cattura_pokemon(pokemon_iniziale)
    print(f"Hai scelto {pokemon_iniziale.nome} come tuo Pokémon iniziale.")
    
    while True:
        azione = input("Vuoi cercare un Pokémon? (s/n): ").lower()
        if azione == "n":
            break
        
        pokemon_selvatico = trova_pokemon()
        print(f"Hai trovato un {pokemon_selvatico.nome} di livello {pokemon_selvatico.livello} con {pokemon_selvatico.hp} HP.")
        
        combatti = input("Vuoi combattere? (s/n): ").lower()
        if combatti == "s":
            while pokemon_selvatico.hp > 0 and pokemon_iniziale.hp > 0:
                danno = random.randint(10, 30)
                pokemon_sconfitto = pokemon_selvatico.ricevi_danno(danno)
                if pokemon_sconfitto:
                    pokedex.cattura_pokemon(pokemon_selvatico)
                    print(f"Hai catturato {pokemon_selvatico.nome}!")
                    break
                
                danno = random.randint(10, 30)
                pokemon_sconfitto = pokemon_iniziale.ricevi_danno(danno)
                if pokemon_sconfitto:
                    print("Hai perso il combattimento!")
                    break
        else:
            print(f"{pokemon_selvatico.nome} è scappato!")
        
        pokedex.mostra_pokemon()

if __name__ == "__main__":
    main()
