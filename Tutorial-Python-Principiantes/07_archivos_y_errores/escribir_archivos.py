# CAPÍTULO 7. ESCRIBIR ARCHIVOS
from pathlib import Path

CARPETA = Path(__file__).parent
ruta = CARPETA / "salida.txt"

# --- Modo "w": crea el archivo (o BORRA el anterior) ---
with open(ruta, "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea con tildes y ñ\n")
print("Archivo creado:", ruta.name)

# --- Modo "a": agrega al final sin borrar ---
with open(ruta, "a", encoding="utf-8") as archivo:
    archivo.write("Esta línea se agregó después\n")

# --- Comprobar el resultado ---
with open(ruta, "r", encoding="utf-8") as archivo:
    print("\nContenido actual:")
    print(archivo.read())

# --- Escribir una lista de gastos, uno por línea ---
gastos = [
    {"descripcion": "Arriendo", "valor": 900000},
    {"descripcion": "Mercado", "valor": 350000},
    {"descripcion": "Transporte", "valor": 120000},
]

with open(CARPETA / "gastos.txt", "w", encoding="utf-8") as archivo:
    for gasto in gastos:
        archivo.write(f"{gasto['descripcion']},{gasto['valor']}\n")
print("Gastos guardados en gastos.txt")

# --- Un pequeño diario: cada ejecución agrega una entrada ---
from datetime import datetime

with open(CARPETA / "diario.txt", "a", encoding="utf-8") as archivo:
    marca = datetime.now().strftime("%d/%m/%Y %H:%M")
    archivo.write(f"[{marca}] Practicando archivos en Python\n")
print("Se agregó una entrada a diario.txt")

# EJERCICIO:
# Pide al usuario 3 frases y guárdalas en un archivo "frases.txt",
# una por línea. Luego léelas y muéstralas numeradas.
