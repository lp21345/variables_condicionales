# descuento_tienda.py
# Calcula el precio final de un producto aplicando descuentos

precio = float(input("Ingrese el precio del producto: "))
tarjeta = input("¿Tiene tarjeta de fidelidad? (si/no): ").lower()

descuento = 0

# Condiciones de descuento según el precio
if precio > 100000:
    descuento = 0.15
elif precio >= 50000:
    descuento = 0.10
elif precio >= 10000:
    descuento = 0.05

# Descuento adicional por tarjeta de fidelidad
if tarjeta == "si":
    descuento += 0.05

precio_final = precio - (precio * descuento)

print(f"El precio final con descuentos aplicados es: ${precio_final:,.0f}")
