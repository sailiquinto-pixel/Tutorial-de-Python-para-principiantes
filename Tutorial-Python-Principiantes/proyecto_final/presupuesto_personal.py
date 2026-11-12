# PROYECTO FINAL: PRESUPUESTO PERSONAL
# Este programa registra ingresos y gastos y calcula el saldo.
# Los valores se ingresan en pesos, sin separadores de miles.

def pedir_valor(mensaje):
    """Solicita un valor numérico no negativo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Por favor, escribe un número válido.")


print("=== PRESUPUESTO PERSONAL ===")
ingreso = pedir_valor("¿Cuánto dinero recibiste este mes? ")

gastos = []
cantidad = int(pedir_valor("¿Cuántos gastos deseas registrar? "))

for numero in range(1, cantidad + 1):
    descripcion = input(f"Descripción del gasto {numero}: ")
    valor = pedir_valor("Valor del gasto: ")
    gastos.append({"descripcion": descripcion, "valor": valor})

total_gastos = sum(gasto["valor"] for gasto in gastos)
saldo = ingreso - total_gastos

print("\n=== RESUMEN ===")
print(f"Ingreso: ${ingreso:,.2f}")
for gasto in gastos:
    print(f"- {gasto['descripcion']}: ${gasto['valor']:,.2f}")
print(f"Total de gastos: ${total_gastos:,.2f}")
print(f"Saldo disponible: ${saldo:,.2f}")

if saldo > 0:
    print("Terminaste el periodo con dinero disponible.")
elif saldo == 0:
    print("Utilizaste todo el ingreso registrado.")
else:
    print("Tus gastos superaron el ingreso registrado.")

# Posible mejora: guardar los datos en un archivo para consultarlos después.
# → ¡Ya está hecha! Mira presupuesto_con_archivo.py
