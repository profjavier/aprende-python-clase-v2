# Colocación de baldosas
# Diseñe un script que guarde en variables las dimensiones de un aula
# (5 m de ancho y 12 m de largo) y finalmente muestre cuántas baldosas de 1m  × 1m son necesarias para cubrir el suelo.

import math

print("Colocación de Baldosas")

ancho = 5
largo = 12
area = ancho * largo
baldosa = 1 * 1

numero_baldosas = area / baldosa # obtenemos el entero superior

print("Para embaldosar el suelo se necesitan",numero_baldosas ,"baldosas")
print("Para embaldosar el suelo se necesitan ",numero_baldosas ," baldosas",sep="")
print("Para embaldosar el suelo se necesitan",numero_baldosas ,"baldosas",sep=":")
