# Plan: OpenAI y sandbox en tu computador y en OpenAI

Actualizado: 17 de noviembre de 2026. Estado: planificación; implementación pendiente.

## Objetivo

Estudiar, probar y explicar dos modalidades de entorno de ejecución de Agents API
mediante una misma tarea: **leer un CSV sintético, generar un informe y verificarlo**.

| Escenario | Dónde se ejecutan las herramientas | Quién prepara el entorno |
|---|---|---|
| Self-hosted local | En el computador del presentador | El presentador |
| OpenAI-hosted | En infraestructura de OpenAI | OpenAI, según la configuración solicitada |

En ambos escenarios se usa Agents API. El modelo y la coordinación del agente
permanecen en OpenAI. El entorno local se conecta mediante `codex exec-server`.

## Alcance

- Preparar dos pruebas mínimas comparables y una presentación en español.
- Explicar tarea, ejecución, límites y resultados antes de los detalles técnicos.
- Incluir OCI en una lámina final como extensión de self-hosted, con el ejemplo
  del Cookbook. No desplegar recursos de OCI.
- Conservar la presentación y las pruebas existentes de Codex y Auto-review como
  material complementario. Abrir `codex` en terminal no sustituye la prueba
  self-hosted de Agents API.
- Esta actualización solo modifica el plan. No ejecuta pruebas, consume APIs,
  modifica presentaciones ni publica cambios.

## Secuencia de trabajo

### 1. Comprobar viabilidad

Revisar documentación vigente, acceso a Agents API y modelos, SDK compatible,
credenciales, requisitos de `exec-server` en el computador y conectividad.
Identificar costos y definir un límite para la prueba antes de consumir servicios.
Comprobar que existe autorización para ese consumo. Separar las claves de
aplicación y ejecutor según la documentación.

Si un escenario no está disponible, registrar el impedimento y su efecto. La
prueba previa de Codex puede servir de respaldo, identificada como una prueba
distinta; no presentarla como ejecución de Agents API.

### 2. Preparar un único caso

Revisar el ejemplo CSV y su verificador en `share_knowledge_1/examples/` y
reutilizar los componentes mínimos adecuados. Preparar en `openai_sandbox/` un
paquete autocontenido con datos sintéticos, tarea, formato del informe y referencia
esperada. Mantener las mismas entradas, instrucciones y criterios de verificación
en ambos escenarios, y el mismo modelo cuando esté disponible.

### 3. Ejecutar self-hosted en el computador

Preparar un directorio de trabajo dedicado y los controles de aislamiento
compatibles; indicar una carpeta no crea por sí solo un sandbox. Crear la sesión,
conectar `codex exec-server`, enviar la tarea y recuperar el informe. Verificar la
salida y documentar los controles efectivos observables. Cerrar la sesión y detener
el ejecutor al terminar.

### 4. Ejecutar OpenAI-hosted

Crear la sesión con el entorno alojado, proporcionar el mismo CSV y las
dependencias necesarias, enviar la tarea y descargar el informe. Aplicar el mismo
verificador y documentar configuración, resultados y limitaciones. Eliminar la
sesión al terminar para solicitar la limpieza del entorno.

### 5. Comparar lo observado

Registrar por escenario: fecha, modelo, entorno, preparación requerida, comandos
de reproducción, ubicación de archivos, controles configurados, resultado de la
verificación y errores. Registrar consumo y duración solo si pueden medirse;
una ejecución por modalidad no constituye un benchmark.

Distinguir configuración declarada, controles observados y garantías documentadas.
Un informe correcto demuestra el resultado de esa tarea, no aislamiento completo.

### 6. Preparar la presentación

Crear `presentation/openai-y-sandbox/` con LaTeX/Beamer, notas y diagramas TikZ.
Propuesta: ocho láminas y 20–25 minutos de contenido más preguntas.

| Lámina | Idea principal |
|---|---|
| 1 | La tarea: del CSV al informe verificable. |
| 2 | Qué hace el agente y qué aporta el sandbox. |
| 3 | Dos modalidades: tu computador y OpenAI. |
| 4 | Self-hosted local: recorrido y demostración. |
| 5 | OpenAI-hosted: recorrido y demostración. |
| 6 | Resultados y diferencias observadas. |
| 7 | Conclusiones, límites y cómo repetir las pruebas. |
| 8 | Extensión: self-hosted en OCI y enlace al Cookbook. |

Mantener el mismo ejemplo y una idea por lámina. Usar posiciones, etiquetas y
colores consistentes para comparar los dos entornos. Dejar instalación detallada,
TOML, otras APIs y Auto-review como material de consulta.

### 7. Verificar y ensayar

Compilar el PDF, renderizar y revisar todas las páginas. Comprobar enlaces y
legibilidad al compartir pantalla. Ensayar con cronómetro y conservar informes,
registros saneados y capturas o grabación real como respaldo.

Comprobar que una persona pueda responder: ¿dónde se ejecutó cada tarea?,
¿qué preparó el presentador?, ¿qué resultados verificamos?, ¿dónde encajaría OCI?

## Entregables

- Ejemplo mínimo con las dos modalidades, instrucciones y verificador.
- Registro comparativo de ejecuciones y limitaciones, sin credenciales.
- Presentación PDF con fuentes LaTeX, notas y diagramas editables.
- Índice actualizado para encontrar y reproducir los materiales.

## Criterios de aceptación

- La comparación central es self-hosted local frente a OpenAI-hosted en Agents API.
- Se usa la misma tarea y se verifican los informes con una referencia independiente.
- Cada escenario figura como ejecutado, fallido o pendiente según su evidencia real.
- Se explica el alcance de los controles sin deducirlo del éxito del cálculo.
- OCI aparece como extensión documental; no es requisito para completar la sesión.
- PDF revisado visualmente y demostración ensayada con respaldo disponible.

## Decisiones pendientes

Confirmar acceso y compatibilidad, presupuesto de las pruebas, duración final y
nivel de la audiencia. Usar español y una audiencia técnica mixta como supuesto
de preparación. No realizar commits ni push sin instrucción posterior.

## Referencias

- [Arquitectura de Agents API](https://developers.openai.com/api/docs/guides/agents-api/architecture).
- [Self-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted).
- [OpenAI-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted).
- [Extensión OCI: Cookbook](https://github.com/openai/openai-cookbook/tree/main/examples/agents_api/sandboxes/oci/application_managed).
- [AERO: enseñanza explícita](https://www.edresearch.edu.au/guides-resources/practice-guides/explicit-instruction-practice-guide-full-publication).
- [The Carpentries: demostraciones](https://carpentries.github.io/instructor-training/17-live.html).
- [TikZ: gráficos](https://tikz.dev/guidelines).
