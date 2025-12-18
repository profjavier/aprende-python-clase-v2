usuarios = [
    {"username":"pepito", "password":"1234"},
    {"username":"luisito", "password":"1234"},
]

intentos = {}
for usuario in usuarios:
    intentos[usuario["username"]] = 0
print(intentos)
while True:
    username = input("username: ")
    if username in intentos and intentos[username] < 3:
        password = input("Password: ")

        # usuario = [u for u in usuarios if p["nombre"] == username]

        # usuario =
        # next((u for u in _usuarios if u["username"] == username), None)
        # if usuario:

        #usuario = ([u for u in usuarios if u["username"] == username] or [None])[0]
        # if usuario:
        # print (usuario)
        #usuario = ([u for u in usuarios if u["username"] == "pepito"] or [None])[0]

        pos = 0
        while pos<len(usuarios) and usuarios[pos]["username"] != username:
            pos +=  1

        if usuarios[pos]["username"] == username:
            if (usuarios[pos]["password"] == password):
                intentos[username] = 0
                permitido_acceso = True
                print("Acceso permitido")
            else:
                intentos[username] += 1
                print("Credenciales incorrectas")
        else:
            print("Usuario no encontrado")
    else:
        print("Acceso no permitido")