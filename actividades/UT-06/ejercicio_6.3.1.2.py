'''
Ejercicio 2 (ejercicio_2.py). Escribir un programa que utilice una
función circular(*nombres) que muestre una carta circular.
'''

# def circular(*args : list) -> None:
#     for item in args:
#         carta = f'''
#         Hola {item}.
#             ,.......
#         '''
#         print (carta)


# def circular(*args: list) -> None:
#     carta = '''Hola {}.
#             .....
#             '''
#     for item in args:
#         print(carta.format(item))

def circular(*args: list) -> None:
    carta = '''Hola {nombre}.
            .....
            '''
    for item in args:
        print(carta.format(nombre=item))


circular("Pepito", "Luisita")