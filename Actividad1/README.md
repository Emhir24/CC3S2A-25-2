# Actividad 1: Introducción a DevOps y DevSecOps  

**Estudiante:** Emhir Rodríguez 
**Fecha:** 11/09/2025  
**Tiempo total invertido:** 00:00  

---

## Contexto del entorno  
El trabajo lo realicé en mi laptop con Windows 10, usando Visual Studio Code y el navegador Chrome.  
Para las evidencias utilicé herramientas básicas como DevTools (HTTP/TLS), nslookup (DNS) y netstat (puertos).  
  
## 4.1 DevOps vs Cascada tradicional  
**Explicación breve:**  
**cascada**: Este modelo sigue fases lineales; primero requisitos, luego diseño, después implementación, pruebas y recién al final despliegue.  
Funciona cuando los requisitos son estables, pero el problema es que el feedback llega tarde y corregir errores al final suele ser caro y lento.  

**DevOps**:Busca trabajar en ciclos más cortos y repetitivos. Se apoya en integración y despliegue continuo (CI/CD), pruebas automatizadas y colaboración entre desarrollo y operaciones. Esto permite detectar fallos antes, entregar más rápido y adaptarse mejor a los cambios.  

**Situaciones donde cascada todavía se usa:**  
1. Proyectos que requieren certificaciones formales (ejemplo: software médico o aeronáutico).  
2. Sistemas que dependen mucho de hardware y donde rehacer pruebas es costoso.  

**Diferencia clave:** cascada da más control y formalidad, pero a costa de tiempo; DevOps gana velocidad y flexibilidad, aunque exige disciplina y automatización.  

**Tabla comparativa:**

| Aspecto      | Cascada                | DevOps                |
|--------------|------------------------|-----------------------|
| Estructura   | Lineal, por fases      | Cíclica e iterativa   |
| Feedback     | Al final del ciclo     | En cada iteración     |
| Flexibilidad | Baja, rígida           | Alta, adaptable       |
| Velocidad    | Lenta                  | Rápida                |
| Riesgo       | Alto                   | Menor (fallos detectados antes) |

![Comparativa DevOps vs Waterfall](imagenes/Devops-vs-waterfall.png)

## 4.2 Ciclo tradicional y silos
En el enfoque clásico de desarrollo, lo normal era que el trabajo terminara en la fase de construcción y recién ahí pasara al área de operaciones.  
Al no haber comunicación constante, cada grupo avanzaba por su cuenta como si estuvieran en silos, lo cual genera varios problemas.

**Limitaciones que aparecen:**
1. **Cambios grandes y poco controlados:** en lugar de probar pequeños ajustes, se entrega un bloque completo de código. Si algo falla, encontrar la causa se vuelve complicado y corregirlo es más caro.  
2. **Acumulación de errores:** al no recibir retroalimentación inmediata, se van sumando defectos que después llegan todos juntos al final del ciclo.

**Anti-patrones típicos:**
**“Lanzar la pelota”:** los devs entregan el sistema y se desligan, esperando que operaciones lo ponga en marcha. Esto causa reprocesos y malentendidos porque el equipo que recibe no estuvo involucrado antes.  
**Seguridad atrasada:** se revisa la seguridad como un trámite final. Esto retrasa la entrega y deja abierta la posibilidad de que vulnerabilidades pasen a producción.

**Consecuencia directa:**  
Este modelo crea muchos *handoffs* (pases entre equipos) con pérdida de información. El resultado son tiempos más largos para resolver incidentes (**MTTR**) y repeticiones de los mismos problemas en distintos despliegues.

![Silos organizacionales](imagenes/silos-equipos.png)


## 4.3 Principios y beneficios de DevOps (CI/CD, Agile, colaboración)

El corazón de DevOps está en la integración continua (CI) y la entrega continua (CD).  
En lugar de esperar semanas para juntar cambios grandes, se trabaja con modificaciones pequeñas que se integran y prueban casi de inmediato. Esto ayuda a detectar errores cerca del código original y facilita la colaboración entre equipos.

**Puntos clave de CI/CD:**
Cambios chicos y frecuentes en vez de grandes lotes.  
Pruebas automatizadas que corren apenas se sube el código.  
Un pipeline que promueve o bloquea el paso de versiones según los resultados.  

**Relación con Agile:**  
Prácticas ágiles como las reuniones diarias o las retrospectivas ayudan a que Dev y Ops tomen decisiones rápidas sobre el pipeline.  
Por ejemplo: en una retro se puede acordar que cierto tipo de errores ya no se pasen de pruebas a producción. De esa forma, Agile y DevOps se refuerzan mutuamente.

