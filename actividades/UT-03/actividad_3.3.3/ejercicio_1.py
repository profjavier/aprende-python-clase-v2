# Monedas
# Diseñe un programa que, a partir de una cantidad (entera) introducida por teclado,
# indique el número de billetes de 500€, 200€, 100€, 50€, 20€, 10€, 5€ y monedas de 2€ y 1€

cantidad = int(input("Introduce la cantidad: "))
billetes_500= cantidad // 500
resto= cantidad % 500
billetes_200= resto // 200
resto= resto % 200
billetes_100= resto // 100
resto= resto % 100
billetes_50= resto // 50
resto= cantidad % 50
billetes_20= resto // 20
resto= resto % 20
billetes_10= resto // 10
resto= resto % 10
billetes_5= resto // 5
resto= resto % 5
monedas_2= resto // 2
resto= resto % 2
monedas_1= resto // 1

print(billetes_500,"billetes de 500€")
print(billetes_200,"billetes de 200€")
print(billetes_100,"billetes de 100€")
print(billetes_50,"billetes de 50€")
print(billetes_20,"billetes de 20€")
print(billetes_10,"billetes de 10€")
print(billetes_5,"billetes de 5€")
print(monedas_2,"monedas de 2€")
print(monedas_1,"monedas de 1€")

