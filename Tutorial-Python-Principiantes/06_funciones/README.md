# Capítulo 6 · Funciones y módulos

Una **función** es un bloque de código con nombre que puedes **reutilizar** las veces que quieras. Hacen tus programas más cortos, ordenados y fáciles de corregir.

## Qué aprenderás

- Crear funciones con `def`, parámetros y `return`.
- Usar valores por defecto y argumentos con nombre.
- Entender el **alcance** de las variables (local vs. global).
- Documentar funciones con *docstrings*.
- Usar módulos estándar como `math`, `random` y `datetime`.

## 1. Definir y llamar una función

```python
def saludar(nombre):
    """Muestra un saludo personalizado."""
    print("Hola,", nombre)

saludar("Laura")      # llamada a la función
```

| Parte | Descripción |
|---|---|
| `def` | Palabra clave que crea la función |
| `saludar` | Nombre (usa `snake_case`) |
| `(nombre)` | **Parámetro**: dato que la función recibe |
| `"""..."""` | *Docstring*: explica qué hace |
| `"Laura"` | **Argumento**: valor real que se pasa al llamarla |

## 2. `return`: devolver un resultado

`print()` **muestra** un valor; `return` **entrega** un valor para que lo uses después.

```python
def calcular_promedio(n1, n2, n3):
    return (n1 + n2 + n3) / 3

resultado = calcular_promedio(4.0, 3.5, 4.5)
```

Cuando se ejecuta `return`, la función termina. Si no hay `return`, devuelve `None`.

## 3. Parámetros

```python
def precio_final(precio, descuento=0, iva=0.19):
    ...

precio_final(1000)                    # usa los valores por defecto
precio_final(1000, 10)                # posicional
precio_final(1000, iva=0)             # con nombre
```

Las funciones también pueden devolver **varios valores** (como una tupla):

```python
def minimo_maximo(lista):
    return min(lista), max(lista)

menor, mayor = minimo_maximo([5, 2, 9])
```

## 4. Alcance de las variables

- **Variable local:** se crea dentro de la función y solo existe ahí.
- **Variable global:** se crea fuera y se puede leer desde cualquier parte.

Buena práctica: que las funciones reciban lo que necesitan por **parámetros** y entreguen resultados con **return**, en lugar de modificar variables globales.

## 5. Módulos y librerías

Python incluye muchas herramientas listas para usar. Se cargan con `import`:

```python
import math
print(math.sqrt(16))        # 4.0

from random import randint
print(randint(1, 6))        # número aleatorio entre 1 y 6
```

| Módulo | Para qué sirve |
|---|---|
| `math` | Raíces, potencias, redondeos, π |
| `random` | Números y elecciones aleatorias |
| `datetime` | Fechas y horas |

## 6. Buenas prácticas

- Una función debe hacer **una sola cosa**.
- Usa nombres que describan la acción: `calcular_total`, `es_par`, `validar_edad`.
- Escribe un docstring corto.
- Prueba tus funciones con varios valores.

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `funciones.py` | Definir, llamar y devolver valores |
| `parametros_y_retorno.py` | Parámetros por defecto, con nombre y retornos múltiples |
| `alcance_variables.py` | Variables locales y globales |
| `modulos.py` | `math`, `random` y `datetime` |
| `ejercicios.md` | Enunciados |
| `soluciones.py` | Soluciones |

## Errores comunes

- Definir la función pero **olvidar llamarla**: no se ejecuta nada.
- Confundir `print` con `return`.
- Llamar la función con una cantidad incorrecta de argumentos → `TypeError`.
- Usar una variable local fuera de su función → `NameError`.
- Poner `return` dentro de un ciclo sin querer: termina la función en la primera vuelta.

## Siguiente capítulo

➡️ [`07_archivos_y_errores`](../07_archivos_y_errores/README.md): manejar errores y guardar información en archivos.
