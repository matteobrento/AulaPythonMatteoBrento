numeri = [1, 2, 3, 4, 5, 6, 7, 8]

def numeri_pari(a):

    return a%2 == 0

numeri_true = []

for numero in numeri:
    numeri_true.append(numeri_pari(numero))

print(numeri_true)
print("\n")

numeri_true = list(map(numeri_pari, numeri))
print(numeri_true) #fanno la stessa cosa ma questa usa la funzione map
#map applica a tutti gli elementi di un iterabile una funzione

listavuota = []
for numero in numeri:
    if numeri_pari(numero):
        listavuota.append(numero)
    
print(f"{listavuota}")

listavuota = list(filter(numeri_pari, numeri))
print(listavuota)
#restituiscono un oggetto quindi bisogna convertirli nel tipo
#filter filtra un iterabile tramite una funzione