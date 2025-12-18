from cuenta import Cuenta
from codigos_ansi import CodigosAnsi as CA

def limpiar_pantalla():
    print("\033[2J\033[H", end="")

def pulsa_continuar():
    # input(f"{CA.BG_RED}Pulse INTRO para continuar...{CA.RESET}")
    input(f"{CA.FG_BRIGHT_GREEN}Pulse INTRO para continuar...{CA.RESET}")



def menu_sucursal()->str:
    opcion= "X"

    while opcion not in  ("0", "1", "2", "3"):
        limpiar_pantalla()
        CA.activa(CA.BG_WHITE)
        CA.activa(CA.FG_BRIGHT_MAGENTA)
        print("****************************")
        print("*  1. Nueva cuenta         *")
        print("*  2. Listado de cuentas   *")
        print("*  3. Seleccionar cuenta   *")
        print("*  0. Salir                *")
        print("****************************")
        # print(f"{CA.RESET}", end="")
        CA.reset()
        CA.activa(CA.FG_CYAN)
        print("OPCION:", end="")
        CA.activa(CA.FG_YELLOW)
        opcion = input()
        CA.reset()
    return opcion

def menu_cuenta(cuenta:Cuenta)->str:
    limpiar_pantalla()
    print("-" * 20)
    print("Cuenta: ", cuenta.iban)
    print("-" * 20)
    opcion= "X"
    while opcion not in  ("0", "1", "2", "3"):
        opcion = input('''
                1. Operación
                2. Consulta
                3. Movimientos
                0. Salir
                OPCION: ''')
    return opcion