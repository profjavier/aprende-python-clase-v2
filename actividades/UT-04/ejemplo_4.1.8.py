
importe = float(input("Importe de la compra: "))

dto = 0
if importe < 0:
    print("El importe no puede ser negativo")
elif importe < 100:
    dto = 0
elif importe < 500:
    dto = 0.05
elif importe < 1000:
    dto = 0.10
else:
    dto = 0.15

total = importe * (1-dto)   # importe - importe * dto

print("El total de la compra es: " + str(total))