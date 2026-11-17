# Fuentes y decisiones de diseño

Consulta: 17 de noviembre de 2026. Esta guía explica una arquitectura; no registra una prueba del servicio ni un despliegue en OCI.

## Fuentes técnicas

| Fuente oficial | Qué se contrastó |
|---|---|
| [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) | Trabajo interactivo sobre archivos y herramientas de la máquina. |
| [Modo no interactivo](https://learn.chatgpt.com/docs/non-interactive-mode) | `codex exec` ejecuta tareas desde scripts y CI. |
| [Arquitectura de Agents API](https://developers.openai.com/api/docs/guides/agents-api/architecture) | Separación entre aplicación, coordinación y entorno de ejecución. |
| [Self-hosted sandboxes](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted) | Función de `exec-server`, autenticación separada, conexión saliente y preparación del entorno. |

## Cómo se buscó facilitar la comprensión

Se adaptaron recomendaciones educativas al formato de una guía técnica. Son decisiones editoriales; no se ha medido su eficacia con lectores.

- **Un ejemplo resuelto:** mantener CSV y gráfico en ambos recorridos permite concentrarse en la diferencia arquitectónica. Basado en [CESE: Cognitive load theory in practice](https://education.nsw.gov.au/about-us/education-data-and-research/cese/publications/practical-guides-for-educators-/cognitive-load-theory-in-practice).
- **Información esencial junto al dibujo:** cada diagrama tiene inmediatamente su explicación. Misma fuente de CESE.
- **Avanzar de lo concreto a lo abstracto:** tarea, recorridos, comparación y elección. Basado en [AERO: Managing cognitive load optimises learning](https://www.edresearch.edu.au/summaries-explainers/explainers/managing-cognitive-load-optimises-learning).
- **Comprobar comprensión:** tres preguntas con respuesta permiten revisar el concepto. Basado en [AERO: Explicit instruction](https://www.edresearch.edu.au/guides-resources/practice-guides/explicit-instruction-practice-guide-full-publication).

Los diagramas usan etiquetas y límites de ubicación; su significado no depende de colores. Se dejaron fuera detalles de instalación, costos y aprovisionamiento para mantener el foco. Los comandos son ilustrativos y requieren el entorno y la versión compatibles indicados por la documentación vigente.

## Revisión gráfica con LaTeX y TikZ

Las figuras se redibujaron con TikZ y LuaLaTeX. Se consultó el [manual oficial: Guidelines on Graphics](https://tikz.dev/guidelines), especialmente las secciones 7.3 a 7.5 y 7.7: figuras que se entiendan por sí mismas, consistencia tipográfica, rótulos legibles junto al elemento y énfasis sin decoración innecesaria.

Aplicación al material:

- Las tres figuras comparten tamaño, columnas, tipografía y posición de las herramientas. Así es más fácil localizar qué cambia.
- El borde y fondo índigo identifican la coordinación, con texto explícito que conserva el significado en escala de grises.
- Las flechas tienen espacio para sus etiquetas y no se cruzan. Son intercambios de mensajes; la nota sobre WebSocket aclara quién inicia la conexión.
- Se usan títulos descriptivos, un caso concreto y una conclusión al pie de cada figura.
- El PDF conserva los elementos vectoriales y el Markdown incorpora PNG de 2000 píxeles de ancho para visores comunes.

Referencias de implementación: [Nodes and Edges](https://tikz.dev/tikz-shapes), para anclas y bloques de texto; [Arrows](https://tikz.dev/tikz-arrows), para puntas uniformes con `arrows.meta`. Las figuras se dibujan a su tamaño final en LaTeX, sin reducir un dibujo sobredimensionado.

Verificación: compilación de tres páginas sin desbordamientos ni caracteres faltantes y revisión visual de las tres imágenes exportadas. No se ejecutaron comandos de Codex ni recursos de OCI para crear estas ilustraciones.

## Adaptación a la presentación única

Se cambió OCI por el computador local y se unificó el caso como CSV a informe.
Se añadió OpenAI-hosted para separar modalidad y proveedor. Los tres diagramas
comparten sus archivos TikZ con la presentación canónica, conservando Fira y su
paleta. Las figuras explican funciones y ubicaciones; no registran pruebas API.
