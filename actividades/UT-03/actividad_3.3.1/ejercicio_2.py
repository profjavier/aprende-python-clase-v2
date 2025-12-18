# Volumen de un prisma rectangular
# Diseñe un script que calcule las dimensiones de un prisma rectangular.
# Se introducirán los lados en metros y la salida será en cm³.

print("Cálculo del volumen de un prisma rectangular")
print("v = lado1_base x lado2_base * altura")
lado1_base = int(input("Base, lado 1 (m): "))
lado2_base = int(input("Base, lado 2 (m): "))
altura = int(input("Altura (m): "))
volumen_en_cm3 = lado1_base * lado2_base * altura * 1000000

print(f"El volumen de un prisma rectangular de base {lado1_base}m x {lado2_base}m y altura {altura}m es: {volumen_en_cm3}cm3")
