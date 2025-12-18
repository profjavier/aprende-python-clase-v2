try:
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))
    if numero1 % numero2 == 0:
        print(f"El numero {numero1} es múltiplo de {numero2}")
    else:
        print(f"El numero {numero1} NO es múltiplo de {numero2}")
except:
    print("No ha introducido núimeros correctos")
