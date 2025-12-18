# Factura
# Diseñe un programa para realizar la factura de la compra de tres artículos, pedirá los datos correspondientes y visualizará la factura. Los datos que debe tener en cuenta son:  
#
# Nombre y nif de la empresa
# Nombre y nif del cliente/a
# Descuento que se aplicará a los artículos
# Descripción, precio y unidades de cada artículo (para tres artículos)
# El IVA será el 21%

IVA = 0.21
print("="*40)

print("Empresa")
nombre_empresa = input("\tNombre/Razón social: ")
nif_empresa = input("\tNif: ")

print("Cliente")
nombre_cliente= input("\tNombre/Razón social: ")
nif_cliente = input("\tNif: ")
dto_cliente = float(input("\tDescuento (%): "))

print("Articulos")
nombre_articulo1= input("\tArticulo 1: ")
precio_articulo1= float(input("\t\tPrecio: "))
unidades_articulo1= float(input("\t\tUnidades: "))

nombre_articulo2= input("\tArticulo 2: ")
precio_articulo2= float(input("\t\tPrecio: "))
unidades_articulo2= float(input("\t\tUnidades: "))

nombre_articulo3= input("\tArticulo 3: ")
precio_articulo3= float(input("\t\tPrecio: "))
unidades_articulo3= float(input("\t\tUnidades: "))



print("="*40)
print("\n\n")
print("="*15,"FACTURA","="*15)

print("EMPRESA")
print("\tNombre/Razón social: ",nombre_empresa,"\t\t","Nif: ",nif_empresa)
print()

print("CLIENTE")
print("\tNombre/Razón social: ",nombre_cliente)
print("\tNif: ",nif_cliente)
print()

print("DETALLE")

print("\tArticulo", nombre_articulo1)
print("\t\tPrecio", precio_articulo1)
print("\t\tUnidades", unidades_articulo1)
print("\t\tTotal", precio_articulo1*unidades_articulo1)
print("\t\tTotal con dto", precio_articulo1*unidades_articulo1*(1-dto_cliente/100))

print("\tArticulo", nombre_articulo2)
print("\t\tPrecio", precio_articulo2)
print("\t\tUnidades", unidades_articulo2)
print("\t\tTotal", precio_articulo2*unidades_articulo2)
print("\t\tTotal con dto", precio_articulo2*unidades_articulo2*(1-dto_cliente/100))

print("\tArticulo", nombre_articulo3)
print("\t\tPrecio", precio_articulo3)
print("\t\tUnidades", unidades_articulo3)
print("\t\tTotal", precio_articulo3*unidades_articulo3)
print("\t\tTotal con dto", precio_articulo3*unidades_articulo3*(1-dto_cliente/100))

base_imponible = (  precio_articulo1*unidades_articulo1 +
                    precio_articulo2*unidades_articulo2 +
                    precio_articulo3*unidades_articulo3)*(1-dto_cliente/100)
iva_a_pagar =  base_imponible * IVA

print("RESUMEN")
print("\tBase imponible: ", base_imponible)
print("\tIVA (",IVA*100,"): ", iva_a_pagar)
print("\tTotal: ", base_imponible+iva_a_pagar)

print("="*50)