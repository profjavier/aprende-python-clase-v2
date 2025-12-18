try:
    numero = int(input("Introduce un numero: "))
    print("Es par" if numero % 2 == 0 else "Es impar")
except:
    print("No ha introducido un numero correcto")
