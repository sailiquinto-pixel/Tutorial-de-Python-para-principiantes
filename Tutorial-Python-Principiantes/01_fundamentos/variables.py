# CAPÍTULO 1. VARIABLES
# Una variable es un nombre que usamos para guardar un dato.

nombre = "Laura"       # Texto (str)
edad = 20              # Número entero (int)
estatura = 1.65        # Número decimal (float)
es_estudiante = True   # Booleano (bool)

print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Es estudiante?", es_estudiante)

# --- Una variable puede cambiar de valor ---
edad = 21
print("Edad actualizada:", edad)

# Puedes usar el valor anterior para calcular el nuevo.
edad = edad + 1
print("Edad un año después:", edad)

# --- Reglas de nombres ---
# Buenos nombres: describen qué guardan y usan snake_case.
precio_unitario = 2500
cantidad_productos = 4
total_a_pagar = precio_unitario * cantidad_productos
print("Total a pagar:", total_a_pagar)

# Malos nombres (funcionan, pero son difíciles de entender):
# x = 2500
# y = 4
# z = x * y

# --- Asignación múltiple ---
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Varias variables con el mismo valor:
a = b = c = 0
print("a, b, c =", a, b, c)

# --- Intercambiar valores ---
primero = "A"
segundo = "B"
primero, segundo = segundo, primero
print("Después de intercambiar:", primero, segundo)

# --- Constantes ---
# Python no tiene constantes reales, pero por convención se escriben
# en MAYÚSCULAS para indicar que no deberían cambiar.
IVA = 0.19
print("IVA:", IVA)

# EJERCICIO:
# Cambia los valores anteriores por otros y vuelve a ejecutar el archivo.
# Después crea tres variables (producto, precio, cantidad) y muestra
# el total a pagar.
