
from models.articulo import Articulo
class Articulosdao:

    def __init__(self, filename="articulos.dat"):
        self.filename = filename

    def save(self, articulo: Articulo):
        try:
            with open(self.filename, "a") as f:
                resultado = "|".join(lista)
                for index, linea in enumerate(f_origen, start=1):
                        f_destino.write(f"{index}. {linea}")

            print("Archivo copiado")
        except Exception as e:
            print(f"Se ha producido un erroral realizar la copia: {e}")