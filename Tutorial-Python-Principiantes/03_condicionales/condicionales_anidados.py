# CAPÍTULO 3. CONDICIONALES ANIDADOS Y EJEMPLOS PRÁCTICOS

# --- Ejemplo 1: descuento según el monto de la compra ---
print("=== DESCUENTO POR COMPRA ===")
compra = float(input("Valor de la compra: "))

if compra >= 200000:
    porcentaje = 15
elif compra >= 100000:
    porcentaje = 10
elif compra >= 50000:
    porcentaje = 5
else:
    porcentaje = 0

descuento = compra * porcentaje / 100
print(f"Descuento aplicado: {porcentaje}% (${descuento:,.2f})")
print(f"Total a pagar: ${compra - descuento:,.2f}")

# --- Ejemplo 2: año bisiesto ---
# Un año es bisiesto si es divisible por 4, excepto los divisibles por 100,
# a menos que también sean divisibles por 400.
print("\n=== AÑO BISIESTO ===")
anio = int(input("Escribe un año: "))

if anio % 400 == 0:
    print(anio, "es bisiesto.")
elif anio % 100 == 0:
    print(anio, "no es bisiesto.")
elif anio % 4 == 0:
    print(anio, "es bisiesto.")
else:
    print(anio, "no es bisiesto.")

# --- Ejemplo 3: condicionales anidados ---
print("\n=== ACCESO A UN SISTEMA ===")
usuario = input("Usuario: ")
clave = input("Clave: ")

if usuario == "admin":
    if clave == "1234":
        print("Bienvenido, administrador.")
    else:
        print("Clave incorrecta.")
else:
    print("Usuario no registrado.")

# --- Ejemplo 4: menú de opciones ---
print("\n=== MENÚ ===")
print("1. Ver saldo")
print("2. Depositar")
print("3. Salir")
opcion = input("Elige una opción: ")

if opcion == "1":
    print("Tu saldo es $150,000.")
elif opcion == "2":
    print("Función de depósito en construcción.")
elif opcion == "3":
    print("Hasta pronto.")
else:
    print("Opción no válida.")

# EJERCICIO:
# Pide tres números y muestra cuál es el mayor.
