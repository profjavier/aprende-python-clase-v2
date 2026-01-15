class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca} Modelo: {self.modelo}")

    def tipo_vehiculo(self):
        print("Tipo vehiculo")

if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Yaris")
    vehiculo.mostrar_info()

