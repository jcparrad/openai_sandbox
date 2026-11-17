# Plan: una sola presentación conceptual de OpenAI y sandbox

Fecha: 17 de noviembre de 2026. Estado: implementación conceptual completada y verificada.

## Objetivo y entrega

Dejar una sola presentación activa, clara y completa para explicar OpenAI y
sandbox a un equipo técnico mixto. Integrar lo más relevante de las presentaciones
existentes y de la guía Markdown con diagramas.

La historia común será **leer un CSV de importes y generar un informe**. Explicar
cómo se realiza esa tarea en dos modalidades de Agents API:

- **Self-hosted local:** el entorno de ejecución está en el computador del presentador.
- **OpenAI-hosted:** OpenAI proporciona el entorno de ejecución.

La presentación enseñará los conceptos y recorridos en presente, como una
explicación terminada para la audiencia: «la aplicación crea la sesión», «el
entorno ejecuta Python». No será una exposición de nuestro plan ni contendrá
resultados inventados. **Las pruebas de ambas modalidades se ejecutarán después,
fuera del alcance de este plan.**

Una presentación significa una fuente de contenido y un PDF principal. Puede
existir un PDF adicional con las mismas láminas y sus notas para el presentador;
no será otra charla ni tendrá contenido independiente.

## Material que se integrará

Rutas relativas al directorio que contiene ambos repositorios.

| Material existente | Qué conservar | Qué adaptar o pasar a consulta |
|---|---|---|
| `share_knowledge_1/presentation/openai-sandbox.tex` | Caso CSV, distinción de componentes, verificación de archivos y límites de las conclusiones. | El recorrido de cinco opciones pasa a documentación; no organiza la charla. |
| `share_knowledge_1/presentation/que-es-un-sandbox/` | Definición, por qué se necesita, archivos/red y diagramas sencillos. | Las políticas ilustrativas deben seguir identificadas como ejemplos. |
| `openai_sandbox/presentation/sandbox-permisos-app/` | Diseño reciente, distinción sandbox/aprobación, ejemplo de escritura y revisión. | TOML, modos detallados y configuración empresarial quedan en guías. |
| `openai_sandbox/docs/codex-vs-exec-server/README.md` | Separación entre recibir tareas, coordinar y ejecutar; explicación de CLI, exec y exec-server. | Cambiar el ejemplo OCI/gráfico por computador local/CSV/informe en el recorrido principal. |
| `openai_sandbox/docs/codex-vs-exec-server/diagramas.tex` y sus imágenes | Estructura visual, columnas, flechas etiquetadas y énfasis en la coordinación. | Redibujar las arquitecturas necesarias; no pegar figuras con el escenario anterior. |
| `openai_sandbox/results/comparacion-aprobaciones.md` | Evidencia histórica y sus límites. | Un apoyo dentro de la presentación, sin confundirlo con las futuras pruebas API. |
| `share_knowledge_1/examples/` | Datos sintéticos, formato de informe y referencia esperada. | Lectura conceptual ahora; ejecución experimental después. |
| `openai_sandbox/PENDIENTES.md` | Enlace al Cookbook OCI. | Una lámina de extensión; no despliegue ni demostración. |

## Contenido propuesto

Diez láminas de recorrido y dos de apoyo en el mismo documento. Ajustar el número
solo si la revisión de comprensión lo requiere; no comprimir varias ideas para
cumplir una cifra heredada. Duración orientativa: 20–25 minutos más preguntas.

