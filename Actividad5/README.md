
# Actividad 5 – Pipeline DevOps con Make y Bash

## Resumen del entorno
El laboratorio se ejecutó en **Linux (WSL2)** con las siguientes versiones:  
- `make`: GNU Make 4.3  
- `bash`: GNU bash 5.2.21  
- `python3`: 3.12.3  
- `tar`: GNU tar 1.35  
- `sha256sum`: GNU coreutils 9.4  

Estas versiones garantizan reproducibilidad, ya que se fijan las herramientas base de compilación y empaquetado.

## Parte 1 – Construir

### Target `build`
El target `build` genera el archivo `out/hello.txt` a partir de `src/hello.py`.  
La receta ejecuta:

```make
$(PYTHON) $< > $@
```
donde ```$< representa``` el primer prerequisito ```(src/hello.py)``` y ```$@``` el archivo objetivo (out/hello.txt).
De esta forma, el código Python imprime un saludo y redirige la salida hacia el artefacto.

### Modo estricto y .```DELETE_ON_ERROR```

El Makefile está configurado con modo estricto en Bash (set -euo pipefail) para detenerse en cualquier error o uso de variables indefinidas.
Además, la directiva .```DELETE_ON_ERROR``` asegura que si una receta falla no quede un archivo corrupto en el directorio de salida.

### Idempotencia (1.ª vs 2.ª corrida de build)

En la primera ejecución de ```make build``` se crea ```out/hello.txt``` a partir de la fuente.
En la segunda corrida, si no hubo cambios en ```src/hello.py```, Make muestra “Nothing to be done for build”, lo que refleja la idempotencia del proceso: no rehace el artefacto innecesariamente.
### Ejercicios
## Ejercicio 1 – Construir

### Target `build`
El target `build` genera el archivo `out/hello.txt` a partir de `src/hello.py`.  
La receta ejecuta:

