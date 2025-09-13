
# Actividad 4 – Introducción a herramientas CLI en entornos Unix-like para DevSecOps
### 1. Navegación básica

En esta parte se evidencia cómo moverse entre directorios y listar archivos.

```bash
pwd | tee -a $ACT4/evidencias/pwd.txt
ls -la | tee "$ACT4/evidencias/listado_inicial.txt"
cd /tmp
pwd | tee -a "$ACT4/evidencias/pwd.txt"
### 1.2 Creación de archivos y globbing
- Se creó un directorio temporal `tmp-cli` con tres archivos (`archivo1.txt`, `archivo2.txt`, `archivo3.doc`).  
- Se listaron los archivos con patrón `archivo*.txt`.  
```
Evidencia: `globbing_archivos_txt.txt`

---
### 2. Globbing
Se crean archivos de prueba y se utilizan patrones para listarlos.
```bash
mkdir -p "$ACT4/tmp-cli" && cd "$ACT4/tmp-cli"
touch archivo1.txt archivo2.txt archivo3.doc

ls archivo*.txt | tee "$ACT4/evidencias/globbing_archivos_txt.txt"
```
Evidencias generadas:

`globbing_archivos_txt.txt`

### 3. Tuberías (Pipes)

Se combina ls con wc para contar archivos.
```bash
ls | wc -l | tee "$ACT4/evidencias/total_en_tmp_cli.txt"
```

Evidencias generadas:`total_en_tmp_cli.txt`

### 4. Redirecciones

Ejemplo de guardar salidas en archivos, añadir texto y manejar errores.
```bash
ls > "$ACT4/evidencias/lista.txt"
printf "Hola\n" >> "$ACT4/evidencias/lista.txt"
wc -l < "$ACT4/evidencias/lista.txt" | tee "$ACT4/evidencias/lista_lines.txt"
ls noexiste 2> "$ACT4/evidencias/errores.txt" || true
```

bashEvidencias generadas:

`bashlista.txt`

`bashlista_lines.txt`

`basherrores.txt`

#### 5. Uso de xargs

Se prepara un borrado seguro usando find y xargs en modo dry-run.
```bash
find . -maxdepth 1 -name 'archivo*.txt' -print0 | xargs -0 echo rm -- \
| tee "$ACT4/evidencias/xargs_dry_run.txt"
```
Evidencias generadas:```bashxargs_dry_run.txt```
