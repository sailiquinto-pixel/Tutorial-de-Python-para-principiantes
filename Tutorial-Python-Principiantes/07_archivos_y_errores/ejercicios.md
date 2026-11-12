# Ejercicios · Capítulo 7: Errores y archivos

Compara con [`soluciones.py`](soluciones.py) cuando termines.

## Nivel básico

**1. Entero seguro.** Pide un número entero. Si el usuario escribe algo inválido, muestra un mensaje en lugar de dejar que el programa falle.

**2. División segura.** Pide dos números y divídelos, controlando `ValueError` y `ZeroDivisionError`.

**3. Escribir.** Guarda tu nombre y tu ciudad en `perfil.txt`, cada dato en una línea.

**4. Leer.** Lee `perfil.txt` y muestra su contenido.

## Nivel intermedio

**5. Validar hasta acertar.** Crea `pedir_positivo(mensaje)` que repita hasta que el usuario escriba un número mayor que cero.

**6. Agregar líneas.** Pide frases al usuario hasta que escriba `fin`; guárdalas en `frases.txt` (modo `"a"`). Después muestra el archivo numerado.

**7. Promedio desde archivo.** Lee `ejemplo.txt` (nombre,nota) y muestra el promedio y el nombre de quien obtuvo la mejor nota.

**8. Contar palabras.** Lee un archivo de texto y muestra cuántas líneas y cuántas palabras tiene.

## Nivel desafío

**9. Lista de tareas.** Crea un programa con menú: agregar tarea, ver tareas y salir. Las tareas deben guardarse en `tareas.json` para que existan la próxima vez que lo ejecutes.

**10. Archivo inexistente.** Pide el nombre de un archivo y muéstralo; si no existe, avisa sin que el programa se detenga con un error.

**11. Convertir TXT a JSON.** Convierte `ejemplo.txt` en un archivo `estudiantes.json` con una lista de diccionarios `{"nombre": ..., "nota": ...}`.
