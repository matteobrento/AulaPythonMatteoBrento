"""
Scrivere un programma Python che ricerca e stampa gli elementi di un documento XML chesoddisfano determinati criteri. 
Considera il seguente documento XML:
<prodotti>
<prodotto>
<nome>Laptop</nome>
<prezzo>800</prezzo>
</prodotto>
<prodotto>
<nome>Smartphone</nome>
<prezzo>500</prezzo>
</prodotto>
<prodotto>
<nome>Tablet</nome>
<prezzo>300</prezzo>
</prodotto>
</prodotti>
Il programma dovrebbe cercare e stampare tutti i prodotti con un prezzo inferiore a 600.
"""


import xml.etree.ElementTree as ET

def da_xml_a_stringa():

    contenuto = '''<prodotti>
    <prodotto>
    <nome>Laptop</nome>
    <prezzo>800</prezzo>
    </prodotto>
    <prodotto>
    <nome>Smartphone</nome>
    <prezzo>500</prezzo>
    </prodotto>
    <prodotto>
    <nome>Tablet</nome>
    <prezzo>300</prezzo>
    </prodotto>
    </prodotti>
    '''

    root = ET.fromstring(contenuto)
    return root

root = da_xml_a_stringa()

for prodotto in root.findall('prodotto'):   #tag da cercare
    prezzo = int(prodotto.find('prezzo').text)
    if prezzo < 600:
        nome = prodotto.find('nome').text
        print(f"Nome del Prodotto: {nome}, Prezzo: {prezzo}")
    else:
        nome = prodotto.find('nome').text
        print(f"Il prezzo di {nome} è maggiore di 600!")