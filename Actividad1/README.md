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