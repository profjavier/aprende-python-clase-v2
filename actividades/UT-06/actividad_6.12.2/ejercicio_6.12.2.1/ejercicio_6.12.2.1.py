'''
Ejercicio 1 (ejercicio_1.py). Escribir un programa para la gestión de entradas de un concierto. Observaciones:

La información (nº de entrada) se guardará en un fichero de texto con nombre "entradas.txt"
Las entradas siempre tendrán 5 dígitos (Ej. 00001)
Habrá un menú con las siguientes opciones: 1- Añadir entrada; 2- Consulta de entrada; 3-Listado de entradas; 0-Salir
En esta versión se producirá un volcado del archivo a una colección, se trabajará con la colección y se volcará la colección en el fichero en la opción 1.
'''

FILENAME = "entradas.txt"

def menu() -> int:
    print("1- Nueva entrada")
    print("2- Consulta de entrada")
    print("3- Listado de entradas")
    print("0- Salir")
    opcion = ""
    while not opcion in ["1","2","3","0"]:
        opcion = input("Opción: ")
    return int(opcion)

def cargar_fichero()->list:
    try:
        entradas = []
        with open(FILENAME, "r", encoding="utf-8") as f:
            #entradas = f.readlines()

            entradas = [linea.rstrip("\n") for linea in f.readlines()]
    except FileNotFoundError as e:
        f = open(FILENAME, "w", encoding="utf-8")
        f.close()
    except Exception as e:
        print("Se ha producido un error al cargar el fichero: " + e)
    return entradas

def guardar(entrada:str):
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write( entrada+"\n" )

def listar(entradas)->None:
    for entrada  in entradas:
        print(entrada)

def valida_entrada(entrada):
    return entrada.isdigit() and len(entrada) == 5

entradas = cargar_fichero()
print(entradas)

guardar("12122")
entradas.append("12122")
print(entradas)

guardar("43434")
entradas = cargar_fichero()
print(entradas)

listar(entradas)