'''
Ejercicio 7 (ejercicio_7.py).
Escribir un programa que lea un fichero y guarde en otro archivo solo las líneas
que no estén vacías. Las líneas aparecerán numeradas (1. ..., 2. ...)
'''

origen = input("Archivo de origen: ")
destino = input("Archivo de destino: ")

try:
    with open(origen, "r") as f_origen, open(destino, "w") as f_destino:
        for index, linea in enumerate(f_origen, start=1):
            if linea.strip():
                f_destino.write(f"{index}. {linea}")

    print("Archivo copiado")
except Exception as e:
    print(f"Se ha producido un erroral realizar la copia: {e}")

