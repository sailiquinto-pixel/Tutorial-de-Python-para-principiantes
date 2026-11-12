# Capítulo 5 · Estructuras de datos: listas, diccionarios, tuplas y conjuntos

Una variable guarda **un** dato. Las **estructuras de datos** guardan **muchos** datos juntos y permiten organizarlos.

## Qué aprenderás

- Crear y modificar **listas**.
- Guardar información con **diccionarios** (clave → valor).
- Conocer las **tuplas** (listas que no cambian) y los **conjuntos** (sin repetidos).
- Combinar estructuras: una lista de diccionarios.

## Cuál elegir

| Estructura | Sintaxis | Ordenada | Se puede modificar | Permite repetidos | Úsala para… |
|---|---|---|---|---|---|
| Lista | `[1, 2, 3]` | ✅ | ✅ | ✅ | Colecciones que cambian |
| Tupla | `(1, 2, 3)` | ✅ | ❌ | ✅ | Datos fijos (coordenadas) |
| Diccionario | `{"a": 1}` | ✅ (por inserción) | ✅ | Claves únicas | Datos con etiqueta |
| Conjunto | `{1, 2, 3}` | ❌ | ✅ | ❌ | Eliminar repetidos, comparar |

## 1. Listas

```python
notas = [4.0, 3.5, 4.8]
notas[0]           # 4.0  (primer elemento: índice 0)
notas[-1]          # 4.8  (último elemento)
notas.append(2.9)  # agrega al final
```

Métodos más usados:

| Método | Qué hace |
|---|---|
| `lista.append(x)` | Agrega `x` al final |
| `lista.insert(i, x)` | Inserta `x` en la posición `i` |
| `lista.remove(x)` | Elimina la primera aparición de `x` |
| `lista.pop()` | Quita y devuelve el último (o el de índice dado) |
| `lista.sort()` | Ordena la lista (la modifica) |
| `lista.reverse()` | Invierte el orden |
| `len(lista)` | Cantidad de elementos |
| `sum(lista)`, `min(lista)`, `max(lista)` | Suma, mínimo y máximo |
| `x in lista` | ¿Está `x` en la lista? |

También funcionan los **rebanados**: `lista[1:3]`, `lista[:2]`, `lista[::-1]`.

## 2. Diccionarios

```python
estudiante = {"nombre": "Laura", "semestre": 3}
estudiante["nombre"]            # "Laura"
estudiante["carrera"] = "Economía"   # agrega o modifica
```

| Método | Qué hace |
|---|---|
| `d.get("clave", defecto)` | Devuelve el valor o el `defecto` si no existe (sin error) |
| `d.keys()` / `d.values()` / `d.items()` | Claves, valores o pares |
| `d.pop("clave")` | Elimina y devuelve el valor |
| `"clave" in d` | ¿Existe la clave? |

> Si usas `d["clave_que_no_existe"]` obtienes un `KeyError`. Para evitarlo usa `.get()` o comprueba antes con `in`.

## 3. Tuplas y conjuntos

```python
coordenada = (4.6, -74.1)      # tupla: no se puede cambiar
colores = {"rojo", "azul", "rojo"}   # conjunto: queda {"rojo", "azul"}
```

## 4. Estructuras anidadas

Es muy común guardar una **lista de diccionarios** para representar varios registros con los mismos campos:

```python
gastos = [
    {"descripcion": "Arriendo", "valor": 900000},
    {"descripcion": "Mercado", "valor": 350000},
]
```

Esta es justo la forma que usa el [proyecto final](../proyecto_final/README.md).

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `listas.py` | Crear, modificar, ordenar y recorrer listas |
| `diccionarios.py` | Crear, consultar y recorrer diccionarios |
| `tuplas_y_conjuntos.py` | Tuplas, conjuntos y sus operaciones |
| `estructuras_anidadas.py` | Lista de diccionarios y diccionario de listas |
| `ejercicios.md` | Enunciados |
| `soluciones.py` | Soluciones |

## Errores comunes

- `IndexError`: pedir una posición que no existe (`lista[10]` en una lista de 3 elementos).
- `KeyError`: pedir una clave que no existe en un diccionario.
- Confundir `lista.sort()` (modifica la lista, devuelve `None`) con `sorted(lista)` (devuelve una lista nueva).
- Copiar una lista con `b = a`: **no** crea una copia, ambas variables apuntan a la misma lista. Usa `b = a.copy()`.

## Siguiente capítulo

➡️ [`06_funciones`](../06_funciones/README.md): organizar tu código en bloques reutilizables.
