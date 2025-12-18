x = int(input("Dime un ancho: "))
y = int(input("Dime un alto: "))

for i in range(y):
    for j in range(x):
        if i==j:
            print("O", end="")
        else:
            print("*", end="")
    print()

print("-----------------")
for i in range(y):
    print("*"*min(i,x), end="")
    print("O" if i<x else "", end="")
    print("*" * max((x-i-1),0), end="")
    print()
