class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def cambia_nombre(self, nombre):
        self.nombre = nombre


if __name__ == '__main__':
    # mi_perro = Perro()
    # print(mi_perro)
    # print(mi_perro.nombre)
    # print(mi_perro.raza)
    # mi_perro.nombre = "Anubis"
    # mi_perro.raza= "Bodeguero"
    # print(mi_perro)
    # print(mi_perro.nombre)
    # print(mi_perro.raza)

    # perro = Perro()
    # perro.cambia_nombre("Lucas")
    # print(perro.nombre)
    # perro.raza = "Bodeguero"

    perro = Perro("Anubis", "Bodeguero")