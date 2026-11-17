# Diagnóstico: consolidar una sola presentación de OpenAI y sandbox

Fecha: 17 de noviembre de 2026. Estado: diagnóstico y recomendaciones; sin implementación.

## Recomendación principal

Mantener **una sola presentación activa en `openai_sandbox/`**, con una historia:
el mismo CSV se procesa mediante Agents API en dos entornos, **self-hosted en el
computador del presentador** y **OpenAI-hosted**. OCI queda como extensión al final.

Consolidar por selección y reescritura, no concatenando los PDF existentes.
Reutilizar el ejemplo y recorrido de la presentación general, la explicación breve
del sandbox y el sistema visual de la versión reciente de Codex. Los contenidos
avanzados de permisos y Auto-review quedan como documentación de apoyo.

Una presentación puede tener dos exportaciones: PDF para proyectar y PDF con
notas. Ambos deben generarse desde una misma fuente de contenido.

## Qué se revisó

- Estructura de los dos repositorios Git hermanos: `openai_sandbox/` y
  `share_knowledge_1/`. El directorio que los contiene no es un repositorio Git.
- Solicitud original, instrucciones del proyecto, README, plan vigente,
  investigación, guías, pendientes y registros de resultados.
- Contenido textual completo de los PDF principales de 17, 12 y 6 páginas;
  fuentes LaTeX, estilos y scripts de compilación relevantes.
- Muestras renderizadas de las tres familias para valorar consistencia visual.
  Esta revisión no constituye una nueva certificación visual de todas las páginas.
- Scripts del CSV y su verificador, instrucciones de la demo Auto-review,
  diferencias entre copias y contenido del ZIP público.
- Comprobación de enlaces relativos: sin destinos inexistentes en los 28 Markdown
  del recorrido revisado, excluyendo planes, copias del paquete y archivos de build.

No se ejecutaron demos, servicios API ni recursos OCI. El acceso API actual no
se volvió a comprobar. No se modificaron presentaciones, fuentes, guías ni ejemplos.

## Inventario: qué presentaciones existen realmente

Rutas relativas al directorio de trabajo que contiene ambos repositorios.

| Material | Ubicación | Estado y función |
|---|---|---|
| General, 12 láminas | `share_knowledge_1/presentation/openai-sandbox.tex` | CSV, cinco opciones, ejecución local y verificación. Buen recorrido, alcance más amplio que el acordado ahora. |
| General con notas, 12 páginas | `share_knowledge_1/presentation/openai-sandbox-notas.tex` | Importa la fuente general. Es la misma presentación con notas, no otra charla. |
| Introducción, 6 láminas | `share_knowledge_1/presentation/que-es-un-sandbox/` | Definición y diagramas sencillos; reutilizable en la apertura. |
| Codex, 16 láminas | `share_knowledge_1/presentation/sandbox-permisos-app/` | Versión anterior del material especializado. |
| Codex, 17 láminas | `share_knowledge_1/repo-publico/presentation/sandbox-permisos-app/` | Copia de distribución; distinta de la versión del repo activo. |
| Codex, 17 láminas | `openai_sandbox/presentation/sandbox-permisos-app/` | Versión reciente, con apertura aclarada el 6 de noviembre, demo y estilo separado. |
| ZIP de distribución | `share_knowledge_1/repo-publico.zip` | Contiene el PDF de la copia de distribución; no coincide con el PDF reciente. |
| Diagramas CLI/exec-server, 2 páginas | `openai_sandbox/docs/codex-vs-exec-server/` | Documento explicativo independiente; no es una presentación de la sesión. Usa OCI como ejemplo. |

**Hay tres familias de contenido, varias versiones y dos exportaciones de la
general.** Mantener todas visibles como puntos de entrada dificulta saber cuál usar.

## Hallazgos

### 1. Falta una referencia única para la sesión

El README de `openai_sandbox/` dirige a la charla de Codex. El de
`share_knowledge_1/` dirige a la general, al paquete público y al ZIP. La selección
del PDF depende de la carpeta desde la que se empieza.

**Recomendación:** designar `openai_sandbox/` como lugar de mantenimiento actual.
Su remoto configurado es `https://github.com/jcparrad/openai_sandbox.git`.
Tratar el proyecto original como antecedente y dejar de mantener copias paralelas
del paquete público. No fusionar historias Git para resolver este problema.

### 2. Ninguna presentación actual refleja por completo el enfoque acordado

