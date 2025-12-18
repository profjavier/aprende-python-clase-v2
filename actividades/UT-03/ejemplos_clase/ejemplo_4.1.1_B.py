'''
Notas de un grupo. Pedir el número de alumnos e ir preguntando las notas.
 - Si el número introducido es negativo se mostrará el mensaje
                "Nota incorrecta" y se desechará la nota.
 - Al finalizar mostrará un mensaje con el número de notas introducidas válidas,
   el número de notas desechadas, el número de aprobados, el de suspensos,
   la media. un mensaje que indique si la media está aprobada (en la misma línea)
   y un mensaje que indique el % de alumnos aprobados

   VARIANTE:
        muestra el mensaje "→ Nota incorrecta" en la misma línea del input
'''

ANSI_AZUL = "\033[34m"
ANSI_VERDE = "\033[32m"
ANSI_ROJO = "\033[31m"
ANSI_RESET = "\033[0m"
ANSI_ARRIBA = "\033[F"
ANSI_COLUMNA_40 = "\033[40C"


num_notas_validadas = 0
media = 0
num_aprobados = 0

num_alumnos = int(input(f"{ANSI_AZUL}Numero de alumnos del grupo:{ANSI_RESET} "))
for i in range(num_alumnos):
    print (f"{ANSI_AZUL}Nota del alumno {i+1}:{ANSI_RESET} ", end="")
    nota = int(input())
    if nota < 0:
        print(f"{ANSI_ARRIBA}{ANSI_COLUMNA_40}{ANSI_ROJO}→ Nota incorrecta{ANSI_RESET}")
    else:
        num_notas_validadas += 1
        media += nota
        if nota >= 5:
            num_aprobados += 1

if (num_notas_validadas > 0):
    nota_media = media / num_notas_validadas
    porcentaje_aprobados = num_aprobados / num_notas_validadas * 100

    # print(f"{ANSI_VERDE}={ANSI_RESET}" * 50)
    print(f"{ANSI_VERDE}",
          "="*50,
          f"{ANSI_RESET}")
    print(f"{ANSI_AZUL}Notas introducidas válidas:{ANSI_RESET} ", num_notas_validadas)
    print(f"{ANSI_AZUL}Notas introducidas desechadas:{ANSI_RESET} ", num_alumnos-num_notas_validadas)
    print(f"{ANSI_AZUL}Número de aprobados:{ANSI_RESET} ", num_aprobados)
    print(f"{ANSI_AZUL}Número de suspensos:{ANSI_RESET} ", num_notas_validadas-num_aprobados)

    # devuelve "MEDIA APROBADA" si la nota media es >=5, y si no devuelve "MEDIA NO APROBADA"

    print(f"{ANSI_AZUL}Media del grupo:{ANSI_RESET} ", nota_media,
          f"{ANSI_VERDE}MEDIA APROBADA{ANSI_RESET}" if nota_media >= 5 else "")
    print(f"{ANSI_AZUL}% de aprobados:{ANSI_RESET}", porcentaje_aprobados)
else:
    print(f"{ANSI_ROJO}No se ha introducido ninguna nota válida{ANSI_RESET}")
