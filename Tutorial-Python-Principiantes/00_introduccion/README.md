# Capítulo 0 · Introducción a Python

Antes de escribir código, conviene entender **qué es Python**, **qué es un programa** y **cómo se ejecuta**. Este capítulo es corto, pero te ahorra muchas dudas más adelante.

## Qué aprenderás

- Qué es Python y para qué se usa.
- Qué es un programa y qué significa "ejecutarlo".
- Cómo escribir comentarios y por qué la **indentación** es obligatoria.
- Cómo leer un mensaje de error sin asustarte.

## ¿Qué es Python?

Python es un **lenguaje de programación** de propósito general. Se usa en análisis de datos, automatización de tareas, desarrollo web, inteligencia artificial, ciencia, videojuegos y mucho más. Es muy popular para aprender porque su sintaxis se parece bastante al lenguaje natural.

Un **programa** es una lista de instrucciones que el computador sigue **en orden, de arriba hacia abajo**. Python lee tu archivo `.py` línea por línea y ejecuta cada instrucción.

## Tu primer programa

```python
print("¡Hola, mundo!")
```

`print()` es una **función** que muestra información en pantalla. Lo que va entre comillas es un **texto** (en Python se llama `str`, de *string*).

Ejecútalo desde la terminal, estando en la carpeta principal del proyecto:

```bash
python 00_introduccion/hola_mundo.py
```

> En algunos equipos Windows el comando es `py` en lugar de `python`. En macOS y Linux puede ser `python3`.

## Comentarios

Un comentario es texto que Python **ignora**. Sirve para explicar el código a quien lo lea (incluido tu yo del futuro).

```python
# Esto es un comentario de una línea
print("Hola")  # También puede ir al final de una línea
```

## Indentación

En Python los **bloques de código** se marcan con espacios al inicio de la línea. Lo habitual es usar **4 espacios**.

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")   # Esta línea pertenece al if
print("Fin del programa")         # Esta ya no
```

Si la indentación es incorrecta, Python muestra un `IndentationError`.

## Cómo leer un error

Los errores son normales; todo programador los ve a diario. Python te dice **qué** falló y **en qué línea**:

```text
  File "hola_mundo.py", line 1
    print("Hola)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Lee siempre **la última línea** primero: indica el tipo de error. En [`docs/errores_comunes.md`](../docs/errores_comunes.md) encontrarás una guía con los más frecuentes.

## Archivos de esta carpeta

| Archivo | Qué muestra |
|---|---|
| `hola_mundo.py` | Tu primer programa con `print()` |
| `comentarios_e_indentacion.py` | Comentarios, docstrings e indentación |

## Ejercicios

1. Ejecuta `hola_mundo.py` sin modificarlo.
2. Cámbialo para que muestre tu nombre y tu comida favorita en dos líneas distintas.
3. Borra una comilla a propósito y observa el error. Luego corrígelo.
4. Escribe un comentario de varias líneas explicando qué hace tu programa.

## Siguiente capítulo

➡️ [`01_fundamentos`](../01_fundamentos/README.md): variables, tipos de datos y operadores.
