
nota = float(input("Nota: "))

#if nota >= 0 and nota < 5:
'''if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")'''

if nota < 0 or nota > 10:
    print("La nota debe estar entre 0 y 10")
elif nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")