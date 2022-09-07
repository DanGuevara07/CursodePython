"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos
impares de una lista pasada por parámetro con filter 
y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]

lista = filter(lambda x: x % 2, lista)
lista2 = list(lista).copy()
print(lista2)
suma = reduce(lambda a,b: a + b, lista2)
print(suma)
