# CAPÍTULO 4. CICLO FOR
# Se utiliza para recorrer una secuencia o repetir un bloque
# una cantidad conocida de veces.

for numero in range(1, 6):
    print("Vuelta número:", numero)

# --- Variantes de range() ---
print("\nDel 0 al 4:", list(range(5)))
print("Pares del 2 al 10:", list(range(2, 11, 2)))
print("Cuenta regresiva:", list(range(5, 0, -1)))

# Recorrer una lista:
frutas = ["manzana", "pera", "mango"]
for fruta in frutas:
    print("Fruta:", fruta)

# Recorrer un texto, letra por letra:
for letra in "Python":
    print(letra, end=" ")
print()

# --- enumerate(): posición y valor a la vez ---
for posicion, fruta in enumerate(frutas, start=1):
    print(f"{posicion}. {fruta}")

# --- Acumulador: sumar valores ---
total = 0
for n in range(1, 11):
    total += n
print("Suma del 1 al 10:", total)

# --- Contador: cuántos cumplen una condición ---
pares = 0
for n in range(1, 21):
    if n % 2 == 0:
        pares += 1
print("Pares entre 1 y 20:", pares)

# --- Promedio de una lista ---
notas = [4.0, 3.5, 4.8, 2.9]
suma = 0
for nota in notas:
    suma += nota
print("Promedio:", round(suma / len(notas), 2))

# EJERCICIO:
# Usa range() para mostrar los números del 1 al 10.
