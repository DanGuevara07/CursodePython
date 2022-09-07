
"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
lo abráis y escribáis dentro del archivo. 
Para ello, tendréis que acceder dos veces al archivo creado.
"""
def main():
    f = open('archivo.txt','w+')
    f.write('Hola')
    f.write(' mi nombre es\n')
    f.write('Daniel Guevara\n')
    f.write('y estoy practicando\n')
    f.write('la manipulación de ficheros')
    f.close()

if __name__=='__main__':
    main()
