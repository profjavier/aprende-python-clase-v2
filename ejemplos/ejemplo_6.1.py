'''
Explicando paso por referencia
Paso de una lista, añadir, devolver, inicializar
'''

x = [10,20,30]
def mueve(entrada,*valor):
    for v in valor:
        entrada.append(v)
    print(entrada)
    lista = []
    for v in entrada:
        lista.append(v)
    entrada.clear()
    return lista
lista = mueve(x,1,2,3)
print(lista)
print(x)


# SOLUCION 2
x = [10,20,30]
def mueve(entrada,*valor):
    lista = entrada.copy()
    entrada.clear()
    for v in valor:
        lista.append(v)
    return lista
lista = mueve(x,1,2,3)
print(lista)
print(x)