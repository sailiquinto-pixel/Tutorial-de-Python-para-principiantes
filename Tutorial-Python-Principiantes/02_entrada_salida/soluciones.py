# SOLUCIONES · CAPÍTULO 2: ENTRADA Y SALIDA
# Este archivo pide datos por teclado: respóndelos cuando el programa los pida.

# --- 1. Saludo ---
print("--- Ejercicio 1 ---")
nombre = input("Nombre: ")
print(f"Bienvenida, {nombre}")

# --- 2. Carrera ---
print("\n--- Ejercicio 2 ---")
carrera = input("Carrera: ")
print(f"{nombre} estudia {carrera}.")

# --- 3. Doble ---
print("\n--- Ejercicio 3 ---")
numero = int(input("Escribe un número entero: "))
print("El doble es", numero * 2)

# --- 4. Separadores ---
print("\n--- Ejercicio 4 ---")
print("12", "11", "2026", sep="/")

# --- 5. Edad futura ---
print("\n--- Ejercicio 5 ---")
anio_nacimiento = int(input("Año de nacimiento: "))
print(f"En 2030 tendrás {2030 - anio_nacimiento} años.")

# --- 6. Propina ---
print("\n--- Ejercicio 6 ---")
cuenta = float(input("Valor de la cuenta: "))
propina = cuenta * 0.10
print(f"Cuenta:  ${cuenta:,.2f}")
print(f"Propina: ${propina:,.2f}")
print(f"Total:   ${cuenta + propina:,.2f}")

# --- 7. Conversor de temperatura ---
print("\n--- Ejercicio 7 ---")
celsius = float(input("Grados Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C equivalen a {fahrenheit:.1f}°F")

# --- 8. Tabla ---
print("\n--- Ejercicio 8 ---")
print(f"{'Título':<20}{'Año':>6}{'Nota':>8}")
print("-" * 34)
print(f"{'El Padrino':<20}{1972:>6}{9.2:>8}")
print(f"{'Parásitos':<20}{2019:>6}{8.5:>8}")
print(f"{'Coco':<20}{2017:>6}{8.4:>8}")

# --- 9. Compra con descuento ---
print("\n--- Ejercicio 9 ---")
precio = float(input("Precio del producto: "))
porcentaje = float(input("Porcentaje de descuento (ej. 15): "))
ahorro = precio * porcentaje / 100
print(f"Precio final: ${precio - ahorro:,.2f}")
print(f"Te ahorraste: ${ahorro:,.2f}")

# --- 10. Tarjeta de presentación ---
print("\n--- Ejercicio 10 ---")
nombre_t = input("Nombre: ")
profesion = input("Profesión: ")
correo = input("Correo: ")
ancho = max(len(nombre_t), len(profesion), len(correo)) + 2
print("+" + "-" * ancho + "+")
print(f"| {nombre_t:<{ancho - 2}} |")
print(f"| {profesion:<{ancho - 2}} |")
print(f"| {correo:<{ancho - 2}} |")
print("+" + "-" * ancho + "+")

# --- 11. Reparto ---
print("\n--- Ejercicio 11 ---")
personas = int(input("¿Cuántas personas hay? "))
total = float(input("Valor total de la cuenta: "))
print(f"Cada persona paga ${total / personas:,.2f}")
