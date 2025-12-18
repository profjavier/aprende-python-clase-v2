_usuarios = [
    {"username":"pepito", "password":"1234"},
    {"username":"luisito", "password":"1234"},
]

_intentos = {}

NUM_INTENTOS_MAX = 3


def index(username):
    ''' Recorre usuarios y devuelve la posición en la que
     encuentra el username,
    -1 si no existe'''
    return next((i for i,u in enumerate(_usuarios) if u["username"] == username), -1)


def exist(username):
    return index(username)>=0

def get(username):
    ''' Devolver el usuario o None si no existe
    '''
    pass

def login(username, password):
    ''' Devuelve True si el usuario es valido'''
    pass

def get_intentos(username):
    ''' Devuelve el número de intentos o 0 si no existe'''
    pass
def set_intentos(username, num_intento):
    ''' Establece el numero de intentos '''
    pass
def reset_intentos(username):
    ''' Reinicia el contador de intentos '''
    pass
def inc_intentos(username):
    ''' Incrementa el número de intentos'''
    pass
def excedidos_intentos(username):
    ''' devuelve true si se ha excedido el número de intentos'''
    pass