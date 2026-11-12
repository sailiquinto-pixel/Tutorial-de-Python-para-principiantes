# SOLUCIÓN · RETO 7: DIARIO CON ARCHIVOS
from datetime import datetime
from pathlib import Path

RUTA = Path(__file__).parent / "diario.txt"


def escribir_entrada():
    texto = input("Escribe tu entrada: ").strip()
    if not texto:
        print("La entrada no puede estar vacía.")
        return
    marca = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open(RUTA, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{marca}] {texto}\n")
    print("Entrada guardada.")


def leer_entradas():
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("Todavía no hay entradas.")
        return
    print("\n=== TU DIARIO ===")
    for linea in lineas:
        print(linea.strip())


def buscar(palabra):
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            coincidencias = [l.strip() for l in archivo if palabra.lower() in l.lower()]
    except FileNotFoundError:
        print("Todavía no hay entradas.")
        return
    print(f"\n{len(coincidencias)} resultado(s) para '{palabra}':")
    for linea in coincidencias:
        print(" ", linea)


while True:
    print("\n1. Escribir  2. Leer todo  3. Buscar  4. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        escribir_entrada()
    elif opcion == "2":
        leer_entradas()
    elif opcion == "3":
        buscar(input("Palabra a buscar: "))
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
