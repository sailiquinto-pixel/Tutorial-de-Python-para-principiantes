# SOLUCIONES · CAPÍTULO 5: ESTRUCTURAS DE DATOS
# Este archivo pide un dato por teclado en el ejercicio 9.

# --- 1. Gastos ---
print("--- Ejercicio 1 ---")
gastos = [25000, 12000, 8500, 40000, 15000]
print("Total de gastos:", sum(gastos))

# --- 2. Primer y último ---
print("\n--- Ejercicio 2 ---")
colores = ["rojo", "verde", "azul", "amarillo"]
print("Primero:", colores[0])
print("Último:", colores[-1])

# --- 3. Producto ---
print("\n--- Ejercicio 3 ---")
producto = {"nombre": "Cuaderno", "precio": 4500, "cantidad": 10}
for clave, valor in producto.items():
    print(clave, ":", valor)

# --- 4. Agregar ---
print("\n--- Ejercicio 4 ---")
frutas = ["manzana", "pera"]
frutas.append("mango")
print(frutas)

# --- 5. Mayor, menor y promedio ---
print("\n--- Ejercicio 5 ---")
numeros = [12, 5, 9, 20, 7]
print("Mayor:", max(numeros))
print("Menor:", min(numeros))
print("Promedio:", sum(numeros) / len(numeros))

# --- 6. Ordenar ---
print("\n--- Ejercicio 6 ---")
original = [8, 3, 10, 1, 6]
descendente = sorted(original, reverse=True)
print("Original:", original)
print("Ordenada:", descendente)

# --- 7. Pares e impares ---
print("\n--- Ejercicio 7 ---")
pares = []
impares = []
for n in range(1, 21):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Pares:", pares)
print("Impares:", impares)

# --- 8. Contar palabras ---
print("\n--- Ejercicio 8 ---")
frase = "el perro y el gato y el loro"
conteo = {}
for palabra in frase.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)

# --- 9. Agenda ---
print("\n--- Ejercicio 9 ---")
agenda = {"Ana": "3001112233", "Luis": "3104445566", "Marta": "3207778899"}
buscado = input("¿A quién buscas? ")
print(agenda.get(buscado, "No encontrado"))

# --- 10. Inventario ---
print("\n--- Ejercicio 10 ---")
inventario = [
    {"nombre": "Lápiz", "precio": 800, "cantidad": 50},
    {"nombre": "Cuaderno", "precio": 4500, "cantidad": 20},
    {"nombre": "Borrador", "precio": 600, "cantidad": 30},
]
valor_total = 0
for item in inventario:
    valor_total += item["precio"] * item["cantidad"]
print(f"Valor total del inventario: ${valor_total:,}")

# --- 11. Invitados ---
print("\n--- Ejercicio 11 ---")
lista1 = ["Ana", "Luis", "Marta"]
lista2 = ["Marta", "Pedro", "Ana"]
print("En ambas:", sorted(set(lista1) & set(lista2)))
print("Solo en la primera:", sorted(set(lista1) - set(lista2)))

# --- 12. Sin repetidos conservando el orden ---
print("\n--- Ejercicio 12 ---")
datos = [3, 1, 3, 2, 1, 5]
unicos = []
for d in datos:
    if d not in unicos:
        unicos.append(d)
print(unicos)
