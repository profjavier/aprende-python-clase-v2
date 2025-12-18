# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"
# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2
# Realizamos unas operaciones con a,b,c
d = (a + b) * c
# Definimos una variable booleana
imprimir = False

print("El valor de a es: ", a)
print("El valor de b es: ", b)
print("El valor de c es: ", c)
print("El valor de d es: ", d)
print("El valor de imprimir es: ", imprimir)

#print("El valor de a es: " + a)
print("El valor " + "de a es: ", a)
print("El valor de a es: " + str(a))
print(a + b)
print(str(a) + str(b))


if 3==3:  # Si son iguales
    print("Son iguales")



# Si imprimir, print()
if imprimir:
    print(x, d)
# Salida: El valor de (a+b)*c es 14

'''
Esto es un comentario
de varias líneas
de código
'''

mensaje = '''
Esto NO es un comentario
de varias líneas
de código
'''
print(mensaje)
print ('''
Esto NO es un comentario
de varias líneas
de código
''')
