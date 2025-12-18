import random


class FakerNombre:
    __nombres = [
        "Sofía",
        "Mateo",
        "Valentina",
        "Santiago",
        "Isabella",
        "Leonardo",
        "Camila",
        "Nicolás",
        "Martina",
        "Daniel",
        "Emma",
        "Sebastián",
        "Lucía",
        "Gabriel",
        "Amelia",
        "Alejandro",
        "Victoria",
        "Samuel",
        "Olivia",
        "Diego"
    ]

    def __init__(self):
        pass

    def __iter__(self):
        random.shuffle(self.__nombres)
        return iter(self.__nombres)
        # nombres_mezclados = self.__nombres.copy()
        # random.shuffle(nombres_mezclados)
        # return iter(nombres_mezclados)



faker = FakerNombre()
iterador = iter(faker)

print(next(iterador))
print(next(iterador))

print("-----------")
for item in faker:
    print(item)
