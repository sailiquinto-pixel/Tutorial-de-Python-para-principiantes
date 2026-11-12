# EJERCICIOS PRÁCTICOS DE REPASO
# Cada ejercicio es independiente: ejecuta el archivo y sigue las preguntas.

# ------------------------------------------------------------------
# 1. Calculadora sencilla
# ------------------------------------------------------------------
print("=== 1. CALCULADORA SENCILLA ===")
numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", numero1 + numero2)
elif operacion == "-":
    print("Resultado:", numero1 - numero2)
elif operacion == "*":
    print("Resultado:", numero1 * numero2)
elif operacion == "/":
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("No se puede dividir entre cero.")
else:
    print("Operación no reconocida.")

# ------------------------------------------------------------------
# 2. Promedio de notas
# ------------------------------------------------------------------
print("\n=== 2. PROMEDIO DE NOTAS ===")
nota1 = float(input("Primera nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"Promedio: {promedio:.2f}")
print("Aprobado" if promedio >= 3 else "Reprobado")

# ------------------------------------------------------------------
# 3. Lista de compras
# ------------------------------------------------------------------
print("\n=== 3. LISTA DE COMPRAS ===")
compras = []
for numero in range(1, 4):
    producto = input(f"Producto {numero}: ")
    compras.append(producto)

print("\nTu lista de compras:")
for posicion, producto in enumerate(compras, start=1):
    print(f"{posicion}. {producto}")

# ------------------------------------------------------------------
# RETOS EXTRA (resuélvelos por tu cuenta)
# ------------------------------------------------------------------
# a) Mejora la calculadora para que se repita hasta que el usuario escriba "salir".
# b) Pide cuántas notas se ingresarán (en vez de siempre tres) y calcula el promedio.
# c) Haz que la lista de compras permita agregar productos hasta escribir "fin"
#    y que muestre al final cuántos productos hay.
