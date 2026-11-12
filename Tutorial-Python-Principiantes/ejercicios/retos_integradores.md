# Retos integradores

Cada reto combina varios temas. Las soluciones están en [`soluciones/`](soluciones/), pero intenta resolverlos tú primero.

| Reto | Nombre | Dificultad | Temas |
|---|---|---|---|
| 1 | Cajero automático | ⭐⭐ | Ciclos, condicionales, funciones |
| 2 | Piedra, papel o tijera | ⭐⭐ | `random`, ciclos, condicionales |
| 3 | Analizador de texto | ⭐⭐ | Cadenas, diccionarios |
| 4 | Carrito de compras | ⭐⭐⭐ | Listas de diccionarios, formato |
| 5 | Generador de contraseñas | ⭐⭐ | `random`, cadenas, funciones |
| 6 | Libreta de calificaciones | ⭐⭐⭐ | Funciones, estructuras, estadística |
| 7 | Diario con archivos | ⭐⭐⭐ | Archivos, errores, fechas |

---

## Reto 1 · Cajero automático

Simula un cajero con saldo inicial de `$500.000` y este menú:

```
1. Consultar saldo
2. Depositar
3. Retirar
4. Salir
```

**Requisitos**
- El menú se repite hasta elegir "Salir".
- No se permiten depósitos ni retiros negativos o iguales a cero.
- No se puede retirar más de lo que hay en el saldo.
- Si el usuario escribe letras en lugar de números, el programa no debe fallar.

## Reto 2 · Piedra, papel o tijera

El usuario juega contra el computador, que elige al azar.

**Requisitos**
- Se juega al mejor de 3 victorias (primero en llegar a 3 gana).
- Los empates no suman puntos.
- Muestra el marcador después de cada ronda.
- Valida que la jugada sea una de las tres opciones.

## Reto 3 · Analizador de texto

Pide una frase y muestra:

- Cantidad de caracteres (con y sin espacios).
- Cantidad de palabras.
- Cantidad de vocales.
- La palabra más larga.
- Cuántas veces aparece cada palabra (ignorando mayúsculas y signos de puntuación).

## Reto 4 · Carrito de compras

Crea un programa donde el usuario agrega productos (nombre, precio, cantidad) hasta escribir `fin`.

**Requisitos**
- Guarda cada producto como un diccionario dentro de una lista.
- Al terminar, muestra una tabla alineada con subtotal por producto.
- Calcula el total, el IVA (19 %) y el total con IVA.
- Si el total pasa de `$200.000`, aplica un 10 % de descuento.

## Reto 5 · Generador de contraseñas

Crea la función `generar_contraseña(longitud, usar_simbolos=True)`.

**Requisitos**
- Debe incluir al menos una mayúscula, una minúscula y un número.
- Si `usar_simbolos` es `True`, debe incluir al menos un símbolo (`!@#$%&*`).
- Pide al usuario la longitud (mínimo 8) y muestra 3 contraseñas distintas.

> Pista: módulo `random` y el módulo `string` (`string.ascii_uppercase`, `string.digits`…).

## Reto 6 · Libreta de calificaciones

Crea un programa que administre estudiantes con tres notas cada uno.

**Requisitos**
- Una función para agregar estudiantes, otra para calcular el promedio de cada uno y otra para mostrar el ranking.
- Muestra el promedio del curso, la nota más alta y quién la obtuvo.
- Indica cuántos estudiantes aprobaron (promedio ≥ 3.0) y cuántos no.

## Reto 7 · Diario con archivos

Crea un diario personal por consola.

**Requisitos**
- Menú: escribir entrada, leer todas las entradas, buscar por palabra, salir.
- Cada entrada se guarda con fecha y hora en `diario.txt` (modo `"a"`).
- Si el archivo todavía no existe, "leer" debe avisarlo sin fallar.
- La búsqueda no debe distinguir mayúsculas de minúsculas.

---

### ¿Terminaste todos?

Sigue con el [proyecto final](../proyecto_final/README.md) o inventa tus propios retos: lo mejor para aprender es programar algo que te interese.
