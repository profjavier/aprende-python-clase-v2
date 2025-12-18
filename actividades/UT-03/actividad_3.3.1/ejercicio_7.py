# Área y perímetro de un círculo
# Diseñe un script que guarde en una variable el radio de un círculo
# y finalmente muestre su área y su perímetro.

import math

# SI no queremos utilizar el módulo math podemos definir una constante PI = 3.14156
print("Área y perímetro de un círculo")

radio = int(input("Radio del círculo: "))

area = math.pi * radio ** 2   # No hace falta math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print("Área:", area)
print("perimetro:", perimetro)

