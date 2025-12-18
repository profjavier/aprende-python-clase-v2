fecha1 = input("Fecha 1ª (dia/mes/año): ")
fecha2 = input("fecha 2ª (dia/mes/año): ")

lista_fecha1 = fecha1.split("/")
lista_fecha2 = fecha2.split("/")

if (len(lista_fecha1)==3 and len(lista_fecha2)==3):
    dia1, mes1, anio1 = lista_fecha1
    dia2, mes2, anio2 = lista_fecha2

    dia1, mes1, anio1 = int(dia1), int(mes1), int(anio1)
    dia2, mes2, anio2 = int(dia2), int(mes2), int(anio2)
    # dia1, mes1, anio1 = [int(x) for x in lista_fecha1]
    # dia2, mes2, anio2 = [int(x) for x in lista_fecha2]

    if (anio1 > anio2):
        print("El fecha 1 es mayor a la fecha 2")
    elif (anio1 < anio2):
        print("El fecha 2 es mayor a la fecha 1")
    elif (mes1 > mes2):
        print("El fecha 1 es mayor a la fecha 2")
    elif (mes1 < mes2):
        print("El fecha 2 es mayor a la fecha 1")
    elif (dia1 > dia2):
        print("El fecha 1 es mayor a la fecha 2")
    elif (dia1 < dia2):
        print("El fecha 2 es mayor a la fecha 2")
    else:
        print("las fechas son iguales")
else:
    print("Formato de fechas incorrecto")


# Otra solucion
'''
fecha1 = input("Fecha 1ª (dia/mes/año): ")
fecha2 = input("fecha 2ª (dia/mes/año): ")

lista_fecha1 = fecha1.split("/")
lista_fecha2 = fecha2.split("/")

if (len(lista_fecha1)==3 and len(lista_fecha2)==3):
    dia1, mes1, anio1 = lista_fecha1
    dia2, mes2, anio2 = lista_fecha2

    # dia1, mes1, anio1 = int(dia1), int(mes1), int(anio1)
    # dia2, mes2, anio2 = int(dia2), int(mes2), int(anio2)
    dia1, mes1, anio1 = [int(x) for x in lista_fecha1]
    dia2, mes2, anio2 = [int(x) for x in lista_fecha2]

    if [anio1, mes1, dia1] > [anio2, mes2, dia2]:
        print("El fecha 1 es mayor a la fecha 2")
    elif [anio1, mes1, dia1] < [anio2, mes2, dia2]:
       print("El fecha 2 es mayor a la fecha 2")
    else:
        print("las fechas son iguales")
else:
    print("Formato de fechas incorrecto")
'''

# Otra solucion
'''
fecha1 = input("Fecha 1ª (dia/mes/año): ")
fecha2 = input("fecha 2ª (dia/mes/año): ")

lista_fecha1 = fecha1.split("/")
lista_fecha2 = fecha2.split("/")

if (len(lista_fecha1)==3 and len(lista_fecha2)==3):
    dia1, mes1, anio1 = [int(lista_fecha1[2]), int(lista_fecha1[1]), int(lista_fecha1[0])]
    dia2, mes2, anio2 = [int(lista_fecha2[2]), int(lista_fecha2[1]), int(lista_fecha2[0])]

    if [anio1, mes1, dia1] > [anio2, mes2, dia2]:
        print("El fecha 1 es mayor a la fecha 2")
    elif [anio1, mes1, dia1] < [anio2, mes2, dia2]:
       print("El fecha 2 es mayor a la fecha 2")
    else:
        print("las fechas son iguales")
else:
    print("Formato de fechas incorrecto")
'''

# Otra solucion
'''
fecha1 = input("Fecha 1ª (dia/mes/año): ")
fecha2 = input("fecha 2ª (dia/mes/año): ")

lista_fecha1 = fecha1.split("/")
lista_fecha2 = fecha2.split("/")

if (len(lista_fecha1)==3 and len(lista_fecha2)==3):
    fecha_numerica1 = int(lista_fecha1[2]) * 10000 + int(lista_fecha1[1]) * 100 + int(lista_fecha1[0])
    fecha_numerica2 = int(lista_fecha2[2]) * 10000 + int(lista_fecha2[1]) * 100 + int(lista_fecha2[0])


    if fecha_numerica1  > fecha_numerica2:
        print("El fecha 1 es mayor a la fecha 2")
    elif fecha_numerica1  < fecha_numerica2:
       print("El fecha 2 es mayor a la fecha 2")
    else:
        print("las fechas son iguales")
else:
    print("Formato de fechas incorrecto")
'''

'''
SOLUCION CHATGPT
'''
from datetime import datetime

fecha1 = input("Fecha 1ª (dia/mes/año): ")
fecha2 = input("fecha 2ª (dia/mes/año): ")

fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")

if fecha1 < fecha2:
    print("La fecha menor es:", fecha1)
elif fecha2 < fecha1:
    print("La fecha menor es:", fecha2)
else:
    print("Ambas fechas son iguales.")

