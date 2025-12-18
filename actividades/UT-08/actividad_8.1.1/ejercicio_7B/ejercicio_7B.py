from sucursal import Sucursal
from cuenta import Cuenta
from movimiento import Movimiento

sucursal = Sucursal()

cuenta = Cuenta("12", "Pepito Perez", 100)

sucursal.nueva_cuenta(cuenta)


movimiento = Movimiento("Comida de Navidad",
                        Movimiento.INGRESO, 10)
cuenta.nuevo_movimiento(movimiento)

print(cuenta.movimientos)
for movimiento in cuenta.movimientos:
    print(movimiento)

# movimiento.fechas = "sdpiofsh djfiok"
# print(movimiento.__dict__)
# print(movimiento.__slots__)