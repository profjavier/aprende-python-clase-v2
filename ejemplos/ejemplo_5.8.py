str = "Curso de Especialización" + " de Python"


print('c' in str)       # True
print('C' in str)       # True
print('Python' in str)  # True

for x in str: print(x, end=',')
print()
print('-'*30)           # ------------------------------
print(30*'=')           # ==============================

print(str[0])           # C
print(str[-1])
print(str[len(x)-1])

print(str[9:11])        # Es
print(str[9:24])        # Especialización
print(str[9:])          # Especialización de Python
print(str[9:24:2])      # Epcaiain

print(len(str))         # 34
print(min(str))   # Devuelve espacio, que es el de menor código
print(min('aAbB'))      # A

print(str.index('Python'))          # 28
try:
    print(str.index('Python1'))
except ValueError as e:
    print(e)                        # substring not found

print(str.count('a'))       # 2

lista = [1, 5, 7, 0]
print(min(lista))

