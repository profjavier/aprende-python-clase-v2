import random

matriz = [ [ 1, 2, 3, 4 ],
           [ 4, 5, 6, 9 ],
           [ 7, 8, 9, 8 ],
           [ 7, 8, 9, 8 ],
       ]

'''matriz=[]
for i in range (4):
    matriz.append([])
    for j in range (4):
        matriz[i].append( random.randint( 0, 100 ) )

print(matriz)'''

numero = int(input("Ingresa un numero: "))

# pos_x = -1
# pos_y = -1
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] == numero:
#             pos_x = j
#             pos_y = i
#             break
#     if pos_x != -1:
#         break

# posicion = None
#
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] == numero:
#             posicion = (j,i)
#             break
#     if posicion != None:
#         break

def find(valor):
    posicion = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                posicion = (j, i)
                return posicion
    return None

print(find(numero))