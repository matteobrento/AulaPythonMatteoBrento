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

#converti_dict_json()

#converti_json_dict()