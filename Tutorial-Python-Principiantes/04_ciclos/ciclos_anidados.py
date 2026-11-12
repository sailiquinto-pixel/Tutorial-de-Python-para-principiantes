# CAPÍTULO 4. CICLOS ANIDADOS
# Un ciclo dentro de otro: por cada vuelta del externo,
# el interno se ejecuta completo.

# --- Tabla de multiplicar de un número ---
numero = 7
print(f"Tabla del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i:>2} = {numero * i:>3}")

# --- Tablas del 1 al 5 en forma de cuadrícula ---
print("\nTabla de multiplicar (1 a 5):")
for fila in range(1, 6):
    for columna in range(1, 6):
        print(f"{fila * columna:>4}", end="")
    print()   # Salto de línea al terminar cada fila

# --- Figuras con asteriscos ---
print("\nTriángulo:")
for fila in range(1, 6):
    print("*" * fila)

print("\nTriángulo con ciclo anidado:")
for fila in range(1, 6):
    for _ in range(fila):
        print("*", end="")
    print()

print("\nPirámide:")
altura = 5
for fila in range(1, altura + 1):
    espacios = " " * (altura - fila)
    estrellas = "*" * (2 * fila - 1)
    print(espacios + estrellas)

# --- Combinaciones ---
print("\nCombinaciones de camisa y pantalón:")
camisas = ["blanca", "azul"]
pantalones = ["negro", "gris", "beige"]
for camisa in camisas:
    for pantalon in pantalones:
        print(f"Camisa {camisa} con pantalón {pantalon}")

# EJERCICIO:
# Muestra un rectángulo de 4 filas por 8 columnas hecho con "#".
