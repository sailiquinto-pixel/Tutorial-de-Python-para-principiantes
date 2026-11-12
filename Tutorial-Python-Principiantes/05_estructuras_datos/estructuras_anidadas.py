# CAPÍTULO 5. ESTRUCTURAS ANIDADAS
# Combinar estructuras permite representar información real.

# --- Lista de diccionarios: varios registros con los mismos campos ---
estudiantes = [
    {"nombre": "Laura", "nota": 4.5},
    {"nombre": "Camilo", "nota": 3.2},
    {"nombre": "Sofía", "nota": 2.8},
    {"nombre": "Andrés", "nota": 4.0},
]

print("=== LISTA DE ESTUDIANTES ===")
for estudiante in estudiantes:
    print(f"{estudiante['nombre']:<10} {estudiante['nota']}")

# Calcular el promedio de todas las notas
suma = 0
for estudiante in estudiantes:
    suma += estudiante["nota"]
print("\nPromedio del grupo:", round(suma / len(estudiantes), 2))

# Quiénes aprobaron (nota >= 3)
aprobados = [e["nombre"] for e in estudiantes if e["nota"] >= 3]
print("Aprobaron:", aprobados)

# El mejor estudiante
mejor = estudiantes[0]
for estudiante in estudiantes:
    if estudiante["nota"] > mejor["nota"]:
        mejor = estudiante
print("Mejor nota:", mejor["nombre"], "con", mejor["nota"])

# Ordenar por una clave
ordenados = sorted(estudiantes, key=lambda e: e["nota"], reverse=True)
print("\nRanking:")
for puesto, e in enumerate(ordenados, start=1):
    print(f"{puesto}. {e['nombre']} ({e['nota']})")

# --- Diccionario de listas ---
notas_por_materia = {
    "Matemáticas": [4.0, 3.5, 4.2],
    "Historia": [3.0, 3.8],
    "Inglés": [5.0, 4.5, 4.7],
}

print("\n=== PROMEDIO POR MATERIA ===")
for materia, notas in notas_por_materia.items():
    print(f"{materia:<12} {sum(notas) / len(notas):.2f}")

# --- Agregar un nuevo registro ---
estudiantes.append({"nombre": "Valentina", "nota": 4.9})
print("\nTotal de estudiantes:", len(estudiantes))

# EJERCICIO:
# Crea una lista de tres productos (diccionarios con nombre, precio y
# cantidad) y calcula el valor total del inventario.
