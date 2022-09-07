"""
En este segundo ejercicio, tendréis que crear un programa que
tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.
Deberéis de definir los métodos para 
inicializar sus atributos, imprimirlos
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""


class Alumno:
    nombre = None
    nota = None
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se llama ", self.nombre)
        print("Y su nota es: ", self.nota)
    def estaAprobado(self):
        if self.nota<3:
            print("El alumno ha desaprobado")
        else:
            print("el alumno ha aprovado")

a = Alumno("Jose", 2.5)
a.estaAprobado()
