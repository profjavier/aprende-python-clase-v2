from menus import menu_sucursal, menu_cuenta, limpiar_pantalla, pulsa_continuar
from sucursal import Sucursal
from cuenta import Cuenta
from movimiento import Movimiento, TipoMovimiento

'''CREAR MENU SUCURSAL
CREAR MENU CUENTA

CREAR FUNCIONES

BUCLE SUCURSAL
    LEER OPCION (AÑADIR CUENTA, LISTAR CUENTAS, SALIR)
    BUCLE CUENTA 
        LEER OPCION (NUEVO MOVIMIENTO, CONSULTA, LISTADO MOVIMIENTOS, SALIR)'''

# FUNCIONES OPERATIVAS

def nueva_cuenta(sucursal:Sucursal):
    iban = input("IBAN: ")
    titular = input("Titular: ")
    ingreso = float(input("Ingreso: "))

    try:
        cuenta = Cuenta(iban=iban, titular_principal=titular, ingreso=ingreso)
        sucursal.nueva_cuenta(cuenta)
        print("Cuenta añadida.")
        pulsa_continuar()

    except Exception as e:
        print("-" * 50)
        print(e)
        print("-" * 50)

def listado_cuentas(sucursal:Sucursal):
    for iban, cuenta in sucursal.cuentas.items():
        print("IBAN: ", iban,"\tTitular 1: ", cuenta.titulares[0])

    pulsa_continuar()

def seleccion_cuenta(sucursal:Sucursal) -> Cuenta:
    iban = input("IBAN: ")
    cuenta = sucursal.obtener_cuenta(iban)
    return cuenta

# OPCIONES DE CUENTA

def cuenta_operacion(cuenta:Cuenta):
    tipo_int = int(input("Tipo: Reintegro(1), Ingreso(2), transferencia(3): "))
    concepto = input("Concepto: ")
    cantidad = abs(float(input("Cantidad: ")))
    try:
        tipo = TipoMovimiento(tipo_int)
        if tipo == TipoMovimiento.REINTEGRO:
            cantidad = -cantidad
        movimiento = Movimiento(concepto=concepto,
                                cantidad=cantidad,
                                tipo=tipo)
        cuenta.nuevo_movimiento(movimiento)
        ver_movimiento(movimiento)
        pulsa_continuar()

    except ValueError:
        print("Tipo de movimiento inválido")
    pulsa_continuar()

def cuenta_movimientos  (cuenta:Cuenta):
    for movimiento in cuenta.movimientos:
        print(movimiento)
    pulsa_continuar()

def ver_movimiento(movimiento:Movimiento):
    print("Movimiento: ")
    print("\tConcepto: ", movimiento.concepto)
    print("\tTipo: ", movimiento.tipo)
    print("\tCantidad: ", movimiento.cantidad)
    print("\tFecha: ", movimiento.fecha)
    print("\tSaldo: ", movimiento.saldo)


# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    sucursal = Sucursal()

    opcion_sucursal = menu_sucursal()
    while opcion_sucursal != "0":
        match opcion_sucursal:
            case "1": nueva_cuenta(sucursal)
            case "2": listado_cuentas(sucursal)
            case "3":                           # Menu de cuenta
                cuenta = seleccion_cuenta(sucursal)
                opcion_cuenta = menu_cuenta(cuenta)
                while opcion_cuenta != "0":
                    match opcion_cuenta:
                        case "1":
                            cuenta_operacion(cuenta)
                        case "3":
                            cuenta_movimientos(cuenta)
                    opcion_cuenta = menu_cuenta(cuenta)
        opcion_sucursal = menu_sucursal()