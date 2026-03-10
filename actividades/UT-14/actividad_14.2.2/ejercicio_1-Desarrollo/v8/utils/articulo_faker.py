import random


class ArticuloFaker:
    _descripciones = [
        "Martillo",
        "Destornillador plano",
        "Destornillador Phillips",
        "Llave inglesa",
        "Alicates",
        "Pinzas de punta",
        "Sierra manual",
        "Sierra de calar",
        "Taladro eléctrico",
        "Broca para madera",
        "Broca para metal",
        "Cinta métrica",
        "Nivel de burbuja",
        "Escuadra metálica",
        "Lija para madera",
        "Cepillo manual",
        "Cuchillo multiusos",
        "Sargentos",
        "Tornillos",
        "Clavos",
        "Tuercas",
        "Arandelas",
        "Cinta aislante",
        "Cinta adhesiva",
        "Tubo de silicona",
        "Sellador de juntas",
        "Pegamento epóxico",
        "Llave de tubo",
        "Llave Allen",
        "Juego de llaves combinadas",
        "Flexómetro",
        "Cortatubos",
        "Soplete",
        "Masilla plástica",
        "Tijeras para metal",
        "Guantes de trabajo",
        "Casco de seguridad",
        "Gafas de protección",
        "Mascarilla",
        "Linterna",
        "Batería recargable",
        "Cable eléctrico",
        "Regleta múltiple",
        "Clavadora",
        "Pistola de silicona",
        "Cepillo de alambre",
        "Escalera plegable",
        "Carretilla",
        "Taladro percutor",
        "Juego de brocas"
    ]
    _observaciones = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
    in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
    nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
    sunt in culpa qui officia deserunt mollit anim id est laborum.
    """

    @staticmethod
    def _generar_referencia():
        return random.randint(10000000, 99999999)

    @staticmethod
    def _generar_precio():
        return round(random.uniform(1.5, 250), 2)

    @staticmethod
    def _generar_stock():
        return round(random.uniform(0, 500), 3)

    @classmethod
    def _generar_descripcion(cls):
        return random.choice(cls._descripciones)

    @classmethod
    def _generar_observaciones(cls, num_palabras=15):
        palabras = cls._observaciones.split()
        return " ".join(random.sample(palabras, num_palabras))

    @classmethod
    def generar(cls):
        return {
            #"referencia": ArticuloFaker._generar_referencia(),
            "referencia": cls._generar_referencia(),
            "descripcion": cls._generar_descripcion(),
            "precio": cls._generar_precio(),
            "stock": cls._generar_stock(),
            "observaciones": cls._generar_observaciones(),
        }

    @classmethod
    def generar_lote(cls, n):
        return [cls.generar() for _ in range(n)]

if __name__ == "__main__":
    # Genera y muestra un artículo aleatorio
    print(ArticuloFaker.generar())