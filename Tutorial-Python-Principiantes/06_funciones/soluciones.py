# SOLUCIONES · CAPÍTULO 6: FUNCIONES
import math
import random


# --- 1. Mayor ---
def mayor(a, b):
    """Devuelve el mayor de dos números."""
    if a > b:
        return a
    return b


print("--- Ejercicio 1 ---")
print(mayor(8, 15))


# --- 2. Saludo ---
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")


print("\n--- Ejercicio 2 ---")
saludar("Laura")
saludar("Laura", "Buenos días")


# --- 3. Cuadrado ---
def cuadrado(n):
    return n ** 2


print("\n--- Ejercicio 3 ---")
print(cuadrado(7))


# --- 4. Áreas ---
def area_rectangulo(base, altura):
    return base * altura


def area_circulo(radio):
    return math.pi * radio ** 2


print("\n--- Ejercicio 4 ---")
print("Rectángulo:", area_rectangulo(4, 6))
print("Círculo:", round(area_circulo(3), 2))


# --- 5. Mayor de edad ---
def es_mayor_de_edad(edad):
    return edad >= 18


print("\n--- Ejercicio 5 ---")
print(es_mayor_de_edad(20), es_mayor_de_edad(15))


# --- 6. Promedio de lista ---
def promedio(lista):
    return sum(lista) / len(lista)


print("\n--- Ejercicio 6 ---")
print(promedio([4.0, 3.5, 4.5, 5.0]))


# --- 7. Conteo de vocales ---
def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiouáéíóú":
            contador += 1
    return contador


print("\n--- Ejercicio 7 ---")
print(contar_vocales("Programación en Python"))


# --- 8. Calculadora ---
def calculadora(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b == 0:
            return "No se puede dividir entre cero"
        return a / b
    return "Operación no reconocida"


print("\n--- Ejercicio 8 ---")
print(calculadora(10, 4, "+"), calculadora(10, 4, "/"), calculadora(10, 0, "/"))


# --- 9. Palíndromo ---
def es_palindromo(texto):
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]


print("\n--- Ejercicio 9 ---")
print(es_palindromo("Anita lava la tina"), es_palindromo("Python"))


# --- 10. Número primo ---
def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


print("\n--- Ejercicio 10 ---")
print([n for n in range(1, 51) if es_primo(n)])


# --- 11. Descuento escalonado ---
def calcular_descuento(compra):
    if compra > 200000:
        return 15
    elif compra > 100000:
        return 10
    elif compra > 50000:
        return 5
    return 0


print("\n--- Ejercicio 11 ---")
for valor in [30000, 60000, 150000, 250000]:
    print(f"Compra ${valor:,}: {calcular_descuento(valor)}% de descuento")


# --- 12. Dados dobles ---
def lanzar_dobles():
    return random.randint(1, 6) == random.randint(1, 6)


print("\n--- Ejercicio 12 ---")
dobles = sum(1 for _ in range(100) if lanzar_dobles())
print(f"En 100 lanzamientos salieron {dobles} dobles (lo esperado: ~17).")