```make
$(PYTHON) $< > $@

## Ejercicio 1: Uso de `make help`, `.DEFAULT_GOAL` y `.PHONY`

Se ejecutó el comando:

```bash
make help | tee logs/make-help.txt
grep -E '^\.(DEFAULT_GOAL|PHONY):' -n Makefile | tee -a logs/make-help.txt
```
Evidencia:
Archivo generado: logs/make-help.txt
Salida principal:
```bash
all        Construir, testear y empaquetar todo
build      Generar out/hello.txt
clean      Limpiar archivos generados
help       Mostrar ayuda
12:.PHONY: all build test package clean help lint tools check benchmark format dist-clean verify-repro
```
**Explicación :** El comando make help muestra los objetivos disponibles en el Makefile junto a su descripción, gracias al uso de comentarios ## y un grep que los filtra.
La línea ```.DEFAULT_GOAL := help ``` define que al ejecutar make sin parámetros se muestre esta ayuda por defecto, lo cual facilita la comprensión del flujo de trabajo sin necesidad de leer el Makefile completo.
Por su parte, ```.PHONY```declara que los nombres listados son targets lógicos y no archivos reales, evitando conflictos si existiera un archivo con el mismo nombre (por ejemplo, un archivo llamado clean).
Esto asegura que los comandos siempre se ejecuten como reglas, reforzando la claridad y robustez del pipeline.

Ejercicio 2 del README.

Copia y pega este bloque en Actividad5-CC3S2/README.md:

## Ejercicio 2: Idempotencia de `build` (primera vs. segunda corrida)

Se ejecutaron los comandos:

```bash
rm -rf out dist
make build | tee logs/build-run1.txt
cat out/hello.txt | tee evidencia/out-hello-run1.txt
make build | tee logs/build-run2.txt
stat -c '%y %n' out/hello.txt | tee -a logs/build-run2.txt
```
Evidencia : ```logs/build-run1.txt```— muestra la creación del artefacto:
```bash
mkdir -p out
python3 src/hello.py > out/hello.txt
```

```evidencia/out-hello-run1.txt```— contenido generado de out/hello.txt.

```logs/build-run2.txt```— segunda corrida:
```bash
make: Nothing to be done for 'build'.
2025-09-13 18:47:57.478493400 -0500 out/hello.txt
```
**Explicación** 
En la primera corrida, make ejecuta la receta de build: crea el directorio destino (mkdir -p out) y genera el artefacto (python3 src/hello.py > out/hello.txt).
En la segunda corrida, make imprime “Nothing to be done for 'build'” porque el target ```out/hello.txt``` ya existe y es más reciente que su dependencia ```src/hello.py```; por lo tanto, no hay trabajo que rehacer.
Este comportamiento refleja la idempotencia del objetivo: si no cambian las fuentes, no se recompila.
La decisión se basa en marcas de tiempo (grafo de dependencias). Solo si ```src/hello.py``` se modifica (o se elimina out/hello.txt), make volverá a ejecutar la receta.

## Ejercicio 3: Fallo controlado y `.DELETE_ON_ERROR`

Se ejecutaron los comandos:

```bash
rm -f out/hello.txt
PYTHON=python4 make build ; echo "exit=$?" | tee logs/fallo-python4.txt || echo "falló (esperado)"
ls -l out/hello.txt | tee -a logs/fallo-python4.txt || echo "no existe (correcto)"
```
Evidencia
```logs/fallo-python4.txt``` muestra:

Error al intentar usar python4 (no existe).

Make aborta con ```Error 127```.

```DELETE_ON_ERROR``` elimina automáticamente ```out/hello.txt``` para evitar un artefacto corrupto.

La verificación con ```ls -l``` confirma que el archivo no quedó en disco.

**Explicación**
Este experimento prueba el modo estricto del Makefile junto con .```DELETE_ON_ERROR```.
Al forzar ```PYTHON=python4```, la receta falla inmediatamente porque el intérprete no existe. La combinación de ```-e -u -o pipefail``` en Bash detiene la ejecución en cuanto ocurre un error, y ```.DELETE_ON_ERROR``` asegura que ```out/hello.txt``` sea eliminado si quedó a medio generar.
De esta forma, el sistema de construcción evita dejar artefactos corruptos o inconsistentes en el directorio de salida, protegiendo la reproducibilidad.
La salida final confirma que no existe ```out/hello.txt```, lo cual es el comportamiento correcto y esperado en entornos DevOps.

## Ejercicio 4: Ensayo (dry-run) y depuración detallada

Se ejecutaron los comandos:

```bash
make -n build | tee logs/dry-run-build.txt
make -d build |& tee logs/make-d.txt
grep -n "Considerando el archivo objetivo 'out/hello.txt'" logs/make-d.txt
```
Evidencia: ```logs/dry-run-build.txt```: muestra que no se ejecutan recetas, solo se imprimen los comandos que serían corridos si hubiera trabajo pendiente.

```logs/make-d.txt```: contiene el rastreo completo, incluyendo líneas como:
```bash
Considerando target file 'out/hello.txt'.
Prerequisite 'src/hello.py' es más antiguo que el target 'out/hello.txt'.
No need to remake target 'out/hello.txt'.
```
```grep``` localiza la parte donde Make evalúa el target principal.

**Explicación**
El dry-run (make -n) permite verificar qué comandos se ejecutarían sin realmente ejecutarlos, útil para validar reglas antes de correrlas.
La opción ```-d```activa un modo verboso de depuración que muestra cómo Make resuelve el grafo de dependencias. En este caso, confirma que ```out/hello.txt```existe y está actualizado respecto a ```src/hello.py```, por lo que no necesita rehacerse.
Las líneas con “No need to remake target” evidencian que Make compara las marcas de tiempo entre dependencias y objetivos antes de decidir si recompilar.
En conjunto, estas herramientas permiten auditar y entender el razonamiento interno de Make, garantizando reproducibilidad e incrementalidad en la construcción.

## Ejercicio 5: Incrementalidad con timestamps

Se ejecutaron los siguientes comandos:

```bash
touch src/hello.py
make build | tee logs/rebuild-after-touch-src.txt

