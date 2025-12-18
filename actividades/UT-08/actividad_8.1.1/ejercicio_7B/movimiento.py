#import datetime as d
from datetime import datetime

class Movimiento:
    REGINTEGRO = 1
    INGRESO = 2
    TRANSFERENCIA = 3
    # __slots__ = ("tipo", "concepto","cantidad","saldo","fecha")

    def __init__(self, concepto, tipo, cantidad, saldo=0):
        if not tipo in [Movimiento.REGINTEGRO,
                        Movimiento.INGRESO,
                        Movimiento.TRANSFERENCIA]:
            raise ValueError("Tipo de movimiento invalido")

        self.tipo = tipo
        self.concepto = concepto
        self.cantidad = cantidad
        self.saldo = saldo
        self.fecha = datetime.now()

    def __str__(self):
        return (f'{self.concepto} {self.tipo} {self.cantidad} {self.saldo} {self.fecha}')
