"""
Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
"""


paises= input("Ingrese la lista de paises separados por coma")
lista = paises.split(',')
miset = set()
for i in lista:
    if i.startswith(' '):
        aux=list(i)
        aux.pop(0)
        i=''.join(map(str,aux))
    miset.add(i)

lista = list(miset)
lista.sort()
print("Lista de Paises")
for i in lista:
    print('{}, '.format(i), end='')

