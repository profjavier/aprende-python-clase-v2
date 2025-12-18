"""
Módulo: funciones_asistentes
Autor: Fco. Javier García
Descripción:
    Contiene funciones operativas con la coleccion asistentes
Versión: 1.0
"""

def menu():
    """
    Lee la opción de menu
    Parámetros:
    Retorna:
    string: opcion (1,2,3,0:salir)
    """
    opcion= "X"
    while opcion < "0" or opcion > "3":
        opcion = input(''':
        1. Nueva entrada
        2. Consulta
        3. Listado
        0. Salir
        ''')
    return opcion

def nuevo_asistente(asistentes):
    """
    Lee desde teclado y añade a la coleccion asistentes un nuevo asistente
    Parámetros:
        asistentes: lista de asistentes
    Retorna:
    """
    entrada = input("Ingresa el numero de entrada: ")
    nombre = input("Ingresa el nombre: ")
    dni = input("Ingresa el DNI: ")
    mayor_edad = input("¿Eres mayor de edad?(SI/NO)")
    if mayor_edad == "SI":
        mayor_edad = 1
    else:
        mayor_edad = 0
    asistente = {'entrada': entrada, 'nombre': nombre, 'dni': dni, 'mayor_de_edad': mayor_edad}
    #asistente = (entrada, nombre, dni, mayor_edad)
    asistentes.append(asistente)

def consulta_asistente(asistentes):
    numero_entrada = input("Ingresa el numero de entrada: ")
    for asistente in asistentes:
        if asistente['entrada'] == numero_entrada:
            print("La entrada ha sido utilizada")
            break

def listado_asistentes(asistentes):
    print("Listado de asistentes:")
    for asistente in asistentes:
        # print(asistente['nombre'], "Menor de edad" if asistente['mayor_de_edad'] == 0 else "")
        print(asistente['nombre'], "Menor de edad" if not asistente['mayor_de_edad'] else "")


# asistentes = []
# nuevo_asistente(asistentes)
# listado_asistentes(asistentes)

if __name__ == "__main__":
    # asistentes = []
    # nuevo_asistente(asistentes)
    # listado_asistentes(asistentes)
    help(menu)

