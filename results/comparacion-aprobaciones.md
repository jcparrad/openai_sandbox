# Registro: sandbox y revisión de aprobaciones en Codex

Actualizado: 5 de noviembre de 2026.

## Comparación interactiva

**Estado: comparación completada. Manual: 4 intervenciones humanas; Auto-review: 0. Ambas tareas verificadas.** El usuario compartió las solicitudes visibles de la sesión manual, los resultados finales de ambas sesiones y confirmó que la automática terminó sin pedirle permisos. Las validaciones funcionales locales de abajo son comprobaciones independientes.

Pregunta: ¿cuántas intervenciones humanas requiere completar la misma evaluación sintética y exportar su informe fuera del alcance ordinario del sandbox?

| Modo | Solicitudes elegibles observadas | Intervenciones humanas por permisos | Revisión/decisión observada | Informe y exportación verificados |
| --- | --- | --- | --- | --- |
| Manual | 4 solicitudes de aprobación visibles | 4 en el recorrido: 3 de inspección inicial y 1 de exportación | Solicitudes manuales en la interfaz compartida por el usuario | Sí: 6/6 y copia idéntica |
| Auto-review | Exportación reportada como excepción solicitada; total de solicitudes no observable en el resumen | 0, confirmado por el usuario de la terminal | Configuración expone auto_review; decisión individual no identificada en el resumen | Sí: 6/6 y copia idéntica |

En este recorrido hubo cuatro intervenciones humanas menos con Auto-review y ambos resultados fueron correctos. Tres solicitudes manuales correspondieron a inspecciones iniciales y una a la exportación. Es una pasada por modo, no una tasa general de ahorro ni un benchmark: los comandos de inspección que el agente decide ejecutar pueden variar. El conteo humano no permite deducir el número de revisiones automáticas internas ni atribuir una decisión individual no expuesta.

### Recorrido manual observado

Laboratorio nuevo después de corregir el prompt. CLI 0.166.0 y Python 3.13.7 informados por el usuario. Modelo solicitado al lanzar: `gpt-6.1-sol`; el agente no pudo verificar el identificador efectivo ni el revisor desde su contexto. El revisor manual se respalda en la invocación y las pantallas de aprobación que el usuario compartió aquí, no en una afirmación del agente.

| Solicitud distinta | Operación | Motivo visible |
| --- | --- | --- |
| 1 | Resolver rutas y consultar temporales | Revisión de código Python en línea |
| 2 | Leer instrucciones AGENTS.md de carpetas superiores | Revisión de código Python en línea |
| 3 | Comprobar enlaces y pertenencia a raíces declaradas | Revisión de código Python en línea |
| 4 | Exportar informe a `../entregas/informe.json` | Excepción fuera de las raíces de escritura |

Las distintas capturas de la tercera solicitud corresponden al mismo prompt y no se suman de nuevo. El conteo del recorrido incluye inspecciones previas solicitadas por el prompt: tres intervenciones iniciales y una de la tarea. Mantener ambas categorías al comparar; no atribuir las cuatro al cruce de escritura del sandbox.

Según el resultado compartido, los cuatro comandos de la tarea terminaron con código 0; solo la exportación solicitó la excepción puntual, sin regla persistente. El informe y su copia pasaron la referencia de seis casos. La lectura posterior de ambos artefactos confirmó contenido idéntico y SHA-256 `677fdafb91aacc2f82251337524c2a7147aa7b6a4e4477ef1ed67e41f1c30b5a`. No se compartieron fallos ni timeout. No se inspeccionaron transcripciones privadas ni políticas administradas para este registro.

### Recorrido con Auto-review

El usuario compartió el resultado de la segunda sesión: los cuatro comandos terminaron con código 0 y la exportación figura como excepción solicitada. La sesión informa que la configuración expone `auto_review`, pero el resumen no identifica una decisión manual o automática concreta. No se atribuye ninguna decisión individual al revisor solo por el éxito del comando. No se informaron fallos ni timeout, ni cambios a scripts, configuración o reglas persistentes.

Se leyeron los dos informes internos y las dos copias exportadas de las sesiones reales: todos son idénticos y pasan los seis casos. Se comprobó también identidad byte a byte de `evaluar.py`, `casos.json` y `prompt.txt` entre ambos proyectos. Esa comprobación no acredita que todos los comandos de inspección o controles efectivos fueran idénticos.

