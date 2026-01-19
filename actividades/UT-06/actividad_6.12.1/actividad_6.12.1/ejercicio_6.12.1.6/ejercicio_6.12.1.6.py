'''
Ejercicio 6 (ejercicio_6.py).
Escribir un programa que copie el contenido de un fichero en otro fichero nuevo.
'''

origen = input("Archivo de origen: ")
destino = input("Archivo de destino: ")

try:
    with open(origen, "r") as origen:
        contenido = origen.read()  # Leemos todo el contenido

    with open(destino, "w") as destino:
        destino.write(contenido)

    print("Archivo copiado")
except Exception as e:
    print(f"Se ha producido un erroral realizar la copia: {e}")

