# CAPÍTULO 3. ESTRUCTURAS CONDICIONALES
# Permiten ejecutar instrucciones dependiendo de una condición.

nota = float(input("Escribe tu nota (0 a 5): "))

if nota < 0 or nota > 5:
    print("La nota debe estar entre 0 y 5.")
elif nota >= 4.5:
    print("Excelente: ¡sigue así!")
elif nota >= 3:
    print("Aprobaste.")
else:
    print("No aprobaste.")

# --- Expresión condicional en una sola línea ---
estado = "Aprobado" if nota >= 3 else "Reprobado"
print("Estado final:", estado)

# --- ¿Importa el orden de los elif? ¡Sí! ---
# Python ejecuta SOLO el primer bloque cuya condición sea verdadera.
# Si pusiéramos "nota >= 3" antes que "nota >= 4.5", una nota de 5
# nunca llegaría al mensaje "Excelente".

# EJERCICIO:
# Pide la edad de una persona. Si tiene 18 años o más,
# muestra "Es mayor de edad"; en caso contrario, "Es menor de edad".
