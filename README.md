
# Python desde cero: tutorial para principiantes

**Autora:** SAili Listeh Quinto Palacios  
**Nivel:** principiante (no se necesita experiencia previa)  
**Idioma:** español  
**Herramientas:** Python 3, Visual Studio Code y Git/GitHub  
**Estado:** proyecto educativo en desarrollo

## Descripción

Este repositorio es un curso práctico para aprender los fundamentos de Python desde cero. Cada capítulo incluye:

- 📖 **Explicación** de los conceptos en su propio `README.md`, con tablas y ejemplos.
- 💻 **Archivos de código** ejecutables y comentados línea por línea.
- ✏️ **Ejercicios** de tres niveles (básico, intermedio y desafío).
- ✅ **Soluciones** para comprobar tu trabajo.

Al terminar habrás construido un programa completo de control de presupuesto personal que guarda sus datos en un archivo.

## Objetivos de aprendizaje

Al finalizar el tutorial podrás:

- Reconocer la sintaxis básica de Python y leer mensajes de error.
- Usar variables, tipos de datos y operadores.
- Leer datos ingresados por el usuario y mostrar resultados con formato.
- Tomar decisiones con condicionales.
- Repetir instrucciones mediante ciclos.
- Organizar información en listas, diccionarios, tuplas y conjuntos.
- Crear y utilizar funciones y módulos.
- Controlar errores y guardar información en archivos de texto y JSON.
- Aplicar todo lo aprendido en un pequeño proyecto real.

## Contenido

| # | Carpeta | Tema | Qué encontrarás |
|---|---|---|---|
| 0 | [`00_introduccion`](00_introduccion/) | Primeros pasos | Qué es Python, `print()`, comentarios, indentación |
| 1 | [`01_fundamentos`](01_fundamentos/) | Variables, tipos y operadores | Tipos de datos, conversiones, operadores y cadenas de texto |
| 2 | [`02_entrada_salida`](02_entrada_salida/) | `input()` y `print()` | Lectura de datos, f-strings y formato de tablas |
| 3 | [`03_condicionales`](03_condicionales/) | `if`, `elif` y `else` | Decisiones, operadores lógicos y menús |
| 4 | [`04_ciclos`](04_ciclos/) | `for` y `while` | `range()`, `break`, `continue` y ciclos anidados |
| 5 | [`05_estructuras_datos`](05_estructuras_datos/) | Listas, diccionarios, tuplas y conjuntos | Métodos, recorridos y estructuras anidadas |
| 6 | [`06_funciones`](06_funciones/) | Funciones y módulos | Parámetros, `return`, alcance, `math`, `random`, `datetime` |
| 7 | [`07_archivos_y_errores`](07_archivos_y_errores/) | Errores y archivos | `try/except`, lectura y escritura, JSON |
| — | [`ejercicios`](ejercicios/) | Repaso e integración | 7 retos que combinan varios temas |
| — | [`proyecto_final`](proyecto_final/) | Presupuesto personal | Dos versiones: básica y con archivo |
| — | [`docs`](docs/) | Material de apoyo | Instalación, Git/GitHub, errores comunes, glosario, recursos |

## Estructura del repositorio

```text
Tutorial-Python-Principiantes/
├── README.md
├── .gitignore
├── 00_introduccion/
│   ├── README.md
│   ├── hola_mundo.py
│   └── comentarios_e_indentacion.py
├── 01_fundamentos/
│   ├── README.md
│   ├── variables.py · tipos_datos.py · operaciones.py · cadenas_texto.py
│   ├── ejercicios.md
│   └── soluciones.py
├── 02_entrada_salida/        (misma estructura: README, ejemplos, ejercicios, soluciones)
├── 03_condicionales/
├── 04_ciclos/
├── 05_estructuras_datos/
├── 06_funciones/
├── 07_archivos_y_errores/
├── ejercicios/
│   ├── README.md · ejercicios_practicos.py · retos_integradores.md
│   └── soluciones/           (reto_01 … reto_07)
├── proyecto_final/
│   ├── README.md
│   ├── presupuesto_personal.py
│   └── presupuesto_con_archivo.py
└── docs/
    ├── instalacion.md · git_y_github.md · errores_comunes.md
    └── glosario.md · recursos.md
```

