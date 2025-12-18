import math
import time

from sucursal import Sucursal
from cuenta import Cuenta
from movimiento import Movimiento, TipoMovimiento

from menus import menu_sucursal, menu_cuenta


def nueva_cuenta(sucursal:Sucursal):
    iban = input("IBAN: ")
    titular = input("Titular: ")
    ingreso = float(input("Ingreso: "))
    try:
        cuenta = Cuenta(iban=iban, titular_principal=titular, ingreso=ingreso)
        sucursal.nueva_cuenta(cuenta)
    except Exception as e:
        print("-"*50)
        print(e)
        print("-"*50)

def listado_cuentas(sucursal:Sucursal):
    for iban, cuenta in sucursal.cuentas.items():
        print("IBAN: ", iban,"\tTitular 1: ", cuenta.titulares[0])

def seleccion_cuenta(sucursal:Sucursal) -> Cuenta:
    iban = input("IBAN: ")
    cuenta = sucursal.obtener_cuenta(iban)
    return cuenta

def cuenta_operacion(cuenta:Cuenta):
    concepto = input("Concepto: ")
    cantidad = abs(float(input("Cantidad: ")))
    tipo_int = int(input("Tipo: Ingreso(1), Reintegro(2), transferencia(3): "))
    try:
        tipo = TipoMovimiento(tipo_int)  # convierte entero a Enum
        if tipo == TipoMovimiento.INGRESO or tipo == TipoMovimiento.TRANSFERENCIA:
            cantidad = -cantidad
        movimiento = Movimiento(concepto=concepto, cantidad=cantidad, tipo=tipo)
        cuenta.nuevo_movimiento(movimiento)
    except ValueError:
        print("Tipo de movimiento inválido")

def cuenta_movimientos  (cuenta:Cuenta):
    for movimiento in cuenta.movimientos:
        print(movimiento)

if __name__ == "__main__":
    sucursal = Sucursal()

    opcion_sucursal = menu_sucursal()
    while opcion_sucursal != "0":
        match opcion_sucursal:
            case "1": nueva_cuenta(sucursal)
            case "2": listado_cuentas(sucursal)
            case "3":
                    cuenta = seleccion_cuenta(sucursal)
                    opcion_cuenta = menu_cuenta(cuenta)
                    while opcion_cuenta != "0":
                        match opcion_cuenta:
                            case "1": cuenta_operacion(cuenta)
                            case "3":
                                    cuenta_movimientos(cuenta)

                        opcion_cuenta = menu_cuenta(cuenta)
                    print("CERRANDA OPERATIVIDAD CON CUENTA", cuenta.iban)
        opcion_sucursal = menu_sucursal()