La general dedica sus láminas 4–5 al mapa de cinco opciones y su demostración es
local con Codex. La reciente de Codex dedica las láminas 6–13 a revisión,
configuración, escritura, red y modos. Son materiales útiles, pero no presentan
la comparación self-hosted local / OpenAI-hosted como recorrido central.

**Recomendación:** sintetizar el relato en ocho láminas, manteniendo los detalles
avanzados en las guías. No sumar 12 + 17 láminas ni agregar otra introducción de seis.

### 3. Las dos demos existentes responden preguntas diferentes

| Demo | Qué está registrado | Uso recomendado |
|---|---|---|
| CSV de importes | Seis filas, total 700, JSON y CSV contrastados con referencia, repetición y error de entrada. Ejecución local desde Codex. | Reutilizar datos, formato y verificador para las nuevas pruebas. |
| Evaluador de seis casos / Auto-review | Informe y copia verificados; cuatro intervenciones manuales frente a cero en el recorrido automático, según evidencia y confirmación del usuario. | Mantener como caso complementario de revisión de acciones. |

No son el mismo conjunto de datos ni la misma prueba. La comparación de
intervenciones tampoco permite atribuir las cuatro solicitudes a una sola
frontera: tres fueron inspecciones previas y una fue la exportación.

### 4. Las pruebas centrales de Agents API todavía faltan

No hay evidencia en los materiales revisados de ejecución de los dos escenarios
del plan nuevo. Los registros históricos de acceso describen el entorno de
octubre y no permiten concluir qué acceso existe hoy.

**Recomendación:** comprobar viabilidad primero y ejecutar el mismo caso en ambas
modalidades antes de redactar resultados comparativos. Si una falla o no está
disponible, indicarlo. Abrir Codex no sustituye conectar `codex exec-server` a
Agents API. Preparar la explicación local con los controles de aislamiento que
realmente admita el equipo; una carpeta dedicada no acredita aislamiento.

### 5. Demostrar cálculo no explica por sí solo los límites del sandbox

La evidencia actual verifica archivos y resultados. El caso de entrada inexistente
comprueba manejo de errores. Ninguno demuestra por sí solo una frontera de acceso.

**Recomendación:** explicar los controles configurados y distinguirlos de los
observados. Si es viable, añadir una comprobación pequeña de un límite concreto
con datos de laboratorio y resultado esperado definido; por ejemplo, una petición
de red bajo una política que la deshabilita. Elegir la prueba después de verificar
el soporte de cada modalidad. No convertir esto en una batería de seguridad ni
atribuir cualquier fallo a un bloqueo del sandbox.

### 6. Los diagramas recientes necesitan adaptar el escenario

La guía de CLI/exec-server dibuja OCI como entorno. El enfoque vigente usa el
computador del presentador. Usarlos sin cambios volvería a introducir la confusión
entre modalidad e infraestructura.

**Recomendación:** reutilizar su técnica de TikZ, no las figuras tal cual. Dibujar
primero self-hosted local frente a OpenAI-hosted, con el mismo ejemplo y etiquetas
de ubicación explícitas. Explicar `exec-server` solo donde hace falta para el local.

### 7. Hay documentación y empaquetado que quedaron desalineados

- `share_knowledge_1/repo-publico/README.md` dice que no se publicó remoto, mientras
  el README del repositorio actual registra la publicación y Git tiene `origin`.
- El índice original sigue ofreciendo versiones anteriores y el ZIP como entradas
  principales. Los PDF de Codex de 16 y 17 páginas no son copias idénticas.
- El título del README actual sigue centrado en Codex y Auto-review.
- El compilador reciente exige exactamente 17 páginas; deberá ajustarse al nuevo
  contenido. Su estilo fuerza notas ocultas: no basta copiarlo para exportar notas.
- El proyecto general ya resuelve las notas mediante un archivo que importa la
  fuente principal; conviene reutilizar ese patrón.
- Hay tres lenguajes visuales: general, introducción y Codex. Importar páginas como
  imágenes conservaría esa mezcla e impediría editar los elementos.
- El ejemplo CSV y su referencia aún viven en el repositorio original. El paquete
  nuevo debe funcionar sin depender de `../share_knowledge_1/`.
- El verificador del CSV está fijado a los datos originales. Conservar la entrada
  para ambas pruebas o cambiar explícitamente la referencia si se cambia el caso.

## Diseño recomendado para la presentación única

Título: **OpenAI y sandbox: la misma tarea en tu computador y en OpenAI**.

