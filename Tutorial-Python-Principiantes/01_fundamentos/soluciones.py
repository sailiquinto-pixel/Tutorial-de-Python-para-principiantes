# SOLUCIONES · CAPÍTULO 1: FUNDAMENTOS
# Intenta resolver los ejercicios por tu cuenta antes de mirar este archivo.
# Recuerda: existen muchas formas correctas de resolver un problema.

# --- 1. Presentación ---
print("--- Ejercicio 1 ---")
nombre = "Laura"
edad = 20
ciudad = "Bogotá"
es_estudiante = True
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("¿Es estudiante?", es_estudiante)

# --- 2. Tipos ---
print("\n--- Ejercicio 2 ---")
print(type("7"), type(7), type(7.0), type(True))

# --- 3. Operaciones ---
print("\n--- Ejercicio 3 ---")
n1 = 12
n2 = 5
print("Suma:", n1 + n2)
print("Resta:", n1 - n2)
print("Multiplicación:", n1 * n2)
print("División:", n1 / n2)

# --- 4. Conversión ---
print("\n--- Ejercicio 4 ---")
precio = "2500"
precio_numero = float(precio)
print("Nuevo precio:", precio_numero + 1000)

# --- 5. Área y perímetro ---
print("\n--- Ejercicio 5 ---")
base = 8
altura = 5
print("Área:", base * altura)
print("Perímetro:", 2 * (base + altura))

# --- 6. Cambio de vuelto ---
print("\n--- Ejercicio 6 ---")
costo = 3750
pago = 5000
print("Te devuelven:", pago - costo)

# --- 7. Par o impar ---
print("\n--- Ejercicio 7 ---")
numero = 14
print("¿Es par?", numero % 2 == 0)

# --- 8. Horas y minutos ---
print("\n--- Ejercicio 8 ---")
total_minutos = 135
horas = total_minutos // 60
minutos = total_minutos % 60
print(horas, "horas y", minutos, "minutos")

# --- 9. Texto ---
print("\n--- Ejercicio 9 ---")
frase = "  python es genial  "
limpia = frase.strip()
print(limpia.upper())
print("Cantidad de letras (con espacios internos):", len(limpia))

# --- 10. Iniciales ---
print("\n--- Ejercicio 10 ---")
nombre = "Laura"
apellido = "Gómez"
print(nombre[0] + "." + apellido[0] + ".")

# --- 11. Promedio ---
print("\n--- Ejercicio 11 ---")
promedio = (4.0 + 3.5 + 4.5) / 3
print("Promedio:", round(promedio, 2))

# --- 12. Intercambio ---
print("\n--- Ejercicio 12 ---")
a = 5
b = 9
a, b = b, a
print("a =", a, "y b =", b)
