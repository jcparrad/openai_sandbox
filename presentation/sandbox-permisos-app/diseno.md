# Diseño de la presentación

Investigación y aplicación: 5 de noviembre de 2026.

## Temas comparados

| Tema | Qué aporta | Decisión para este material |
| --- | --- | --- |
| [Moloch](https://ctan.org/pkg/moloch) | Diseño minimalista y opciones de personalización | Base elegida, con un estilo local que conserva la composición editable existente |
| [Focus](https://ctan.org/pkg/beamertheme-focus) | Diseño limpio centrado en el contenido | Buena alternativa para presentaciones convencionales con menos ajustes de composición |
| [Gotham](https://ctan.org/pkg/beamertheme-gotham) | Flexibilidad sobre LaTeX3 e inspiración en Metropolis | Alternativa para un sistema de temas más amplio; innecesaria para estas 17 páginas |

El manual de Beamer recomienda textos breves, títulos informativos, contraste alto, uso moderado del color y evitar reducir la fuente para encajar más texto. También aconseja evitar particiones de palabras. Estas recomendaciones guían la revisión; las notas conservan los detalles técnicos.

La elección es un criterio de diseño para esta presentación, no una clasificación universal. La versión instalada de Moloch puede diferir de la publicada actualmente en CTAN.

## Paquetes aplicados

- [fontspec](https://ctan.org/pkg/fontspec): selección de Fira Sans y Fira Mono con LuaLaTeX. El peso ligero distingue los títulos y el seminegrita destaca conclusiones y etiquetas.
- [microtype](https://ctan.org/pkg/microtype): ajuste microtipográfico compatible con LuaLaTeX. No sustituye la revisión del espacio disponible.
- [booktabs](https://ctan.org/pkg/booktabs): tablas con reglas horizontales y espacio entre filas. Se aplica a las dimensiones de permisos y a los resultados de la demo.
- [tcolorbox](https://ctan.org/pkg/tcolorbox) con [listings](https://ctan.org/pkg/listings): ejemplo TOML con título y resaltado de sintaxis, sin shell-escape ni dependencia de Pygments.
- TikZ: se conservan los diagramas explicativos editables y se unifica el tratamiento de conectores, límites y nodos.

## Criterios aplicados

La guía oficial de [Beamer](https://ctan.org/pkg/beamer), las [recomendaciones de sus autores](https://github.com/josephwright/beamer/blob/main/doc/beamerug-guidelines.tex) y las documentaciones de los paquetes anteriores sirven como referencias técnicas. Las siguientes decisiones de composición son específicas de este material:

1. Una idea principal por página y notas para los matices técnicos. Se mantienen las 17 páginas, las referencias y las condiciones de interpretación.
2. Composiciones según el contenido: apertura asimétrica, diagramas, comparaciones, código y resultados con cifras grandes.
3. Márgenes consistentes, títulos ligeros y jerarquía de tamaño y peso. Menos etiquetas repetidas en el encabezado.
4. Paleta contenida: índigo, lavanda y neutros claros. El color destaca información, junto con texto que explica su significado.
5. Páginas oscuras seleccionadas para dar ritmo a la apertura y a conceptos centrales, con título en peso regular para mejorar su lectura sobre fondo oscuro. El código usa una superficie oscura delimitada.
6. Las cifras 4 y 0 describen solo la demo observada. Se conservan la confirmación del usuario, el resultado 6/6 y la limitación de una pasada por modo.
7. Fuentes libres de TeX Live y un archivo de estilo separado. No se distribuyen archivos tipográficos ni se necesita una ruta local de fuentes.

## Mantenimiento

Editar colores, fuentes y macros comunes en `estilo-sandbox.sty`; contenido y notas en `sandbox-permisos-app.tex`. Compilar con `python3 presentation/sandbox-permisos-app/compilar.py` desde la raíz. Comprobar después las 17 páginas visualmente: un registro sin desbordamientos no detecta por sí solo todos los solapamientos en composiciones con posiciones absolutas.
