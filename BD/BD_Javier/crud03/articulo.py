from tienda_db import TiendaDB


class Articulo:
    """Clase para operaciones CRUD de artículos."""
    def __init__(self, db: TiendaDB):
        self.db = db

    def add(self, referencia, descripcion, precio, proveedor_id):
        self.db.cursor.execute('''
            INSERT INTO articulos (referencia, descripcion, precio, proveedor_id)
            VALUES (?, ?, ?, ?)
        ''', (referencia, descripcion, precio, proveedor_id))
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get(self, articulo_id):
        self.db.cursor.execute("SELECT * FROM articulos WHERE id = ?", (articulo_id,))
        return self.db.cursor.fetchone()

    def get_all(self):
        self.db.cursor.execute('''
            SELECT a.id, a.referencia, a.descripcion, a.precio, p.nombre AS proveedor
            FROM articulos a
            JOIN proveedores p ON a.proveedor_id = p.id
        ''')
        return self.db.cursor.fetchall()

    def update(self, articulo_id, **kwargs):
        campos = []
        valores = []
        for key, value in kwargs.items():
            if key in ['referencia', 'descripcion', 'precio', 'proveedor_id']:
                campos.append(f"{key} = ?")
                valores.append(value)
        valores.append(articulo_id)
        if campos:
            sql = f"UPDATE articulos SET {', '.join(campos)} WHERE id = ?"
            self.db.cursor.execute(sql, valores)
            self.db.conn.commit()

    def delete(self, articulo_id):
        self.db.cursor.execute("DELETE FROM articulos WHERE id = ?", (articulo_id,))
        self.db.conn.commit()
