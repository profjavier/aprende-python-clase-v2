usuarios = [
    {"username":"pepito", "password":"1234"},
    {"username":"luisito", "password":"1234"},
]


def index(username):
    ''' Recorre usuarios y devuelve la posición en la que
     encuentra el username,
    -1 si no existe'''
    # SOL 1
    # pos = 0
    # while pos < len(usuarios) and uusuarios[pos]["username"] != username:
    #     pos += 1
    # return pos if pos < len(usuarios) else -1

    #SOL 2
    # pos = len(usuarios)-1
    # while pos > 0 and usuarios[pos]["username"] != username:
    #     pos -= 1
    # return pos

    #SOL 3
    return next((i for i,u in enumerate(usuarios) if u["username"] == username), -1)


def exist(username):
    return index(username)>=0