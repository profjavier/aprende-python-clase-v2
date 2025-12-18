# División de cuentas
# Diseñe un script que guarde en variables el total de una cuenta en un restaurante
# y el número de personas, y finalmente muestre cuánto debe pagar cada persona.
total_factura = 275
numero_comensales =27
pago_por_comensal = total_factura / numero_comensales
pago_por_comensal_real = round(pago_por_comensal)
print("Cuantía de la factura:", total_factura)
print ("Número de comansales:", numero_comensales)
print("A pagar por comansal",pago_por_comensal)
print("A pagar por comensal",pago_por_comensal_real)

print("Factura:", total_factura,"Pagado:",pago_por_comensal_real*numero_comensales)
