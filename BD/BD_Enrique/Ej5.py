import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='castelar2122'
)

cursor = conexion.cursor()

usuario_id = int(input("Ingrese el ID del usuario que desea modificar: "))

cursor.execute("USE MiBaseDeDatos;")
cursor.execute("SELECT nombre, email, contraseña FROM tb_usuarios WHERE id = %s;", (usuario_id,))
usuario = cursor.fetchone()

if usuario:
    nombre_actual, email_actual, contraseña_actual = usuario

    nuevo_nombre = input(f"Nombre [{nombre_actual}]: ").strip()
    if not nuevo_nombre:
        nuevo_nombre = nombre_actual

    nuevo_email = input(f"Email [{email_actual}]: ").strip()
    if not nuevo_email:
        nuevo_email = email_actual

    nueva_contraseña = input(f"Contraseña [********]: ").strip()
    if not nueva_contraseña:
        nueva_contraseña = contraseña_actual

    actualizar_usuario = """
    UPDATE tb_usuarios
    SET nombre = %s, email = %s, contraseña = %s
    WHERE id = %s;
    """

    try:
        cursor.execute(actualizar_usuario, (nuevo_nombre, nuevo_email, nueva_contraseña, usuario_id))
        conexion.commit()
        print("Usuario actualizado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error al actualizar el usuario: {err}")

else:
    print("No se encontró un usuario con ese ID.")

cursor.close()
conexion.close()