**Indicador de colaboración (ejemplo no financiero):**  
Tiempo desde que un pull request está listo hasta que se despliega en el entorno de pruebas.*  
Si tarda mucho, significa que la comunicación entre Dev y Ops no es fluida.  
Si se mantiene corto, quiere decir que hay coordinación real.  

**Cómo medirlo sin herramientas caras:**  
Revisar los registros de PRs en GitHub o GitLab.  
Mirar los logs de despliegue en el servidor.  
Llevar una bitácora manual con las horas de aprobación y despliegue.

## 4.4 Evolución a DevSecOps

El paso de DevOps a DevSecOps significa que la seguridad ya no se revisa al final, sino que está presente desde el inicio del pipeline.  
Se aplican pruebas estáticas y dinámicas que permiten encontrar fallas antes de que el software llegue a producción.

**Tipos de análisis:**

**SAST (Static Application Security Testing):** revisa el código fuente o los binarios antes de ejecutar. Sirve para detectar inyecciones, malas prácticas o uso de librerías vulnerables.  
**DAST (Dynamic Application Security Testing):** analiza la aplicación *en ejecución*, simulando ataques reales (por ejemplo, XSS o SQL Injection).

**Gate mínimo de seguridad (umbrales propuestos):**
SAST → 0 vulnerabilidades críticas o altas(CVSS ≥ 7.0).  
DAST → mínimo 80% de cobertura en rutas críticas de la API.  

Si no se cumplen, el pipeline debe detener la promoción de esa versión.

**Política de excepción:**  
En caso de que no se pueda corregir de inmediato:
 Se permite una excepción de máximo **7 días**.  
 Se asigna un responsable técnico.  
 Se debe dejar documentado un plan de corrección (ejemplo: aplicar parche temporal o mitigación con firewall).

**Cómo evitar el “teatro de seguridad”:**  
No basta con cumplir checklist. Dos señales de eficacia que sí miden impacto real son:  
1. **Reducción de hallazgos repetidos:** que las mismas vulnerabilidades no vuelvan a aparecer en cada despliegue.  
2. **Tiempo de remediación más corto:** que una vulnerabilidad crítica se cierre en menos de 48 horas desde que se detecta.

Estas métricas se pueden obtener comparando reportes de SAST/DAST y revisando los commits de corrección.

## 4.5 CI/CD y estrategias de despliegue
Cuando se trata de un servicio clave como el de inicio de sesión, no conviene arriesgarse a desplegar todo de golpe.  
Por eso, una buena práctica es usar el método canario, que consiste en liberar la nueva versión solo a una parte pequeña de los usuarios.  
Si la versión es estable, se amplía el alcance hasta cubrir al 100%. Si aparecen fallos, se revierte rápido y la mayoría de usuarios nunca lo nota.

**Riesgos que pueden surgir y cómo se controlan:**
- **Errores en funciones básicas:** antes de enviar a todos, se validan contratos de API y pruebas de integración.  
- **Mayor costo en infraestructura:** mantener dos versiones en paralelo solo por un tiempo corto para evitar gastos innecesarios.  
- **Sesiones interrumpidas:** aplicar *drain connections* y cuidar que los cambios de base de datos sean compatibles.

**Indicadores para decidir si avanzar o no:**
- **KPI técnico:** porcentaje de respuestas 5xx ≤ 0.1% en la primera hora del despliegue.  
- **KPI de producto:** tasa de conversión (ejemplo: usuarios que completan registro) no debe bajar más del 5% respecto al promedio anterior.

**Comentario:**  
Es importante mirar tanto lo técnico como lo funcional. Puede pasar que el sistema no marque errores 5xx, pero que los usuarios abandonen el flujo porque algo cambió en la interfaz o en la lógica.  
Por eso ambos tipos de métricas deben coexistir al momento de tomar la decisión.

![Pipeline Canary](imagenes/pipeline_canary.png)

### 4.6 Fundamentos prácticos 
### 1. HTTP – contrato observable
Para esta evidencia revisé una petición HTTP en GitHub usando las DevTools del navegador.  
En la captura (`imagenes/http-evidencia.png`) se observa:

**Método:** GET  
**Código de estado:** 200 OK  
**Cabecera 1:** `Cache-Control: no-cache` → obliga al cliente a validar siempre con el servidor, lo que asegura información actualizada pero puede aumentar la carga.  
**Cabecera 2:** `Accept-Encoding: gzip, deflate, br, zstd` → habilita compresión en la respuesta, optimizando el uso de red y reduciendo tiempos de carga.

**Interpretación:**  
Estas cabeceras muestran un balance entre consistencia y rendimiento: aunque se fuerza a revalidar (menos caché), la compresión mantiene la respuesta rápida y ligera. Esto da trazabilidad y control sobre la entrega de contenido.
