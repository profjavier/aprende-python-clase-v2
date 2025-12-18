from cuenta import Cuenta
class Sucursal:

    def __init__(self):
        self.__cuentas = {}

    def nueva_cuenta(self, cuenta:Cuenta):
        self.__cuentas[cuenta.get_iban()] = cuenta

    def get_cuentas(self):
        return self.__cuentas
    def set_cuentas(self, cuentas):
        self.__cuentas = cuentas

    def __str__(self):
        return "\n\n".join(str(cuenta) for cuenta in self.__cuentas.values())