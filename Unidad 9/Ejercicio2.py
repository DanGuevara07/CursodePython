from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

lista = filter(lambda x: x % 2, lista)
lista2 = list(lista).copy()
print(lista2)
suma = reduce(lambda a,b: a + b, lista2)
print(suma)