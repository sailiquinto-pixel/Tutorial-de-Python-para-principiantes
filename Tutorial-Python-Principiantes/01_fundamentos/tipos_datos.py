# CAPÍTULO 1. TIPOS DE DATOS
# Los tipos indican qué clase de información contiene una variable.

texto = "Python"
entero = 15
decimal = 3.14
logico = False
vacio = None   # Representa "no hay valor todavía"

print(type(texto))
print(type(entero))
print(type(decimal))
print(type(logico))
print(type(vacio))

# --- El tipo importa: no es lo mismo "5" que 5 ---
print("5" + "5")   # Une textos (concatenación): 55
print(5 + 5)       # Suma números: 10
print("Ja" * 3)    # Repite el texto: JaJaJa

# --- Conversión de tipos ---
edad_texto = "19"
edad_numero = int(edad_texto)
print("Edad dentro de cinco años:", edad_numero + 5)

precio_texto = "2500.50"
precio = float(precio_texto)
print("Precio con 1000 más:", precio + 1000)

numero = 42
print("Número como texto: " + str(numero))   # Necesario para unir con texto

# int() recorta los decimales (no redondea):
print(int(9.99))        # 9
print(round(9.99))      # 10

# --- Convertir a bool ---
# Estos valores se consideran "falsos": 0, 0.0, "" (texto vacío), None.
# Todo lo demás se considera "verdadero".
print(bool(0), bool(""), bool(None))     # False False False
print(bool(1), bool("hola"), bool(-5))   # True True True

# --- Comprobar el tipo ---
valor = 3.5
print(isinstance(valor, float))   # True
print(isinstance(valor, int))     # False

# --- Qué pasa cuando la conversión es imposible ---
# Descomenta la siguiente línea para ver el ValueError:
# numero_invalido = int("hola")

# EJERCICIO:
# Crea una variable con un precio como texto, conviértela a float
# y súmale 1000.
