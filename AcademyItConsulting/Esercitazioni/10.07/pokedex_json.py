"""
Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in
caso non fosse presente vi permetterà di catturarlo salvando il numero
identificativo, nome, abilità, xp(punti esperienza),peso
e altezza.
(Sul sistema API sono presenti poco più di 1000 pokemon)
"""

import requests
import json
import random
import os

def cerca_pokemon():
    numero = random.randint(1,1002)
    pokedex = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}").text
    dizionario_pokedex=json.loads(pokedex)

    nome = dizionario_pokedex["forms"][0]["name"]
    id = numero
    abilita = []
    for dato in dizionario_pokedex["abilities"]:
        nome_abilità=dato["ability"]["name"]
        abilita.append(nome_abilità)

    exp = dizionario_pokedex["base_experience"]
    altezza = dizionario_pokedex["height"]
    peso = float(dizionario_pokedex["weight"])

    return {
            "id": id,
            "nome": nome,
            "abilita": abilita,
            "exp": exp,
            "altezza": altezza,
            "peso": peso
        }

def carica_pokedex():
    
    if os.path.exists("pokedex.json"):
        with open("pokedex.json", "r") as file:
            leggi = file.read()
            return json.loads(leggi)
    else:
        return {}

def salva_pokedex(pokedex):
    salva = json.dumps(pokedex) #scrivere prima dell'apertura del file
    with open("pokedex.json", "w") as file:
        file.write(salva)
    
def aggiungi_pokemon():

    pokedex = carica_pokedex()
    pokemon = cerca_pokemon()
    
    if str(pokemon["id"]) not in pokedex:
        pokedex[str(pokemon["id"])] = pokemon
        print(f"Hai catturato: ID: {pokemon['id']} Nome: {pokemon['nome']} e lo hai aggiunto al Pokedex!")
        print("Pokedex aggiornato: ")
        for chiave,valore in pokedex.items():
            print(f"ID: {valore['id']}, Nome: {valore['nome']}, Abilità: {valore['abilita']}, Exp: {valore['exp']}, Altezza: {valore['altezza']}, Peso: {valore['peso']}")
        
        salva_pokedex(pokedex)
    else:
        print(f"Pokémon ID: {pokemon['id']} Nome: {pokemon['nome']} è già nel Pokedex.")


controllo = True
print("Benvenuto in Pokemon! \n")
while controllo:

    print("Cerca Pokemon... ")
    aggiungi_pokemon()
    print("\n")
    controllo = True
    
    continua = input("Desideri cercare un altro Pokemon ? ")
    if continua.lower() != "si":
        print("Arrivederci")
        controllo = False











""" if pokedex=={}:
    json2= json.dumps(pokedex)

    with open("pokedex.json","w") as file:
        file.write(json2)
        print("file creato!")

else:
    json2= json.dumps(pokedex)

    with open("pokedex.json","a") as file:
        file.write(json2)
        print("pokemon aggiunto") """
