# CAPÍTULO 5. LISTAS
# Una lista guarda varios elementos y permite modificarlos.

calificaciones = [4.0, 3.5, 4.8, 2.9]

print("Lista:", calificaciones)
print("Primera calificación:", calificaciones[0])
print("Última calificación:", calificaciones[-1])

calificaciones.append(4.2)  # Agrega un elemento al final.
print("Lista actualizada:", calificaciones)

promedio = sum(calificaciones) / len(calificaciones)
print("Promedio:", round(promedio, 2))

# --- Estadísticas rápidas ---
print("Cantidad:", len(calificaciones))
print("Mayor:", max(calificaciones))
print("Menor:", min(calificaciones))

# --- Agregar, insertar y eliminar ---
compras = ["pan", "leche", "huevos"]
compras.insert(1, "queso")     # Inserta en la posición 1
print("\nDespués de insertar:", compras)

compras.remove("leche")        # Elimina por valor
print("Después de remover:", compras)

ultimo = compras.pop()         # Quita y devuelve el último
print("Se quitó:", ultimo, "→", compras)

# --- Modificar un elemento ---
compras[0] = "pan integral"
print("Modificada:", compras)

# --- Ordenar ---
numeros = [8, 3, 10, 1, 6]
print("\nOriginal:", numeros)
print("Ordenada (sin modificar):", sorted(numeros))
numeros.sort(reverse=True)     # Modifica la lista original
print("Orden descendente:", numeros)

# --- Rebanados (slicing) ---
print("\nPrimeros 3:", numeros[:3])
print("Últimos 2:", numeros[-2:])
print("Al revés:", numeros[::-1])

# --- Buscar ---
print("\n¿Está el 10?", 10 in numeros)
print("Posición del 6:", numeros.index(6))
print("Veces que aparece el 3:", numeros.count(3))

# --- Recorrer con for ---
print()
for compra in compras:
    print("- Comprar:", compra)

# --- Comprensión de listas (forma compacta de crear listas) ---
cuadrados = [n ** 2 for n in range(1, 6)]
pares = [n for n in range(1, 11) if n % 2 == 0]
print("\nCuadrados:", cuadrados)
print("Pares:", pares)

# --- Cuidado al copiar ---
a = [1, 2, 3]
b = a            # NO es una copia: ambas apuntan a la misma lista
b.append(4)
print("\na después de modificar b:", a)

c = a.copy()     # Esta sí es una copia independiente
c.append(5)
print("a:", a, "| c:", c)

# EJERCICIO:
# Crea una lista con cinco gastos y calcula el total usando sum().
