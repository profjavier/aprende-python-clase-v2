'''
Ejercicio 1. (ejercicio_1.py).
Escriba un programa que lea un fichero de texto y muestre su contenido línea por línea.
'''

'''
LECTURA DE TODO EL FICHERO
'''
# with open("fichero.txt", "r") as f:
#     print(f.read())


'''
LECTURA DEL FICHERO POR BLOQUES
'''
with open("fichero.txt", "r", encoding="utf-8") as f:

    datos = "X"
    acumulado = ""
    while datos:
        datos = f.read(20)
        acumulado +=datos
    print(acumulado)

'''
LECTURA DEL FICHERO POR BLOQUES
'''
with open("fichero.txt", "r", encoding="utf-8") as f:

    datos = "X"
    while datos:
        datos = f.read(20)
        print(datos, end="")
    print()
