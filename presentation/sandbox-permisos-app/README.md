# Sandbox y permisos en Codex

[Abrir la presentación](sandbox-permisos-app.pdf): diecisiete páginas, incluidas una lámina de demo y dos de apoyo. Explica responsabilidades, límites, modos, aprobaciones, configuración, red y ejecución local/cloud. El bloque Auto-review desarrolla activación, evaluación y resultados en tres páginas.

La lámina 15 resume la [demo de dos revisores](../../examples/demo-sandbox/README.md): ambos recorridos completaron la tarea, con cuatro intervenciones humanas en el manual y cero en el automático, confirmado por el usuario. El [registro](../../results/comparacion-aprobaciones.md) distingue resultados verificados, observaciones de interfaz y datos no observables en el resumen. Es una pasada por modo, sin generalizar el ahorro.

Fuente principal: [Sandbox, superficie app](https://learn.chatgpt.com/docs/sandboxing?surface=app), consultada el 5 de noviembre de 2026. Las notas de la fuente LaTeX contienen referencias complementarias y matices.

Los ejemplos son conceptuales: lectura y escritura con permisos distintos, revisión de una excepción, una carpeta adicional y acceso de red. Las comparaciones de configuración parten de una base común y cambian un ajuste a la vez. No se aplica la configuración al equipo.

La captura fue aportada por el usuario y se conserva en el apoyo. El PDF recorta la imagen original al menú relevante sin recrear sus etiquetas. Las notas incluyen fuentes, condiciones de interpretación y preguntas de comprensión.

## Compilar

Desde la raíz del proyecto:

```bash
python3 presentation/sandbox-permisos-app/compilar.py
```

Requisitos: LuaLaTeX, latexmk, Beamer/Moloch, fontspec, microtype, booktabs, array, tcolorbox, babel, TikZ, listings, graphicx, pgfpages, Poppler y las familias Fira Sans y Fira Mono (incluidas en TeX Live). No instala dependencias ni cambia la configuración de Codex. `ejemplo-config.toml` es material didáctico, no una configuración activa.

Diseño editorial independiente sobre Moloch: páginas claras, aperturas y conceptos seleccionados en índigo oscuro, Fira Sans y Fira Mono. `estilo-sandbox.sty` centraliza la paleta, tipografía y macros. Conserva diagramas y notas editables, usa booktabs para tablas y tcolorbox/listings para código. La [guía de diseño](diseno.md) recoge la investigación y los criterios aplicados. Los registros e intermedios quedan en `presentation/build/sandbox-permisos-app/`, ignorado por Git. El compilador comprueba diecisiete páginas y detiene la entrega ante desbordamientos o caracteres faltantes.

Para revisar las páginas:

```bash
pdftoppm -scale-to 1600 -png presentation/sandbox-permisos-app/sandbox-permisos-app.pdf presentation/build/sandbox-permisos-app/slide
```
