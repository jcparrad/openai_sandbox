# Codex: sandbox, permisos y Auto-review

Material educativo en español sobre el sandbox de Codex y la revisión de excepciones. Incluye una demo preparada para comparar intervenciones humanas con revisión manual y Auto-review, manteniendo el mismo sandbox.

Ejemplo personal e independiente. No representa una política empresarial ni contiene una configuración corporativa. Documentación consultada el 5 de noviembre de 2026; las funciones y su disponibilidad pueden cambiar.

## Por dónde empezar

1. Leer la [presentación en PDF](presentation/sandbox-permisos-app/sandbox-permisos-app.pdf): 17 diapositivas sobre sandbox, aprobaciones, Auto-review y la demo.
2. Seguir la [demo de dos revisores](examples/demo-sandbox/README.md): ejecutar seis casos sintéticos, verificar un informe y exportarlo fuera del alcance ordinario. Mismo sandbox y tarea; solo cambia el revisor.
3. Consultar el [registro comparativo](results/comparacion-aprobaciones.md): **4 intervenciones humanas en el manual y 0 con Auto-review**, con la tarea correcta en ambos recorridos. Es el resultado de esta demo, no una garantía para otras tareas.

Como complemento, la [guía de configuración general](examples/codex-auto-review/README.md) incluye recomendaciones sobre dependencias, Docker y APIs. Su [config.toml](examples/codex-auto-review/config.toml) no se activa por estar aquí y no es el perfil sin red de la demo.

## Qué incluye

```text
examples/codex-auto-review/
  config.toml                  Perfil de laboratorio y revisión automática
  README.md                    Explicación, uso, límites y fuentes
examples/demo-sandbox/
  README.md                    Preparar y abrir las dos sesiones en terminal
  evaluar.py, casos.json       Evaluación sintética y verificación independiente
  laboratorio.py, prompt.txt   Arranque de sesiones con la misma tarea
  *.config.toml               Variantes manual y automática
results/
  comparacion-aprobaciones.md  Validación local y registro de la comparación
presentation/sandbox-permisos-app/
  sandbox-permisos-app.pdf      Presentación conceptual
  sandbox-permisos-app.tex      Fuente editable con notas y referencias
  ejemplo-config.toml          Ejemplo tradicional utilizado en las slides
  compilar.py                  Compilación y comprobaciones del PDF
  README.md                    Requisitos y comandos
  assets/selector-permisos.png Captura de interfaz utilizada en una slide
```

El ejemplo práctico usa perfiles `default_permissions`; la presentación también explica la familia tradicional `sandbox_mode`. Son ejemplos alternativos para entender los controles: no combinarlos en una configuración activa.

## Qué está comprobado

- Sintaxis TOML del ejemplo y coherencia con la documentación citada.
- PDF de 17 páginas, compilado y revisado visualmente.
- Revisión de los archivos seleccionados y del texto del PDF para excluir rutas personales, credenciales reconocibles y datos internos.
- Demo: generación y verificación de seis casos, exportación idéntica, rechazo de sobrescrituras y detección de un resultado alterado. Preparación de proyectos equivalentes e invocaciones revisadas sin abrir las sesiones.

Los dos recorridos interactivos completaron los seis casos y la exportación; los informes son idénticos. En el manual se observaron cuatro solicitudes: tres de inspección y una de exportación. El usuario confirmó cero intervenciones en el automático. Su resumen expone `auto_review`, pero no identifica una decisión individual: no se inventan decisiones internas ni se afirma aislamiento integral. Una pasada por modo muestra el resultado de este recorrido, sin generalizar el ahorro. No se modificó la configuración personal, ni se ejecutaron evaluaciones API externas o Docker. La demo interactiva usa el acceso habitual al servicio de Codex.

La personalización `[auto_review].policy` permanece comentada: reemplaza la política existente y exige conservar primero su contenido completo. No publicar políticas internas para completar el ejemplo. El revisor automático conserva sus límites y puede equivocarse; tampoco impone un presupuesto de API.

## Recompilar la presentación

```bash
python3 presentation/sandbox-permisos-app/compilar.py
```

Requiere las herramientas y fuentes indicadas en la [guía de compilación](presentation/sandbox-permisos-app/README.md). La presentación usa Fira Sans y Fira Mono, familias libres incluidas en TeX Live; el PDF ya compilado puede consultarse sin instalar fuentes adicionales. Las notas del presentador están en los bloques `\note{...}` del archivo LaTeX.

## Publicación de esta carpeta

Esta carpeta se preparó como paquete independiente, sin el historial del proyecto original. Para crear el repositorio público, usar únicamente su contenido como raíz de un repositorio nuevo; no copiar el `.git` del proyecto de trabajo. Revisar después cualquier archivo añadido y habilitar las protecciones de secretos disponibles en GitHub.

La selección excluye configuraciones personales activas, archivos de autenticación, políticas administradas, datos de clientes, transcripciones, evidencia local, la solicitud de trabajo original y presentaciones de referencia. No se distribuyen fuentes tipográficas ni dependencias.

No se ha creado ni publicado un repositorio remoto, ni se ha elegido una licencia de redistribución para este material.

## Referencias principales

- [Sandbox y permisos](https://learn.chatgpt.com/docs/sandboxing?surface=app).
- [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review).
- [Perfiles de permisos](https://learn.chatgpt.com/docs/permissions).
- [Configuración de Codex](https://learn.chatgpt.com/docs/config-file/config-basic).

Las guías y las notas de las diapositivas incluyen las fuentes específicas y sus limitaciones.
