'''
Ejercicio 2 (ejercicio_2.py).
Escribir un programa que cuente cuantas líneas tiene un fichero de texto.
'''

with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_lineas = 0
    for _ in fichero:
        num_lineas += 1

print (f"El fichero tiene {num_lineas} lineas")


with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_lineas = 0
    c = fichero.read(1)
    while c:
        if c == "\n":
            num_lineas += 1
        c = fichero.read(1)
print (f"El fichero tiene {num_lineas} lineas")