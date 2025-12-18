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

