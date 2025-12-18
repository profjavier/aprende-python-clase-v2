# SOLUCION CHATGPT

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

