import sqlite3
import logging

from Libro import Libro


class LibrosDB:
    logger = logging.getLogger("LibroDB")

    SELECT = "SELECT id, isbn, titulo, autor, editorial, fecha_publicacion, descripcion FROM libros"

    def __init__(self, db_name="libros_v4.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row  # Permite acceso por nombre de columna
        self.cursor = self.conn.cursor()
        self._crear_tablas()
        logging.info("Conexión con la BD realizada con exito.")

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
            self.logger.info(f"Se ha añadido el libro de id¡sbn {libro['isbn']}")
            return self.cursor.lastrowid
        except Exception as e:
            self.logger.error(e)
            return 0

    def delete_libro(self, id: int) -> bool:
        try:
            sql = "DELETE FROM libros WHERE id = ?"
            self.cursor.execute(sql,(id,))
            self.conn.commit()
            return True
        except Exception as e:
            self.logger.error(e)
            return False

    def update_libro(self, id: int, libro: dict) -> int:
        try:
            sql = "UPDATE libros SET isbn = ?, titulo=?, autor=?, editorial, fecha_publicacion=?, descripcion=? WHERE id = ?"
            self.cursor.execute(sql,(libro['isbn'], libro['titulo'], libro['autor'], libro['editorial'], libro['fecha_publicacion'],id))
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.logger.error(e)
            return -1

    def get_libro(self, id:int) -> dict:
        sql = LibrosDB.SELECT + " WHERE id = ?"
        #sql = self.SELECT + " WHERE id = ?"
        self.cursor.execute(sql, (id,))
        libro = self.cursor.fetchone()
        libro_dict = dict(libro) if libro else None
        return libro_dict

    def get_all_libros(self)-> list:
        sql = LibrosDB.SELECT
        self.cursor.execute(sql)
        libros = self.cursor.fetchall()

        libros_obj = [Libro.from_dict( dict(libro) ) for libro in libros]
        return libros_obj

    def get_by_isbn(self, isbn: str) -> dict:
        sql = LibrosDB.SELECT + " WHERE isbn = ?"
        self.cursor.execute(sql, (isbn,))
        libro = self.cursor.fetchone()
        libro_dict = dict(libro) if libro else None
        return libro_dict

    def update_by_isbn(self, isbn:str, libro: dict) -> int:
        try:
            sql = "UPDATE libros SET isbn = ?, titulo=?, autor=?, editorial=?, fecha_publicacion=?, descripcion=? WHERE isbn = ?"
            self.cursor.execute(sql,(libro['isbn'], libro['titulo'], libro['autor'], libro['editorial'], libro['fecha_publicacion'],isbn))
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.logger.error(e)
            return -1

    def delete_by_isbn(self, isbn:str) -> bool:
        try:
            sql = "DELETE FROM libros WHERE isbn = ?"
            self.cursor.execute(sql,(isbn,))
            self.conn.commit()
            return True
        except Exception as e:
            self.logger.error(e)
            return False

    def get_filter_autor(self, autor:str) -> list:
        sql = LibrosDB.SELECT + " WHERE autor = ?"
        self.cursor.execute(sql, (autor,))
        libros = self.cursor.fetchall()
        libros_dict = [dict(libro) for libro in libros]
        return libros_dict

    def close(self):
        if self.conn:
            self.conn.close()
