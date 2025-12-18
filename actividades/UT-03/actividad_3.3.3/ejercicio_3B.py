# Calificaciones
# Diseñe un programa que pregunte el nombre de la persona y los nombres y notas
# de 5 asignaturas y finalmente muestre una ficha resumen de estos datos y la media.

materias = []
nombre = input("Nombre del alumno: ")
for n in range(0,5):
    materia = input(f"Materia {n+1}: ")
    nota = input(f"Nota {n+1}: ")
    materias.append( (materia, nota) )

# print(materias)

print(f"Alumno: {nombre}")
for materia in materias:
    print(f"Materia: {materia[0]}   Nota: {materia[1]}")

