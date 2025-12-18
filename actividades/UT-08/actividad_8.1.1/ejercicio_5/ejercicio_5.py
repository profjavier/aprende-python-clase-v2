from producto import Producto

productos = []
for i in range(3):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = float(input("Ingrese el cantidad del producto: "))
    precio_compra = float(input("Ingrese el precio del compra: "))
    producto = Producto(nombre, precio, cantidad, precio_compra)
    productos.append(producto)

ganancia = 0
for producto in productos:
    print(producto.resumen())
    ganancia += producto.ganancia_prevista()

print(f'La ganancia prevista total es: {ganancia}')