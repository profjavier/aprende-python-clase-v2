
str = input("Indique la cadena: ")

longitud = len(str)
if longitud > 0:
    print(f"Longitud: {longitud}")
    print(f"Primer carácter: '{str[0]}'")
    print(f"Último carácter: '{str[-1]}'")
    print("1234567890"*8)
    # Solución segun lo estudiado
    inicio = 40 - longitud // 2
    # print(inicio)
    print(f" " * inicio, str, sep="")
    # Solución chatgpt
    print(f"{str.upper().center(80)}")
else:
    print("La cadena está vacía")
