

'''
SOLUCION chatgpt
# Pedir al usuario una serie de palabras separadas por comas
entrada = input("Introduce palabras separadas por comas: ")

# Eliminar los espacios y dividir por comas
palabras = [p.strip() for p in entrada.split(",")]

# Mostrar la lista resultante
print("Lista de palabras:", palabras)
'''




print()
print("\033[1;36m*\033[0m"*50)
print(f"============= ELIMINAR ESPACIOS =================")
print()
serie = input("Introduce palabras separadas por comas: ")
print(f"La serie introducida es:  ", serie)
palabras=serie.split(",")  # primero hay que dividir la cadena por comas la serie en palabras. si no se hace primero no funciona eliminar los espacios
print(f"La cadena dividida por comas es:  ", palabras)

for i in range(len(palabras)):
    palabras︃︃︃[i]=palabras[i].strip()

print(f"La serie introducida corregida sin espacios es:   ", palabras_limpias)
print()
print("\033[1;36m*\033[0m"*50)