from cuenta import Cuenta
def limpiar_pantalla():
    print("\033[2J\033[H", end="")

def menu_sucursal():
    limpiar_pantalla()
    opcion= "X"
    #while opcion < "0" or opcion > "1":
    while opcion not in  ("0", "1", "2", "3"):
        opcion = input(''':
        1. Nueva cuenta
        2. Listado de cuentas
        3. Seleccionar cuenta
        0. Salir
        OPCION: ''')
    return opcion


def menu_cuenta(cuenta:Cuenta):
    limpiar_pantalla()
    opcion= "X"
    print("-" * 20)
    print("Cuenta: ", cuenta.iban)
    print("-" * 20)
    #while opcion < "0" or opcion > "10":
    while opcion not in ("0", "1", "2", "3"):
        opcion = input(''':
        1. Operacion
        2. Consulta
        3. Movimientos
        0. Salir
        OPCION: ''')
    return opcion
