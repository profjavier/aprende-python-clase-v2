try:
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))
    if numero1 > numero2:
        print(f"El numero {numero1} es mayor que {numero2}")
    elif numero1 < numero2:
        print(f"El numero {numero2} es mayor que {numero1}")
    else:
        print(f"El numero {numero1} es igual que {numero2}")
except:
    print("No ha introducido números correctos")
