# Corredor 
# Un atleta corre una pista circular de 400m. Diseñe un programa que pregunte 
# los metros recorridos y devuelva el número de vueltas que ha dado y cuantos metros 
# le faltan para finalizar la última vuelta.

LONGITUD_PISTA = 400
print("="*40)
metros_recorridos = int(input("Metros recorrido por el atleta: "))

print("Ha recorrido ", metros_recorridos//LONGITUD_PISTA,"vueltas y ",
      metros_recorridos % LONGITUD_PISTA,"metros")

