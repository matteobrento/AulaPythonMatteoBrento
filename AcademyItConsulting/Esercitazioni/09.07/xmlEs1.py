"""
Scrivere un programma Python che analizza un documento XML e stampa leinformazioni desiderate. 
Ad esempio, considera il seguente documento XML:
<studenti>
<studente>
<nome>Alice</nome>
<eta>22</eta>
</studente>
<studente>
<nome>Bob</nome>
<eta>25</eta>
</studente>
</studenti>
Il programma dovrebbe analizzare il documento XML e stampare i nomi e le età degli studenti.
Infine salvate l'xml su file
"""

import xml.etree.ElementTree as ET

def da_xml_a_stringa():

    contenuto = '''<studenti>
    <studente>
    <nome>Alice</nome>
    <eta>22</eta>
    </studente>
    <studente>
    <nome>Bob</nome>
    <eta>25</eta>
    </studente>
    </studenti>
    '''

    root = ET.fromstring(contenuto)
    return root


root = da_xml_a_stringa()

for studente in root.findall('studente'):
        nome = studente.find('nome').text
        eta = studente.find('eta').text
        print(f'Nome: {nome}, Età: {eta}')


tree = ET.ElementTree(root)
tree.write("es1.xml")
print("File Scritto")

