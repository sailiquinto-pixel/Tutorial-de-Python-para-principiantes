# CAPÍTULO 7. JSON: GUARDAR Y CARGAR ESTRUCTURAS DE DATOS
import json
from pathlib import Path

CARPETA = Path(__file__).parent
ruta = CARPETA / "datos.json"

# --- Guardar un diccionario ---
estudiante = {
    "nombre": "Laura",
    "carrera": "Economía",
    "notas": [4.0, 3.5, 4.8],
    "activa": True,
}

with open(ruta, "w", encoding="utf-8") as archivo:
    # ensure_ascii=False conserva tildes y ñ; indent=4 lo hace legible.
    json.dump(estudiante, archivo, ensure_ascii=False, indent=4)
print("Datos guardados en datos.json")

# --- Cargar los datos de vuelta ---
with open(ruta, "r", encoding="utf-8") as archivo:
    cargado = json.load(archivo)

print("\nDatos cargados:", cargado)
print("Nombre:", cargado["nombre"])
print("Promedio:", round(sum(cargado["notas"]) / len(cargado["notas"]), 2))

# --- Guardar una lista de diccionarios ---
gastos = [
    {"descripcion": "Arriendo", "valor": 900000},
    {"descripcion": "Mercado", "valor": 350000},
]
ruta_gastos = CARPETA / "gastos.json"
with open(ruta_gastos, "w", encoding="utf-8") as archivo:
    json.dump(gastos, archivo, ensure_ascii=False, indent=4)

# --- Cargar con valor por defecto si el archivo no existe ---
def cargar_datos(ruta_archivo, por_defecto):
    """Devuelve el contenido del JSON o 'por_defecto' si no se puede leer."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return por_defecto


print("\nGastos:", cargar_datos(ruta_gastos, []))
print("Archivo inexistente:", cargar_datos(CARPETA / "nada.json", []))

# EJERCICIO:
# Crea una agenda (diccionario nombre → teléfono), guárdala en
# "agenda.json" y vuelve a cargarla.
