# Capítulo 7 · Manejo de errores y archivos

Los programas reales fallan: el usuario escribe letras donde esperabas un número, un archivo no existe, se divide entre cero… En este capítulo aprenderás a **anticipar** esos errores y a **guardar información** para que no se pierda al cerrar el programa.

## Qué aprenderás

- Capturar errores con `try` / `except` / `else` / `finally`.
- Reconocer las excepciones más comunes.
- Leer y escribir archivos de texto con `open()` y `with`.
- Guardar y cargar estructuras de datos en formato **JSON**.

## 1. Excepciones: `try` / `except`

Cuando algo sale mal, Python "lanza" una **excepción** y el programa se detiene. Con `try` / `except` puedes controlarla:

```python
try:
    edad = int(input("Edad: "))
    print("Dentro de un año tendrás", edad + 1)
except ValueError:
    print("Debes escribir un número entero.")
```

| Bloque | Se ejecuta… |
|---|---|
| `try` | Siempre; aquí va el código que podría fallar |
| `except TipoError` | Solo si ocurre ese error |
| `else` | Solo si **no** hubo error |
| `finally` | **Siempre**, haya o no error (útil para "limpiar") |

### Excepciones frecuentes

| Excepción | Cuándo ocurre |
|---|---|
| `ValueError` | Valor con tipo correcto pero contenido inválido: `int("hola")` |
| `TypeError` | Operación entre tipos incompatibles: `"5" + 3` |
| `ZeroDivisionError` | División entre cero |
| `IndexError` | Posición inexistente en una lista |
| `KeyError` | Clave inexistente en un diccionario |
| `FileNotFoundError` | El archivo no existe |

> **Buena práctica:** captura errores **específicos** (`except ValueError`) y evita el `except:` vacío, porque oculta fallas que sí deberías ver.

## 2. Leer y escribir archivos

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola\n")
```

`with` cierra el archivo automáticamente al terminar. Los modos más usados:

| Modo | Significado |
|---|---|
| `"r"` | Leer (por defecto). Falla si no existe |
| `"w"` | Escribir. **Borra** el contenido anterior |
| `"a"` | Agregar al final sin borrar |

> Usa siempre `encoding="utf-8"` para que las tildes y la `ñ` se guarden bien.

Formas de leer:

| Método | Resultado |
|---|---|
| `archivo.read()` | Todo el contenido como un solo texto |
| `archivo.readlines()` | Lista con una línea por elemento |
| `for linea in archivo:` | Recorre línea por línea (ideal para archivos grandes) |

## 3. Rutas de archivos

Si ejecutas el programa desde otra carpeta, una ruta relativa como `"notas.txt"` puede no encontrar el archivo. Para evitarlo, calcula la ruta a partir de la ubicación del propio script:

```python
from pathlib import Path
CARPETA = Path(__file__).parent
ruta = CARPETA / "ejemplo.txt"
```

## 4. JSON: guardar estructuras completas

JSON es un formato de texto para guardar listas y diccionarios. Es ideal para que un programa recuerde sus datos entre ejecuciones.

```python
import json

with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, ensure_ascii=False, indent=4)

with open("datos.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
```

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `manejo_errores.py` | `try`, `except`, `else`, `finally` y validación |
| `leer_archivos.py` | Tres formas de leer `ejemplo.txt` |
| `escribir_archivos.py` | Crear, sobrescribir y agregar texto |
| `json_basico.py` | Guardar y cargar un diccionario/lista con JSON |
| `ejemplo.txt` | Archivo de práctica para leer |
| `ejercicios.md` | Enunciados |
| `soluciones.py` | Soluciones |

> Los archivos que generan los scripts (`salida.txt`, `diario.txt`, `datos.json`, etc.) están en `.gitignore`, así no se suben a GitHub.

## Errores comunes

- Usar el modo `"w"` y borrar sin querer un archivo existente.
- Olvidar `encoding="utf-8"` y obtener caracteres extraños.
- Abrir un archivo que no existe (modo `"r"`) → `FileNotFoundError`.
- Leer un archivo y olvidar que cada línea termina en `\n` (usa `.strip()`).

## Siguiente paso

➡️ Practica con [`ejercicios/`](../ejercicios/README.md) y construye el [`proyecto_final`](../proyecto_final/README.md).
