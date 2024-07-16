import json

def converti_json_dict():
    with open("file.json", "r") as file:
        contenuto = file.read()
    dizionario_json = json.loads(contenuto)
    print(dizionario_json["colore"])

def converti_dict_json():
    dizionario = {"colore":"blu","frutto":"mela"}
    json2= json.dumps(dizionario)
    
    with open("file.json","w") as file:
        file.write(json2)
    print("file creato!")


import requests
def request_and_json():
    risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m")
    risposta = requests.request("GET", "https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m")
    risposta_text = risposta.text

    risposta_json = json.loads(risposta_text)

    for element in risposta_json:
        print(element)

def request1():
    risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m")
    risposta_json = risposta.json()
    print(type(risposta_json))

request1()