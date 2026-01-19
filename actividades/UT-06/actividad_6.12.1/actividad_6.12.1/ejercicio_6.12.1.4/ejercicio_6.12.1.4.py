'''
Ejercicio 4 (ejercicio_4.py).
Escribir un programa que cuente cuantos caracteres tiene el fichero excluyendo \n
'''

with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_caracteres = 0
    for linea in fichero:
        num_caracteres += len(linea)
        if linea[-1] == "\n":
            num_caracteres -= 1

print (f"El fichero tiene {num_caracteres} caracteres")


