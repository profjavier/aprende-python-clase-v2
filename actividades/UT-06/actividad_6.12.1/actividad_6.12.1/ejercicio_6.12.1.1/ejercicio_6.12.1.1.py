'''
Ejercicio 1. (ejercicio_1.py).
Escriba un programa que lea un fichero de texto y muestre su contenido línea por línea.
'''

fichero = open("fichero.txt", "r", encoding="utf-8")


# SALIDA SIN ELIMINAR SALTO DE LINEA
'''
 for linea in fichero:
     print(linea)
'''

# SALIDA ELIMINANDO EL SALTO DE LINEA
for linea in fichero:
    print(linea.strip())

fichero.close()
