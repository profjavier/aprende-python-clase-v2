import sqlite3

DATABASE_NAME = 'libros.db'
conexion = sqlite3.connect(DATABASE_NAME)
cursor = conexion.cursor()

#--------------------------
cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn VARCHAR(15) UNIQUE NOT NULL,
        titulo VARCHAR(255) NOT NULL,
        autor VARCHAR(100) NOT NULL,
        editorial VARCHAR(100) NOT NULL,
        fecha_publicacion INTEGER NOT NULL,
        descripcion TEXT)
''')
conexion.commit()

#--------------------------
isbn = input("ISBN")
titulo = input("Titulo: ")
autor = input("Autor: ")
editorial = input("Editorial: ")
fecha_publicacion = input("Año de publicación: ")

sql =   """ INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion) 
                VALUES (?, ?, ?, ?, ?)
        """  # En mysql era (%s, %s, %s, %s, %s)

try:
    cursor.execute(sql, (isbn, titulo, autor, editorial, fecha_publicacion) )
    conexion.commit()
    print("Libro guardado.")
except Exception as e:
    print(f"Error al añadir el libro: {e}")

#--------------------------

sql = "SELECT id, isbn, titulo, autor, editorial, fecha_publicacion FROM libros"
cursor.execute(sql)
libros = cursor.fetchall()

print("- Prueba 1 -------")
print(libros)
print("--------")

print("- Prueba 2 -------")
for libro in libros:
    print(libro)
print("--------")

print("- Prueba 3 -------")
for libro in libros:
    print(libro[0], libro[1])
print("--------")

cursor.close()
conexion.close()