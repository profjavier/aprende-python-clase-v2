'''
Ejercicio 5 (ejercicio_5.py).
Escribir un programa que pida al usuario una palabra y muestra cuántas veces aparece en el fichero.
'''

''' ESTA VERSIÖNB IGNORA LAS TILDES '''

# Diccionario de mapeo: cada vocal con tilde -> vocal sin tilde
mapa_tildes = str.maketrans(
    "áéíóúÁÉÍÓÚ",
    "aeiouAEIOU"
)

palabra_buscada = input("Introduce una palabra a buscar: ")
with open("fichero.txt", "r", encoding="utf-8") as fichero:
    num_ocurrencias = 0
    for linea in fichero:
        palabras = linea.split()
        for palabra in palabras:
            palabra = palabra.translate(mapa_tildes)
            if palabra.lower() == palabra_buscada.lower():
                num_ocurrencias += 1

print (f"La palabra aparece {num_ocurrencias} veces en el fichero.")


