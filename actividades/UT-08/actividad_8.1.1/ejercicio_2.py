import math
import time

class Circulo:

    def __init__(self, radio):
        self.radio = radio
        self.posicion = (0,0)

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def mueve_to(self, posicion):
        self.posicion = posicion

    def colisiona(self, circulo):
        x1, y1 = self.posicion
        x2, y2 = circulo.posicion
        # h**2 = base**2 + altura**2
        return (x2-x1)**2 + (y2-y1)**2 < (self.radio + circulo.radio)**2

if __name__ == "__main__":
    circulo1 = Circulo(5)
    print(circulo1.area())
    print(circulo1.radio)

    circulo2 = Circulo(20)
    print(circulo1.colisiona(circulo2))
    for i in range(60):
        circulo1.mueve_to((i, 0))
        print(circulo1.posicion, circulo2.posicion, "Colisiona" if circulo1.colisiona(circulo2) else "-")
        time.sleep(0.1)