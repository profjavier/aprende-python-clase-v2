import sqlite3
from datetime import datetime

class EmpleadosDB:
    def __init__(self, db_name="empleados.db"):
        """Inicializa la conexión a la base de datos."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Crea la tabla 'empleados' si no existe."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido1 TEXT NOT NULL,
                apellido2 TEXT NOT NULL,
                sueldo REAL NOT NULL,
                fecha_alta TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_empleado(self, nombre, apellido1, apellido2, sueldo, fecha_alta):
        """Agrega un nuevo empleado a la base de datos."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute('''
            INSERT INTO empleados (nombre, apellido1, apellido2, sueldo, fecha_alta, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido1, apellido2, sueldo, fecha_alta, now, now))
        self.conn.commit()

    def update_empleado(self, empleado_id, **kwargs):
        """Actualiza los datos de un empleado dado su ID."""
        campos = []
        valores = []
        for key, value in kwargs.items():
            if key in ['nombre', 'apellido1', 'apellido2', 'sueldo', 'fecha_alta']:
                campos.append(f"{key} = ?")
                valores.append(value)
        valores.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # updated_at
        valores.append(empleado_id)
        if campos:
            sql = f"UPDATE empleados SET {', '.join(campos)}, updated_at = ? WHERE id = ?"
            self.cursor.execute(sql, valores)
            self.conn.commit()

    def get_empleado(self, empleado_id):
        """Obtiene un empleado por su ID."""
        self.cursor.execute("SELECT * FROM empleados WHERE id = ?", (empleado_id,))
        return self.cursor.fetchone()

    def get_all_empleados(self):
        """Obtiene todos los empleados."""
        self.cursor.execute("SELECT * FROM empleados")
        return self.cursor.fetchall()

    def delete_empleado(self, empleado_id):
        """Elimina un empleado por su ID."""
        self.cursor.execute("DELETE FROM empleados WHERE id = ?", (empleado_id,))
        self.conn.commit()

    def close(self):
        """Cierra la conexión a la base de datos."""
        self.conn.close()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    db = EmpleadosDB()
    db.add_empleado("Juan", "Pérez", "García", 2500.0, "2026-01-01")
    print(db.get_all_empleados())
    db.update_empleado(1, sueldo=3000.0)
    print(db.get_empleado(1))
    db.delete_empleado(1)
    db.close()
