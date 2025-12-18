from movimiento import Movimiento

class Cuenta:
    def __init__(self, iban, titular_principal, ingreso):
        self.__iban = iban
        self.__titulares = [ titular_principal ]

        movimiento = Movimiento(
            concepto=f'Creación de cuenta - {titular_principal}',
            tipo = Movimiento.INGRESO,
            cantidad = ingreso,
        )
        self.__movimientos = [movimiento]

    def nuevo_titular(self, titular):
        self.__titulares.append(titular)

    def nuevo_movimiento(self, movimiento):
        movimiento.saldo = self.__movimientos[-1].get_saldo() + movimiento.get_cantidad()
        self.__movimientos.append(movimiento)

    def get_iban(self):
        return self.__iban
    def set_iban(self, iban):
        self.__iban = iban

    def get_titulares(self):
        return self.__titulares
    def set_titulares(self, titulares):
        self.__titulares = titulares

    def get_movimientos(self):
        return self.__movimientos
    def set_movimientos(self, cuentas):
        self.__movimientos = cuentas

    def __str__(self):
        return (f'''
            IBAN: {self.__iban} 
            TITULARES: {self.__titulares} 
            MOVIMIENTOS: {self.__movimientos}''')

    def __str__(self):
        titulares_str = ", ".join(self.__titulares)
        movimientos_str = "\n    ".join(str(m) for m in self.__movimientos)

        return (
            f"Cuenta {self.__iban}\n"
            f"  Titulares: {titulares_str}\n"
            f"  Movimientos:\n    {movimientos_str}"
        )