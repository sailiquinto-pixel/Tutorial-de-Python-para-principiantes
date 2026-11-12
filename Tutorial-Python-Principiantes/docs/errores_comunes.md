# Guía de errores comunes en Python

Los mensajes de error de Python están en inglés, pero siguen siempre el mismo formato. Esta guía te ayuda a traducirlos.

## Cómo leer un error

```text
Traceback (most recent call last):
  File "ejemplo.py", line 3, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

1. **Última línea:** el *tipo* de error y qué pasó. ← empieza por aquí.
2. **`line 3`:** la línea donde ocurrió.
3. **El código mostrado:** la instrucción que falló.

> A veces el error real está **antes** de la línea señalada (por ejemplo, una comilla o un paréntesis sin cerrar).

## Errores de sintaxis (el programa ni siquiera arranca)

| Mensaje | Causa típica | Ejemplo y corrección |
|---|---|---|
| `SyntaxError: unterminated string literal` | Comilla sin cerrar | `print("Hola)` → `print("Hola")` |
| `SyntaxError: expected ':'` | Falta `:` en `if`, `for`, `while`, `def` | `if x > 3` → `if x > 3:` |
| `SyntaxError: '(' was never closed` | Paréntesis sin cerrar | `print("a"` → `print("a")` |
| `SyntaxError: invalid syntax` | Error genérico: operador o palabra mal escrita | Revisa la línea y la anterior |
| `IndentationError: expected an indented block` | Falta sangría después de `:` | Agrega 4 espacios a la línea siguiente |
| `IndentationError: unindent does not match` | Sangría inconsistente (espacios y tabuladores mezclados) | Usa solo espacios |

## Errores de ejecución (el programa arranca y luego falla)

| Mensaje | Qué significa | Ejemplo y corrección |
|---|---|---|
| `NameError: name 'x' is not defined` | Usas una variable que no existe (¿mal escrita? ¿sin comillas?) | `print(nombre)` sin haberla creado; o `nombre = Laura` → `"Laura"` |
| `TypeError: can only concatenate str (not "int") to str` | Unes texto con número usando `+` | `"Edad: " + 20` → `"Edad: " + str(20)` o f-string |
| `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | Sumas número y texto | Convierte con `int()` o `float()` |
| `TypeError: ... takes 2 positional arguments but 3 were given` | Llamas a una función con más (o menos) argumentos | Revisa cuántos parámetros tiene `def` |
| `ValueError: invalid literal for int() with base 10: 'hola'` | El texto no se puede convertir a número | Valida con `try/except` |
| `ZeroDivisionError: division by zero` | Divides entre cero | Comprueba `if divisor != 0` |
| `IndexError: list index out of range` | Pides una posición que no existe | La lista de 3 elementos llega hasta el índice 2 |
| `KeyError: 'edad'` | La clave no existe en el diccionario | Usa `.get("edad")` o `if "edad" in d` |
| `AttributeError: 'str' object has no attribute 'append'` | Usas un método que ese tipo no tiene | `append` es de listas, no de textos |
| `FileNotFoundError: [Errno 2] No such file or directory` | El archivo no existe o la ruta es incorrecta | Revisa el nombre y la carpeta actual |
| `ModuleNotFoundError: No module named '...'` | El módulo no está instalado o está mal escrito | Revisa la ortografía; instala con `pip install` |
| `UnboundLocalError` | Usas una variable local antes de asignarla | Revisa el alcance (capítulo 6) |

## Errores de lógica (el programa corre, pero el resultado es incorrecto)

Son los más difíciles porque **Python no muestra ningún mensaje**.

| Síntoma | Causa frecuente |
|---|---|
| El resultado de una suma sale como `"55"` en vez de `10` | Los datos son texto (`input()` sin `int()`) |
| El ciclo nunca termina | La variable de control no se actualiza |
| El ciclo da una vuelta de más o de menos | Confusión con `range(1, 5)` (llega hasta 4) |
| Un `elif` nunca se ejecuta | Una condición anterior es más amplia y se cumple primero |
| El promedio sale mal | Falta paréntesis: `a + b / 2` ≠ `(a + b) / 2` |
| La lista cambia "sola" | Usaste `b = a` en lugar de `b = a.copy()` |

## Técnicas para encontrar errores

1. **Lee el mensaje completo**, sobre todo la última línea.
2. **Imprime valores intermedios** con `print()`: `print("DEBUG:", variable, type(variable))`.
3. **Simplifica:** comenta partes del código hasta aislar la que falla.
4. **Explícalo en voz alta** (a un amigo o a un patito de goma 🦆). Funciona sorprendentemente bien.
5. **Visualiza la ejecución paso a paso** en <https://pythontutor.com/>.
6. **Busca el mensaje exacto** en internet, quitando las partes específicas de tu código (nombres de variables, rutas).
