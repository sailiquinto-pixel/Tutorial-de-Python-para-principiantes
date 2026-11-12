# CAPÍTULO 7. MANEJO DE ERRORES
# Un programa robusto anticipa lo que puede salir mal.

# --- try / except básico ---
try:
    numero = int(input("Escribe un número entero: "))
    print("El doble es", numero * 2)
except ValueError:
    print("Eso no es un número entero válido.")

# --- Varios tipos de error ---
try:
    a = float(input("\nNumerador: "))
    b = float(input("Denominador: "))
    print("Resultado:", a / b)
except ValueError:
    print("Debes escribir números.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# --- else y finally ---
try:
    valor = int(input("\nEscribe un número: "))
except ValueError:
    print("Valor inválido.")
else:
    print("Todo salió bien, escribiste", valor)   # solo si NO hubo error
finally:
    print("Este mensaje aparece siempre.")


# --- Función que repite hasta recibir un dato válido ---
def pedir_entero(mensaje):
    """Pide un entero y repite hasta que el usuario lo escriba bien."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Intenta de nuevo: debe ser un número entero.")


edad = pedir_entero("\n¿Cuántos años tienes? ")
print("Tienes", edad, "años.")

# --- Errores comunes con colecciones ---
lista = [10, 20, 30]
try:
    print(lista[5])
except IndexError:
    print("\nEsa posición no existe en la lista.")

datos = {"nombre": "Laura"}
try:
    print(datos["edad"])
except KeyError:
    print("Esa clave no existe en el diccionario.")

# --- Lanzar tu propio error con raise ---
def calcular_raiz(numero):
    if numero < 0:
        raise ValueError("No existe raíz real de un número negativo.")
    return numero ** 0.5


try:
    calcular_raiz(-4)
except ValueError as error:
    print("Error capturado:", error)

# EJERCICIO:
# Escribe una función pedir_decimal(mensaje) que repita hasta que
# el usuario escriba un número decimal válido y positivo.
