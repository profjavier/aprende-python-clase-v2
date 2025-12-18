libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))

try:
    print(next(marcapaginas))
except StopIteration:
    print("No hay más elementos")

marcapaginas = iter(libro)

while True:
    try:
        print(next(marcapaginas))
    except StopIteration:
        break