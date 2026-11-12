# CAPÍTULO 2. ENTRADA Y SALIDA
# input() recibe información. Todo lo que recibe inicialmente es texto.

nombre = input("¿Cómo te llamas? ")
ciudad = input("¿En qué ciudad vives? ")

# Para operar con números debemos convertir el texto.
edad = int(input("¿Cuántos años tienes? "))

print("\nHola,", nombre)
print("Vives en", ciudad)
print("El próximo año tendrás", edad + 1, "años.")

# --- Decimales ---
estatura = float(input("\n¿Cuánto mides en metros? (ej. 1.65) "))
print("Mides", estatura, "metros, es decir", round(estatura * 100), "centímetros.")

# --- ¿Qué pasa si no convertimos? ---
# numero = input("Escribe un número: ")
# print(numero * 3)   # Si escribes 4, muestra "444" (repite el TEXTO)

# --- Limpiar lo que escribe el usuario ---
# .strip() quita espacios sobrantes; .title() pone mayúscula inicial.
nombre_limpio = nombre.strip().title()
print("\nNombre limpio:", nombre_limpio)

# EJERCICIO:
# Pregunta al usuario su carrera y muestra una frase con la respuesta.