## Requisitos

1. Instalar [Python 3](https://www.python.org/downloads/) (versión 3.8 o superior).
2. Instalar [Visual Studio Code](https://code.visualstudio.com/).
3. En VS Code, instalar la extensión **Python** de Microsoft.
4. (Opcional, para publicar el proyecto) Instalar [Git](https://git-scm.com/downloads) y crear una cuenta en [GitHub](https://github.com/).

¿Necesitas ayuda con la instalación? Consulta la [guía paso a paso](docs/instalacion.md).

## Cómo ejecutar los archivos

Abre esta carpeta en Visual Studio Code. Abre **Terminal → New Terminal** y ejecuta, por ejemplo:

```bash
python 01_fundamentos/variables.py
```

En algunos equipos Windows puede ser necesario usar `py` en lugar de `python`, y en macOS/Linux `python3`:

```bash
py 01_fundamentos/variables.py
python3 01_fundamentos/variables.py
```

Ejecuta los demás archivos siguiendo la ruta que aparece en el índice.

> Algunos archivos piden datos con `input()`: el programa se detiene hasta que escribas una respuesta y pulses **Enter**. Para cancelar un programa en cualquier momento usa `Ctrl + C`.

## Ruta recomendada de aprendizaje

Para cada capítulo:

1. **Lee** el `README.md` de la carpeta.
2. **Ejecuta** cada ejemplo sin modificarlo y observa el resultado.
3. **Modifica** los valores y predice qué pasará antes de ejecutar.
4. **Resuelve** los ejercicios de `ejercicios.md` en un archivo propio.
5. **Compara** con `soluciones.py` (después de intentarlo).
6. **Explica** con tus palabras qué hace cada programa.

### Plan sugerido

| Semana | Capítulos | Dedicación aproximada |
|---|---|---|
| 1 | 0, 1 y 2 | 4–6 horas |
| 2 | 3 y 4 | 4–6 horas |
| 3 | 5 y 6 | 5–7 horas |
| 4 | 7, retos y proyecto final | 6–8 horas |

Es solo una guía: avanza a tu ritmo y repite los capítulos que necesites.

## Material de apoyo

- 🛠️ [Instalación paso a paso](docs/instalacion.md)
- 🐞 [Guía de errores comunes](docs/errores_comunes.md)
- 📚 [Glosario](docs/glosario.md)
- 🌱 [Git y GitHub](docs/git_y_github.md)
- 🔗 [Recursos para seguir aprendiendo](docs/recursos.md)

## Publicar en GitHub

Crea un repositorio vacío en GitHub. Abre la terminal en la carpeta principal del proyecto y ejecuta:

```bash
git init
git add .
git commit -m "Publico tutorial inicial de Python"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git push -u origin main
```

Reemplaza la dirección de ejemplo por la URL real de tu repositorio. Para publicar cambios posteriores:

```bash
git add .
git commit -m "Actualizo ejercicios y ejemplos"
git push
```

Más detalles, comandos útiles y solución de errores en la [guía de Git y GitHub](docs/git_y_github.md).

## Preguntas frecuentes

**¿Necesito saber programar?** No. El tutorial parte desde cero.

**¿Qué hago si un ejemplo da error?** Lee la última línea del mensaje y busca su significado en la [guía de errores](docs/errores_comunes.md).

**¿Puedo ver las soluciones antes de intentar?** Puedes, pero aprenderás mucho más si primero lo intentas durante al menos 15 minutos.

**¿Los ejemplos usan librerías externas?** No. Todo funciona con la biblioteca estándar de Python, sin instalar nada adicional.

## Cómo contribuir

¿Encontraste un error o tienes una idea para mejorar el tutorial? Abre un *issue* en el repositorio o envía un *pull request* describiendo tu cambio.

## Licencia

Puedes añadir una licencia si deseas permitir que otras personas reutilicen el material (por ejemplo, MIT). Si el proyecto es únicamente académico, consulta primero las indicaciones de tu docente. Consulta la [guía de Git y GitHub](docs/git_y_github.md) para ver cómo agregarla.
