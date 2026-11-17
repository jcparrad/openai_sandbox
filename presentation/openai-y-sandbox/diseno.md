# Diseño y procedencia

Revisión: 17 de noviembre de 2026. La presentación explica conceptos y recorridos;
las pruebas API se realizarán después.

## Referencia visual conservada

Se adaptó `estilo-sandbox.sty` de la presentación de 17 láminas conservada en el
historial Git (`1721187`). Se mantienen lienzo 320 × 180 mm, Fira Sans y Mono,
jerarquía editorial, numeración discreta y paleta: noche `#17182B`, nieve `#F8F9FC`,
índigo `#5148B5`, lavanda `#B8B2FF` y ciruela `#7941A3`.

El contenido usa una fuente LaTeX y un estilo compartido. Las notas se activan en
un archivo que importa el contenido; no se duplican láminas para mantenerlas.
Los diagramas son vectoriales y editables, con la misma tipografía del documento.

## Selección del contenido

| Procedencia | Qué se integró |
|---|---|
| Presentación general de doce láminas | Caso CSV, piezas, verificación y conclusiones limitadas a la evidencia. |
| Introducción de seis láminas | Definición, propósito y dimensiones de control del sandbox. |
| Presentación de Codex | Estilo, distinción de límites y aprobación, resultado histórico manual/Auto-review. |
| Guía Markdown CLI/exec-server | Recibir tarea, coordinar y ejecutar; distinción entre CLI, exec y ejecutor. |
| Plan vigente | Self-hosted en el computador frente a OpenAI-hosted; OCI solo como extensión. |

Las versiones de origen del proyecto original se consideran históricas. La charla
actual no concatena sus páginas ni depende de ese repositorio para compilar.

## Prácticas aplicadas

- [Beamer, guía de sus autores](https://raw.githubusercontent.com/josephwright/beamer/main/doc/beamerug-guidelines.tex): títulos informativos, texto breve y detalles en notas. Se conserva una idea principal por lámina.
- [TikZ, Guidelines on Graphics](https://tikz.dev/guidelines): intención explícita, rótulos junto al objeto, fuentes uniformes y color con significado.
- [TikZ, nodos](https://tikz.dev/tikz-shapes): anclas y anchos de texto; flechas uniformes con `arrows.meta`.
- [Moloch](https://ctan.org/pkg/moloch), [fontspec](https://ctan.org/pkg/fontspec) y [microtype](https://ctan.org/pkg/microtype): reutilización del tema y tipografía existentes con LuaLaTeX.
- [booktabs](https://ctan.org/pkg/booktabs): tablas editables con pocas columnas y reglas horizontales.
- [latexmk](https://ctan.org/pkg/latexmk): recompilación automática, sin actualizar la distribución como requisito.

Los recorridos self-hosted y alojado mantienen fijos el computador, OpenAI, la
aplicación y el agente. El sandbox con Python se mueve de columna: el énfasis
índigo señala el lugar donde se ejecuta el trabajo. El texto
explica los roles, de modo que el significado no depende solo del color. Las
flechas dobles son intercambios de mensajes. Las notas aclaran por separado el
inicio de conexión saliente del ejecutor local.

Las decisiones de duración y número de láminas son editoriales para este material;
no son reglas universales de las herramientas citadas.

## Alcance de revisión

Compilar las dos exportaciones y revisar sus renderizados antes de entregar. La
lectura conceptual no sustituye un ensayo con audiencia ni una prueba de servicio.
Los controles de calidad y el resultado final se registran en el plan de trabajo.

Revisión de claridad: las láminas 5 y 6 muestran explícitamente «sandbox en tu
computador» y «sandbox en OpenAI». La diferencia principal se expresa por posición,
texto y énfasis, sin exigir deducirla del fondo de un grupo.

La lámina 4 introduce tres recorridos: Codex CLI y los dos escenarios de Agents
API. Así se distingue el uso del cliente de las modalidades de entorno antes de
mostrar los dibujos de self-hosted y OpenAI-hosted. En el alojado se aclara que
el usuario no inicia exec-server.
