"""
En este segundo ejercicio, tendréis que crear un archivo py 
y dentro crearéis una clase Vehículo, haréis un objeto de ella, 
lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle
class Vehiculo:
    def __init__(self, Marca, Color):
            self.Marca =  Marca
            self.Color =  Color
    def __str__(self):
        return f"Soy un vehiculo de marca {self.Marca} y color {self.Color}"

carro =Vehiculo('Honda', 'Rojo')
print(carro)
file = open('carro.dat','wb+')
pickle.dump(carro, file)
file.close()

file2 = open('carro.dat','rb')
carro2= pickle.load(file2)
file2.close()
print(carro2)


