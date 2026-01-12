f = open("ejemplo.txt", "r")
for linea in f:
    print(linea.strip())
f.close()
print("-----------")
with open("ejemplo.txt", "r") as f:
    for linea in f:
        print(linea.strip())
print("-----------")
with open("ejemplo.txt", "r", encoding="UTF-8") as f:
    for linea in f:
        print(linea.strip())
print("-----------")
with open("ejemplo.txt", "r", encoding="UTF-8") as f:
    for linea in f:
        print(linea)

# Conn control de excepciones/errores
print("-----------")
try:
    with open("ejemplo.txt", "r", encoding="UTF-8") as f:
        for linea in f:
            print(linea)
except FileNotFoundError as e:
    print("No existe el fichero ejemplo.txt:",e)
except Exception as e:
    print("Se ha producido un error al acceder al fichero: ", e)
