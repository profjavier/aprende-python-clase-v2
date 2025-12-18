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

    if [anio1, mes1, dia1] > [anio2, mes2, dia2]:
        print("El fecha 1 es mayor a la fecha 2")
    elif [anio1, mes1, dia1] < [anio2, mes2, dia2]:
       print("El fecha 2 es mayor a la fecha 2")
    else:
        print("las fechas son iguales")
else:
    print("Formato de fechas incorrecto")

