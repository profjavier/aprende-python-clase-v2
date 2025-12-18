# Notas de un estudiante
# Diseñe un script que declare una lista con cinco calificaciones de un
# estudiante y una variable booleana que indique si aprobó, y
# finalmente muestre las notas y lo indicado en la variable booleana.

nota1 = int( input("Introduzca la nota 1:") )
nota2 = int( input("Introduzca la nota 2:") )
nota3 = int( input("Introduzca la nota 3:") )
nota4 = int( input("Introduzca la nota 4:") )
nota5 = int( input("Introduzca la nota 5:") )
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

#if media >= 5:
#    aprobado = True
#else:
#    aprobado = False

aprobado = media >= 5

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Nota 4:", nota4)
print("Nota 5:", nota5)
print("Media:", media)
print("Aprobado:", aprobado)
