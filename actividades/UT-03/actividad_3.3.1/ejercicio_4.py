# Colocación de baldosas
# Diseñe un script que guarde en variables las dimensiones de un aula
# (5 m de ancho y 12 m de largo) y finalmente muestre cuántas baldosas de 30 cm × 60 cmm son necesarias para cubrir el suelo.

import math

print("Colocación de Baldosas")

ancho = 5 * 100   # Trabajaremos en cm
largo = 12 * 100  # Trabajaremos en cm
area = ancho * largo
baldosa = 60 * 60

numero_baldosas = math.ceil(area / baldosa) # obtenemos el entero superior

print("Para embaldosar el suelo se necesitan ",numero_baldosas ,"baldosas")
