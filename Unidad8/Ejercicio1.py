
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