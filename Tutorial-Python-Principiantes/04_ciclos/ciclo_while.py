# CAPÍTULO 4. CICLO WHILE
# Repite instrucciones mientras una condición sea verdadera.

contador = 1

while contador <= 5:
    print("Contador:", contador)
    contador += 1  # Aumenta el contador para evitar un ciclo infinito.

# --- Cuenta regresiva ---
print()
segundos = 5
while segundos > 0:
    print(segundos)
    segundos -= 1
print("¡Despegue!")

# --- Validación de datos: repetir hasta que la entrada sea correcta ---
print()
edad = int(input("Escribe tu edad (debe ser positiva): "))
while edad <= 0:
    print("Valor no válido. Inténtalo de nuevo.")
    edad = int(input("Escribe tu edad (debe ser positiva): "))
print("Edad registrada:", edad)

# --- Ciclo con bandera: seguir hasta que el usuario decida salir ---
print()
suma = 0
numero = int(input("Escribe un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Escribe otro número (0 para terminar): "))
print("La suma total es:", suma)

# --- while True + break: otra forma de repetir hasta una condición ---
print()
while True:
    clave = input("Escribe la clave secreta: ")
    if clave == "python":
        print("¡Correcto!")
        break
    print("Clave incorrecta.")

# EJERCICIO:
# Crea un contador que empiece en 10 y disminuya hasta llegar a 1.
