import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',       # o la IP del servidor
    user='root',      # reemplaza con tu usuario
    password='castelar2122' # reemplaza con tu contraseña
)

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS MiBaseDeDatos;")
print("Base de datos creada o ya existente.")


cursor.execute("USE MiBaseDeDatos;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_usuarios_tipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tb_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo_usuario_id INT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    -- Puedes añadir más campos que consideres necesarios
    FOREIGN KEY (tipo_usuario_id) REFERENCES tb_usuarios_tipos(id)
);
""")

print("Tablas creadas correctamente.")

# Cerrar conexión
cursor.close()
conexion.close()