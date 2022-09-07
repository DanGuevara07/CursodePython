# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 15:24:18 2022

@author: LENOVO

Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
"""

numero_inicial = 1
numero_final = 16

for i in range (numero_inicial, numero_final):
    if i % 2 != 0:
        print(i)
        
        
