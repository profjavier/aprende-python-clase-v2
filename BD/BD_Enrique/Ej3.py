import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',       # Cambia si es necesario
    user='tu_usuario',      # Reemplaza con tu usuario
    password='tu_contraseña', # Reemplaza con tu contraseña
    database='MiBaseDeDatos'
)
cursor = conexion.cursor()

query = """
SELECT u.nombre, u.email, t.nombre AS tipo
FROM tb_usuarios u
JOIN tb_usuarios_tipos t ON u.tipo_usuario_id = t.id;
"""
cursor.execute(query)
usuarios = cursor.fetchall()

for nombre, email, tipo in usuarios:
    print(f"{nombre} - {email} - {tipo}")

cursor.close()
conexion.close()