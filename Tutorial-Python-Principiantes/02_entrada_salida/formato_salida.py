# CAPÍTULO 2. FORMATO DE SALIDA
# Aprende a mostrar la información de forma clara y ordenada.

# --- Parámetros de print(): sep y end ---
print("2026", "11", "12", sep="-")        # 2026-11-12
print("Cargando", end="...")
print("listo")

# --- f-strings: variables dentro del texto ---
nombre = "Laura"
edad = 20
print(f"Hola, {nombre}. Tienes {edad} años.")
print(f"Dentro de 5 años tendrás {edad + 5}.")   # También admite cálculos

# --- Formato de números ---
precio = 1234567.891
print(f"Sin formato:      {precio}")
print(f"2 decimales:      {precio:.2f}")
print(f"Con miles:        {precio:,.2f}")
print(f"Entero con miles: {1500000:,}")
print(f"Porcentaje:       {0.256:.1%}")

# --- Alineación (útil para tablas) ---
print()
print(f"{'Producto':<12}{'Cantidad':>10}{'Precio':>12}")
print("-" * 34)
print(f"{'Manzanas':<12}{3:>10}{4500.5:>12,.2f}")
print(f"{'Pan':<12}{10:>10}{12000:>12,.2f}")
print(f"{'Leche':<12}{2:>10}{7800.75:>12,.2f}")

# --- Centrar títulos ---
print()
print(f"{' RESUMEN ':=^34}")    # Centrado con signos "="

# --- Caracteres especiales ---
print("\nPrimera línea\nSegunda línea")
print("Nombre:\tLaura")
print("Ruta de Windows: C:\\Usuarios\\Laura")

# --- Textos de varias líneas ---
mensaje = """Este texto
ocupa varias líneas
sin necesidad de \\n."""
print(mensaje)

# EJERCICIO:
# Crea una tabla con tres películas: título, año y calificación.
# Alinea las columnas usando f-strings.
