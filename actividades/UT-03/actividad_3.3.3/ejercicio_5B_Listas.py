# Factura
# Diseñe un programa para realizar la factura de la compra de tres artículos, pedirá los datos correspondientes y visualizará la factura. Los datos que debe tener en cuenta son:  
#
# Nombre y nif de la empresa
# Nombre y nif del cliente/a
# Descuento que se aplicará a los artículos
# Descripción, precio y unidades de cada artículo (para tres artículos)
# El IVA será el 21%

IVA = 0.21

articulos = []
print("="*40)

print("Empresa")
nombre_empresa = input("\tNombre/Razón social: ")
nif_empresa = input("\tNif: ")

print("Cliente")
nombre_cliente= input("\tNombre/Razón social: ")
nif_cliente = input("\tNif: ")
dto_cliente = float(input("\tDescuento (%): "))


print("Articulos")
for i in range(1, 4):
    nombre_articulo= input(f"\tArticulo {i}: ")
    precio_articulo= float(input("\t\tPrecio: "))
    unidades_articulo= float(input("\t\tUnidades: "))
    articulos.append( ( nombre_articulo, precio_articulo, unidades_articulo ) )


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

for articulo in articulos:
    print("\tArticulo", articulo[0])
    print("\t\tPrecio", articulo[1])
    print("\t\tUnidades", articulo[2])
    print("\t\tTotal", articulo[1] * articulo[2])
    print("\t\tTotal con dto", (articulo[1] * articulo[2]) * (1 - dto_cliente / 100))

base_imponible = 0
for articulo in articulos:
    base_imponible += articulo[1] * articulo[2]

base_imponible = base_imponible*(1-dto_cliente/100)
iva_a_pagar =  base_imponible * IVA

print("RESUMEN")
print("\tBase imponible: ", base_imponible)
print("\tIVA (",IVA*100,"): ", iva_a_pagar)
print("\tTotal: ", base_imponible+iva_a_pagar)

print("="*50)