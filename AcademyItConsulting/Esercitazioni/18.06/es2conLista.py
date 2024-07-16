#Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare 
#(aggiungi, rimuovi, elimina)

lista = []


print("**Menu** \n")
print(" 1 per aggiungere la stringa in ultima posizione\n 2 inserire una stringa in una posizione e per modificarla\n 3 per rimuovere la stringa\n Altrimenti Fine")
print("\n")
print(lista)
print("\n")
cod = int(input("Digita un opzione: "))

if(cod==1):
    lista.append('Ciao')
    print(lista)
        
elif(cod==2):
    lista.insert(0, 'Python')
    print(lista)
    lista[0] = 'Python & Machine Learning'
    print(lista)
    print("Stringa Modificata")

elif(cod==3):
    lista.insert(0, 'Ciao') 
    print(lista)
    lista.remove('Ciao') 
    print(lista)
    print("Stringa Rimossa")

else:
    print("Fine")