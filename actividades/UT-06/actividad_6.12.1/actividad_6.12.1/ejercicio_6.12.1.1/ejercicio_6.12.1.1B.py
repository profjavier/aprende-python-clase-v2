'''
Ejercicio 1. (ejercicio_1.py).
Escriba un programa que lea un fichero de texto y muestre su contenido línea por línea.
'''

# Uso de la estructura with
'''
# Con bucle FOR
with open("fichero.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
'''

# Con bucle WHILE
'''with open("fichero.txt", "r", encoding="utf-8") as f:
    linea = f.readline()
    while linea:
        print(linea.strip())
        linea = f.readline()'''

# Con bucle WHILE - LECTURA DE CARACTERES
'''with open("fichero.txt", "r", encoding="utf-8") as f:
    caracter = f.readline(1)
    while caracter:
        print(caracter, end="")
        caracter = f.readline(1)'''


# Con bucle WHILE - LECTURA EN COLECCIÓN
with open("fichero.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    for linea in lineas:
        print(linea.strip())
