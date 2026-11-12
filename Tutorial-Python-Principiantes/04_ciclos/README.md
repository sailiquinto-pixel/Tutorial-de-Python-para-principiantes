# Capítulo 4 · Ciclos (bucles)

Un **ciclo** repite un bloque de instrucciones. En vez de escribir `print()` cien veces, escribes un ciclo que lo haga por ti.

## Qué aprenderás

- Repetir una cantidad conocida de veces con `for` y `range()`.
- Repetir mientras se cumpla una condición con `while`.
- Controlar el ciclo con `break` y `continue`.
- Usar ciclos anidados (un ciclo dentro de otro).
- Usar patrones típicos: acumuladores, contadores y validación de datos.

## 1. El ciclo `for`

Se usa cuando sabes **cuántas veces** repetir o cuando quieres **recorrer** una colección.

```python
for numero in range(1, 6):
    print(numero)        # 1, 2, 3, 4, 5
```

### `range()`

| Llamada | Genera |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

> El valor final **nunca se incluye**.

### Recorrer listas y textos

```python
for fruta in ["manzana", "pera", "mango"]:
    print(fruta)

for letra in "Hola":
    print(letra)
```

## 2. El ciclo `while`

Se usa cuando **no sabes cuántas veces** se repetirá; depende de una condición.

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1       # ¡Sin esto, el ciclo sería infinito!
```

> ⚠️ **Ciclo infinito:** si la condición nunca se vuelve falsa, el programa no termina. Para detenerlo, presiona `Ctrl + C` en la terminal.

## 3. `break` y `continue`

| Instrucción | Efecto |
|---|---|
| `break` | Termina el ciclo inmediatamente |
| `continue` | Salta a la siguiente repetición |

## 4. Patrones muy usados

**Acumulador** (sumar valores):

```python
total = 0
for n in range(1, 11):
    total += n
print(total)    # 55
```

**Contador** (contar cuántos cumplen algo):

```python
pares = 0
for n in range(1, 21):
    if n % 2 == 0:
        pares += 1
```

**Validación de datos** (repetir hasta que la entrada sea correcta):

```python
edad = int(input("Edad: "))
while edad < 0:
    print("No puede ser negativa.")
    edad = int(input("Edad: "))
```

## 5. Ciclos anidados

Por cada vuelta del ciclo externo, el interno se ejecuta completo. Es la base de las tablas y las cuadrículas.

```python
for fila in range(1, 4):
    for columna in range(1, 4):
        print(fila * columna, end=" ")
    print()
```

## ¿`for` o `while`?

| Usa `for` cuando… | Usa `while` cuando… |
|---|---|
| Sabes cuántas repeticiones hay | No sabes cuántas habrá |
| Recorres una lista, texto o rango | Esperas que ocurra algo (entrada válida, un resultado) |

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `ciclo_for.py` | `for`, `range()` y recorridos |
| `ciclo_while.py` | `while`, contadores y validación |
| `break_continue.py` | Control del ciclo y búsquedas |
| `ciclos_anidados.py` | Tablas de multiplicar y figuras |
| `ejercicios.md` | Enunciados |
| `soluciones.py` | Soluciones |

## Errores comunes

- **Ciclo infinito** por olvidar actualizar la variable de control.
- Olvidar que `range(1, 5)` llega solo hasta el 4.
- Modificar una lista mientras se recorre.
- Mala indentación: una línea dentro o fuera del ciclo cambia por completo el resultado.

## Siguiente capítulo

➡️ [`05_estructuras_datos`](../05_estructuras_datos/README.md): guardar muchos datos en listas, diccionarios y más.
