class Producto:
    def __init__(self, nombre, precio, cantidad=1, precio_compra=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.precio_compra = precio_compra


    def entrada(self, unidades=1):
        self.cantidad += unidades

    def salida(self, unidades=1):
        stock_final = self.cantidad - unidades
        if stock_final  < 0:
            self.cantidad  = 0
            return unidades - self.cantidad
        else:
            self.cantidad = stock_final
            return unidades

    def ganancia_prevista(self):
        return self.cantidad * self.precio - self.cantidad * self.precio_compra

    def resumen(self):
        return f"{self.nombre} {self.precio} {self.cantidad} {self.precio_compra} {self.ganancia_prevista()}"

if __name__ == "__main__":
    producto = Producto("Monitor", 100, 5)
    producto.precio_compra = 50
    print("Ganancia prevista:", producto.ganancia_prevista())