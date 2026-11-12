# Capítulo 3 · Estructuras condicionales

Hasta ahora, tus programas ejecutaban todas las líneas en orden. Con los **condicionales** el programa puede **decidir** qué hacer según la situación.

## Qué aprenderás

- Escribir decisiones con `if`, `elif` y `else`.
- Combinar condiciones con `and`, `or` y `not`.
- Anidar condicionales y entender cuándo conviene hacerlo.
- Usar los operadores `in` y `not in`.
- Reconocer valores "verdaderos" y "falsos" en Python.

## 1. Estructura básica

```python
nota = 3.5

if nota >= 3:
    print("Aprobaste")
else:
    print("No aprobaste")
```

- La condición termina con **dos puntos `:`**.
- El código que depende de la condición va **indentado** (4 espacios).
- `else` es opcional y se ejecuta cuando ninguna condición anterior fue verdadera.

## 2. Varias opciones con `elif`

```python
if nota < 0 or nota > 5:
    print("Nota inválida")
elif nota >= 4.5:
    print("Excelente")
elif nota >= 3:
    print("Aprobaste")
else:
    print("No aprobaste")
```

Python revisa las condiciones **de arriba hacia abajo** y ejecuta solo el **primer bloque** cuya condición sea verdadera. Por eso el **orden importa**.

## 3. Operadores de comparación y lógicos

| Operador | Significado |
|---|---|
| `==` / `!=` | igual / distinto |
| `>` `<` `>=` `<=` | mayor, menor, mayor o igual, menor o igual |
| `and` | se cumplen **ambas** condiciones |
| `or` | se cumple **al menos una** |
| `not` | invierte el resultado |
| `in` / `not in` | pertenece / no pertenece a una colección o texto |

### Tabla de verdad

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

## 4. Valores "verdaderos" y "falsos"

Python considera **falsos**: `False`, `0`, `0.0`, `""` (texto vacío), `[]` (lista vacía), `{}` y `None`. Todo lo demás es **verdadero**. Por eso puedes escribir:

```python
nombre = input("Nombre: ")
if nombre:            # equivale a: if nombre != "":
    print("Hola", nombre)
```

## 5. Condicionales anidados

Puedes poner un `if` dentro de otro:

```python
if edad >= 18:
    if tiene_documento:
        print("Puede entrar")
```

Muchas veces se puede simplificar con `and`: `if edad >= 18 and tiene_documento:`.

## 6. Expresión condicional en una línea

```python
estado = "Aprobado" if nota >= 3 else "Reprobado"
```

Úsala solo cuando sea fácil de leer.

## 7. (Opcional) `match` / `case`

Desde Python 3.10 existe una estructura para comparar un valor con varias opciones:

```python
opcion = "b"
match opcion:
    case "a":
        print("Elegiste A")
    case "b":
        print("Elegiste B")
    case _:
        print("Opción desconocida")
```

Para empezar, `if / elif / else` es suficiente.

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `condicionales.py` | `if`, `elif`, `else` con la nota del estudiante |
| `operadores_logicos.py` | `and`, `or`, `not`, `in` y valores verdaderos/falsos |
| `condicionales_anidados.py` | Descuentos, año bisiesto y un menú |
| `ejercicios.md` | Enunciados |
| `soluciones.py` | Soluciones |

## Errores comunes

- Olvidar los dos puntos `:` al final del `if` → `SyntaxError`.
- Indentación inconsistente → `IndentationError`.
- Usar `=` en lugar de `==` en la condición.
- Escribir `if edad > 18 or < 30` → debe ser `if edad > 18 or edad < 30`.
- Poner las condiciones en mal orden con `elif` (primero la más específica).

## Siguiente capítulo

➡️ [`04_ciclos`](../04_ciclos/README.md): repetir instrucciones sin copiar y pegar.
