'''
Ejercicio 3(ejercicio_3.py).
Escribir un programa que cuente el número total de palabras del fichero.
'''

with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_palabras = 0
    for linea in fichero:
        num_palabras += len(linea.split())

print (f"El fichero tiene {num_palabras} palabras")


