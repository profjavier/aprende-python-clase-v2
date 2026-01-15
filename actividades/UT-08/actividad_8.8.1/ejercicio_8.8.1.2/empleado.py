class Empleado:
    def __init__(self, nombre, salario):
        self.nombre=nombre
        self.salario = salario


if __name__ == "__main__":
    empleado = Empleado("Pepito Pérez", "2000")
    print (empleado.nombre)
