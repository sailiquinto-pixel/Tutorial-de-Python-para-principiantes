# CAPÍTULO 6. MÓDULOS DE LA BIBLIOTECA ESTÁNDAR
# Python trae muchas herramientas listas para usar con "import".

import math
import random
from datetime import date, datetime

# --- math ---
print("Raíz cuadrada de 81:", math.sqrt(81))
print("π =", round(math.pi, 4))
print("Redondear hacia arriba 4.1:", math.ceil(4.1))
print("Redondear hacia abajo 4.9:", math.floor(4.9))
print("2 elevado a la 10:", math.pow(2, 10))

# Área de un círculo
radio = 5
print(f"Área de un círculo de radio {radio}: {math.pi * radio ** 2:.2f}")

# --- random ---
print("\nDado:", random.randint(1, 6))
colores = ["rojo", "verde", "azul", "amarillo"]
print("Color al azar:", random.choice(colores))

cartas = [1, 2, 3, 4, 5]
random.shuffle(cartas)
print("Cartas mezcladas:", cartas)

# --- datetime ---
hoy = date.today()
print("\nHoy es:", hoy)
print("Año:", hoy.year, "| Mes:", hoy.month, "| Día:", hoy.day)
print("Fecha formateada:", hoy.strftime("%d/%m/%Y"))

ahora = datetime.now()
print("Hora actual:", ahora.strftime("%H:%M"))

# Calcular una edad aproximada
nacimiento = date(2004, 5, 20)
edad = hoy.year - nacimiento.year
print("Edad aproximada:", edad)

# --- Tus propios módulos ---
# Cualquier archivo .py puede importarse desde otro.
# Si guardas funciones en "utilidades.py", puedes hacer:
#   from utilidades import es_par

# EJERCICIO:
# Simula tres lanzamientos de dado y muestra la suma de los resultados.
