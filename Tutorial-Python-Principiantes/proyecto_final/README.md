# Proyecto final · Presupuesto personal

Aquí aplicas **todo** lo aprendido: variables, entrada y salida, condicionales, ciclos, listas, diccionarios, funciones, manejo de errores y archivos. El proyecto se construye en **dos versiones** para que veas cómo un programa va creciendo.

## Versiones

| Archivo | Nivel | Qué hace |
|---|---|---|
| `presupuesto_personal.py` | Básico | Registra un ingreso y varios gastos en una sola ejecución y calcula el saldo |
| `presupuesto_con_archivo.py` | Intermedio | Menú interactivo, categorías, resumen por categoría y **guardado en JSON** entre ejecuciones |

## Cómo ejecutarlos

Desde la carpeta principal del repositorio:

```bash
python proyecto_final/presupuesto_personal.py
python proyecto_final/presupuesto_con_archivo.py
```

> En algunos equipos Windows usa `py` en lugar de `python`.

## Versión 1 · `presupuesto_personal.py`

**Flujo del programa**

1. Pide el ingreso del mes.
2. Pregunta cuántos gastos se van a registrar.
3. Por cada gasto pide una descripción y un valor.
4. Calcula el total de gastos y el saldo (`ingreso - gastos`).
5. Muestra un resumen y un mensaje según el saldo.

**Conceptos que usa**

| Concepto | Dónde aparece |
|---|---|
| Funciones | `pedir_valor()` valida cada número |
| `while True` + `try/except` | Repite hasta recibir un número válido |
| Listas y diccionarios | `gastos` es una lista de diccionarios |
| Ciclo `for` | Registra cada gasto |
| f-strings | Formato de dinero: `${valor:,.2f}` |
| Condicionales | Mensaje final según el saldo |

## Versión 2 · `presupuesto_con_archivo.py`

Agrega lo que la versión 1 dejaba como "posible mejora":

- **Menú** para registrar ingresos y gastos cuando quieras.
- **Categorías** (Vivienda, Alimentación, Transporte…).
- **Resumen por categoría** con porcentaje del total.
- **Persistencia**: los datos se guardan en `presupuesto.json` y se cargan automáticamente la próxima vez.
- **Reinicio de datos** con confirmación.

**Estructura de los datos**

```json
{
    "ingresos": [
        {"descripcion": "Salario", "valor": 2500000}
    ],
    "gastos": [
        {"descripcion": "Arriendo", "categoria": "Vivienda", "valor": 900000}
    ]
}
```

> El archivo `presupuesto.json` está en `.gitignore`: es información personal y no debe subirse a GitHub.

## Ideas para seguir mejorando

Cuando termines, prueba a añadir una de estas mejoras (de más fácil a más difícil):

1. Mostrar el porcentaje del ingreso que representa cada gasto.
2. Permitir **eliminar** un gasto por su número.
3. Agregar una **meta de ahorro** y mostrar cuánto falta para alcanzarla.
4. Guardar la **fecha** de cada movimiento y filtrar por mes.
5. Exportar el resumen a un archivo `.csv` (módulo `csv`) para abrirlo en Excel.
6. Dividir el programa en varios archivos (`datos.py`, `calculos.py`, `main.py`) y usar `import`.

## Preguntas para reflexionar

- ¿Qué pasaría si el usuario escribe letras en lugar de un valor? ¿Dónde se controla?
- ¿Por qué `gastos` es una lista de diccionarios y no varias listas separadas?
- ¿Qué ventaja tiene separar la lógica en funciones pequeñas?
