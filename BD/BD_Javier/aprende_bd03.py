import sqlite3


class LibroDB:
    def __init__(self, db_name="libros_v2.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isbn VARCHAR (15) UNIQUE NOT NULL,
                    titulo VARCHAR
                (
                    255
                ) NOT NULL,
                    autor VARCHAR
                (
                    100
                ) NOT NULL,
                    editorial VARCHAR
                (
                    100
                ) NOT NULL,
                    fecha_publicacion INTEGER NOT NULL,
                    descripcion TEXT)
                ''')
        self.conn.commit()

    def add_libro(self, libro):
        sql = """ INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion) \
                  VALUES (?, ?, ?, ?, ?)
                """  # En mysql era (%s, %s, %s, %s, %s)

        try:
            self.cursor.execute(sql, (libro['isbn'], libro['titulo'], libro['autor'], libro['editorial'], libro['fecha_publicacion']))
            self.conn.commit()
            print("Libro guardado.")
        except Exception as e:
            print(f"Error al añadir el libro: {e}")

    def delete_libro(self, id):
        pass

    def update_libro(self, id, libro):
        pass

    def get_libro(self, id):
        pass

    def get_all_libros(self):
        sql = "SELECT id, isbn, titulo, autor, editorial, fecha_publicacion FROM libros"
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        return libros

    def close(self):
        pass

if __name__ == "__main__":
    db = LibroDB()
    db.add_libro(
        {"isbn": "978-00-00-000001",
         "titulo":"El Quijote",
         "autor":"Cervantes",
         "editorial":"Desconocida",
         "fecha_publicacion":1600}
    )
    print(db.get_all_libros())
