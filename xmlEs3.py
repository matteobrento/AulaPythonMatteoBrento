"""
Scrivere un programma Python che modifica un documento XML esistente.Considera il seguente documento XML:
<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>
Il programma dovrebbe aggiungere un nuovo libro al documento XML e stampare il documento risultante.
"""

import xml.etree.ElementTree as ET

def xml_to_file():  #output dal file
    tree = ET.parse("example.xml") #parse salva il file xml in una variabile
    root = tree.getroot()   #getroot() mi da la radice dell'albero
    return root #ritorna root per ottenere la radice

titolo = input("Inserisci il nome del libro: ")
autore = input("Inserisci il nome dell'autore: ")

root = xml_to_file()
nuovo_libro = ET.Element('libro')
nome_libro_elem = ET.SubElement(nuovo_libro, 'titolo')
nome_libro_elem.text = titolo
autore_libro_elem = ET.SubElement(nuovo_libro, 'autore')
autore_libro_elem.text = autore
root.append(nuovo_libro)

tree = ET.ElementTree(root)

try:
    tree.write("example2.xml", xml_declaration=True)  #scrivo su file
    print("File scritto correttamente")
except:
    print("Errore! ")

