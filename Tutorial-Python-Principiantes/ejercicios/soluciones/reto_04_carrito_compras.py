# SOLUCIÓN · RETO 4: CARRITO DE COMPRAS

IVA = 0.19
UMBRAL_DESCUENTO = 200000
DESCUENTO = 0.10

carrito = []
print("=== CARRITO DE COMPRAS (escribe 'fin' para terminar) ===")

while True:
    nombre = input("\nProducto: ").strip()
    if nombre.lower() == "fin":
        break
    try:
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Datos no válidos, intenta de nuevo.")
        continue
    if precio < 0 or cantidad <= 0:
        print("El precio y la cantidad deben ser positivos.")
        continue
    carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

if not carrito:
    print("El carrito está vacío.")
else:
    print(f"\n{'Producto':<15}{'Cant.':>6}{'Precio':>14}{'Subtotal':>14}")
    print("-" * 49)
    total = 0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['nombre']:<15}{item['cantidad']:>6}{item['precio']:>14,.2f}{subtotal:>14,.2f}")
    print("-" * 49)

    descuento = total * DESCUENTO if total > UMBRAL_DESCUENTO else 0
    base = total - descuento
    valor_iva = base * IVA

    print(f"{'Total productos:':<35}{total:>14,.2f}")
    if descuento:
        print(f"{'Descuento (10%):':<35}{-descuento:>14,.2f}")
    print(f"{'IVA (19%):':<35}{valor_iva:>14,.2f}")
    print(f"{'TOTAL A PAGAR:':<35}{base + valor_iva:>14,.2f}")
