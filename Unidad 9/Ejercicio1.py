
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

