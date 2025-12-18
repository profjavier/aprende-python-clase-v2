# Conversión de temperatura
# Diseñe un script que guarde en una variable una temperatura en grados Celsius
# y finalmente muestre su equivalente en grados Fahrenheit.

print("Conversión de temperatura")

temperatura_celsius = float(input("Introduzca la temperatura (en celsius): "))
temperatura_farenheit = temperatura_celsius * 9 / 5 + 32

print(f"{temperatura_celsius} grados celsius equivalen a {temperatura_farenheit} grados fahrenheit")
