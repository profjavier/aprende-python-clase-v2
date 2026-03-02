import sqlite3

'''
DEVUELVE TUPLAS 
UTILIZA CONSTANTE SELECT 
'''

class LibroDB:

    SELECT = "SELECT id, isbn, titulo, autor, editorial, fecha_publicacion, descripcion FROM libros"

    def __init__(self, db_name="libros_v3B.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tablas()

    def _crear_tablas(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isbn VARCHAR (15) UNIQUE NOT NULL,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(100) NOT NULL,
                    editorial VARCHAR(100) NOT NULL,
                    fecha_publicacion INTEGER NOT NULL,
                    descripcion TEXT)
                ''')
        self.conn.commit()

    def add_libro(self, libro: dict) -> int:
        sql = """ INSERT INTO libros (isbn, titulo, autor, editorial, fecha_publicacion) \
                  VALUES (?, ?, ?, ?, ?)
                """  # En mysql era (%s, %s, %s, %s, %s)

        try:
            self.cursor.execute(sql, (libro['isbn'], libro['titulo'], libro['autor'], libro['editorial'], libro['fecha_publicacion']))
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            return 0

    def delete_libro(self, id: int) -> bool:
        try:
            sql = "DELETE FROM libros WHERE id = ?"
            self.cursor.execute(sql,(id,))
            self.conn.commit()
            return True
        except Exception as e:
            return False

    '''def update_libro(self, id:int, libro:dict)-> int:
        isbn = libro["isbn"]
        titulo = libro["titulo"]
        autor = libro["autor"]
        editorial = libro["editorial"]
        fecha_publicacion = libro["fecha_publicacion"]

        sql = """UPDATE libros SET isbn = ?, titulo = ?, autor = ? ,editorial = ? ,fecha_publicacion = ?
                               WHERE id=?
                       """

        try:
            self.cursor.execute(sql, (isbn, titulo, autor, editorial, fecha_publicacion,id))
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            return -1
    '''

    def update_libro(self, id: int, libro: dict) -> int:
        try:
            sql = "UPDATE libros SET isbn = ?, titulo=?, autor=?, editorial, fecha_publicacion=?, descripcion=? WHERE id = ?"
            self.cursor.execute(sql,(libro['isbn'], libro['titulo'], libro['autor'], libro['editorial'], libro['fecha_publicacion'],id))
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            return -1

    def get_libro(self, id:int) -> tuple:
        sql = LibroDB.SELECT + " WHERE id = ?"
        self.cursor.execute(sql, (id,))
        libro = self.cursor.fetchone()
        return libro

    def get_all_libros(self) -> list:
        sql = LibroDB.SELECT
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()
        return libros

    def get_by_isbn(self, isbn: str) -> tuple:
        sql = LibroDB.SELECT + " WHERE isbn = ?"
        self.cursor.execute(sql, (isbn,))
        libros = self.cursor.fetchall()
        return libros

    def update_by_isbn(self, isbn:str, libro: dict) -> int:
        try:
            sql = "UPDATE libros SET isbn = ?, titulo=?, autor=?, editorial=?, fecha_publicacion=?, descripcion=? WHERE isbn = ?"
            self.cursor.execute(sql,(libro['isbn'], libro['titulo'], libro['autor'], libro['editorial'], libro['fecha_publicacion'],isbn))
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            return -1

    def delete_by_isbn(self, isbn:str) -> bool:
        try:
            sql = "DELETE FROM libros WHERE isbn = ?"
            self.cursor.execute(sql,(isbn,))
            self.conn.commit()
            return True
        except Exception as e:
            return False

    def get_filter_autor(self, autor:str) -> list:
        sql = LibroDB.SELECT + " WHERE autor = ?"
        self.cursor.execute(sql, (autor,))
        libros = self.cursor.fetchall()
        return libros

    def close(self):
        if self.conn:
            self.conn.close()

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
