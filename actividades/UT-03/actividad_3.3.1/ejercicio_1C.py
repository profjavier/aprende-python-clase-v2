# Media de notas
# Diseñe un script que lea las calificaciones de cinco asignaturas y
# finalmente muestre la media de todas ellas.

notas = []
for i in range(5):
    nota = int(input(f"Asignatura {i+1}: "))
    notas.append(nota)

# SOLUCION 1
media = sum(notas)/len(notas)
print(notas)
print("Media:", media)

# SOLUCION 2
media = 0
for i in range(len(notas)):
    media += notas[i]
media = media / len(notas)
print("Media:", media)

# SOLUCION 3
media = 0
for nota in notas:
    media += nota
media = media / len(notas)
print("Media:", media)