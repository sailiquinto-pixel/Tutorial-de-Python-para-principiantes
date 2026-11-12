# CAPÍTULO 7. LEER ARCHIVOS
from pathlib import Path

# La ruta se calcula a partir de la ubicación de este script,
# así funciona sin importar desde qué carpeta lo ejecutes.
CARPETA = Path(__file__).parent
ruta = CARPETA / "ejemplo.txt"

# --- Forma 1: read() — todo el contenido como un solo texto ---
with open(ruta, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
print("=== read() ===")
print(contenido)

# --- Forma 2: readlines() — una lista con cada línea ---
with open(ruta, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
print("=== readlines() ===")
print("Cantidad de líneas:", len(lineas))
print("Primera línea cruda:", repr(lineas[0]))   # incluye el \n del final

# --- Forma 3: recorrer línea por línea (la más recomendada) ---
print("\n=== for linea in archivo ===")
suma = 0
cantidad = 0
with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, nota = linea.strip().split(",")   # strip quita el \n
        nota = float(nota)
        print(f"{nombre:<10} {nota}")
        suma += nota
        cantidad += 1

print(f"\nPromedio del grupo: {suma / cantidad:.2f}")

# --- Convertir el archivo en una lista de diccionarios ---
estudiantes = []
with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, nota = linea.strip().split(",")
        estudiantes.append({"nombre": nombre, "nota": float(nota)})
print("\nComo lista de diccionarios:", estudiantes[:2], "...")

# --- Archivo que no existe ---
try:
    with open(CARPETA / "no_existe.txt", "r", encoding="utf-8") as archivo:
        archivo.read()
except FileNotFoundError:
    print("\nEl archivo 'no_existe.txt' no se encontró.")

# EJERCICIO:
# Lee ejemplo.txt y muestra solo los estudiantes con nota mayor o igual a 4.
