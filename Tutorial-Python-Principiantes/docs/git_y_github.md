# Guía de Git y GitHub para publicar este tutorial

**Git** guarda el historial de cambios de tu proyecto en tu computador. **GitHub** es un sitio web donde puedes subir ese proyecto para compartirlo y respaldarlo.

## 1. Preparación (una sola vez)

1. Instala Git desde <https://git-scm.com/downloads>.
2. Crea una cuenta en <https://github.com/>.
3. Dile a Git quién eres (usa el mismo correo de tu cuenta de GitHub):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"
```

## 2. Publicar el proyecto por primera vez

**Paso 1.** En GitHub pulsa **New repository**, escribe un nombre (por ejemplo `Tutorial-Python-Principiantes`), una descripción corta y déjalo **público**. **No** marques "Add a README" porque ya tienes uno.

**Paso 2.** En la terminal, dentro de la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Publico tutorial inicial de Python"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git push -u origin main
```

**Paso 3.** Actualiza la página del repositorio en GitHub: deberías ver tus carpetas y el `README.md` mostrado como portada.

> 🔑 **Autenticación:** GitHub ya no acepta la contraseña de tu cuenta para `git push` por HTTPS. Lo más cómodo es que Git te abra una ventana del navegador para iniciar sesión (viene incluida con Git para Windows y macOS), o usar un *token de acceso personal* o la herramienta **GitHub CLI**. Consulta la documentación oficial de GitHub si te pide credenciales.

## 3. Flujo de trabajo diario

Cada vez que hagas cambios:

```bash
git status                      # ¿qué cambió?
git add .                       # preparar todos los cambios
git commit -m "Describo lo que cambié"
git push                        # subir a GitHub
```

| Comando | Para qué sirve |
|---|---|
| `git status` | Ver qué archivos cambiaron |
| `git add archivo.py` | Preparar un archivo concreto |
| `git add .` | Preparar todos los cambios |
| `git commit -m "mensaje"` | Guardar una "foto" del proyecto con un mensaje |
| `git push` | Subir los commits a GitHub |
| `git pull` | Traer cambios desde GitHub |
| `git log --oneline` | Ver el historial resumido |
| `git diff` | Ver las diferencias exactas antes de guardar |
| `git clone URL` | Descargar un repositorio completo |

## 4. Cómo escribir buenos mensajes de commit

- Describe **qué** cambiaste y, si hace falta, **por qué**.
- Usa el mismo tiempo verbal siempre (por ejemplo, presente: "Agrego ejercicios del capítulo 4").
- Evita mensajes como `cambios`, `arreglo` o `asdf`.

| ❌ Poco útil | ✅ Mejor |
|---|---|
| `cambios` | `Agrego soluciones del capítulo 3` |
| `arreglo` | `Corrijo error de indentación en ciclo_for.py` |

## 5. Qué NO subir

El archivo `.gitignore` ya excluye lo más común: `__pycache__/`, entornos virtuales (`.venv/`), archivos `.env` y los datos que generan los programas (como `presupuesto.json`).

**Nunca subas** contraseñas, claves de API ni datos personales. Si subes uno por accidente, cambiar el archivo después no basta: el secreto queda en el historial y debes considerarlo comprometido (cambia la clave).

## 6. Mejorar la presentación del repositorio

- Escribe una **descripción** y añade **topics** (por ejemplo `python`, `tutorial`, `principiantes`, `español`) con el icono de engranaje de la página principal del repositorio.
- Agrega una **licencia** (botón **Add file → Create new file**, nombre `LICENSE`, y elige una plantilla). La licencia **MIT** es una opción habitual si quieres que otras personas reutilicen el material. Si el trabajo es académico, consulta primero las indicaciones de tu docente.
- Mantén el `README.md` actualizado: es la primera impresión de tu proyecto.

## 6.1 Autoevaluación antes de publicar

- [x] Agregué mi nombre como autora en el `README.md`.
- [ ] Ejecuté todos los archivos y funcionan.
- [ ] No hay datos personales ni contraseñas.
- [ ] Los enlaces del README abren las carpetas correctas.
- [ ] Reemplacé `TU-USUARIO/TU-REPOSITORIO` por mi URL real.

## 7. Errores frecuentes

| Mensaje | Qué significa | Solución |
|---|---|---|
| `fatal: not a git repository` | Estás fuera de la carpeta del proyecto o no hiciste `git init` | Entra con `cd` o ejecuta `git init` |
| `remote origin already exists` | Ya agregaste el remoto | Usa `git remote set-url origin URL` |
| `rejected ... non-fast-forward` | GitHub tiene cambios que tú no tienes | Ejecuta `git pull` y luego `git push` |
| `nothing to commit` | No hay cambios nuevos | Normal; modifica algo primero |
| `Author identity unknown` | Falta configurar nombre y correo | Repite los comandos `git config` del paso 1 |

## Para aprender más

- Libro oficial *Pro Git* (en español): <https://git-scm.com/book/es/v2>
- Documentación de GitHub: <https://docs.github.com/es>
