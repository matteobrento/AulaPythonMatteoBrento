conteggio = 0   #regola di conteggio

while conteggio < 10:   #regola di rottura
    print(conteggio)
    conteggio +=1

print("\n")



#while True:     #ripete all'infinito finchè non trova un break

#    break


controllociclo = True
x=0
while controllociclo:     #ripete all'infinito finchè non trova un break

    print(x)
    x+=1

    if(x>5):
        controllociclo = False #posso chiuderlo con break oppure convertendo il booleano 
else:
    print("Ciclo Finito")