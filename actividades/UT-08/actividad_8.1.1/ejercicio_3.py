class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.color = None


    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return self.ancho * 2 + self.alto * 2

    def cambia_color(self, color):
        self.color = color

if __name__ == "__main__":
    rectangulo = Rectangulo(20,20)
    print(rectangulo.perimetro())
    print(rectangulo.area())
