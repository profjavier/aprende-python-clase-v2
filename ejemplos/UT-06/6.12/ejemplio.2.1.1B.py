try:
    fichero = open('ejemplo.txt', encoding="utf-8")
    caracter = fichero.read(1)
    while caracter != "":
        print( caracter, end="")
        caracter = fichero.read(1)
except Exception as e:
    print("Se ha producido un error al acceder al fichero: ", e)