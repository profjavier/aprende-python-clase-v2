'''
Ejercicio 5 (ejercicio_5.py).
Escribir un programa que pida al usuario una palabra y muestra cuántas veces aparece en el fichero.
'''

palabra_buscada = input("Introduce una palabra a buscar: ")
with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_ocurrencias = 0
    for linea in fichero:
        palabras = linea.split()
        for palabra in palabras:
            if palabra.lower() == palabra_buscada.lower():
                num_ocurrencias += 1

print (f"La palabra aparece {num_ocurrencias} veces en el fichero.")

# Utilizando una expresión generdora
'''palabra_buscada = input("Introduce una palabra a buscar: ")
with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_ocurrencias = 0
    for linea in fichero:
        palabras = linea.split()
        num_ocurrencias += sum(1 for palabra in palabras if palabra == palabra_buscada)

print (f"La palabra aparece {num_ocurrencias} veces en el fichero.")'''
