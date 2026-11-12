# CAPÍTULO 4. BREAK Y CONTINUE

# --- break: termina el ciclo de inmediato ---
print("Buscando el primer múltiplo de 7 mayor que 20:")
for numero in range(21, 100):
    if numero % 7 == 0:
        print("Encontrado:", numero)
        break

# --- continue: salta a la siguiente repetición ---
print("\nNúmeros del 1 al 10 sin los múltiplos de 3:")
for numero in range(1, 11):
    if numero % 3 == 0:
        continue
    print(numero, end=" ")
print()

# --- Buscar un elemento en una lista ---
nombres = ["Ana", "Luis", "Marta", "Pedro"]
buscado = "Marta"
encontrado = False

for posicion, nombre in enumerate(nombres):
    if nombre == buscado:
        encontrado = True
        print(f"\n{buscado} está en la posición {posicion}.")
        break

if not encontrado:
    print(f"\n{buscado} no está en la lista.")

# --- for ... else: el else se ejecuta si el ciclo NO fue interrumpido ---
for numero in range(2, 10):
    if numero == 11:
        break
else:
    print("Nunca se encontró el 11 en el rango.")

# --- ¿Es primo? ---
n = 29
es_primo = n > 1
for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        es_primo = False
        break
print(f"\n¿{n} es primo? {es_primo}")

# EJERCICIO:
# Recorre los números del 1 al 50 y muestra solo los que sean
# divisibles por 5. Detén el ciclo al llegar al 40.
