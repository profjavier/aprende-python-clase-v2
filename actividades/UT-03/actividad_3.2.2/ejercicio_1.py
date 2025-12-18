# Configuración de usuario
# Diseñe un script que cree un diccionario con la información de un usuario
# (nombre de usuario, correo electrónico y si está activo), y finalmente muestre el
# diccionario en pantalla.

usuario = {
    "nombre": "Francisco Javier García Aróstegui",
    "email": "javier@iescastelar.com",
    "activo": True
}
'''
Creado con dict sería 
usuario = dict(
    nombre="Francisco Javier García Aróstegui",
    email="javier@iescastelar.com",
    activo=True
)
'''

print(usuario)
print(usuario["nombre"])
print(usuario["email"])
print(usuario["activo"])


