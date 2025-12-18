# Media de notas
# Diseñe un script que lea las calificaciones de cinco asignaturas y
# finalmente muestre la media de todas ellas.

suma_notas = 0
for i in range(5):
    nota = int(input(f"Asignatura {i+1}: "))
    suma_notas += nota

print("Media:", suma_notas/5)
