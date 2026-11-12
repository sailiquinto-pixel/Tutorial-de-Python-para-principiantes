# CAPÍTULO 6. PARÁMETROS Y VALORES DE RETORNO

# --- Parámetros con valor por defecto ---
def precio_final(precio, descuento=0, iva=0.19):
    """Calcula el precio final aplicando descuento (%) e IVA."""
    con_descuento = precio * (1 - descuento / 100)
    return con_descuento * (1 + iva)


print(precio_final(100000))                  # solo con IVA
print(precio_final(100000, 10))              # 10 % de descuento
print(precio_final(100000, iva=0))           # sin IVA (argumento con nombre)
print(precio_final(iva=0.05, precio=50000))  # el orden no importa si usas nombres


# --- Devolver varios valores ---
def estadisticas(numeros):
    """Devuelve el mínimo, el máximo y el promedio de una lista."""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)


menor, mayor, promedio = estadisticas([4, 8, 15, 16, 23, 42])
print(f"\nMenor: {menor} | Mayor: {mayor} | Promedio: {promedio:.2f}")


# --- Función sin return devuelve None ---
def mostrar_mensaje(texto):
    print(texto)


valor = mostrar_mensaje("Hola")
print("Lo que devolvió la función:", valor)   # None


# --- Número variable de argumentos con *args ---
def sumar_todo(*numeros):
    """Suma cualquier cantidad de números."""
    return sum(numeros)


print("\nSuma de 3 números:", sumar_todo(1, 2, 3))
print("Suma de 6 números:", sumar_todo(1, 2, 3, 4, 5, 6))


# --- Pasar listas y diccionarios a funciones ---
def mostrar_estudiante(datos):
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")


print("\nDatos del estudiante:")
mostrar_estudiante({"nombre": "Laura", "carrera": "Economía"})


# --- Funciones con validación ---
def dividir(a, b):
    """Divide a entre b; devuelve None si b es cero."""
    if b == 0:
        return None
    return a / b


print("\n10 / 4 =", dividir(10, 4))
print("10 / 0 =", dividir(10, 0))

# EJERCICIO:
# Escribe una función `area_rectangulo(base, altura=1)` y llámala
# con uno y con dos argumentos.