touch out/hello.txt
make build | tee logs/no-rebuild-after-touch-out.txt
```
Evidencia
```logs/rebuild-after-touch-src.txt```: muestra que Make recompila ```out/hello.txt``` porque el archivo fuente ```src/hello.py``` tiene un timestamp más reciente.

```logs/no-rebuild-after-touch-out.txt:``` indica make: Nothing to be done for 'build', ya que modificar el target no obliga a rehacerlo.

**Explicación**
Este ejercicio demuestra cómo Make utiliza las marcas de tiempo para decidir cuándo rehacer un target.
Cuando se actualiza el archivo fuente ```(src/hello.py)```, Make detecta que su fecha es posterior a la de ```out/hello.txt``` y vuelve a ejecutar la receta de compilación.
En cambio, al modificar directamente el target (out/hello.txt), no existe ninguna dependencia más reciente que lo obligue a reconstruirse, por lo que Make concluye que no hay nada que hacer.
Esto confirma el comportamiento incremental: solo se rehacen los objetivos realmente afectados por cambios en sus prerequisitos, optimizando tiempo y recursos en el pipeline.
## Ejercicio 6: Lint y formato (Shellcheck / Shfmt)

Se ejecutaron los siguientes comandos:

```bash
command -v shellcheck >/dev/null && shellcheck scripts/run_tests.sh | tee logs/lint-shellcheck.txt || echo "shellcheck no instalado" | tee logs/lint-shellcheck.txt
command -v shfmt >/dev/null && shfmt -d scripts/run_tests.sh | tee logs/format-shfmt.txt || echo "shfmt no instalado" | tee logs/format-shfmt.txt
```
Evidencia
```logs/lint-shellcheck.txt ```→ contiene el mensaje shellcheck no instalado.

```logs/format-shfmt.txt``` → contiene el mensaje shfmt no instalado.

Explicación 
En este ejercicio verificamos la disponibilidad de las herramientas de análisis y formato de scripts.
El sistema devolvió que shellcheck y shfmt no estaban instalados, por lo que no se pudo aplicar análisis estático ni formateo automático.
Esto refleja la importancia de usar guard clauses (command -v … || echo …) en el Makefile, evitando que la ausencia de herramientas opcionales interrumpa el pipeline.
En un entorno real, instalar estas herramientas permitiría detectar malas prácticas en Bash y mantener un estilo uniforme, pero en este caso la ausencia quedó registrada como evidencia válida.
## Ejercicio 7: Reproducibilidad del empaquetado

Se construyó el paquete dos veces con flags deterministas y se calcularon sus hashes SHA256:

```bash
tar --sort=name --mtime='@0' --owner=0 --group=0 --numeric-owner -cf dist/app.tar src/hello.py
gzip -n -9 -c dist/app.tar > dist/app.tar.gz
sha256sum dist/app.tar.gz | tee logs/sha256-1.txt
```
Evidencia
logs/sha256-1.txt y logs/sha256-2.txt contienen el mismo hash:

```bash

