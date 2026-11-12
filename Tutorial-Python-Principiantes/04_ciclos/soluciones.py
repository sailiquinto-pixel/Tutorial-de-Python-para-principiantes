# SOLUCIONES · CAPÍTULO 4: CICLOS
# Este archivo pide datos por teclado: respóndelos cuando el programa los pida.

# --- 1. Del 1 al 10 ---
print("--- Ejercicio 1 ---")
for n in range(1, 11):
    print(n, end=" ")
print()

# --- 2. Cuenta regresiva ---
print("\n--- Ejercicio 2 ---")
n = 10
while n >= 1:
    print(n, end=" ")
    n -= 1
print("¡Despegue!")

# --- 3. Pares ---
print("\n--- Ejercicio 3 ---")
for n in range(2, 21, 2):
    print(n, end=" ")
print()

# --- 4. Suma ---
print("\n--- Ejercicio 4 ---")
total = 0
for n in range(1, 101):
    total += n
print("La suma del 1 al 100 es", total)

# --- 5. Tabla de multiplicar ---
print("\n--- Ejercicio 5 ---")
numero = int(input("Número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# --- 6. Promedio de notas ---
print("\n--- Ejercicio 6 ---")
cantidad = int(input("¿Cuántas notas? "))
suma = 0
for i in range(1, cantidad + 1):
    suma += float(input(f"Nota {i}: "))
print("Promedio:", round(suma / cantidad, 2))

# --- 7. Contraseña con intentos ---
print("\n--- Ejercicio 7 ---")
intentos = 0
acceso = False
while intentos < 3:
    clave = input("Clave: ")
    if clave == "python":
        acceso = True
        break
    intentos += 1
    print(f"Incorrecta. Te quedan {3 - intentos} intentos.")
print("Acceso permitido" if acceso else "Cuenta bloqueada")

# --- 8. Mayor y menor ---
print("\n--- Ejercicio 8 ---")
numero = float(input("Número (0 para terminar): "))
if numero == 0:
    print("No ingresaste números.")
else:
    mayor = menor = numero
    while numero != 0:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
        numero = float(input("Número (0 para terminar): "))
    print("Mayor:", mayor, "| Menor:", menor)

# --- 9. Factorial ---
print("\n--- Ejercicio 9 ---")
n = int(input("Número para el factorial: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# --- 10. Fibonacci ---
print("\n--- Ejercicio 10 ---")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()

# --- 11. Adivina el número ---
print("\n--- Ejercicio 11 ---")
secreto = 7
intentos = 0
while True:
    intento = int(input("Adivina el número: "))
    intentos += 1
    if intento == secreto:
        print(f"¡Acertaste en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor.")
    else:
        print("Es menor.")

# --- 12. Pirámide invertida ---
print("\n--- Ejercicio 12 ---")
altura = 5
for fila in range(altura, 0, -1):
    print(" " * (altura - fila) + "*" * (2 * fila - 1))
