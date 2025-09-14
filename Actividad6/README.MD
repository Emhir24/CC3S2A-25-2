# Actividad 6: Introducción a Git (conceptos básicos y operaciones esenciales)

**Objetivo:** Configurar Git, crear un repo, preparar/confirmar cambios, ver historial y gestionar ramas (incluido un merge con conflicto y su resolución).

## Estructura de evidencias
- `logs/git-version.txt` — salida de `git --version`.
- `logs/config.txt` — salida de `git config --list` (LOCAL).
- `logs/init-status.txt` — `git init` + `git status` inicial.
- `logs/add-commit.txt` — secuencia `git add` + `git commit -m`.
- `logs/log-oneline.txt` — `git log --oneline`.
- `logs/branches.txt` — `git branch -vv`.
- `logs/merge-o-conflicto.txt` — `git merge` con conflicto y su resolución.
- (Opcionales: `revert.txt`, `rebase.txt`, `cherry-pick.txt`, `stash.txt` si se usaron.)

## Resumen por tema 

### 1) `git config`
Configuré identidad **local** (no global) para este repo de práctica y verifiqué con `git config --list`.  
Evidencia: `logs/config.txt`.

### 2) `git init`
Inicialicé un repositorio con `git init` y validé el estado inicial con `git status`.  
Evidencia: `logs/init-status.txt`.

### 3) `git add` / `git commit`
Preparé y confirmé cambios de `README.md`, `CONTRIBUTING.md` y `main.py` en commits sucesivos.  
Evidencias: `logs/add-commit.txt` y `logs/log-oneline.txt`.

### 4) `git log`
Usé `git log --oneline` para revisar el historial de manera compacta.  
Evidencia: `logs/log-oneline.txt`.

### 5) Ramas y merge (con resolución de conflicto)
Creé `feature/advanced-feature`, hice cambios allí y en `main`, provoqué un conflicto con `git merge`, lo resolví manualmente y confirmé.  
Evidencias: `logs/merge-o-conflicto.txt` (intento de merge, estado, archivo con marcadores y commit de resolución) y `logs/branches.txt`.

## Configuración inicial
Se configuró el usuario de Git con nombre y correo, y se verificó la configuración:
- `git config --list` → evidencia en `logs/config.txt`
- Se registró nombre: **Emhir** y correo: **emhirrodriguez@gmail.com**

## Inicialización del repositorio
Se creó el directorio de práctica `demo-repo`, se ejecutó `git init` y se verificó el estado inicial:
- `git init` y `git status` → evidencia en `logs/init-status.txt`

## Primer commit
Se creó el archivo `README.md` y se realizó el primer commit:
- `git add README.md`
- `git commit -m "Commit inicial con README.md"` → evidencia en `logs/add-commit.txt`

## Seguimiento del historial
Se añadieron más archivos (`CONTRIBUTING.md`, `main.py`) y se registraron commits sucesivos.
- `git log --oneline` → evidencia en `logs/log-oneline.txt`

## Manejo de ramas
Se creó la rama `feature/advanced-feature`:
- Se añadió una nueva función `greet()` en `main.py` dentro de la rama.
- En `main`, se modificó el mensaje original de `main.py`.
- Al fusionar, se generó **conflicto de merge**, resuelto manualmente.
- Evidencia: `logs/merge-o-conflicto.txt`

## Restauración de cambios (reset/restore)
Se probó la manipulación del historial:
- `git reset --hard HEAD~1` → eliminó el último commit y revirtió `main.py`.
- Se probó `git restore` para revertir cambios no confirmados en `README.md`.
- Evidencia: `logs/reset-restore.txt`

## Trabajo colaborativo y remoto
Se configuró un remoto en GitHub (`https://github.com/Emhir24/prueba`) y se probó el flujo de ramas colaborativas:
- `git branch feature/team-feature`
- `git push origin feature/team-feature`
- Se simuló un Pull Request (PR).  
URL del PR: **<https://github.com/Emhir24/prueba/pull/new/feature/team-feature>**
- Evidencia: `logs/remote-pr.txt`

## Cherry-pick y Stash
- Se creó un commit en `main.py` con el mensaje "Cherry pick!" y se aplicó en otra rama con `git cherry-pick`.
- Se probó `git stash` para guardar y luego recuperar cambios temporales:
  - `git stash push -m "stash de ejemplo en main.py"`
  - `git stash pop`
- Evidencia: `logs/cherry-stash.txt`

---


## Preguntas rápidas

**¿Cómo te ayudó Git a mantener un historial claro?**  
Cada `commit` documenta un paso atómico con mensaje; `git log --oneline` permite navegar y auditar fácilmente.

**¿Beneficios de usar ramas para nuevas features/fix?**  
Aíslan el trabajo, facilitan PRs/revisiones y evitan romper `main`; luego se integran con `merge`.

---

## Comandos que generaron cada log

- `logs/git-version.txt`: `git --version`  
- `logs/config.txt`: `git config --list`  
- `logs/init-status.txt`: `git init` y `git status` (anexado)  
- `logs/add-commit.txt`: secuencia `git add` + `git commit -m "..."`  
- `logs/log-oneline.txt`: `git log --oneline`  
- `logs/branches.txt`: `git branch -vv`  
- `logs/merge-o-conflicto.txt`: intento de `git merge`, `git status`, vista de `main.py` con marcadores y commit de resolución

## Conclusiones
1. **Git config** permite identificar al autor de cada commit y mantener trazabilidad.
2. **Init, add y commit** son la base del control de versiones: inicializar, preparar y confirmar cambios.
3. **Log** permite navegar el historial, mientras que las **ramas** y **merges** permiten trabajo paralelo y colaborativo.
4. **Reset y restore** permiten deshacer cambios, mientras que **cherry-pick** y **stash** son útiles para aplicar commits específicos o guardar cambios temporales.
5. La práctica con remoto (GitHub) y PR demuestra cómo Git soporta un flujo colaborativo real.

En resumen, Git garantiza un historial claro, control sobre los cambios, y flexibilidad para colaborar en equipo de manera organizada.
 


s