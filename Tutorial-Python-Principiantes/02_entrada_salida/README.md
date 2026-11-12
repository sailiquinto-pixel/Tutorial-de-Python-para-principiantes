# Capítulo 2 · Entrada y salida de datos

Un programa útil **recibe** información del usuario y **muestra** resultados de forma clara. En este capítulo aprenderás a hacer ambas cosas.

## Qué aprenderás

- Leer datos con `input()` y convertirlos al tipo correcto.
- Mostrar información con `print()` y sus parámetros `sep` y `end`.
- Dar formato a textos y números con **f-strings**.
- Alinear y redondear valores (dinero, porcentajes, tablas).

## 1. Entrada: `input()`

```python
nombre = input("¿Cómo te llamas? ")
```

El texto entre paréntesis es el **mensaje** que ve el usuario. El programa se detiene hasta que la persona escribe algo y pulsa **Enter**.

> ⚠️ `input()` **siempre devuelve texto (`str`)**, incluso si el usuario escribe un número. Para operar con él hay que convertirlo:

```python
edad = int(input("¿Cuántos años tienes? "))       # entero
precio = float(input("¿Cuánto cuesta? "))         # decimal
```

## 2. Salida: `print()`

```python
print("Hola", "mundo")                  # Hola mundo
print("Hola", "mundo", sep="-")         # Hola-mundo
print("Cargando", end="...")            # no salta de línea
print("listo")                          # Cargando...listo
```

| Parámetro | Para qué sirve | Valor por defecto |
|---|---|---|
| `sep` | Separador entre valores | un espacio |
| `end` | Lo que se imprime al final | salto de línea (`\n`) |

## 3. f-strings: la forma moderna de formatear

Antepón una `f` al texto y escribe las variables entre llaves `{}`:

```python
nombre = "Laura"
edad = 20
print(f"Hola, {nombre}. Tienes {edad} años.")
```

Dentro de las llaves puedes hacer cálculos y dar formato:

| Formato | Ejemplo | Resultado |
|---|---|---|
| Dos decimales | `f"{3.14159:.2f}"` | `3.14` |
| Separador de miles | `f"{1500000:,}"` | `1,500,000` |
| Miles y decimales | `f"{1500000:,.2f}"` | `1,500,000.00` |
| Porcentaje | `f"{0.256:.1%}"` | `25.6%` |
| Alinear a la izquierda | `f"{'Ana':<10}"` | `Ana       ` |
| Alinear a la derecha | `f"{'Ana':>10}"` | `       Ana` |
| Centrar | `f"{'Ana':^10}"` | `   Ana    ` |

## 4. Caracteres especiales

| Secuencia | Significado |
|---|---|
| `\n` | Salto de línea |
| `\t` | Tabulación |
| `\"` | Comilla doble dentro de un texto |
| `\\` | Barra invertida |

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `entrada_datos.py` | `input()` y conversión de tipos |
| `formato_salida.py` | `print()` avanzado y f-strings |
| `mini_programa_factura.py` | Un programa corto que une todo lo anterior |
| `ejercicios.md` | Enunciados para practicar |
| `soluciones.py` | Soluciones de los ejercicios |

## Errores comunes

- Olvidar convertir: `input("Edad: ") + 1` → `TypeError`.
- Escribir letras cuando se espera un número → `ValueError`. (En el [capítulo 7](../07_archivos_y_errores/README.md) aprenderás a controlarlo.)
- Olvidar la `f` antes del texto: `print("Hola {nombre}")` muestra literalmente `{nombre}`.

## Siguiente capítulo

➡️ [`03_condicionales`](../03_condicionales/README.md): hacer que el programa tome decisiones.
