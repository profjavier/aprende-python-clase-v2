
try:
    fichero = open('ejemplo.txt', encoding="UTF-8")
    print(fichero.read())
    fichero.close()
except Exception as e:
    print("Se ha producido un error al acceder al fichero: ", e)