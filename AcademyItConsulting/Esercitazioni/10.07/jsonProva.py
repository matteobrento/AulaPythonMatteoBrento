import json

def converti_json_dict():

    with open("file.json", "r") as file:
        contenuto = file.read()

    json_stringa = '{"nome":"Matteo", "eta":"23"}'   #elemento simile ad un dict ma quando leggo è una stringa

    dizionario_json = json.loads(json_stringa)
    print(type(dizionario_json))    #conversione stringa in dict, occhio agli apici
    print(dizionario_json["nome"])  #ora funziona come dict


def converti_dict_json():

    dizionario = {"colore":"blu","frutto":"mela"}
    conversione = json.dumps(dizionario)
    print(type(conversione))

    with open("file.json","w") as file:
        file.write(conversione)
    print("File creato!")

converti_dict_json()