Informes sintéticos revisados: [manual](informe-manual.json) y [automático](informe-automatico.json). Ambos tienen el SHA-256 indicado arriba. El resumen del agente no permite contar intervenciones humanas. El usuario de la terminal confirmó después: la sesión automática terminó sin pedirle nada. Se registra por esa observación directa del usuario un conteo de cero intervenciones, sin inventar decisiones internas del revisor.

## Qué completar después de la ejecución

Primer intento manual, informado por el usuario: el agente se detuvo antes de ejecutar porque el prompt anterior exigía conocer la disponibilidad del revisor y esa información no estaba expuesta. Según ese registro no hubo comandos de la tarea ni solicitudes de aprobación. Es un fallo de diseño del preflight, no una medición de Auto-review. Se corrigió el prompt común para permitir inspecciones de solo lectura y registrar metadatos no visibles como no verificables. Este intento queda excluido de la comparación; ambos modos se repitieron en un laboratorio nuevo con la misma versión corregida.

Para cada modo, registrar aquí solo información revisada para publicación:

- Fecha, sistema operativo, CLI, modelo y esfuerzo de razonamiento.
- Sandbox declarado y rutas reales inspeccionadas; revisor solicitado en la invocación y evidencia que exponga el cliente. Si el revisor no es visible desde el agente, registrarlo sin inferir su disponibilidad. Destino descrito como `../entregas`, sin rutas personales. Indicar qué controles no pudieron verificarse.
- Confirmación de mismo prompt, datos, comandos, política de revisión y estado inicial equivalente. Las carpetas físicas son distintas, con la misma estructura.
- Secuencia de solicitudes elegibles y decisiones observables, con códigos de salida y extractos saneados. Separar denegación del revisor, bloqueo de ejecución y timeout.
- Conteo humano por permisos; otras intervenciones anotadas aparte.
- Comprobación del informe interno y la copia exportada con sus hashes.

Una sesión nueva no borra reglas persistentes. Si una regla previa o un workspace amplio evita la solicitud de exportación, registrar que el preflight no permite este contraste. No publicar políticas administradas, sesiones completas ni identificadores internos.

## Validación funcional local

Estas comprobaciones se ejecutaron el 5 de noviembre de 2026 con Python 3.13.7 local mediante la herramienta de terminal, en una carpeta nueva de trabajo ignorada por Git. No se abrió una sesión anidada de Codex ni se cambió su configuración.

| Comprobación | Resultado observado |
| --- | --- |
| Generar y verificar informe | PASS: seis de seis casos de referencia |
| Exportar y verificar copia | PASS: mismo contenido y SHA-256 |
| Generar sobre archivo existente | Rechazo, código 1; bytes originales conservados |
| Exportar sobre archivo existente | Rechazo, código 1; bytes originales conservados |
| Verificar informe con resultado alterado | Rechazo, código 1 |
| Preparar A/B y revisar sus invocaciones sin abrir sesiones | PASS: entradas idénticas y variantes que solo cambian el revisor |

SHA-256 del informe generado y de su copia: `677fdafb91aacc2f82251337524c2a7147aa7b6a4e4477ef1ed67e41f1c30b5a`.

Comandos del programa, desde un directorio con `evaluar.py` y `casos.json`:

```bash
python3 evaluar.py evaluar --output informe.json
python3 evaluar.py verificar --input informe.json
python3 evaluar.py exportar --input informe.json --dest ../entregas/informe.json
python3 evaluar.py verificar --input ../entregas/informe.json
```

Para los casos negativos se repitieron generación/exportación contra los archivos ya existentes y se verificó una copia alterada del informe. La referencia `casos.json` permaneció intacta. Se revisó además la sintaxis TOML y las opciones del lanzador contra `codex --help` de CLI 0.166.0. La verificación funcional acredita el programa y sus archivos; **no prueba una frontera del sandbox, una aprobación manual ni una decisión de Auto-review**.

## Conclusión disponible

Ambas tareas se completaron y produjeron el mismo informe verificado. La manual requirió cuatro intervenciones visibles, tres de inspección y una de exportación; la automática terminó sin intervención, confirmado por el usuario. **En esta demo, la configuración con Auto-review permitió completar el recorrido con menos interrupciones humanas.** No se midió tiempo ahorrado, coste ni seguridad general. La documentación oficial indica que Auto-review cambia el revisor de solicitudes elegibles y mantiene el sandbox. [Fuente oficial](https://learn.chatgpt.com/docs/sandboxing/auto-review#how-auto-review-works).
