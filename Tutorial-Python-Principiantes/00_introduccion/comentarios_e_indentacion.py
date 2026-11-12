# CAPÍTULO 0. COMENTARIOS E INDENTACIÓN

# Esto es un comentario de una sola línea: Python lo ignora.
print("Los comentarios no se ejecutan")  # También pueden ir al final.

"""
Esto es un texto de varias líneas entre comillas triples.
Se usa a menudo como comentario largo o como "docstring"
(la descripción de un archivo o de una función).
"""

# --- INDENTACIÓN ---
# En Python, los espacios al inicio de la línea indican qué instrucciones
# pertenecen a un bloque. Usa 4 espacios por nivel.

temperatura = 28

if temperatura > 25:
    print("Hace calor")          # Pertenece al if
    print("Usa ropa ligera")     # También pertenece al if
else:
    print("Hace fresco")
    print("Lleva una chaqueta")

print("Esta línea se ejecuta siempre")  # Sin indentación: está fuera del if

# --- ORDEN DE EJECUCIÓN ---
# Python ejecuta las líneas de arriba hacia abajo.
print("Primero")
print("Segundo")
print("Tercero")

# EJERCICIO:
# Cambia el valor de temperatura a 15 y observa qué mensajes aparecen.
# Después quita los 4 espacios de una línea dentro del if y mira el error.
