# import funciones_asistentes
# from funciones_asistentes import nuevo_asistente
import funciones_asistentes as fa

opcion=""
asistentes=[]

while opcion!="0":
    opcion = fa.menu()

    if opcion == "1":
       fa.nuevo_asistente(asistentes)
    elif opcion == "2":
        fa.consulta_asistente(asistentes)
    elif opcion == "3":
        fa.listado_asistentes(asistentes)


print("Has salido del programa")
