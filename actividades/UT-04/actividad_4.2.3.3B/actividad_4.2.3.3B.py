import usuarios as us

intentos = {}
for usuario in us.usuarios:
    intentos[usuario["username"]] = 0
print(intentos)
while True:
    username = input("username: ")
    if username in intentos and intentos[username] < 3:
        password = input("Password: ")

        # usuario = [u for u in usuarios if p["nombre"] == username]

        # usuario =next((u for u in _usuarios if u["username"] == username), None)
        # if usuario:

        #usuario = ([u for u in usuarios if u["username"] == username] or [None])[0]
        # if usuario:
        # print (usuario)
        #usuario = ([u for u in usuarios if u["username"] == "pepito"] or [None])[0]

        pos = us.index(username)

        if pos >= 0:
            if (us.usuarios[pos]["password"] == password):
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