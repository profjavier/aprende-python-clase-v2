import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='castelar2122'
)

cursor = conexion.cursor()

# Mostrar los tipos de usuario disponibles
cursor.execute("USE MiBaseDeDatos;")
cursor.execute("SELECT id, nombre FROM tb_usuarios_tipos;")
tipos_usuarios = cursor.fetchall()

print("Tipos de usuarios disponibles:")
for tipo in tipos_usuarios:
    print(f"{tipo[0]}: {tipo[1]}")

# Solicitar al usuario el tipo de usuario
tipo_usuario_id = int(input("Ingrese el ID del tipo de usuario que desea asignar: "))

# Pedir datos del usuario
nombre = input("Ingrese el nombre del usuario: ")
email = input("Ingrese el email del usuario: ")
contraseña = input("Ingrese la contraseña del usuario: ")

# Insertar el nuevo usuario en la base de datos
insertar_usuario = """
INSERT INTO tb_usuarios (tipo_usuario_id, nombre, email, contraseña)
VALUES (%s, %s, %s, %s);
"""

try:
    cursor.execute(insertar_usuario, (tipo_usuario_id, nombre, email, contraseña))
    conexion.commit()
    print("Usuario insertado correctamente.")
except mysql.connector.Error as err:
    print(f"Error al insertar usuario: {err}")

# Cerrar conexión
cursor.close()
conexion.close()