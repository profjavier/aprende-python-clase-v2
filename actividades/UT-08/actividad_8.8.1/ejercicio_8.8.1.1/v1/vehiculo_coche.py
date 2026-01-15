class Vehiculo:
    def __init__(self):
        self.marca=None
        self.modelo = None

    def mostrar_info(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}")

    def tipo_vehiculo(self):
        print("Tipo vehiculo")

class Coche(Vehiculo):
    def __init__(self, numero_puertas):
        #Vehiculo.__init__(self)
        super().__init__()
        self.numero_puertas = numero_puertas

    def tipo_vehiculo(self):
        print("Soy un coche")


if __name__ == "__main__":
    vehiculo = Vehiculo()
    vehiculo.marca = "Toyota"
    vehiculo.modelo = "Yaris"
    vehiculo.mostrar_info()

    coche = Coche(5)
    coche.marca = "Toyota"
    coche.modelo = "Yaris"
    coche.mostrar_info()
    coche.tipo_vehiculo()
