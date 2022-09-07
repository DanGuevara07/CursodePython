# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:23:38 2022

@author: LENOVO

Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
"""

def añobisiesto(año):
    if año % 4 == 0:
        return True
    else:
        return False

a = int(input("Ingrese un año:"))
if añobisiesto(a):
    print("El año es bisiesto")
else:
    print("el año no es bisiesto")
