# SOLUCIÓN · RETO 3: ANALIZADOR DE TEXTO
import string

frase = input("Escribe una frase: ")

# Limpiar signos de puntuación y pasar a minúsculas para contar palabras
limpia = frase.lower()
for signo in string.punctuation + "¿¡":
    limpia = limpia.replace(signo, "")
palabras = limpia.split()

vocales = sum(1 for letra in frase.lower() if letra in "aeiouáéíóú")

print("\n=== RESULTADOS ===")
print("Caracteres (con espacios):", len(frase))
print("Caracteres (sin espacios):", len(frase.replace(" ", "")))
print("Palabras:", len(palabras))
print("Vocales:", vocales)

if palabras:
    print("Palabra más larga:", max(palabras, key=len))

frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("\nFrecuencia de palabras:")
for palabra, veces in sorted(frecuencias.items(), key=lambda par: par[1], reverse=True):
    print(f"  {palabra:<15} {veces}")
