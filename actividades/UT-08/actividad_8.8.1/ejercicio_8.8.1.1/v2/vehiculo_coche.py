class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}")

    def tipo_vehiculo(self):
        print("Tipo vehiculo")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        #Vehiculo.__init__(self,marca, modelo)
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    def tipo_vehiculo(self):
        print("Soy un coche")


if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Yaris")
    vehiculo.mostrar_info()

    coche = Coche("Toyota", "Yaris",5)
    coche.mostrar_info()
    coche.tipo_vehiculo()
