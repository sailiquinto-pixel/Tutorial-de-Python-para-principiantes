# CAPÍTULO 3. OPERADORES LÓGICOS Y DE PERTENENCIA

edad = 25
tiene_documento = True
es_estudiante = False

# --- and: deben cumplirse TODAS las condiciones ---
if edad >= 18 and tiene_documento:
    print("Puede ingresar al evento.")

# --- or: basta con que se cumpla UNA ---
if es_estudiante or edad >= 60:
    print("Tiene descuento.")
else:
    print("Paga tarifa completa.")

# --- not: invierte la condición ---
if not es_estudiante:
    print("No es estudiante.")

# --- Rangos: edad entre 18 y 30 ---
if 18 <= edad <= 30:        # Python permite encadenar comparaciones
    print("Pertenece al grupo de jóvenes adultos.")

# --- in / not in: ¿está dentro de una colección o un texto? ---
vocales = "aeiou"
letra = "e"
if letra in vocales:
    print(f"'{letra}' es una vocal.")

dias_laborales = ["lunes", "martes", "miércoles", "jueves", "viernes"]
dia = "sábado"
if dia not in dias_laborales:
    print(f"{dia.capitalize()} no es día laboral.")

# --- Valores "verdaderos" y "falsos" ---
# Son falsos: False, 0, 0.0, "" (texto vacío), [] (lista vacía), None.
for valor in [0, 1, "", "hola", [], [1, 2], None]:
    if valor:
        print(repr(valor), "→ se considera verdadero")
    else:
        print(repr(valor), "→ se considera falso")

# --- Comparar textos ---
clave = "python123"
intento = "Python123"
print("¿Son iguales?", clave == intento)                       # False (distingue mayúsculas)
print("¿Iguales sin importar mayúsculas?", clave == intento.lower())  # True

# EJERCICIO:
# Escribe una condición que indique si una persona puede donar sangre:
# debe tener entre 18 y 65 años y pesar al menos 50 kg.
