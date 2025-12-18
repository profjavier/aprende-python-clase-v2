import usuarios as us



# while True:
#     username = input("username: ")
#     password = input("Password: ")
#
#     usuario = us.get(username)
#
#     if usuario and us.login(username, password):
#         if us.get_intentos(username) < us.NUM_INTENTOS_MAX - 1:
#             us.reset_intentos(username)
#             print("Acceso permitido")
#         else:
#             print("El usuario estaba bloqueado")
#     elif usuario:
#         if us.get_intentos(username) >= us.NUM_INTENTOS_MAX - 1:
#             print("Usuario bloqueado")
#         else:
#             us.inc_intentos(username)
#             print("Credenciales incorrectas")
#     else:
#         print("Usuario no encontrado")


acceso_permitido = False
while not acceso_permitido:
    username = input("username: ")
    password = input("Password: ")

    usuario = us.get(username)

    if usuario and us.login(username, password):
        if us.get_intentos(username) < us.NUM_INTENTOS_MAX - 1:
            us.reset_intentos(username)
            print("Acceso permitido")
            acceso_permitido = True
        else:
            print("El usuario estaba bloqueado")
    elif usuario:
        if  us.excedidos_intentos(username):
            print("Usuario bloqueado")
        else:
            us.inc_intentos(username)
            print("Credenciales incorrectas")
    else:
        print("Usuario no encontrado")