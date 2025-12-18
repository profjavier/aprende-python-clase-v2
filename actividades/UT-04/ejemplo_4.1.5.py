try:
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))
    if  numero1 > numero2:
        print(f"{numero1} es mayor que {numero2}")
    elif numero1 < numero2 :
        print(f"{numero2} es mayor que {numero1}")
    else:
        print(f"{numero1} y {numero2} son iguales")
except:
    print("No ha introducido núimeros correctos")
