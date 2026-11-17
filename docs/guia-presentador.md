# Guía de la presentación única

[Abrir las láminas](../presentation/openai-y-sandbox/openai-sandbox.pdf) · [Mismo documento con notas](../presentation/openai-y-sandbox/openai-sandbox-notas.pdf)

Objetivo: que una persona pueda explicar qué hace el agente, dónde se ejecutan
las herramientas y quién proporciona el entorno. Una misma tarea: CSV → informe.
Duración orientativa: 20–25 minutos más preguntas. No es una duración medida.

## Narración y selección de materiales

| Lámina | Qué decir y señalar | Procedencia |
|---|---|---|
| 1 | «Queremos un informe real a partir de un CSV». Mostrar entrada, trabajo y salida antes de nombres de productos. | Caso de la presentación general. |
| 2 | «El sandbox acota las acciones sobre recursos». Distinguir archivos, procesos y red; los límites dependen del entorno. | Introducción breve y fundamentos de Codex. |
| 3 | «Recibir, coordinar y ejecutar son funciones distintas». Seguir una petición entre las piezas; definir harness solo después. | General y guía Markdown. |
| 4 | «El entorno lo proporcionas tú o lo proporciona OpenAI». Es la comparación dentro de Agents API. | Modalidades documentadas. |
| 5 | «Conectamos el computador como lugar de ejecución». Leer la arquitectura siguiendo tarea, órdenes y resultados. | Guía de exec-server adaptada a local. |
| 6 | «Pedimos a OpenAI que proporcione el entorno». Mismas posiciones, distinta agrupación del entorno. | Guía OpenAI-hosted. |
| 7 | «La tarea se conserva; cambia la preparación». Comparar responsabilidades y recuperación de archivos. | Síntesis de arquitectura y archivos. |
| 8 | «Conversar en Codex es distinto de conectar un ejecutor». Una aplicación puede ser un script. | Guía CLI/exec/exec-server. |
| 9 | «Un límite y una revisión hacen trabajos distintos». Ejemplo ilustrativo de exportación; no prometer excepciones. | Presentación de Codex. |
| 10 | «Elegimos el entorno y comprobamos la salida». Volver al mismo pedido; aclarar el estado experimental. | Verificación y conclusiones de la general. |
| Apoyo A | OCI es una ubicación posible de self-hosted. Mostrar solo si aporta al grupo. | Cookbook; no ejecutado. |
| Apoyo B | Explicar el resultado histórico de intervenciones, con su tarea y límites propios. | Registro de Codex del 5 de noviembre. |

## Recorridos que se explican

**Self-hosted local:** preparar el entorno y sus controles; crear sesión;
conectar ejecutor; enviar tarea; recuperar y verificar archivos; finalizar la
sesión y detener el ejecutor. La conexión la inicia el ejecutor hacia el servicio.

**OpenAI-hosted:** solicitar entorno con archivos/configuración; esperar que se
conecte; enviar tarea; recoger el artefacto; conservar la salida y cerrar sesión.
Los diagramas son flujos conceptuales, no capturas de pruebas ejecutadas.

## Estado de la evidencia

- Las dos modalidades de Agents API se explican documentalmente. Sus pruebas no se ejecutaron para preparar esta charla.
- El CSV y su verificador provienen de un caso local con Python, con total de referencia 700. No atribuir ese resultado a una ejecución API.
- El experimento de Auto-review es otra carga de trabajo: seis casos sintéticos y exportación. Manual 4 intervenciones; automático 0 confirmado por el usuario. No es una medición de seguridad, coste o tiempo.
- OCI es una extensión pendiente.

La charla usa presente explicativo («la aplicación envía») sin convertirlo en
pasado experimental («ejecutamos ambas modalidades»). No hay tablas de resultados
API por completar ni cifras simuladas como si fueran observadas.

## Preguntas para revisar la claridad

1. ¿Qué limita el sandbox? Acciones sobre los recursos sujetos a sus controles.
2. ¿Dónde se ejecuta Python? En el entorno local o en el alojado, según modalidad.
3. ¿Para qué sirve exec-server? Para conectar y ejecutar herramientas en el entorno propio de una sesión de Agents API.
4. ¿Dónde encaja OCI? Dentro de self-hosted como infraestructura posible.
5. ¿Un informe correcto acredita aislamiento? No; el resultado y los controles se verifican por separado.

La revisión de contenido y renderizado no equivale a un ensayo con audiencia.
Cronometrar la narración en la aplicación de presentación antes de la sesión.

## Referencias por tema

Documentación consultada el 17 de noviembre de 2026; sus detalles pueden cambiar.
Las fuentes específicas también están enlazadas en las notas del PDF.

- [Arquitectura](https://developers.openai.com/api/docs/guides/agents-api/architecture).
- [Self-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted).
- [OpenAI-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted).
- [Archivos y artefactos](https://developers.openai.com/api/docs/guides/agents-api/environments/files).
- [Ciclo de vida](https://developers.openai.com/api/docs/guides/agents-api/environments/lifecycle).
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) y [modo no interactivo](https://learn.chatgpt.com/docs/non-interactive-mode).
- [Sandbox y aprobaciones](https://learn.chatgpt.com/docs/agent-approvals-security), [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review).
- [OCI en el Cookbook](https://github.com/openai/openai-cookbook/tree/main/examples/agents_api/sandboxes/oci/application_managed).

Para repetir el cálculo de referencia, consultar [el caso CSV](../examples/csv-informe/README.md).
Para preparar las pruebas posteriores, consultar [los pendientes](../PENDIENTES.md).
