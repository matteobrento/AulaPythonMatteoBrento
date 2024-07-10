"""
Database sarà:
-radice: <studenti>
Per ogni studente:
-Elemento <studente> con attributo id
-Elemento figlio <nome> per il nome dello studente
-Elemento figlio <corsi> che contiene elementi <corso> per ogni corso seguito dallo studente
-Elemento figlio <corso> che contiene elementi <voto> per ogni corso seguito dallo studente
Al primo avvio se il database è presente viene letto, se non è presente risulta database vuoto!
L'utente può aggiungere, eliminare o modificare uno studente, un corso o un elemento di corso
"""

import xml.etree.ElementTree as et


def da_xml_a_stringa():

    contenuto = '''<studenti>
    <studente id="1">
        <nome>Alice</nome>
        <corsi>
            <corso id="italiano">
                <voto>8</voto>
                <voto>5</voto>
            </corso>
            <corso id="matematica">
                <voto>4</voto>
                <voto>7</voto>
            </corso>
        </corsi>
    </studente>
    <studente id="2">
        <nome>Pino</nome>
        <corsi>
            <corso id="italiano">
                <voto>19</voto>
                <voto>3</voto>
            </corso>
            <corso id="matematica">
                <voto>4</voto>
                <voto>9</voto>
            </corso>
        </corsi>
    </studente>
    <studente id="3">
        <nome>Garibaldi</nome>
        <corsi>
            <corso id="italiano">
                <voto>1</voto>
                <voto>3</voto>
            </corso>
            <corso id="matematica">
                <voto>7</voto>
                <voto>8</voto>
            </corso>
        </corsi>
    </studente>
</studenti>
    '''
    try:
        root = et.fromstring(contenuto)
        return root
    except:
        print("errore!")
        return 1

dizionario=["italiano","matematica","inglese"]

root=da_xml_a_stringa()
if(root==1):        #se la funzione ritorna 1, vuol dire che l'albero è vuoto, e crea una radice
    root=et.Element("studenti")

def aggiungi_studente():
    nome=input("scrivi il nome dello studente: ")
    counter=0
    for studente in root.findall("studente"):
        counter +=1
    studente=et.Element("studente",{"id":str(counter+1)}) 
    nome_studente=et.SubElement(studente,"nome").text=nome
    corsi_scuola=et.SubElement(studente,"corsi")
    for materia in dizionario:
        num_voti=int(input(f"quanti voti vuoi aggiungere alla materia {materia}? "))
        if num_voti>0:
            corso=et.SubElement(corsi_scuola, "corso", {"id":materia})
            for i in range(0,num_voti):
                voto=input("inserisci voto: ")
                nvoto=et.SubElement(corso,"voto")
                nvoto.text=voto
    root.append(studente)

def rimuovi_studente():
    nome=input("inserisci nome dello studente da rimuovere: ")
    trovato=False
    for studente in root.findall("studente"):
        if studente.find("nome").text==nome:
            root.remove(studente)
            trovato=True
    if trovato:
        print("Studente eliminato")
    else:
        print("Studente non trovato")

def modifica_studente():
    nome=input("inserisci nome dello studente da modificare: ")
    trovato=False
    for studente in root.findall("studente"):
        if studente.find("nome").text==nome:
            new_nome=input("Inserisci il nuovo nome: ")
            studente.find("nome").text=new_nome
            trovato=True
    if trovato:
        print("Studente modificato")
    else:
        print("Studente non trovato")

def aggiungi_corso_studente():
    nome=input("inserisci nome dello studente a cui aggiungere il corso: ")
    trovato=False
    for studente in root.findall("studente"):
        if studente.find("nome").text==nome:
            nuova_materia=input(f"Inserisci il nome della nuova materia per {nome}: ")
            corsi=studente.find("corsi")
            ncorso=et.SubElement(corsi, "corso", {"id":nuova_materia})
            trovato=True
            num_voti=int(input(f"Quanti voti vuoi aggiungere alla materia {nuova_materia}? "))
            if num_voti>0:
                for i in range(0,num_voti):
                    voto=input("inserisci voto: ")
                    nvoto=et.SubElement(ncorso,"voto")
                    nvoto.text=voto
    if trovato:
        print("Materia e voti aggiunti correttamente")
    else:
        print("Studente non trovato")

def modifica_corso_studente():
    nome=input("inserisci nome dello studente a cui modificare il corso: ")
    trovato=False
    for studente in root.findall("studente"):
        if studente.find("nome").text==nome:   
            mat_mod=input("Inserisci la materia da modificare: ")
            nuova_mat=input("Inserisci il nuovo nome della materia: ")
            corsi=studente.find("corsi")
            for corso in corsi.findall("corso"):
                if corso.attrib["id"]==mat_mod:
                    trovato=True
                    corso.attrib["id"]=nuova_mat
    if trovato:
        print("Materia modificata correttamente")
    else:
        print("Studente o materia non trovata")

def rimuovi_corso_studente():
    nome=input("Inserisci nome dello studente a cui rimuovere il corso: ")
    trovato=False
    for studente in root.findall("studente"):
        if studente.find("nome").text==nome: 
            trovato=True
            mat_rim=input("Inserisci la materia da rimuovere: ")
            corsi=studente.find("corsi")
            for corso in corsi.findall("corso"):
                if corso.attrib["id"]==mat_rim:
                    corsi.remove(corso)
    if trovato:
        print("Materia eliminata correttamente")
    else:
        print("Studente o materia non trovata")

tree=et.ElementTree(root)


aggiungi_studente()
rimuovi_studente()
modifica_studente()
aggiungi_corso_studente() 
modifica_corso_studente()
rimuovi_corso_studente()
tree.write("database.xml")