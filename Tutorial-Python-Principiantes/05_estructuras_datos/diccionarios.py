# CAPÍTULO 5. DICCIONARIOS
# Guardan datos mediante pares de clave y valor.

estudiante = {
    "nombre": "Laura",
    "carrera": "Economía",
    "semestre": 3
}

print("Nombre:", estudiante["nombre"])
print("Carrera:", estudiante["carrera"])

# Agregar o modificar un dato:
estudiante["universidad"] = "Mi universidad"
estudiante["semestre"] = 4

for clave, valor in estudiante.items():
    print(clave, ":", valor)

# --- Consultar de forma segura con get() ---
print("\nTeléfono:", estudiante.get("telefono", "No registrado"))
# estudiante["telefono"]  ← Esto provocaría un KeyError

# --- Comprobar si existe una clave ---
if "carrera" in estudiante:
    print("La carrera es", estudiante["carrera"])

# --- Eliminar ---
semestre = estudiante.pop("semestre")
print("\nSe eliminó el semestre:", semestre)

# --- Claves, valores y pares ---
print("Claves:", list(estudiante.keys()))
print("Valores:", list(estudiante.values()))

# --- Diccionario como contador ---
texto = "banana"
frecuencias = {}
for letra in texto:
    frecuencias[letra] = frecuencias.get(letra, 0) + 1
print("\nFrecuencia de letras en 'banana':", frecuencias)

# --- Diccionario como "tabla de búsqueda" ---
precios = {"pan": 2500, "leche": 4200, "huevos": 9800}
producto = "leche"
print(f"\nEl precio de {producto} es ${precios[producto]:,}")

total = sum(precios.values())
print(f"Total de la canasta: ${total:,}")

# --- Actualizar con varios datos a la vez ---
estudiante.update({"ciudad": "Bogotá", "edad": 20})
print("\nDiccionario actualizado:", estudiante)

# EJERCICIO:
# Crea un diccionario de un producto con nombre, precio y cantidad.
