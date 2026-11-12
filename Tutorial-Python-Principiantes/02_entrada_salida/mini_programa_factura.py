# CAPÍTULO 2. MINI PROGRAMA: FACTURA SIMPLE
# Une entrada de datos, operaciones y formato de salida.

IVA = 0.19   # 19 %

print("=== FACTURA SIMPLE ===")
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))

subtotal = precio * cantidad
valor_iva = subtotal * IVA
total = subtotal + valor_iva

print()
print(f"{'Producto:':<18}{producto}")
print(f"{'Cantidad:':<18}{cantidad}")
print(f"{'Precio unitario:':<18}${precio:,.2f}")
print("-" * 33)
print(f"{'Subtotal:':<18}${subtotal:,.2f}")
print(f"{'IVA (19%):':<18}${valor_iva:,.2f}")
print(f"{'TOTAL:':<18}${total:,.2f}")

# EJERCICIO:
# Agrega una pregunta para el nombre del cliente y muéstralo
# en la parte superior de la factura.
