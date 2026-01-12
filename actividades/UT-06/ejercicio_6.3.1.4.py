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

personas = {
    '123': {
        'nif':'123',
        'nombre': 'Pepito1',
        'apellido1': 'Pepito1',
        'apellido2': 'Pepito1'},
    '124': {
        'nif': '124',
        'nombre': 'Pepito2',
        'apellido1': 'Pepito2',
        'apellido2': 'Pepito2'}
}

def update_persona(nif: str, **datos:dict) -> None:
    print (personas.get(nif))
    if personas.get(nif):
        for k, v in datos.items():
            personas[nif][k] = v


update_persona('123', apellido1= 'Pepito111')

print(personas)