from vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        # Vehiculo.__init__(self,marca, modelo)
        super().__init__(marca, modelo)

    def tipo_vehiculo(self):
        print("Soy un coche")


if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Yaris")
    vehiculo.mostrar_info()

    coche = Coche("Toyota", "Yaris")
    coche.mostrar_info()
    coche.tipo_vehiculo()
