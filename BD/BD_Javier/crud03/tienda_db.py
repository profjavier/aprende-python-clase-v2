import sqlite3
from datetime import datetime

from articulo import Articulo
from proveedor import Proveedor


class TiendaDB:
    """Clase central que maneja la conexión y crea las tablas."""
    def __init__(self, db_name="tienda.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = 1")  # Activar claves foráneas
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Crea las tablas 'proveedores' y 'articulos'."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS proveedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cif TEXT NOT NULL,
                razon_social TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS articulos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referencia TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                precio REAL NOT NULL,
                proveedor_id INTEGER NOT NULL,
                FOREIGN KEY (proveedor_id) REFERENCES proveedores(id) ON DELETE CASCADE
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    db = TiendaDB()

    proveedores = Proveedor(db)
    articulos = Articulo(db)

    # Crear proveedores
    prov1_id = proveedores.add("Proveedor A", "A12345678", "Proveedor A S.L.")
    prov2_id = proveedores.add("Proveedor B", "B87654321", "Proveedor B S.A.")

    # Crear artículos
    articulos.add("REF001", "Artículo 1", 10.5, prov1_id)
    articulos.add("REF002", "Artículo 2", 25.0, prov2_id)

    # Consultas
    print("Proveedores:", proveedores.get_all())
    print("Artículos:", articulos.get_all())

    db.close()