| Lámina | Qué debe entender la audiencia | Apoyo visual |
|---|---|---|
| 1 | Qué queremos hacer: pasar de un CSV a un informe comprobable. | Entrada → ejecución → informe. |
| 2 | Qué es el sandbox, para qué sirve y qué límites puede imponer. | Entorno y recursos sujetos a permisos. |
| 3 | Modelo, coordinación, herramientas y entorno cumplen funciones distintas. | Piezas conectadas con etiquetas sencillas. |
| 4 | En Agents API el entorno puede ser self-hosted u OpenAI-hosted. | Dos ubicaciones; OCI aún no aparece. |
| 5 | Self-hosted local: cómo una aplicación conecta el computador y entrega una tarea. | Aplicación → Agents API ↔ ejecutor y Python local. |
| 6 | OpenAI-hosted: cómo se prepara el entorno, se entrega el CSV y se recupera el informe. | Mismas piezas, con el entorno en OpenAI. |
| 7 | Qué prepara y administra cada parte en ambas modalidades. | Comparación de responsabilidades, archivos y preparación. |
| 8 | Abrir Codex en terminal y conectar exec-server resuelven usos diferentes. | Dos recorridos breves, con la coordinación señalada. |
| 9 | El sandbox limita accesos; una aprobación revisa una acción. | Ejemplo de guardar dentro y exportar fuera bajo una política explícita. |
| 10 | Cómo elegir y qué verificar al recibir el resultado. | Recapitulación: tarea, ubicación, límites y salida. |
| Apoyo A | OCI es otra ubicación posible de self-hosted. | Computador / OCI bajo self-hosted y enlace al Cookbook. |
| Apoyo B | Qué observamos previamente con Codex y Auto-review. | Resultado histórico 4/0 con fecha, tarea y limitaciones. |

Las láminas de apoyo pertenecen al mismo PDF y se usan si la audiencia lo necesita.
No mantener otra presentación avanzada en paralelo.

## Explicaciones que deben quedar explícitas

- El modelo y el lugar donde se ejecuta Python son cosas distintas.
- Las dos modalidades comparadas son de Agents API; OCI es un proveedor posible,
  no una tercera modalidad.
- En self-hosted el modelo y la coordinación siguen en OpenAI. Los resultados de
  las herramientas regresan al servicio; alojar el entorno localmente no equivale
  a que todo el procesamiento y los datos permanezcan en el computador.
- `codex exec-server` conecta un entorno a la sesión de Agents API y ejecuta sus
  herramientas. No es una conversación interactiva abierta con `codex`.
- `codex exec` automatiza Codex desde scripts. Explicarlo en las notas o en una
  aclaración breve; no presentarlo como otra modalidad de alojamiento.
- Una carpeta de trabajo no crea por sí sola aislamiento. Explicar los controles
  según la documentación y el contexto específico, sin generalizarlos entre productos.
- Aprobaciones y Auto-review son distintos del alojamiento del entorno. Introducir
  la diferencia sin convertirla en otro eje de comparación de la charla.
- Un cálculo correcto no demuestra aislamiento ni una garantía de seguridad.
- El CSV y el resultado esperado pueden mostrarse como ejemplo de referencia.
  Eso no significa que Agents API ya lo haya ejecutado.

## Estilo visual obligatorio y decisiones LaTeX

Referencia confirmada por el usuario:
`presentation/sandbox-permisos-app/sandbox-permisos-app.pdf`, junto con su fuente
y `estilo-sandbox.sty`. Conservar su identidad visual, no solo usar el mismo tema.

### Qué se conserva de la referencia

- Formato 16:9 de 320 × 180 mm y retícula de márgenes existente.
- Fira Sans para títulos y cuerpo, Fira Mono para código; títulos ligeros,
  seminegrita para énfasis y pesos legibles en las superficies oscuras.
- Paleta existente: noche `#17182B`, nieve `#F8F9FC`, índigo `#5148B5`,
  lavanda `#B8B2FF` y ciruela `#7941A3`.
- Jerarquía de título, bajada, contenido, conclusión y numeración discreta.
- Superficies claras y oscuras según la composición de referencia; código en
  superficies delimitadas. No importar el tema petróleo/coral de la introducción
  ni la tipografía Heros de los diagramas independientes.
- Composiciones variadas según el mensaje: ejemplo, flujo, comparación o tabla.
  No convertir todas las láminas en listas ni repetir tarjetas decorativas.

Reutilizar las macros de estilo que funcionan y parametrizar solo lo necesario
para contenido y notas. Preservar la apariencia no obliga a conservar errores,
solapamientos ni restricciones técnicas del compilador anterior.

### Investigación y aplicación

Fuentes primarias consultadas el 17 de noviembre de 2026. Las especificaciones de
tamaño y color anteriores provienen del proyecto; no se atribuyen a los manuales.

