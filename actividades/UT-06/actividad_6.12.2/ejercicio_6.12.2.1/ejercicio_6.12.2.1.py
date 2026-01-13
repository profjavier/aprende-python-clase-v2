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

def guardar(entrada:str)->bool:
    try:
        guardado = True
        with open(FILENAME, "a", encoding="utf-8") as f:
            f.write( entrada+"\n" )
    except Exception as e:
        guardado = False
    return guardado


def listar(entradas)->None:
    for entrada  in entradas:
        print(entrada)

# Muestra si existe la entrada y la posición en la que se encuentra
def consulta(entradas:list, entrada:str):
    if not entrada:
        return

    # Solución clasica basada en la posición
    pos = 0
    #while entradas[pos] != entrada and pos < len(entradas): # Error si no encontrado
    while pos < len(entradas) and entradas[pos] != entrada:
        pos += 1
    if pos<len(entradas):
        print("Entrada encontrada en la posición:", pos)
    else:
        print("Entrada no encontrada")

    # Solución clasica basada en la variable encontrado
    '''pos = 0
    encontrado = False
    while not encontrado and pos < len(entradas):
        if entradas[pos] == entrada:
            encontrado = True
        pos += 1
    if pos<len(entradas):
        print("Entrada encontrada en la posición:", pos)
    else:
        print("Entrada no encontrada")'''

    # Solución con uso de for y break
    '''encontrado = False
    for index, e in enumerate(entradas): # enumerate(entradas, start=1):
        if e == entrada:
            encontrado = True
            break
    if encontrado:
        print(f"Entrada encontrada en la posición {index}")
    else:
        print("Entrada no encontrada")'''

    # Opción que no indica la posición
    '''if entrada in entradas:
        print("Entrada encontrada")'''

    # Opción que no indica la posición
    '''if any(entrada == e for e in entradas):
        print("Entrada encontrada")
    else:
        print("Entrada no encontrada")'''

    # Buscamos la primera coincidencia y obtenemos su índice
    '''pos = next((index for index, e in enumerate(entradas) if entrada == e), None)
    if pos is not None:
        print(f"Entrada encontrada en la posición {pos}")
    else:
        print("Entrada no encontrada")'''


def valida_entrada(entrada):
    return entrada.isdigit() and len(entrada) == 5

if __name__ == '__main__':
    entradas = cargar_fichero()

    opcion = ""
    while opcion != 0:
        opcion = menu()
        match opcion:
            case 1:
                entrada = ""
                while not valida_entrada(entrada):
                    entrada = input("Nº entrada: ")
                if guardar(entrada):
                    print("Entrada guardada")
                    # entradas = cargar_fichero()
                    entradas.append(entrada)
                else:
                    print("Entrada no guardada")
            case 2:
                entrada = ""
                while not valida_entrada(entrada):
                    entrada = input("Nº entrada: ")
                consulta(entradas, entrada)
            case 3:
                listar(entradas)


# TESTS
'''
entradas = cargar_fichero()
print(entradas)

guardar("12122")
entradas.append("12122")
print(entradas)

guardar("43434")
entradas = cargar_fichero()
print(entradas)

listar(entradas)

guardar("0001")
guardar("0001")
guardar("0001")
entradas = cargar_fichero()
consulta(entradas, '0001')
'''