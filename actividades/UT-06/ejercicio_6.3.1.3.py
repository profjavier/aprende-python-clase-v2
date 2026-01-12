'''
Ejercicio 3 (ejercicio_3.py).  Cree una función info_persona(nombre, *args, **kwargs) que imprima:

El nombre
Los args como “otros datos”
Los kwargs como “información extra”
     y muestre una salida similar a:

Nombre: Luis
Otros datos: (25, 'Ingeniero')
Información extra: {'ciudad': 'Madrid', 'país': 'España'}
'''


def info_persona(nombre: str, *args: list, **kwargs: dict) -> None:
    print('Nombre:', nombre)
    print('otros datos:', args)
    print('Informacion extra:', kwargs)


info_persona('Pepito', 25, 'Ingeniero', ciudad='Madrid', país='España')