'''
Ejercicio 8 (ejercicio_8.py).
 Escribir un programa que lea un fichero y muestre: el número de líneas,
 el número de palabras, el número de caracteres y cuantas ocurrencias hay de cada carácter.
'''

origen = input("Archivo de origen: ")

try:
    with open(origen, "r") as f_origen:
        numero_lineas = 0
        numero_palabras = 0
        numero_caracteres = 0
        numero_caracteres_sin_espacios = 0
        ocurrencias_caracter = {}
        for linea in f_origen:
            linea = linea.strip()
            numero_lineas += 1
            numero_palabras += len(linea.split())
            numero_caracteres += len(linea)
            #sol 1
            # numero_caracteres_sin_espacios += len(linea.replace(" ", "").replace("\t", ""))
            #sol 2
            numero_caracteres_sin_espacios += len("".join(linea.split()))
            for caracter in linea:
                # ocurrencias_caracter[caracter] = ocurrencias_caracter[caracter] +1
                ocurrencias_caracter[caracter] = ocurrencias_caracter.get(caracter, 0) + 1

    print("Nº de lineas: ", numero_lineas)
    print("Numero de palabras:", numero_palabras)
    print("Numero de caracteres: ", numero_caracteres)
    print("Numero de caracteres reales: ", numero_caracteres_sin_espacios)
    for caracter in ocurrencias_caracter:
        print(caracter, ocurrencias_caracter[caracter])

except Exception as e:
    print(f"Se ha producido un erroral realizar la copia: {e}")

