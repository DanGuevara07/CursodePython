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
