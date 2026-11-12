# PROYECTO FINAL (VERSIÓN 2): PRESUPUESTO PERSONAL CON ARCHIVO
# Menú interactivo, categorías, resumen y guardado de datos en JSON.
# Los valores se ingresan en pesos, sin separadores de miles.

import json
from pathlib import Path

RUTA_DATOS = Path(__file__).parent / "presupuesto.json"

CATEGORIAS = [
    "Vivienda",
    "Alimentación",
    "Transporte",
    "Educación",
    "Salud",
    "Ocio",
    "Otros",
]


# ------------------------------------------------------------------
# Guardar y cargar datos
# ------------------------------------------------------------------
def cargar_datos():
    """Lee el archivo JSON. Si no existe o está dañado, empieza vacío."""
    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"ingresos": [], "gastos": []}


def guardar_datos(datos):
    """Escribe los datos en el archivo JSON."""
    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


# ------------------------------------------------------------------
# Entradas del usuario (con validación)
# ------------------------------------------------------------------
def pedir_valor(mensaje):
    """Solicita un valor numérico mayor que cero."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor que cero.")
            else:
                return valor
        except ValueError:
            print("Por favor, escribe un número válido.")


def pedir_texto(mensaje):
    """Solicita un texto que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este dato no puede estar vacío.")


def elegir_categoria():
    """Muestra las categorías y devuelve la elegida."""
    print("\nCategorías:")
    for numero, nombre in enumerate(CATEGORIAS, start=1):
        print(f"  {numero}. {nombre}")
    while True:
        opcion = input("Elige el número de la categoría: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(CATEGORIAS):
            return CATEGORIAS[int(opcion) - 1]
        print("Opción no válida.")


# ------------------------------------------------------------------
# Operaciones del programa
# ------------------------------------------------------------------
def registrar_ingreso(datos):
    descripcion = pedir_texto("Descripción del ingreso: ")
    valor = pedir_valor("Valor del ingreso: ")
    datos["ingresos"].append({"descripcion": descripcion, "valor": valor})
    guardar_datos(datos)
    print("✔ Ingreso registrado.")


def registrar_gasto(datos):
    descripcion = pedir_texto("Descripción del gasto: ")
    categoria = elegir_categoria()
    valor = pedir_valor("Valor del gasto: ")
    datos["gastos"].append(
        {"descripcion": descripcion, "categoria": categoria, "valor": valor}
    )
    guardar_datos(datos)
    print("✔ Gasto registrado.")


def calcular_totales(datos):
    """Devuelve (total_ingresos, total_gastos, saldo)."""
    total_ingresos = sum(i["valor"] for i in datos["ingresos"])
    total_gastos = sum(g["valor"] for g in datos["gastos"])
    return total_ingresos, total_gastos, total_ingresos - total_gastos


def gastos_por_categoria(datos):
    """Devuelve un diccionario {categoria: total gastado}."""
    totales = {}
    for gasto in datos["gastos"]:
        categoria = gasto["categoria"]
        totales[categoria] = totales.get(categoria, 0) + gasto["valor"]
    return totales


def mostrar_resumen(datos):
    total_ingresos, total_gastos, saldo = calcular_totales(datos)

    print("\n" + "=" * 44)
    print(f"{'RESUMEN DEL PRESUPUESTO':^44}")
    print("=" * 44)

    print("\nIngresos:")
    if not datos["ingresos"]:
        print("  (sin registros)")
    for ingreso in datos["ingresos"]:
        print(f"  - {ingreso['descripcion']:<22} ${ingreso['valor']:>12,.2f}")

    print("\nGastos:")
    if not datos["gastos"]:
        print("  (sin registros)")
    for gasto in datos["gastos"]:
        print(f"  - {gasto['descripcion']:<22} ${gasto['valor']:>12,.2f}  [{gasto['categoria']}]")

    por_categoria = gastos_por_categoria(datos)
    if por_categoria:
        print("\nGastos por categoría:")
        ordenadas = sorted(por_categoria.items(), key=lambda par: par[1], reverse=True)
        for categoria, total in ordenadas:
            porcentaje = total / total_gastos * 100
            print(f"  {categoria:<14} ${total:>12,.2f}  ({porcentaje:.1f}%)")

    print("\n" + "-" * 44)
    print(f"{'Total de ingresos:':<24} ${total_ingresos:>14,.2f}")
    print(f"{'Total de gastos:':<24} ${total_gastos:>14,.2f}")
    print(f"{'Saldo disponible:':<24} ${saldo:>14,.2f}")
    print("-" * 44)

    if saldo > 0:
        print("Terminaste el periodo con dinero disponible.")
    elif saldo == 0:
        print("Utilizaste todo el ingreso registrado.")
    else:
        print("Tus gastos superaron el ingreso registrado.")


def reiniciar_datos(datos):
    confirmacion = input("¿Seguro que quieres borrar TODO? (escribe 'si' para confirmar): ")
    if confirmacion.strip().lower() == "si":
        datos["ingresos"].clear()
        datos["gastos"].clear()
        guardar_datos(datos)
        print("✔ Datos reiniciados.")
    else:
        print("Operación cancelada.")


# ------------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------------
def main():
    datos = cargar_datos()
    print("=== PRESUPUESTO PERSONAL ===")

    while True:
        print("\n1. Registrar ingreso")
        print("2. Registrar gasto")
        print("3. Ver resumen")
        print("4. Reiniciar datos")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_ingreso(datos)
        elif opcion == "2":
            registrar_gasto(datos)
        elif opcion == "3":
            mostrar_resumen(datos)
        elif opcion == "4":
            reiniciar_datos(datos)
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


# Esta condición hace que main() solo se ejecute cuando abres este archivo
# directamente, y no cuando otro archivo lo importa.
if __name__ == "__main__":
    main()
