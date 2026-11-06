# Plan: explicar el sandbox de Codex desde una tarea concreta

## Objetivo

Que una persona que empieza pueda explicar qué limita el sandbox, dónde se
ejecutan los comandos y cómo se revisa una excepción antes de leer el TOML.
Conservar las 17 diapositivas, el estilo y los resultados originales de la demo.

## Secuencia de trabajo

1. Crear este plan y hacer el commit inicial antes de editar la presentación.
2. Reescribir la apertura: definición, informe dentro/fuera del proyecto,
   ejecución local, configuración habitual al empezar y solicitud de excepción.
3. Mantener la explicación de Auto-review, distinguiendo límites, revisión y
   decisión. Reutilizar el informe como ejemplo y conservar sus limitaciones.
4. Explicar los modos después de los fundamentos y mantener los ejemplos TOML
   tradicionales como una familia coherente. Mostrar las diferencias entre
   lectura/escritura y red de comandos/otras herramientas.
5. Actualizar notas, referencias y guías. Corregir la afirmación desactualizada
   del README sobre la ausencia de publicación remota.
6. Compilar con el script existente: exigir 17 páginas y ausencia de
   desbordamientos, caracteres ausentes y errores de compilación.
7. Renderizar y revisar visualmente las 17 páginas; corregir lo necesario.
8. Registrar el resultado del plan y hacer el commit final. No hacer push.

## Criterios editoriales

- Definición visible: límites técnicos de archivos y red para comandos de Codex.
- Un ejemplo resuelto de informe, con su política ilustrativa declarada.
- Ejecución local mediante controles del sistema operativo; cloud con entorno
  propio. No representar todo sandbox como una máquina virtual.
- Inicio habitual condicionado a confianza, cliente y configuración efectiva.
- /status y /permissions identificados como comandos del CLI.
- Aprobaciones y Auto-review separados del alcance técnico.
- No afirmar que workspace-write limita todas las lecturas al proyecto.
- Una idea principal por lámina, etiquetas legibles y detalles en notas.

## Fuentes contrastadas

- https://learn.chatgpt.com/docs/agent-approvals-security
- https://learn.chatgpt.com/docs/permissions
- https://learn.chatgpt.com/docs/sandboxing/auto-review
- https://github.com/josephwright/beamer/blob/main/doc/beamerug-guidelines.tex
- https://education.nsw.gov.au/about-us/education-data-and-research/cese/publications/practical-guides-for-educators-/cognitive-load-theory-in-practice

## Estado

Plan preparado. Pendiente implementación y validación.
Las reglas locales de `.codex/rules/` permanecen ignoradas y fuera de estos commits.
