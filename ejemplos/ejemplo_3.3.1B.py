# Media de notas
# Diseñe un script que lea las calificaciones de cinco asignaturas y
# finalmente muestre la media de todas ellas.

nota1 = int(input("Asignatura 1: "))
nota2 = int(input("Asignatura 2: "))
nota3 = int(input("Asignatura 3: "))
nota4 = int(input("Asignatura 4: "))
nota5 = int(input("Asignatura 5: "))
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Nota 4:", nota4)
print("Nota 5:", nota5)
print("Media:", media)

# Una versión de implementación sin utilizar una variable para cada asignatura. apta para bucles:

suma_notas = 0
nota = int(input("Asignatura 1: "))
suma_notas += nota
nota = int(input("Asignatura 2: "))
suma_notas += nota
nota = int(input("Asignatura 3: "))
suma_notas += nota
nota = int(input("Asignatura 4: "))
suma_notas += nota
nota = int(input("Asignatura 5: "))
suma_notas += nota
print("Media:", suma_notas/5)

notas = []
notas.append(int(input("Asignatura 1: ")))
notas.append(int(input("Asignatura 2: ")))
notas.append(int(input("Asignatura 3: ")))
notas.append(int(input("Asignatura 4: ")))
notas.append(int(input("Asignatura 5: ")))
print(notas)
print("Media:", sum(notas)/len(notas))