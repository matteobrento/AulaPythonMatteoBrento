"""
Scrivere un programma Python che crea un documento XML basato su dati forniti. Ad esempio, considera il seguente elenco di studenti:
studenti = [
{'nome': 'Alice', 'eta': '22'},
{'nome': 'Bob', 'eta': '25'},
{'nome': 'Charlie', 'eta': '20'}
]
Il programma dovrebbe creare un documento XML che rappresenti questi studenti.

Infine esportatelo come file.
"""

import xml.etree.ElementTree as ET

studenti = [
{'nome': 'Alice', 'eta': '22'},
{'nome': 'Bob', 'eta': '25'},
{'nome': 'Charlie', 'eta': '20'}
]

root = ET.Element('studenti')   #tag iniziale

for studente in studenti:
    stud = ET.SubElement(root, 'studente')  #creo un sotto-elemento tag studente partendo dalla root col nome studente
    studente_nome = ET.SubElement(stud, 'nome') #sotto-elemento nome di studente
    studente_nome.text = studente['nome']   #mi stampo il text del nome, in questo caso corrisponde alla chiave 'nome' del dict
    studente_eta = ET.SubElement(stud, 'eta')   #sotto-elemento eta di studente
    studente_eta.text = studente['eta'] #mi stampo il text dell'età, in questo caso corrisponde alla chiave 'età' del dict

tree = ET.ElementTree(root) #creo l'albero partendo dalla root

try:
    tree.write("studenti.xml")  #scrivo su file
    print("File scritto correttamente")
except:
    print("Errore! ")
