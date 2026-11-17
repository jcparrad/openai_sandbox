# Presentación única: OpenAI y sandbox

[Abrir presentación](openai-sandbox.pdf) · [Exportación con notas](openai-sandbox-notas.pdf)

**Una misma tarea en tu computador y en OpenAI.** Diez láminas explican el caso,
el sandbox, las piezas del agente, las dos modalidades de Agents API y su relación
con Codex y las aprobaciones. Dos apoyos integrados amplían OCI y la evidencia
histórica de Auto-review. No se presenta una ejecución nueva de Agents API.

## Archivos

- `openai-sandbox.tex`: contenido y notas de las doce láminas.
- `openai-sandbox-notas.tex`: importa el mismo contenido con notas a la derecha.
- `estilo.sty`: adaptación del estilo de sandbox-permisos-app; Fira y paleta original.
- `assets/`: diagramas TikZ compartidos con la guía Markdown.
- `compilar.py`: compilación, control de errores y renderizado.
- [Diseño y procedencia](diseno.md): decisiones, fuentes y selección del material.
- [Guía del presentador](../../docs/guia-presentador.md): relato y estado de las pruebas.

## Compilación y revisión

Desde la raíz del repositorio:

```bash
python3 presentation/openai-y-sandbox/compilar.py
```

Requisitos: TeX Live con LuaLaTeX, latexmk, Beamer, Moloch, fontspec, microtype,
booktabs, array, tcolorbox, listings, babel, pgfpages, TikZ y graphicx; fuentes
Fira Sans y Fira Mono; Poppler (`pdfinfo`, `pdftoppm`). No requiere instalar
Pygments ni habilitar shell-escape. No instala paquetes.

El script exige doce páginas por exportación, controla desbordamientos,
caracteres faltantes y referencias indefinidas, y genera imágenes de revisión a
1600 píxeles. Intermedios y PNG de las láminas quedan en
`presentation/build/openai-y-sandbox/`, ignorado por Git.

Revisar todas las páginas y las notas después de editar: el posicionamiento
absoluto puede producir solapamientos aunque LaTeX no informe un desbordamiento.
Comprobar contraste, tamaño al compartir pantalla, notas, flechas y enlaces.
Ambos PDF deben conservar el mismo orden y contenido de láminas.
