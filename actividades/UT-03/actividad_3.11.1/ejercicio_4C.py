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

