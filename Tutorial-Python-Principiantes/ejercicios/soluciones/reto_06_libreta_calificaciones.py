# SOLUCIÓN · RETO 6: LIBRETA DE CALIFICACIONES


def pedir_nota(mensaje):
    """Pide una nota entre 0 y 5 y repite hasta que sea válida."""
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 5:
                return nota
            print("  La nota debe estar entre 0 y 5.")
        except ValueError:
            print("  Escribe un número.")


def agregar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante: ").strip()
    notas = [pedir_nota(f"  Nota {i}: ") for i in range(1, 4)]
    estudiantes.append({"nombre": nombre, "notas": notas})


def promedio(estudiante):
    return sum(estudiante["notas"]) / len(estudiante["notas"])


def mostrar_ranking(estudiantes):
    ordenados = sorted(estudiantes, key=promedio, reverse=True)
    print("\n=== RANKING ===")
    for puesto, e in enumerate(ordenados, start=1):
        print(f"{puesto}. {e['nombre']:<12} {promedio(e):.2f}")


def mostrar_estadisticas(estudiantes):
    promedios = [promedio(e) for e in estudiantes]
    mejor = max(estudiantes, key=promedio)
    aprobados = sum(1 for p in promedios if p >= 3)
    print("\n=== ESTADÍSTICAS ===")
    print(f"Promedio del curso: {sum(promedios) / len(promedios):.2f}")
    print(f"Nota más alta: {promedio(mejor):.2f} ({mejor['nombre']})")
    print(f"Aprobaron: {aprobados} | No aprobaron: {len(estudiantes) - aprobados}")


estudiantes = []
while True:
    print("\n1. Agregar estudiante  2. Ver ranking y estadísticas  3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        agregar_estudiante(estudiantes)
    elif opcion == "2":
        if estudiantes:
            mostrar_ranking(estudiantes)
            mostrar_estadisticas(estudiantes)
        else:
            print("Aún no hay estudiantes.")
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")