| Lámina | Contenido | Material de partida |
|---|---|---|
| 1 | El pedido: CSV → informe verificable. | Caso de la general. |
| 2 | Qué hace el agente y qué limita el sandbox. | Introducción breve y fundamentos de Codex, reescritos para el contexto. |
| 3 | Dos modalidades dentro de Agents API. | Diagrama nuevo local / OpenAI. |
| 4 | Self-hosted en el computador: pasos y evidencia. | Nueva prueba con `exec-server`. |
| 5 | OpenAI-hosted: mismos datos y verificación. | Nueva prueba alojada. |
| 6 | Comparación observada: preparación, ejecución, archivos y controles. | Registro de las dos pruebas. |
| 7 | Conclusiones, límites y reproducción. | Verificador y evidencias. |
| 8 | Extensión interesante: OCI. | Enlace al Cookbook; marcado como no ejecutado. |

Usar el sistema visual reciente de Codex como base: Beamer/Moloch, Fira Sans,
Fira Mono y estilo en un archivo separado. Redibujar con un único sistema de
colores y diagramas editables. El relato de la general es la base editorial.

## Fuente única y organización propuestas

Dentro de `openai_sandbox/`:

```text
presentation/openai-y-sandbox/
  openai-sandbox.tex        Contenido y notas de la única presentación activa
  openai-sandbox-notas.tex  Activa notas e importa la fuente principal
  estilo.sty               Una tipografía, paleta y reglas de composición
  assets/                  Diagramas editables y recursos utilizados
  compilar.py              Genera y comprueba ambas exportaciones
  openai-sandbox.pdf        Para proyectar
  openai-sandbox-notas.pdf  Mismo contenido, con notas
  README.md                Uso y reproducción
```

El README raíz debe ofrecer un solo enlace principal: «Abrir la presentación».
El PDF de notas se identifica como versión para el presentador. La guía y los
ejemplos quedan accesibles como lectura, sin competir como otra charla.

Cuando se termine y verifique la consolidación, retirar los PDF anteriores de la
navegación activa y acordar su conservación histórica antes de mover o eliminar
archivos. No borrar ahora el trabajo previo ni reemplazar ZIP o commits.

## Orden recomendado de ejecución

1. Confirmar esta decisión editorial y usar el plan vigente para las dos pruebas.
2. Comprobar acceso y compatibilidad de ambas modalidades, sin suponer resultados.
3. Preparar el caso autocontenido y ejecutar/verificar los dos recorridos.
4. Redactar y construir las ocho láminas en la fuente única.
5. Revisar ambos PDF y ensayar la narración y la demostración.
6. Actualizar README, guía y enlaces para que apunten al material canónico.
7. Resolver el archivo histórico de versiones anteriores, sin mantenerlas como
   presentaciones activas ni regenerar copias de distribución manualmente.

El plan `2026-11-17-explicacion-openai-sandbox.md` ya contiene las dos modalidades
acordadas. Al implementar, precisar que «conservar material complementario» no
significa mantener otra presentación activa. Este diagnóstico no ejecuta el plan.

## Comprobación final de la consolidación

- Un solo relato, una fuente de contenido y dos exportaciones sincronizadas.
- Un mismo CSV y verificador; los materiales no dependen del otro repositorio.
- Resultados nuevos distinguidos de los históricos y de lo documentado.
- Auto-review y otras APIs fuera del recorrido principal; OCI solo como extensión.
- Diagramas coherentes con el computador local y OpenAI, sin heredar OCI por error.
- Compilación y enlaces verificados, páginas renderizadas revisadas y ensayo medido.
- Sin nuevas copias activas divergentes, borrados ni publicación implícita.

## Archivos que sustentan el diagnóstico

Respecto de `openai_sandbox/`: `README.md`, `PENDIENTES.md`,
`presentation/sandbox-permisos-app/{sandbox-permisos-app.tex,estilo-sandbox.sty,compilar.py}`,
`examples/demo-sandbox/{README.md,prompt.txt}`, `results/comparacion-aprobaciones.md`,
`docs/codex-vs-exec-server/` y el plan vigente.

Respecto de `share_knowledge_1/`: `request.md`, `AGENTS.md`, `README.md`,
`docs/{alcance.md,acceso-api.md,guia-sesion.md}`, `examples/`, `evidence/resultados.md`,
`presentation/{README.md,openai-sandbox.tex,openai-sandbox-notas.tex,compilar.py}`,
`presentation/que-es-un-sandbox/`, `presentation/sandbox-permisos-app/`,
`repo-publico/` y `repo-publico.zip`.
