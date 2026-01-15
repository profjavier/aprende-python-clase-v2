from empleado  import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

if __name__ == "__main__":
    gerente = Gerente("Pepito Pérez", 3000,"IFC")

    print(gerente.nombre)
    print(gerente.salario)
    print(gerente.departamento)