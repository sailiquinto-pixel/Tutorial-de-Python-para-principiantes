# Capítulo 1 · Fundamentos: variables, tipos de datos y operadores

Aquí construyes la base de todo lo demás: cómo **guardar información**, qué **tipos** de información existen y cómo **operar** con ella.

## Qué aprenderás

- Crear y nombrar variables correctamente.
- Distinguir los tipos básicos: `str`, `int`, `float`, `bool`.
- Convertir un tipo en otro (`int()`, `float()`, `str()`).
- Usar operadores aritméticos, de comparación y lógicos.
- Manipular texto con métodos de cadenas.

## 1. Variables

Una **variable** es un nombre que apunta a un dato guardado en memoria. Se crea con el signo `=` (asignación):

```python
nombre = "Laura"
edad = 20
```

Reglas para los nombres:

| Regla | Ejemplo válido | Ejemplo inválido |
|---|---|---|
| Empiezan con letra o `_` | `precio`, `_total` | `1precio` |
| No tienen espacios | `precio_final` | `precio final` |
| No usan palabras reservadas | `cantidad` | `for`, `if`, `class` |
| Distinguen mayúsculas | `Edad` ≠ `edad` | — |

**Convención:** en Python se usa `snake_case` (minúsculas separadas por guion bajo): `total_gastos`, `nombre_usuario`.

## 2. Tipos de datos básicos

| Tipo | Nombre | Ejemplo | Para qué sirve |
|---|---|---|---|
| `str` | Cadena de texto | `"Hola"` | Nombres, frases |
| `int` | Entero | `15` | Cantidades, edades |
| `float` | Decimal | `3.14` | Precios, medidas |
| `bool` | Booleano | `True` / `False` | Decisiones (sí/no) |
| `NoneType` | Ausencia de valor | `None` | "Todavía no hay dato" |

Con `type(variable)` puedes consultar el tipo de cualquier dato.

### Conversión de tipos

```python
int("19")      # 19    (texto → entero)
float("3.5")   # 3.5   (texto → decimal)
str(100)       # "100" (número → texto)
```

Si el texto no tiene forma de número (por ejemplo `int("hola")`) Python lanza un `ValueError`.

## 3. Operadores

### Aritméticos

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `10 + 3` | `13` |
| `-` | Resta | `10 - 3` | `7` |
| `*` | Multiplicación | `10 * 3` | `30` |
| `/` | División | `10 / 3` | `3.3333…` |
| `//` | División entera | `10 // 3` | `3` |
| `%` | Residuo (módulo) | `10 % 3` | `1` |
| `**` | Potencia | `10 ** 3` | `1000` |

**Precedencia** (qué se calcula primero): paréntesis → `**` → `*`, `/`, `//`, `%` → `+`, `-`.

### Comparación (el resultado es `True` o `False`)

`==` igual · `!=` distinto · `>` mayor · `<` menor · `>=` mayor o igual · `<=` menor o igual

> ⚠️ Error clásico: `=` **asigna** un valor, `==` **compara**.

### Lógicos

| Operador | Significado | Es verdadero cuando… |
|---|---|---|
| `and` | y | ambas condiciones son verdaderas |
| `or` | o | al menos una es verdadera |
| `not` | no | invierte el valor |

## 4. Cadenas de texto

Los textos tienen métodos útiles: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `len(texto)`. Además puedes "cortar" partes con índices: `texto[0]` (primera letra), `texto[-1]` (última), `texto[0:3]` (primeras tres).

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `variables.py` | Crear variables, reglas de nombres, asignación múltiple |
| `tipos_datos.py` | Tipos básicos, `type()` y conversiones |
| `operaciones.py` | Operadores aritméticos, comparación y lógicos |
| `cadenas_texto.py` | Métodos y *slicing* de texto |
| `ejercicios.md` | Enunciados para practicar |
| `soluciones.py` | Soluciones (¡intenta primero sin mirar!) |

## Errores comunes

- Escribir `edad = "20"` y luego intentar `edad + 1` → `TypeError` (es texto, no número).
- Olvidar las comillas en un texto: `nombre = Laura` → `NameError`.
- Usar `=` en lugar de `==` al comparar.
- Dividir y esperar un entero: `10 / 2` da `5.0` (decimal). Para entero usa `//`.

## Siguiente capítulo

➡️ [`02_entrada_salida`](../02_entrada_salida/README.md): leer datos del usuario y mostrar resultados con formato.
