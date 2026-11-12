# SOLUCIONES · CAPÍTULO 7: ERRORES Y ARCHIVOS
# Este archivo pide datos por teclado: respóndelos cuando el programa los pida.
import json
from pathlib import Path

CARPETA = Path(__file__).parent

# --- 1. Entero seguro ---
print("--- Ejercicio 1 ---")
try:
    n = int(input("Escribe un entero: "))
    print("Escribiste", n)
except ValueError:
    print("Eso no es un número entero.")

# --- 2. División segura ---
print("\n--- Ejercicio 2 ---")
try:
    a = float(input("Numerador: "))
    b = float(input("Denominador: "))
    print("Resultado:", a / b)
except ValueError:
    print("Debes escribir números.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# --- 3. Escribir ---
print("\n--- Ejercicio 3 ---")
with open(CARPETA / "perfil.txt", "w", encoding="utf-8") as f:
    f.write("Laura\n")
    f.write("Bogotá\n")
print("perfil.txt creado")

# --- 4. Leer ---
print("\n--- Ejercicio 4 ---")
with open(CARPETA / "perfil.txt", "r", encoding="utf-8") as f:
    print(f.read())


# --- 5. Validar hasta acertar ---
def pedir_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser mayor que cero.")
        except ValueError:
            print("  Debe ser un número.")


print("--- Ejercicio 5 ---")
print("Valor aceptado:", pedir_positivo("Número positivo: "))

# --- 6. Agregar líneas ---
print("\n--- Ejercicio 6 ---")
ruta_frases = CARPETA / "frases.txt"
ruta_frases.write_text("", encoding="utf-8")      # empezar desde cero
while True:
    frase = input("Frase (escribe 'fin' para terminar): ")
    if frase.lower() == "fin":
        break
    with open(ruta_frases, "a", encoding="utf-8") as f:
        f.write(frase + "\n")
with open(ruta_frases, "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):
        print(f"{numero}. {linea.strip()}")

# --- 7. Promedio desde archivo ---
print("\n--- Ejercicio 7 ---")
suma = 0
cantidad = 0
mejor_nombre, mejor_nota = "", -1
with open(CARPETA / "ejemplo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, nota = linea.strip().split(",")
        nota = float(nota)
        suma += nota
        cantidad += 1
        if nota > mejor_nota:
            mejor_nombre, mejor_nota = nombre, nota
print(f"Promedio: {suma / cantidad:.2f}")
print(f"Mejor nota: {mejor_nombre} ({mejor_nota})")

# --- 8. Contar líneas y palabras ---
print("\n--- Ejercicio 8 ---")
with open(CARPETA / "ejemplo.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
palabras = sum(len(linea.split()) for linea in lineas)
print("Líneas:", len(lineas), "| Palabras:", palabras)

# --- 9. Lista de tareas con JSON ---
print("\n--- Ejercicio 9 ---")
ruta_tareas = CARPETA / "tareas.json"
try:
    with open(ruta_tareas, "r", encoding="utf-8") as f:
        tareas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    tareas = []

while True:
    print("\n1. Agregar tarea  2. Ver tareas  3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        tareas.append(input("Nueva tarea: "))
        with open(ruta_tareas, "w", encoding="utf-8") as f:
            json.dump(tareas, f, ensure_ascii=False, indent=4)
    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")

# --- 10. Archivo inexistente ---
print("\n--- Ejercicio 10 ---")
nombre_archivo = input("Nombre del archivo a mostrar: ")
try:
    with open(CARPETA / nombre_archivo, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")

# --- 11. Convertir TXT a JSON ---
print("\n--- Ejercicio 11 ---")
estudiantes = []
with open(CARPETA / "ejemplo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, nota = linea.strip().split(",")
        estudiantes.append({"nombre": nombre, "nota": float(nota)})
with open(CARPETA / "estudiantes.json", "w", encoding="utf-8") as f:
    json.dump(estudiantes, f, ensure_ascii=False, indent=4)
print("estudiantes.json creado con", len(estudiantes), "registros")
