from movimiento import Movimiento

class Cuenta:
    def __init__(self, iban, titular_principal, ingreso):
        self.iban = iban
        self.titulares = [ titular_principal ]
        # self.movimientos = []

        movimiento = Movimiento(
            concepto=f'Creación de cuenta - {titular_principal}',
            tipo = Movimiento.INGRESO,
            cantidad = ingreso,
        )
        # self.movimientos.append(movimiento)
        self.movimientos = [movimiento]

    def nuevo_titular(self, titular):
        self.titulares.append(titular)

    def nuevo_movimiento(self, movimiento):
        movimiento.saldo = self.movimientos[-1].saldo + movimiento.cantidad
        self.movimientos.append(movimiento)
