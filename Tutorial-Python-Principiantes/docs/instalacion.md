# Guía de instalación

Necesitas tres cosas: **Python**, un **editor** (Visual Studio Code) y, para publicar tu trabajo, **Git** y una cuenta de **GitHub**.

## 1. Instalar Python 3

Descarga el instalador oficial desde <https://www.python.org/downloads/>.

### Windows

1. Ejecuta el instalador.
2. ⚠️ **Marca la casilla "Add python.exe to PATH"** en la primera pantalla. Es el paso que más se olvida.
3. Pulsa **Install Now**.

### macOS

1. Descarga el instalador `.pkg` desde python.org y ábrelo.
2. En la terminal el comando suele ser `python3`.

### Linux

Casi todas las distribuciones ya traen Python 3. Para comprobarlo o instalarlo (Debian/Ubuntu):

```bash
python3 --version
sudo apt install python3 python3-pip
```

### Comprobar la instalación

Abre una terminal (en Windows: **PowerShell** o **Símbolo del sistema**) y escribe:

```bash
python --version
```

Si no funciona, prueba con `python3 --version` o `py --version`. Deberías ver algo como `Python 3.12.x`.

> **¿Qué versión necesito?** Todo el contenido funciona con Python 3.8 o superior.

## 2. Instalar Visual Studio Code

1. Descarga el editor desde <https://code.visualstudio.com/>.
2. Ábrelo y entra al panel de **Extensiones** (icono de cuadros a la izquierda o `Ctrl + Shift + X`).
3. Busca **Python** (publicada por Microsoft) e instálala.

## 3. Abrir el tutorial y ejecutar un archivo

1. En VS Code: **File → Open Folder…** y elige la carpeta `Tutorial-Python-Principiantes`.
2. Abre una terminal integrada: **Terminal → New Terminal**.
3. Ejecuta un archivo:

```bash
python 01_fundamentos/variables.py
```

También puedes abrir el archivo y pulsar el botón ▶ (**Run Python File**) de la esquina superior derecha.

## 4. Problemas frecuentes

| Problema | Causa probable | Solución |
|---|---|---|
| `python` no se reconoce como comando | Python no está en el PATH | Reinstala marcando *Add to PATH*, o usa `py` |
| Se abre la tienda de Windows al escribir `python` | Windows usa un acceso directo | Instala Python desde python.org y usa `py` |
| `python: command not found` (Mac/Linux) | El comando se llama distinto | Usa `python3` |
| `can't open file ... No such file or directory` | La terminal está en otra carpeta | Usa `cd` para entrar a la carpeta del proyecto |
| Las tildes se ven mal | Codificación del terminal | En VS Code funciona bien; en Windows prueba con `chcp 65001` |

## 5. (Opcional) Entornos virtuales

Para este tutorial **no** los necesitas, porque solo usa la biblioteca estándar. Cuando empieces a instalar paquetes externos con `pip`, es buena práctica crear uno por proyecto:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac / Linux:
source .venv/bin/activate
```

La carpeta `.venv/` ya está en `.gitignore`.
