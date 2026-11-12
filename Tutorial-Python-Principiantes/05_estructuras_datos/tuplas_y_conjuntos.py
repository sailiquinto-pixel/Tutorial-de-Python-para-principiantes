# CAPÍTULO 5. TUPLAS Y CONJUNTOS

# ===================== TUPLAS =====================
# Parecidas a las listas, pero NO se pueden modificar.
coordenada = (4.6097, -74.0817)
print("Latitud:", coordenada[0])
print("Longitud:", coordenada[1])

# coordenada[0] = 5   ← Provocaría un TypeError

# Desempaquetado: asignar cada valor a una variable
latitud, longitud = coordenada
print(f"Estoy en ({latitud}, {longitud})")

# Las funciones pueden devolver varias cosas como una tupla
def minimo_y_maximo(numeros):
    return min(numeros), max(numeros)

menor, mayor = minimo_y_maximo([5, 2, 9, 1])
print("Menor:", menor, "| Mayor:", mayor)

# Una tupla de un solo elemento lleva coma al final:
una_sola = (7,)
print(type(una_sola))

# ==================== CONJUNTOS ====================
# No tienen orden ni elementos repetidos.
colores = {"rojo", "azul", "rojo", "verde", "azul"}
print("\nConjunto sin repetidos:", colores)

# Eliminar repetidos de una lista:
edades = [20, 25, 20, 30, 25, 40]
sin_repetir = list(set(edades))
print("Edades únicas:", sorted(sin_repetir))

# Agregar y eliminar
colores.add("amarillo")
colores.discard("rojo")
print("Después de modificar:", colores)

# --- Operaciones entre conjuntos ---
python = {"Ana", "Luis", "Marta", "Pedro"}
datos = {"Marta", "Pedro", "Sofía"}

print("\nEn ambos cursos:", python & datos)          # intersección
print("En alguno de los cursos:", python | datos)    # unión
print("Solo en Python:", python - datos)             # diferencia

# ¿Pertenece?
print("¿Ana está en Python?", "Ana" in python)

# EJERCICIO:
# Dadas dos listas de invitados, muestra quiénes están en ambas
# y quiénes están solo en la primera.
