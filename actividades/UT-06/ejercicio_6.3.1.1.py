'''
Ejercicio 1 (ejercicio_1.py). Escriba un programa que utilice la función sumar (*args) que reciba
cualquier cantidad de números y devuelva la suma.
'''

def sumar(*args : list) -> float:
    suma = 0
    for item in args:
        suma += item
    return suma

print ( sumar(1, 3, 5, 8) )