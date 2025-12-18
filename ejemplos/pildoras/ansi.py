import random
import time
BORRA_LINEA = '\033[2K'
CURSOR_INICIO = '\033[1G'
for i in range(1, 10):
    numero = random.randint(1, 10000)
    #print(numero)
    #print(f"{CURSOR_INICIO}Número aleatorio: {numero}", end='', flush=True)
    print(f"{BORRA_LINEA}{CURSOR_INICIO}Número aleatorio: {numero}", end='', flush=True)
    time.sleep(1)
print("\nFIN DEL PROGRAMA")