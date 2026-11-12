# SOLUCIÓN · RETO 1: CAJERO AUTOMÁTICO

def pedir_monto(mensaje):
    """Pide un monto positivo; devuelve None si el dato no es válido."""
    try:
        monto = float(input(mensaje))
    except ValueError:
        print("Debes escribir un número.")
        return None
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return None
    return monto


saldo = 500000

while True:
    print("\n=== CAJERO AUTOMÁTICO ===")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Tu saldo es ${saldo:,.2f}")
    elif opcion == "2":
        monto = pedir_monto("Monto a depositar: ")
        if monto is not None:
            saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo:,.2f}")
    elif opcion == "3":
        monto = pedir_monto("Monto a retirar: ")
        if monto is not None:
            if monto > saldo:
                print("Fondos insuficientes.")
            else:
                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: ${saldo:,.2f}")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción no válida.")
