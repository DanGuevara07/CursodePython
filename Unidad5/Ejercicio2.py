# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:57:40 2022

@author: LENOVO

Escribe una función que pueda
decirte si un número (número entero) es primo o no.
"""

def numeroprimo(numero):
    for n in range(2,numero):
        if numero % n == 0:
            return False
        return True
    
num = int(input("Ingrese un numero..."))
if numeroprimo(num):
    print("El numero es primo")
else:
    print("El numero no es primo")
    
