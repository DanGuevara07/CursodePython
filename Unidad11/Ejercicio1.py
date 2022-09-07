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