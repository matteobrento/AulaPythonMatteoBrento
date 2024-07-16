
import xml.etree.ElementTree as ET  #xml funziona come un albero

def xml_to_file():  #output dal file
    tree = ET.parse("file.xml") #parse salva il file xml in una variabile
    root = tree.getroot()   #getroot() mi da la radice dell'albero
    return tree, root #tree per scrivere su file, root per la radice

def xml_to_string():    #output dalla stringa inserita

    xml_data = '''<?xml version="1.0"?>
    <saluti>
    <saluto id='1'>Hello World</saluto>    
    <saluto id='2'>Hello World2</saluto>
    <saluto id='3'>Hello World3</saluto>
    </saluti>
    ''' #foglie

    root = ET.fromstring(xml_data)

    return root


#root = xml_to_string()    #con to_string prende i 3 saluti sopra definiti
#tree = xml_to_file()
""" for saluto in root.findall('saluto'):   #findall() cerca tutti gli elementi di un tipo nella root, in questo caso 'saluto'
    print(saluto)
    print(saluto.tag)
    print(saluto.text) """


""" saluto = root.find('saluto')    #restituisce il primo elemento che trova di tipo saluto
print(saluto.text)
print(saluto.attrib) """


#tree.write("file.xml")  #scrittura su file xml
tree, root = xml_to_file()
nuovo_elemento = ET.Element('nuovo_tag')
nuovo_elemento.text = "testo del nuovo elemento"
root.append(nuovo_elemento)
try:
    tree.write('file.xml')
    print("File scritto")
except:
    print("Errore")



