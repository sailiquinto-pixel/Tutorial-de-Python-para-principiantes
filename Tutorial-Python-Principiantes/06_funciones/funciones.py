# CAPÍTULO 6. FUNCIONES
# Una función agrupa instrucciones que podemos reutilizar.

def saludar(nombre):
    """Muestra un saludo personalizado."""
    print("Hola,", nombre)


def calcular_promedio(nota1, nota2, nota3):
    """Devuelve el promedio de tres notas."""
    return (nota1 + nota2 + nota3) / 3


saludar("Laura")
resultado = calcular_promedio(4.0, 3.5, 4.5)
print("El promedio es:", round(resultado, 2))

# --- Una función puede llamarse muchas veces ---
saludar("Camilo")
saludar("Sofía")


# --- Funciones que devuelven True o False ---
def es_par(numero):
    """Indica si un número es par."""
    return numero % 2 == 0


print("¿10 es par?", es_par(10))
print("¿7 es par?", es_par(7))


# --- Funciones que usan condicionales ---
def clasificar_nota(nota):
    """Clasifica una nota de 0 a 5."""
    if nota >= 4.5:
        return "Excelente"
    elif nota >= 3:
        return "Aprobado"
    else:
        return "Reprobado"


for n in [5.0, 3.2, 2.1]:
    print(f"Nota {n}: {clasificar_nota(n)}")


# --- Funciones que usan ciclos ---
def sumar_lista(numeros):
    """Suma todos los números de una lista."""
    total = 0
    for numero in numeros:
        total += numero
    return total


print("Suma:", sumar_lista([10, 20, 30]))


# --- Una función puede llamar a otra ---
def mostrar_resumen(nombre, n1, n2, n3):
    promedio = calcular_promedio(n1, n2, n3)
    print(f"{nombre}: promedio {promedio:.2f} → {clasificar_nota(promedio)}")


mostrar_resumen("Laura", 4.0, 3.5, 4.5)

# EJERCICIO:
# Crea una función que reciba dos números y devuelva el mayor.
