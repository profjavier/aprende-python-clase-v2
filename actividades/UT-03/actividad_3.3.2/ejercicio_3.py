# Intercambio de valores
# Diseñe un script que guarde en dos variables los valores de a y b,
# y finalmente muestre sus valores después de intercambiarlos usando operadores aritméticos.
# Implementa una solución utilizando una variable auxiliar
# y otra solución sin variable auxiliar.

# Versión con variable auxiliar
a=7
b=3
print ("Valores iniciales")
print("a=",a, "b=",b)

c = a
a = b
b = c
print("Valores  intercambiados")
print("a=",a, "b=",b)

# Versión sin variable auxiliar con operadores
a=7
b=3

a = a + b
b = a - b
a = a - b

print ("Valores iniciales")
print("a=",a, "b=",b)

a, b = b, a
print("Valores  intercambiados")
print("a=",a, "b=",b)