# Pedido en un restaurante
# Diseñe un script que cree un diccionario con el plato pedido, el precio unitario,
# la cantidad y el total a pagar, y finalmente muestre los datos en forma de ticket.

pedido= {
    "plato": "Croquetas de jamón",
    "precio_unidad": 1.50,
    "cantidad": 6
}
pedido['total'] = pedido['precio_unidad'] * pedido['cantidad']

print("PEDIDO")
print("-"*40)
print("\tPlato: ", pedido['plato'])
print("\tPrecio unidad: ", pedido['precio_unidad'])
print("\tCantidad: ", pedido['cantidad'])
print("\tTotal: ", pedido['total'])
print("-"*40)


