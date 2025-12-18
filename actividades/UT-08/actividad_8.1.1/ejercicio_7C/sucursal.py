from cuenta import Cuenta
class Sucursal:

    def __init__(self):
        self.__cuentas = {}

    def nueva_cuenta(self, cuenta:Cuenta):
        self.__cuentas[cuenta.iban] = cuenta

    @property
    def cuentas(self):
        return self.__cuentas

    ''' 
    El setter no es conveniente ponerlo.
    Si se pone se puede optar por una solución simple o una que verifique la 
    integridad
    '''

    #@cuentas.setter
    #def cuentas(self, cuentas):
    #    self._cuentas = cuentas

    @cuentas.setter
    def cuentas(self, cuentas):
        # Verifica si es una lista
        if not isinstance(cuentas, list):
            raise TypeError("cuentas debe ser una lista")

        # Verifica si todos los elementos son de instancias de la clase Cuenta
        for c in cuentas:
            if not isinstance(c, Cuenta): # o if type(c) is not Cuenta:
                raise TypeError("Todos los elementos deben ser objetos de la clase Cuenta")

        # Realiza la asignacion
        self._cuentas = cuentas


    def __str__(self):
        return "\n\n".join(str(cuenta) for cuenta in self.__cuentas.values())
