"""
En este segundo ejercicios tendréis 
que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
haréis una operación para calcular el tiempo que queda de trabajo.
"""

import time

A = time.localtime()

if A.tm_hour>=19:
    print("Es hora de ir a casa")
else:
    restante = []
    restante.append(60-A.tm_sec)
    if restante[0] !=0:
        restante.append(59-A.tm_min)
    else:
        restante.append(60-A.tm_min)
    if restante[1] !=0:
        restante.append(18-A.tm_hour)
    else:
        restante.append(19-A.tm_hour)
    print("Quedan ",restante[2],"horas",restante[1],"minutos",restante[0], "segundos de trabajo")
