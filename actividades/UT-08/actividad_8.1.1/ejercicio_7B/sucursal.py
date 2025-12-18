class Sucursal:

    def __init__(self):
        self.cuentas = {}

    def nueva_cuenta(self, cuenta):
        self.cuentas[cuenta.iban] = cuenta