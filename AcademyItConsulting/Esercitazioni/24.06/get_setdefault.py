mio_dizionario = {'a': 1, 'b': 2}
valore = mio_dizionario.get('a')  # Restituisce 1
valore = mio_dizionario.get('c', 3)  # Restituisce 3, ma non aggiunge 'c': 3 al dizionario
print(mio_dizionario)


mio_dizionario = {'a': 1, 'b': 2}
valore = mio_dizionario.setdefault('a', 0)  # Restituisce 1, 'a' esiste già
valore = mio_dizionario.setdefault('c', 3)  # Restituisce 3, e aggiunge 'c': 3 al dizionario
print(mio_dizionario)
