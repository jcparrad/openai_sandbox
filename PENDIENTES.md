# Pendientes

## Punto de reanudación para mañana

Registrado el 17 de noviembre de 2026. Retomar el 18 de noviembre, sin ejecutar
las pruebas ni desplegar recursos durante este cierre.

**Ya terminado:** una sola presentación conceptual, con notas y guías, y el mapa
de tres recorridos: Codex CLI, Agents API self-hosted local y OpenAI-hosted.

**Lo que sigue, en este orden:**

1. **Ajuste editorial:** mover OCI de la penúltima a la última lámina y dejar
   explícito: «No implementado ni probado en este proyecto; extensión futura».
   Conservar el enlace al Cookbook y sincronizar notas y guía. Recompilar y revisar.
   Este ajuste todavía no está hecho.
2. **Comprobar viabilidad:** acceso a Agents API, SDK/modelo compatibles,
   requisitos del ejecutor local, configuración segura de credenciales y costo
   estimado. Definir presupuesto antes de consumir servicios.
3. **Probar self-hosted en el computador:** usar el CSV de referencia, conectar
   `codex exec-server`, recuperar el informe, verificarlo y cerrar los recursos.
4. **Probar OpenAI-hosted:** repetir la misma tarea y verificación, descargar los
   artefactos y finalizar la sesión.
5. **Documentar e incorporar resultados reales** en la misma presentación.
   Registrar también fallos o limitaciones; no crear otra presentación.

Las dos pruebas API siguen sin ejecutar. OCI queda como nota final documental,
no como una tercera prueba que deba realizarse para cerrar el proyecto.

## Probar las dos modalidades de Agents API

- Estado: pendiente; la presentación actual explica los recorridos documentalmente.
- Caso común: [CSV e informe](examples/csv-informe/README.md).
- Self-hosted: conectar el computador del presentador con `codex exec-server`.
- OpenAI-hosted: solicitar un entorno, entregar el CSV y recuperar sus artefactos.
- Al retomarlo: comprobar acceso, compatibilidad, controles, credenciales y presupuesto; ejecutar, verificar y registrar resultados y limpieza.
- Incorporar la evidencia en la misma presentación; no crear otra charla.

## Extensión: sandbox self-hosted en OCI

- Registrado: 17 de noviembre de 2026. Estado: no ejecutado.
- Referencia: [OpenAI Cookbook — OCI, application-managed](https://github.com/openai/openai-cookbook/tree/main/examples/agents_api/sandboxes/oci/application_managed).
- Objetivo: estudiar cómo una aplicación crea, conecta, utiliza y elimina un entorno OCI para Agents API.
- Es una extensión posterior; no se necesita para las dos pruebas principales.
- Revisar requisitos, disponibilidad beta y SDK del ejemplo, acceso y costos antes de implementarlo. Incluir limpieza de recursos.
