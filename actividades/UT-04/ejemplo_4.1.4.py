try:
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))
    if  numero2 != 0:
        print(f"{numero1}/{numero2}={numero1/numero2}")
    else:
        print(f"Error: No se puede dividir entre cero")
except:
    print("No ha introducido números correctos")