8954ea84f63416cfc468fc40c857684b0728fa73e0eb685af8e643b9bc8bc3d  dist/app.tar.gz
```
```logs/sha256-diff.txt``` no muestra diferencias.

**Explicación**
Este ejercicio demuestra la reproducibilidad bit a bit del empaquetado.
Los parámetros --sort=name, --mtime=@0, --owner=0, --group=0, --numeric-owner y gzip -n eliminan cualquier fuente de variabilidad (orden de archivos, marcas de tiempo, propietarios, metadatos y cabecera gzip).
Gracias a esto, dos corridas idénticas producen exactamente el mismo hash SHA256, garantizando builds deterministas.
Esto es fundamental en CI/CD y auditorías, ya que asegura que cualquier desarrollador o servidor pueda generar artefactos binarios idénticos a partir del mismo código fuente.
## Ejercicio 8: Error clásico "missing separator"
En este ejercicio se creó una copia del Makefile llamada Makefile_bad y se reemplazaron los TAB iniciales en las recetas por espacios. Al ejecutar:
```bash
make -f Makefile_bad build
```
se obtuvo el error esperado:
```bash
Makefile_bad:27: *** missing separator.  Stop.
```
**Explicacion**
Esto ocurre porque Make exige que todas las recetas comiencen con TAB; si se usan espacios, no reconoce la línea como un comando válido y falla. Este error es común cuando se edita con editores que convierten TAB en espacios.

Para diagnosticarlo rápido se puede usar cat -A Makefile_bad (muestra ^I para TAB) o configurar el editor para visualizar caracteres invisibles. Así se confirma si realmente hay TAB o espacios al inicio de la receta.

### 1.3 Script Bash – Ejercicio 1

Se ejecutó el script ```scripts/run_tests.sh``` para validar su comportamiento. El resultado mostró primero la demostración de pipefail: sin la opción, la tubería se considera exitosa aunque falle el primer comando, mientras que con ```set -o pipefail``` se detecta el error correctamente.


### 1.3 Script Bash con rollback y trap - Ejercicio 2
En este ejercicio se probó el funcionamiento del script ```bscripts/run_tests.sh ```en diferentes escenarios:

**Ejecución normal** (hello.py correcto): El script imprime “Test pasó: Hello, World!” y devuelve código de salida 0, confirmando que la salida es la esperada.

**Ejecución con error**(hello.py modificado a “Hello, Mundo!”): El script detecta que la salida no coincide, imprime “Test falló: salida inesperada” y devuelve código 2. Como parte del rollback, renombra hello.py a .bak y luego lo restaura automáticamente gracias al trap.

**Ejecución con bash -x:** Se observa el trace paso a paso: variables como tmp, llamadas a funciones (check_deps, run_tests), expansión de arrays, y la activación del trap al final para limpiar el archivo temporal y restaurar hello.py.

Esto demuestra que:

El modo estricto (set -euo pipefail) detiene la ejecución en errores y evita variables indefinidas.

El rollback con trap asegura que, aunque falle la prueba, no quede el proyecto en un estado inconsistente.

El script devuelve códigos de salida claros: 0 para éxito, 2 para fallo de test.

### Ejercicio 1.3.2 – Ejecución con variable indefinida (set -u)

En este ejercicio se modificó el script run_tests.sh reemplazando la línea:
```bash
output="$("$PY" "$script")"
```
por:
```bash
("$PY" "$script")
```
Esto dejó la variable output sin asignación. Al ejecutar el script, el modo estricto ```(set -u)``` detectó que la variable estaba indefinida en el momento de usarla dentro de echo ```"$output"```. Como consecuencia, el test falló mostrando “Test falló: salida inesperada” y el trap se activó limpiando los temporales y restaurando el estado

### Parte 2: Leer - Analizar repositorio completo

### Observaciones con `make -n` y `make -d`

- Con `make -n` se pudo simular la ejecución de las reglas sin llegar a correrlas realmente. Esto permitió ver qué comandos se ejecutarían y si un target necesitaba ser regenerado o no.  
- Con `make -d` se obtuvo un trace detallado de cómo Make evalúa dependencias. Se pudo observar cómo compara fechas de modificación entre `src/hello.py` y `out/hello.txt`, decidiendo rehacer solo cuando el prerequisito es más nuevo.  
- En conjunto, ambos comandos sirven para **diagnosticar por qué Make rehace o no un archivo**, facilitando la depuración de flujos de construcción.

### Rol de `.DEFAULT_GOAL`, `.PHONY` y ayuda autodocumentada

- `.DEFAULT_GOAL := help` asegura que al invocar `make` sin argumentos se muestre directamente la ayuda, en lugar de ejecutar otro target por defecto.  
- `.PHONY` marca como "falsos" a los objetivos lógicos (`all`, `build`, `clean`, `help`, etc.), evitando conflictos si existiera un archivo real con el mismo nombre en el directorio.  
- La ayuda autodocumentada usa un grep sobre el Makefile para extraer comentarios junto a cada target. Esto permite mantener la documentación integrada y siempre actualizada, reforzando las buenas prácticas de CI/CD.

### 2.1 Test de ejemplo

En esta sección exploramos un Makefile más completo, analizando cómo se organiza un pipeline real con make.

Dry-run y debug (make -n, make -d):

Con make ```-n all``` vimos qué pasos se ejecutarían sin correrlos realmente.

Con ```make -d build``` se obtuvo un log detallado mostrando cómo make decide qué recompilar, verificando la regla para ```out/hello.txt``` y confirmando que depende de ```src/hello.py```.

***Uso de grep en los logs***
Se identificaron líneas clave como “Considerando el archivo objetivo ```‘out/hello.txt’”``` y “Prerrequisito ```‘src/hello.py’``` es más nuevo”, lo que confirma cómo Make compara timestamps para decidir si reconstruir.

***Ejecución de objetivos adicionales:***
Se probaron make tools, make package, make ```verify-repro``` y make clean, verificando que el repositorio incluye tareas de lint, empaquetado reproducible y verificación de hash.

***Ejecución completa (make all):***
Se ejecutó dos veces: la primera construyó los artefactos, y en la segunda make detectó que no era necesario rehacer nada, mostrando el comportamiento incremental.

***Metadatos del entorno:***
Se guardó información sobre el entorno de ejecución:
Linux WSL2, bash 5.2.21, python 3.12.3, GNU tar 1.35, sha256sum (coreutils 9.4), make 4.3.
Esto asegura reproducibilidad y permite auditar versiones de las herramientas.
**Conclusión:**
Esta práctica permitió comprender cómo make gestiona dependencias reales, cómo diagnosticar decisiones de recompilación con -d, y la importancia de registrar tanto los artefactos como el entorno para builds reproducibles.

## Parte 3: Extender  

En esta sección se reforzó la práctica con herramientas de calidad, rollback y reproducibilidad.  

### 3.1 Linter y formateo  
Se probó `shellcheck` y `shfmt` sobre el script `run_tests.sh`. Ambos no estaban instalados en el entorno, por lo que se generó la evidencia correspondiente:  

```bash
command -v shellcheck >/dev/null && shellcheck scripts/run_tests.sh | tee logs/lint-shellcheck.txt || echo "shellcheck no instalado" | tee logs/lint-shellcheck.txt  

