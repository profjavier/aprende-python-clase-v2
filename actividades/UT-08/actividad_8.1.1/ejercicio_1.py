class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.dni = ""

    def saludo(self):
        print(f"Hola  D/Dª {self.nombre}")

    def saludo2(self):
        return f"Hola  D/Dª {self.nombre}"

    def cambia_dni(self, dni):
        self.dni = dni

if __name__ == "__main__":
    persona = Persona("pepito", 22)
    persona.cambia_dni("1234")
    persona.saludo()
    print(persona.saludo2())
    print(persona.dni)
