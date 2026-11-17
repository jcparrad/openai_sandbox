# OpenAI y sandbox

**[Abrir la presentación](presentation/openai-y-sandbox/openai-sandbox.pdf)** · [Mismas láminas con notas](presentation/openai-y-sandbox/openai-sandbox-notas.pdf)

Una tarea, dos entornos: leer un CSV sintético y generar un informe con Agents API.
La presentación explica self-hosted en tu computador y OpenAI-hosted, y distingue
ubicación, herramientas, controles y revisión de acciones.

Son diez láminas de recorrido y dos de apoyo, en un único documento. El estilo
conserva Fira Sans/Mono, formato 16:9 y la paleta de la presentación anterior de
sandbox y permisos. [Fuentes, diseño y compilación](presentation/openai-y-sandbox/README.md).

## Lectura y preparación

- [Guía del presentador](docs/guia-presentador.md): mensaje, narración y referencias por lámina.
- [Guía con diagramas](docs/codex-vs-exec-server/README.md): Codex CLI, ejecutor y las dos modalidades de Agents API.
- [Caso CSV de referencia](examples/csv-informe/README.md): datos, informe esperado y verificador.
- [Permisos y configuración de Codex](docs/codex-vs-exec-server/permisos-codex.md): lectura complementaria.
- [Demo histórica de dos revisores](examples/demo-sandbox/README.md) y [resultados](results/comparacion-aprobaciones.md): evidencia anterior de Codex.
- [Pendientes](PENDIENTES.md): pruebas de Agents API y extensión OCI.

## Estado de la evidencia

| Material | Estado |
|---|---|
| Arquitectura y recorridos de Agents API | Explicación documental; pruebas en computador local y OpenAI pendientes. |
| CSV de referencia | Cálculo local verificado en el proyecto original; no constituye ejecución de Agents API. |
| Codex manual / Auto-review | Ambos informes correctos. Cuatro intervenciones humanas frente a cero en el recorrido registrado. Una pasada por modo. |
| OCI | Ejemplo del Cookbook estudiado como extensión; no ejecutado. |

Las pruebas API se incorporarán a esta misma presentación. No se midieron ahorro
general, rendimiento comparativo ni seguridad integral. El detalle y límites de
la comparación histórica se conservan en su registro.

## Compilar

```bash
python3 presentation/openai-y-sandbox/compilar.py
```

Requiere LuaLaTeX, latexmk, Beamer/Moloch, Fira Sans/Mono y Poppler. Genera el PDF
principal y el de notas desde la misma fuente, comprueba doce páginas y renderiza
ambos para revisión. No llama a servicios API ni cambia la configuración de Codex.

La presentación de 17 láminas anterior se conserva en el historial Git
(commit `1721187` y anteriores); no se mantiene como otra presentación activa.
Los documentos de figuras son apoyos de lectura, no charlas alternativas.

Repositorio: [jcparrad/openai_sandbox](https://github.com/jcparrad/openai_sandbox).
Material personal educativo; no representa una política empresarial. Sin licencia
de redistribución elegida. Documentación consultada el 17 de noviembre de 2026.