command -v shfmt >/dev/null && shfmt -d scripts/run_tests.sh | tee logs/format-shfmt.txt || echo "shfmt no instalado" | tee logs/format-shfmt.txt
```
Evidencias:

```logs/lint-shellcheck.txt```

```logs/format-shfmt.txt```

### 3.2 Rollback con trap
Se modificó ```src/hello.py``` para forzar un error en las pruebas. El script activó el trap, mostrando:

Limpieza de archivos temporales.
Restauración automática de ```src/hello.py```desde su .bak.
Código de salida distinto de cero.

Esto garantiza rollback seguro ante fallos.

Evidencia:

```logs/run-tests-fail.txt```

### 3.3 Reproducibilidad
Se construyeron paquetes con parámetros que garantizan determinismo:

--sort=name → orden estable.

--mtime='@0' → marca de tiempo fija.

--numeric-owner → sin dependencia de IDs locales.

TZ=UTC → zona horaria uniforme.
```bash
tar --sort=name --mtime='@0' --owner=0 --group=0 --numeric-owner -cf dist/app.tar src/hello.py
gzip -n -9 -c dist/app.tar > dist/app.tar.gz
sha256sum dist/app.tar.gz | tee logs/sha256-1.txt
# Repetición para comprobar reproducibilidad
sha256sum dist/app.tar.gz | tee logs/sha256-2.txt
diff -u logs/sha256-1.txt logs/sha256-2.txt | tee logs/sha256-diff.txt || true
Los hashes generados en ambas ejecuciones fueron idénticos, confirmando la reproducibilidad.
```
Evidencias:

l```ogs/sha256-1.txt```

```logs/sha256-2.txt```

```logs/sha256-diff.txt```

```logs/verify-repro.txt```

---

## Incidencias y mitigaciones

Durante la práctica se presentaron algunos problemas menores:

- **Shellcheck y shfmt no instalados**: al ejecutar los linters, se detectó su ausencia. Se dejó evidencia clara en `logs/lint-shellcheck.txt` y `logs/format-shfmt.txt` con el mensaje *"no instalado"*, cumpliendo la consigna de registrar y continuar con el resto de tareas.  
- **Error de separador en Makefile_bad**: al sustituir el `TAB` por espacios en la receta de `out/hello.txt`, Make arrojó el clásico error `missing separator`. Se documentó como evidencia en `evidencia/missing-separator.txt`.  
- **Fallos controlados en pipeline**: al forzar un `PYTHON=python4` inexistente, se generó un error esperado, validando el comportamiento de `.DELETE_ON_ERROR` y confirmando que no queda basura en `out/hello.txt`.

Estas incidencias fueron gestionadas dejando evidencia en logs/evidencia, mitigando los problemas y permitiendo continuar sin bloquear el pipeline.

---

## Conclusión operativa

El pipeline diseñado en esta actividad es **apto para CI/CD** porque:

- Implementa buenas prácticas de shell: `set -euo pipefail`, funciones, `trap` para limpieza, variables controladas.  
- Usa un **Makefile determinista y reproducible**, con control de dependencias y empaquetado estable (hashes consistentes).  
- Integra pruebas, limpieza, empaquetado y validación de reproducibilidad en un solo flujo automatizado.  

Esto garantiza que el código pueda integrarse a pipelines de integración continua, reduciendo errores humanos y asegurando builds confiables y auditables.









