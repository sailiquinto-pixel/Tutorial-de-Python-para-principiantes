# CAPÍTULO 1. OPERADORES
a = 10
b = 3

# --- Aritméticos ---
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Residuo:", a % b)
print("Potencia:", a ** b)

# --- Precedencia: paréntesis primero, luego **, luego * / // %, luego + - ---
print("2 + 3 * 4 =", 2 + 3 * 4)        # 14
print("(2 + 3) * 4 =", (2 + 3) * 4)    # 20
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)    # 512 (la potencia se agrupa de derecha a izquierda)

# --- Usos prácticos del residuo (%) ---
numero = 14
print("¿Es par?", numero % 2 == 0)
print("Sobrante de repartir 14 galletas entre 4 personas:", 14 % 4)

# --- Operadores de asignación abreviados ---
puntos = 10
puntos += 5     # igual a: puntos = puntos + 5
puntos -= 2     # igual a: puntos = puntos - 2
puntos *= 3     # igual a: puntos = puntos * 3
print("Puntos:", puntos)

# --- Redondeo y utilidades numéricas ---
print(round(10 / 3, 2))    # 3.33
print(abs(-7))             # 7 (valor absoluto)
print(divmod(17, 5))       # (3, 2): cociente y residuo juntos
print(max(4, 9, 2), min(4, 9, 2))

# --- Comparaciones: el resultado es True o False ---
print("¿a es mayor que b?", a > b)
print("¿Son iguales?", a == b)
print("¿Son distintos?", a != b)
print("¿a es menor o igual que 10?", a <= 10)

# --- Operadores lógicos: and, or, not ---
print("¿a es mayor que 5 y b menor que 5?", a > 5 and b < 5)
print("¿a es menor que 5 o b menor que 5?", a < 5 or b < 5)
print("¿a NO es igual a b?", not a == b)

# --- Cuidado con los decimales ---
# Los computadores guardan los decimales de forma aproximada:
print(0.1 + 0.2)              # 0.30000000000000004
print(round(0.1 + 0.2, 2))    # 0.3

# EJERCICIO:
# Guarda dos números y muestra su suma, resta y multiplicación.
