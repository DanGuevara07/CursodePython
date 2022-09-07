"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará
de tres columnas: la columna id de tipo entero,
la columna nombre que será de tipo texto y la columna 
apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import sqlite3
def insertar_alumno(nombre, apellido):
    conn = sqlite3.connect("mifichero.db")
    cursor = conn.cursor()
    query = '''INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)'''
    print("Query a ejecutar:", query)
    rows = cursor.execute(query, (nombre, apellido))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    conn = sqlite3.connect("mifichero.db")
    cursor = conn.cursor()
    query = f'CREATE TABLE Alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, apellido TEXT NOT NULL)'
    print("Query a ejecutar:", query)
    rows = cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    for i in range(8):
        nombre= input(f"Ingrese nombre del alumno # {i}: ")
        apellido = input(f"Ingrese apellido del alumno # {i}: ")
        insertar_alumno(nombre, apellido)





if __name__=='__main__':
    main()