| Herramienta o guía | Uso elegido para esta presentación |
|---|---|
| [Beamer: recomendaciones de sus autores](https://raw.githubusercontent.com/josephwright/beamer/main/doc/beamerug-guidelines.tex) | Títulos que expliquen el mensaje, texto breve, color moderado y tipografía legible. Reescribir o dividir contenido antes de reducir la letra. |
| [Moloch](https://ctan.org/pkg/moloch) | Conservar el tema existente y su personalización local. Es una base adecuada para este estilo, no una afirmación de superioridad universal. |
| [fontspec](https://ctan.org/pkg/fontspec) con LuaLaTeX | Mantener Fira Sans/Mono mediante OpenType, español y fuentes resueltas desde TeX Live, sin rutas personales. |
| [TikZ: Guidelines on Graphics](https://tikz.dev/guidelines) | Una intención por figura, fuentes y grosores coherentes, etiquetas próximas a sus elementos y ausencia de adornos que distraigan. |
| [TikZ: Nodes and Edges](https://tikz.dev/tikz-shapes) | Nodos con anclas y texto de ancho controlado; `positioning`, `calc` y `fit` cuando faciliten alineación y agrupación. Flechas uniformes mediante `arrows.meta`. |
| [booktabs](https://ctan.org/pkg/booktabs) | Tablas editables y compactas. Usar pocas columnas, reglas horizontales y espacio entre filas, en continuidad con la referencia. |
| [tcolorbox](https://ctan.org/pkg/tcolorbox) y listings existente | Fragmentos de código breves y legibles cuando aporten comprensión; evitar capturas de código y dependencias de resaltado innecesarias. |
| [microtype](https://ctan.org/pkg/microtype) | Conservar los ajustes microtipográficos compatibles con LuaLaTeX; no usarlos para disimular contenido excesivo. |
| [latexmk](https://ctan.org/pkg/latexmk) y pgfpages de Beamer | Automatizar recompilaciones y generar notas desde la misma fuente. Separar la activación de notas del estilo, que actualmente fuerza ocultarlas. |

### Reglas concretas para diagramas y legibilidad

1. Redibujar el contenido como TikZ vectorial editable, con Fira y la paleta del
   PDF de referencia. Las imágenes PNG quedan para lectura en Markdown.
2. En las dos modalidades mantener posición, tamaño y nombre de las piezas
   equivalentes; hacer visible dónde cambia el entorno y dónde permanece la
   coordinación. Explicar con texto el significado de los colores.
3. Priorizar alineación y conectores sin cruces, con margen para las etiquetas.
   Distinguir flujo de tarea, intercambio de herramientas e inicio de conexión
   cuando se dibujen juntos; no dar significados diferentes a una flecha sin aclaración.
4. Diseñar a tamaño final. No usar `shrink` ni escalar una lámina densa con
   `resizebox` para hacerla caber. Conservar la escala tipográfica de referencia;
   títulos de 28 pt y cuerpo habitual de 15–18 pt son el punto de partida en
   este lienzo de 320 × 180 mm, no un mínimo universal para todo formato.
5. Usar texto explícito junto al objeto y notas para los detalles. Conservar
   párrafos y etiquetas legibles al compartir pantalla, sin depender de ampliar.
6. Emplear posiciones relativas dentro de las figuras y las macros existentes
   para la composición general. Los elementos con posición absoluta requieren
   revisión visual aunque el log de LaTeX no informe desbordamientos.

### Verificación de fidelidad

Comparar renderizados a igual tamaño con la referencia para una apertura,
una lámina de contenido y un diagrama. Después revisar todas las páginas de la
presentación y de las notas: márgenes, pesos, contraste, conectores, saltos de
línea y numeración. No dar por válido el diseño solo porque compiló.

Usar las versiones instaladas que compilen correctamente y registrar sus
requisitos. No actualizar TeX Live ni añadir paquetes por novedad. La selección
busca la solución más adecuada al contenido y al estilo confirmado.

## Pasos de implementación

### 1. Seleccionar y verificar el contenido

Revisar las fuentes enumeradas y contrastar la documentación oficial vigente.
Crear una selección por lámina para evitar omitir las explicaciones importantes
del Markdown o duplicar conceptos de las presentaciones. Separar arquitectura
documentada, ejemplos ilustrativos y evidencia histórica.

No comprobar credenciales ni ejecutar llamadas API para completar esta fase
conceptual. El acceso experimental y su presupuesto se resolverán posteriormente.

### 2. Escribir un guion único

Redactar títulos, mensajes, narración y fuentes para cada lámina. Introducir una
idea a la vez y conservar el mismo vocabulario: aplicación, modelo, coordinación,
herramienta y entorno. Mantener CSV → informe en todos los recorridos.

Explicar los dos escenarios de principio a fin, incluyendo preparar, conectar o
crear, enviar tarea, ejecutar, recuperar archivos y finalizar. Evitar instrucciones
internas del proyecto, tablas de resultados vacías y mensajes «por completar».
El estado experimental se aclara en las notas y en el cierre: recorridos API
explicados documentalmente, pruebas todavía pendientes.

### 3. Adaptar los diagramas y la guía

Crear figuras TikZ con tamaño, tipografía, espacios, colores y significado de
flechas consistentes. Usar etiquetas de ubicación explícitas y un texto breve
que permita entender cada dibujo por sí mismo.

Reutilizar las explicaciones de `docs/codex-vs-exec-server/` y actualizar sus
recorridos al computador local y al informe CSV. Conservar la distinción CLI / exec /
exec-server y la aclaración de quién inicia la conexión. Mantener la referencia OCI
como extensión, sin mezclarla con las figuras principales. El PDF de figuras es
material de lectura, no otra presentación de la sesión.

### 4. Construir una única presentación

Usar `openai_sandbox/presentation/openai-y-sandbox/` como ubicación canónica.
Mantener LaTeX/Beamer con Moloch, LuaLaTeX, latexmk y TikZ. Aplicar el estilo
obligatorio definido arriba, adaptando `estilo-sandbox.sty` como estilo canónico,
y reutilizar el mecanismo de notas de la presentación general.

```text
presentation/openai-y-sandbox/
  openai-sandbox.tex        Contenido y notas
  openai-sandbox-notas.tex  Importa el mismo contenido con notas activadas
  estilo.sty               Estilo compartido
  assets/                  Recursos gráficos editables y exportados
  compilar.py              Compilación y comprobaciones
  openai-sandbox.pdf        Único PDF principal
  openai-sandbox-notas.pdf  Exportación para el presentador
  README.md                Uso y compilación
```

### 5. Retirar las presentaciones anteriores del uso activo

Antes de retirar archivos, comprobar qué versiones ya están preservadas en Git
y conservar cualquier cambio o recurso único. No eliminar evidencia ni material
que no se haya integrado o preservado.

En `openai_sandbox/`, retirar la presentación especializada anterior como entrega
activa una vez verificada la nueva. Conservar sus conceptos y evidencias en la
presentación unificada o en documentación. Usar el historial Git para versiones
anteriores, en lugar de crear nuevos PDF llamados «final», «v2» o «completa».

En `share_knowledge_1/`, identificar el proyecto y sus presentaciones como archivo
histórico y dirigir su entrada principal a la presentación canónica. No mantener
ni regenerar sus copias o ZIP como entregas actuales. No hace falta borrar ese
repositorio ni fusionar historias Git para dejar una sola presentación vigente.

Actualizar README e índices afectados: una entrada principal «Abrir la
presentación», la exportación de notas identificada y enlaces de lectura sin
presentaciones alternativas. Verificar que el material activo sea autocontenido.

### 6. Verificar el resultado

Compilar ambas exportaciones y revisar todas las páginas renderizadas. Comprobar
texto, márgenes, flechas, contraste, fuentes, notas y enlaces. Verificar que el
compilador compruebe el número final de páginas y no conserve la exigencia antigua
de 17. No ejecutar las pruebas de Agents API como requisito de aceptación.

Hacer una revisión de comprensión con cuatro preguntas: ¿qué limita el sandbox?,
¿dónde se ejecuta Python en cada modalidad?, ¿para qué sirve exec-server?, ¿dónde
encaja OCI? Si no se puede hacer un ensayo con otra persona, registrar la revisión
editorial realizada sin afirmar validación con audiencia.

### 7. Cerrar con commit

Actualizar el estado del plan, revisar el diff y crear el commit final con los
entregables y documentación, sin credenciales, temporales ni cambios ajenos.
El commit está autorizado por el usuario y no requiere nueva confirmación.
Informar su identificador y las verificaciones. No hacer push como parte de este
cierre salvo instrucción adicional.

Si se cambia el README del repositorio histórico, registrar y guardar ese cambio
en su propio repositorio; informar ambos commits. No mezclar repositorios ni
incluir cambios históricos ajenos a la consolidación.

## Entregables y aceptación

- Una sola presentación vigente, con una fuente y exportación opcional de notas.
- Contenido conceptual completo para explicar ambos escenarios antes de probarlos.
- Lo relevante de las tres familias de presentaciones integrado sin concatenarlas.
- Guía y diagramas importantes adaptados al escenario local y a la misma tarea.
- Apariencia coherente con `sandbox-permisos-app.pdf`, verificada con renderizados
  comparables; diagramas y tablas editables con la misma tipografía y paleta.
- Fuentes y notas suficientes para el presentador; ausencia de resultados API ficticios.
- OCI como extensión breve y Auto-review como explicación/apoyo contextual.
- README e índices con un solo punto de entrada; versiones anteriores históricas.
- Todas las páginas revisadas visualmente, enlaces válidos y commit final informado.

## Trabajo posterior: pruebas, fuera de esta entrega

Comprobar acceso, SDK, credenciales, compatibilidad local, controles y presupuesto.
Preparar y ejecutar el mismo CSV en las dos modalidades, recuperar y verificar
los informes, registrar resultados y limpieza de recursos. Después incorporar
la evidencia en esta misma presentación, sin crear una segunda.

No desplegar OCI. El experimento del Cookbook sigue como pendiente independiente.

## Referencias para contrastar al implementar

- [Arquitectura de Agents API](https://developers.openai.com/api/docs/guides/agents-api/architecture).
- [Self-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted).
- [OpenAI-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted).
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli).
- [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review).
- [OCI: Cookbook](https://github.com/openai/openai-cookbook/tree/main/examples/agents_api/sandboxes/oci/application_managed).
- [AERO: enseñanza explícita](https://www.edresearch.edu.au/guides-resources/practice-guides/explicit-instruction-practice-guide-full-publication).
- [TikZ: gráficos](https://tikz.dev/guidelines).

## Cierre de implementación

Completado el 17 de noviembre de 2026.

- Una presentación activa en `presentation/openai-y-sandbox/`: diez láminas de
  recorrido y dos apoyos. El PDF de notas importa la misma fuente.
- Estilo adaptado de la versión anterior: formato 320 × 180 mm, Fira Sans/Mono,
  paleta, composición y numeración conservadas. Figuras TikZ editables.
- Guía CLI/exec-server adaptada al computador local y al caso CSV; añadido el
  escenario alojado. Sus tres figuras comparten fuentes con la presentación.
- Caso CSV y verificador incorporados sin cambios, comprobados byte a byte contra
  el original. No se ejecutaron nuevas pruebas del cálculo ni de servicios API.
- Temas especializados, ejemplo TOML y captura conservados en documentación.
  La presentación anterior del repo activo se retiró, preservada en Git en
  `1721187`. El proyecto original y sus índices están identificados como históricos.
- Compilación con LuaLaTeX y latexmk: doce páginas por exportación, sin errores,
  desbordamientos ni caracteres faltantes. Se corrigieron escapes en notas y
  posiciones de etiquetas durante la revisión.
- Revisados los renderizados de las doce láminas, las doce páginas con notas y
  las tres figuras de la guía. Sin recortes ni solapamientos en la revisión final.
- Enlaces relativos del material activo y de los cuatro índices históricos
  modificados: sin destinos inexistentes. Sintaxis de compiladores y diffs revisados.
- Revisión editorial de comprensión realizada. No se afirma ensayo con audiencia,
  duración medida ni validación de una configuración de sandbox.
- Primer intento de compilación limitado por la caché de fuentes; compilación
  y revisión final realizadas con la escalación autorizada.
- Archivo histórico actualizado y guardado en su repositorio: commit `14d8c71`.
  El commit de cierre del repositorio activo se informa al usuario; no se hace push.

Permanecen para después: acceso y compatibilidad experimental, presupuesto,
pruebas self-hosted/OpenAI-hosted y mediciones. OCI continúa como extensión.
