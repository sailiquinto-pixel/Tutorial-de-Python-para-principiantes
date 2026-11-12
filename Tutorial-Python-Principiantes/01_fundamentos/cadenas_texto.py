# CAPÍTULO 1. CADENAS DE TEXTO
# Las cadenas (str) tienen muchas herramientas para trabajar con texto.

frase = "  Aprender Python es divertido  "

print("Original:", frase)
print("Longitud:", len(frase))

# --- Métodos que transforman el texto (devuelven un texto nuevo) ---
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Sin espacios en los extremos:", frase.strip())
print("Reemplazo:", frase.replace("divertido", "genial"))

limpia = frase.strip()
print("Título:", limpia.title())

# --- Indexación: cada letra tiene una posición, empezando en 0 ---
palabra = "Python"
print(palabra[0])     # P (primera)
print(palabra[1])     # y
print(palabra[-1])    # n (última)

# --- Rebanado (slicing): texto[inicio:fin] — el fin NO se incluye ---
print(palabra[0:3])   # Pyt
print(palabra[2:])    # thon
print(palabra[:4])    # Pyth
print(palabra[::-1])  # nohtyP (al revés)

# --- Buscar dentro del texto ---
print("¿Contiene 'thon'?", "thon" in palabra)
print("Posición de 'h':", palabra.find("h"))
print("Veces que aparece 'a':", "banana".count("a"))
print("¿Empieza con 'Py'?", palabra.startswith("Py"))

# --- Dividir y unir ---
oraciones = "manzana,pera,mango"
lista = oraciones.split(",")
print("Dividido:", lista)
print("Unido con guiones:", "-".join(lista))

# --- Unir textos ---
nombre = "Laura"
apellido = "Gómez"
print(nombre + " " + apellido)      # Concatenación
print(f"{nombre} {apellido}")       # f-string (forma recomendada)

# --- Los textos son inmutables ---
# No se puede hacer palabra[0] = "J". Hay que crear un texto nuevo:
nueva = "J" + palabra[1:]
print(nueva)

# --- Caracteres especiales ---
print("Línea 1\nLínea 2")        # \n = salto de línea
print("Columna1\tColumna2")      # \t = tabulación
print("Ella dijo: \"Hola\"")     # \" = comilla dentro del texto

# EJERCICIO:
# Pide (o define) una palabra y muestra: cuántas letras tiene,
# su primera y su última letra, y la palabra al revés.
