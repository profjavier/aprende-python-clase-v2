from sucursal import Sucursal
from cuenta import Cuenta
from movimiento import Movimiento

sucursal = Sucursal()

cuenta = Cuenta("12", "Pepito Perez", 100)

sucursal.nueva_cuenta(cuenta)


movimiento = Movimiento("Comida de Navidad",
                        Movimiento.INGRESO, 10)
cuenta.nuevo_movimiento(movimiento)

print(cuenta.get_movimientos())
for movimiento in cuenta.get_movimientos():
    print(movimiento)

print("------------")
print(sucursal)