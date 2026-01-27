from tienda_db import TiendaDB


class Proveedor:
    """Clase para operaciones CRUD de proveedores."""
    def __init__(self, db: TiendaDB):
        self.db = db

    def add(self, nombre, cif, razon_social):
        self.db.cursor.execute('''
            INSERT INTO proveedores (nombre, cif, razon_social)
            VALUES (?, ?, ?)
        ''', (nombre, cif, razon_social))
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get(self, proveedor_id):
        self.db.cursor.execute("SELECT * FROM proveedores WHERE id = ?", (proveedor_id,))
        return self.db.cursor.fetchone()

    def get_all(self):
        self.db.cursor.execute("SELECT * FROM proveedores")
        return self.db.cursor.fetchall()

    def update(self, proveedor_id, **kwargs):
        campos = []
        valores = []
        for key, value in kwargs.items():
            if key in ['nombre', 'cif', 'razon_social']:
                campos.append(f"{key} = ?")
                valores.append(value)
        valores.append(proveedor_id)
        if campos:
            sql = f"UPDATE proveedores SET {', '.join(campos)} WHERE id = ?"
            self.db.cursor.execute(sql, valores)
            self.db.conn.commit()

    def delete(self, proveedor_id):
        self.db.cursor.execute("DELETE FROM proveedores WHERE id = ?", (proveedor_id,))
        self.db.conn.commit()

