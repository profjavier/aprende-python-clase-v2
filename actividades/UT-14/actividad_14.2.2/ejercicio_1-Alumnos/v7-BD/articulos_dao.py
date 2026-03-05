import logging
import sqlite3


class ArticulosDao:
    SELECT = "SELECT id, referencia, descripcion, precio, stock, observaciones FROM articulos"

    def __init__(self, filename="articulos.db"):
        self.conn = sqlite3.connect(filename)
        self.conn.row_factory = sqlite3.Row  # Permite acceso por nombre de columna
        self.cursor = self.conn.cursor()
        self._crear_tablas()
        self.config_log()
        self.logger.info("Conexión con la BD realizada con exito.")


    def config_log(self):
        log_file = "articulos.log"
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            encoding="utf-8"
        )
        self.logger = logging.getLogger("ArticulosDao")

    def _crear_tablas(self):
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS articulos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    referencia VARCHAR (15) UNIQUE NOT NULL,
                    descripcion VARCHAR(255) NOT NULL,
                    precio FLOAT NOT NULL,
                    stock FLOAT NOT NULL,
                    observaciones TEXT)
                ''')
        self.conn.commit()

    def save(self, articulo: dict) -> int:
        sql = """ INSERT INTO articulos (referencia, descripcion, precio, stock, observaciones) \
                  VALUES (?, ?, ?, ?, ?)
                """  # En mysql era (%s, %s, %s, %s, %s)

        try:
            self.cursor.execute(sql, (articulo['referencia'], articulo['descripcion'],
                                      articulo['precio'], articulo['stock'],
                                      articulo['observaciones']))
            self.conn.commit()
            self.logger.info(f"Se ha añadido la referencia {articulo['referencia']}")
            return self.cursor.lastrowid
        except Exception as e:
            self.logger.error(e)
            return 0

    def find(self, referencia_buscada: str) -> dict:
        sql = ArticulosDao.SELECT + " WHERE referencia = ?"
        self.cursor.execute(sql, (referencia_buscada,))
        articulo = self.cursor.fetchone()
        articulo_dict = dict(articulo) if articulo else None
        return articulo_dict


