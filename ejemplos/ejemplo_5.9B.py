class MiClase:
    def __init__(self, items):
        self.lista = items

    def __iter__(self):
        return iter(self.lista)


miobjeto = MiClase([5, 4, 3])
iterador = iter(miobjeto)

print(next(iterador))
print(next(iterador))

print("-----------")
for item in miobjeto:
    print(item)