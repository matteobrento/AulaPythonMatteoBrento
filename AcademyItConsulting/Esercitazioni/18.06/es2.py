#Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare 
#(aggiungi, rimuovi, elimina)

s = input("Inserisci una Stringa: ")


print("**Menu** \n")
print(" 1 per leggere la stringa\n 2 per modificare la stringa\n 3 per splittare la stringa\n Altrimenti la cancella\n")
cod = int(input("Digita un opzione: "))

if(cod==1):
    print(s)
        
elif(cod==2):
    print(s.replace('Python', 'Python & Machine Learning')) #Operazione di modifica tramite s.replace
    print("Stringa Modificata")

elif(cod==3):
    print(s.split()) #Operazione di Split tramite s.split

else:
    s = ""
    print("La stringa è stata eliminata")

    

