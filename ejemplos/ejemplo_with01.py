'''
SIN WITH
'''
nombre_archivo = __file__
print("Se va a leer el fichero:", nombre_archivo)
f = open(nombre_archivo , "r")
contenido = f.read()
print(contenido)
f.close()