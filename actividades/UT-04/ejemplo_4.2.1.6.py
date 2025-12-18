x = int(input("Dime un ancho: "))
y = int(input("Dime un alto: "))

linea = "*" * x

for i in range(y):
    print(linea)

# SOL 2
for i in range(y):
    for j in range(x):
        print("*", end="")
    print()
