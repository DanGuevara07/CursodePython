"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

Color

Ruedas

Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

Velocidad

Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
"""


class Vehículo:
    Color = None
    Ruedas = None
    Puertas = None

class Coche(Vehículo):
    Velocidad = None
    Cilindrada = None

miCoche = Coche()
print(miCoche)
