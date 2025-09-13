
# Actividad 4 – Introducción a herramientas CLI en entornos Unix-like para DevSecOps

## Sección 1: Manejo sólido de CLI

En esta primera parte se practicaron los fundamentos del uso de la línea de comandos en entornos Unix-like, con énfasis en navegación, globbing, tuberías, redirecciones y `xargs`.  

---

### 1.1 Navegación básica
- **pwd**: muestra el directorio actual.  
  Evidencia: `pwd.txt`

- **ls -la**: lista con detalle todos los archivos, incluyendo ocultos.  
   Evidencia: `listado_inicial.txt`

---

### 1.2 Creación de archivos y globbing
- Se creó un directorio temporal `tmp-cli` con tres archivos (`archivo1.txt`, `archivo2.txt`, `archivo3.doc`).  
- Se listaron los archivos con patrón `archivo*.txt`.  

Evidencia: `globbing_archivos_txt.txt`

---

### 1.3 Uso de tuberías
- Se contó el número de archivos en el directorio temporal:  

```bash
ls | wc -l
```
Evidencia: 
`total_en_tmp_cli.txt`

### 1.4 Redirecciones
Se redirigió la salida de ls hacia un archivo lista.txt.

Se agregaron líneas con printf y se verificó el conteo con wc -l.

Evidencias:

`lista.txt`

`lista_lines.txt`

### 1.5 Manejo de errores
Se forzó un error con ls noexiste y se redirigió a errores.txt.

Evidencia: `errores.txt`

### 1.6 Uso de xargs (dry-run)
Se probaron borrados seguros con find . -name 'archivo*.txt' -print0 | xargs -0 echo rm.

Evidencia: `xargs_dry_run.txt`

### 1.7 Ejercicios de reforzamiento
Se listaron archivos ocultos de /etc y se guardaron en etc_lista.txt.
Evidencia: `etc_lista.txt`

Se numeraron las líneas de un archivo con nl lista.txt.
Evidencia: `lista_numbered.txt`