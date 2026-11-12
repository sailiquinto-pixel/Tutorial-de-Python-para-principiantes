# SOLUCIONES · CAPÍTULO 3: CONDICIONALES
# Este archivo pide datos por teclado: respóndelos cuando el programa los pida.

# --- 1. Mayoría de edad ---
print("--- Ejercicio 1 ---")
edad = int(input("Edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# --- 2. Positivo, negativo o cero ---
print("\n--- Ejercicio 2 ---")
n = float(input("Número: "))
if n > 0:
    print("Es positivo")
elif n < 0:
    print("Es negativo")
else:
    print("Es cero")

# --- 3. Par o impar ---
print("\n--- Ejercicio 3 ---")
entero = int(input("Entero: "))
print("Es par" if entero % 2 == 0 else "Es impar")

# --- 4. Contraseña ---
print("\n--- Ejercicio 4 ---")
clave = input("Contraseña: ")
if clave == "python":
    print("Acceso permitido")
else:
    print("Acceso denegado")

# --- 5. Mayor de tres ---
print("\n--- Ejercicio 5 ---")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c
print("El mayor es", mayor)

# --- 6. Calificación en letras ---
print("\n--- Ejercicio 6 ---")
puntaje = float(input("Puntaje (0 a 100): "))
if puntaje < 0 or puntaje > 100:
    print("Puntaje inválido")
elif puntaje >= 90:
    print("A")
elif puntaje >= 80:
    print("B")
elif puntaje >= 70:
    print("C")
elif puntaje >= 60:
    print("D")
else:
    print("F")

# --- 7. Triángulo ---
print("\n--- Ejercicio 7 ---")
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Sí forman un triángulo")
else:
    print("No forman un triángulo")

# --- 8. Tarifa de cine ---
print("\n--- Ejercicio 8 ---")
edad_cine = int(input("Edad: "))
if edad_cine < 12:
    tarifa = 8000
elif edad_cine < 60:
    tarifa = 15000
else:
    tarifa = 9000
print(f"Tu tarifa es ${tarifa:,}")

# --- 9. Año bisiesto ---
print("\n--- Ejercicio 9 ---")
anio = int(input("Año: "))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")

# --- 10. Calculadora de IMC ---
print("\n--- Ejercicio 10 ---")
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))
imc = peso / estatura ** 2
if imc < 18.5:
    categoria = "bajo peso"
elif imc < 25:
    categoria = "normal"
elif imc < 30:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"
print(f"Tu IMC es {imc:.1f}: {categoria}")

# --- 11. Piedra, papel o tijera ---
print("\n--- Ejercicio 11 ---")
j1 = input("Jugador 1 (piedra/papel/tijera): ").lower()
j2 = input("Jugador 2 (piedra/papel/tijera): ").lower()
if j1 == j2:
    print("Empate")
elif (j1 == "piedra" and j2 == "tijera") or \
     (j1 == "papel" and j2 == "piedra") or \
     (j1 == "tijera" and j2 == "papel"):
    print("Gana el jugador 1")
else:
    print("Gana el jugador 2")
