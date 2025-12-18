from sucursal import Sucursal
from cuenta import Cuenta
from menus import pulsa_continuar
from codigos_ansi import CodigosAnsi as CA

def _titulo(titulo):
    CA.activa(CA.FG_BRIGHT_BLUE)
    CA.activa(CA.BG_WHITE)
    print('=' * 20, titulo, '=' * 20)
    CA.reset()
    print()

def nueva_cuenta(sucursal:Sucursal):
    _titulo("NUEVA CUENTA")

    # print(f"{CA.texto_color('IBAN: ', CA.FG_GREEN)}", end="")
    CA.print_texto_color('IBAN: ', CA.FG_GREEN)
    iban = input()
    titular = input("Titular: ")
    ingreso = float(input("Ingreso: "))

    try:
        cuenta = Cuenta(iban=iban, titular_principal=titular, ingreso=ingreso)
        sucursal.nueva_cuenta(cuenta)
        CA.print_texto_color('Cuenta añadida.', CA.FG_YELLOW, end="\n")
    except Exception as e:
        print("-" * 50)
        CA.print_texto_color(str(e), CA.FG_RED, end="\n")
        print("-" * 50)
    pulsa_continuar()

def listado_cuentas(sucursal:Sucursal):
    for iban, cuenta in sucursal.cuentas.items():
        print("IBAN: ", iban,"\tTitular 1: ", cuenta.titulares[0])

    pulsa_continuar()

def seleccion_cuenta(sucursal:Sucursal) -> Cuenta:
    iban = input("IBAN: ")
    cuenta = sucursal.obtener_cuenta(iban)
    return cuenta