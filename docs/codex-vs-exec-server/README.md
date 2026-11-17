# `codex` y `codex exec-server`: ¿qué cambia?

Guía conceptual · Lectura: 5 minutos · Revisada el 17 de noviembre de 2026

**Con `codex` abres una sesión de trabajo en la terminal. Con `codex exec-server` conectas una máquina a una sesión de Agents API para que ejecute allí sus herramientas.**

Para entenderlo, sigue una misma tarea en los dos casos: **leer `ventas.csv` y generar `grafico.png` en una máquina de OCI**. Es un ejemplo ilustrativo; todavía no se ha ejecutado este experimento.

## 1. Primero, distingue tres funciones

| Función | Qué hace | Ejemplo |
|---|---|---|
| Recibir la tarea | Permite pedir un resultado. | «Genera un gráfico de ventas». |
| Coordinar el trabajo | Consulta al modelo, solicita herramientas y usa sus resultados para continuar. | Leer el CSV → escribir Python → ejecutarlo → comprobar el gráfico. |
| Ejecutar herramientas | Realiza las operaciones en una máquina. | Ejecutar Python y guardar el PNG. |

La documentación llama **harness** al programa que coordina ese ciclo. El **modelo** propone los pasos; el **entorno** aporta los procesos y archivos. Son piezas diferentes. [Arquitectura de Agents API](https://developers.openai.com/api/docs/guides/agents-api/architecture).

## 2. Recorrido A: abres `codex` en la terminal

Entras por SSH a tu máquina de OCI, abres el directorio de trabajo y ejecutas:

```bash
codex
```

Escribes: «Lee ventas.csv y genera grafico.png».

![Recorrido A: tú entregas la tarea en la terminal; Codex CLI coordina desde OCI, consulta al modelo en OpenAI y ejecuta Python en OCI.](assets/recorrido-1.png)

**Qué mirar:** Codex CLI está en tu máquina y conduce la sesión, consultando al modelo remoto. El gráfico se genera en OCI. Esta ubicación es la elegida para el ejemplo; también puedes abrir Codex en tu portátil. [Codex CLI](https://learn.chatgpt.com/docs/codex/cli).

## 3. Recorrido B: conectas la máquina con `codex exec-server`

Tu aplicación crea una sesión de Agents API. En OCI arrancas el ejecutor, con la autenticación preparada y los datos de conexión que devuelve la API:

```bash
codex exec-server \
  --remote "<URL devuelta por la sesión>" \
  --environment-id "<ID del entorno de la sesión>"
```

Este fragmento muestra el papel del comando; la preparación completa está en la [guía self-hosted](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted).

![Recorrido B: tu aplicación envía la tarea a Agents API en OpenAI; el servicio coordina y el ejecutor en OCI ejecuta Python y devuelve resultados.](assets/recorrido-2.png)

**Qué mirar:** la coordinación está en OpenAI. El ejecutor recibe solicitudes de herramientas y devuelve resultados. Tu aplicación entrega la tarea y gestiona el entorno; no necesita reenviar cada comando. [Arquitectura self-hosted](https://developers.openai.com/api/docs/guides/agents-api/architecture#connect-your-own-environment).

Las flechas muestran el flujo de mensajes. **La conexión de red la inicia el ejecutor desde OCI hacia OpenAI**, mediante WebSocket; los mensajes circulan en ambos sentidos. [Conexión del ejecutor](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted#how-the-connection-works).

## 4. La diferencia, una al lado de la otra

| Pregunta | `codex` | `codex exec-server` con Agents API |
|---|---|---|
| ¿Dónde entregas la tarea? | En la conversación de la terminal. | En tu aplicación, que llama a la API. |
| ¿Dónde se coordina el ciclo? | En el cliente CLI, que consulta al modelo. | En el servicio de OpenAI. |
| ¿Qué hace el proceso en OCI? | Lleva la sesión y ejecuta herramientas. | Ejecuta las herramientas solicitadas por la sesión remota. |
| ¿Dónde se genera el gráfico del ejemplo? | En OCI. | En OCI. |

La tabla compara los dos recorridos dibujados. El resultado puede ser el mismo: cambia cómo se organiza el trabajo.

## 5. Una tercera opción: `codex exec`

También puedes ejecutar una tarea desde un script:

```bash
codex exec "Lee ventas.csv y genera grafico.png"
```

Es Codex en modo no interactivo. Sirve para automatización y CI. **Poder lanzar una tarea por código no obliga a usar `exec-server`.** [Modo no interactivo](https://learn.chatgpt.com/docs/non-interactive-mode).

| Si necesitas… | Opción que encaja |
|---|---|
| Conversar y trabajar desde la terminal. | `codex` |
| Lanzar una tarea desde un script o pipeline. | `codex exec` |
| Que una sesión de Agents API utilice tu máquina como entorno. | `codex exec-server` |

## 6. Lo que conviene recordar

**Dónde está la máquina** y **dónde se coordina el agente** son decisiones distintas. En ambos dibujos, Python corre en OCI y el modelo está en OpenAI.

El entorno self-hosted requiere que prepares sus dependencias y controles de aislamiento. Los resultados de herramientas vuelven al servicio; tener los archivos en OCI no significa que todo el procesamiento ocurra allí. [Responsabilidades del entorno](https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted#prepare-your-environment).

### Comprueba si ya se entiende

1. ¿Necesitas `exec-server` para usar Codex por SSH en una VM? **No; puedes abrir `codex` allí.**
2. ¿Arrancar `exec-server` basta para pedir el gráfico? **Necesitas además una sesión conectada y enviarle la tarea mediante la API.**
3. ¿Qué comparten los dos ejemplos? **La máquina y las herramientas que producen el gráfico.**

Consulta las [fuentes y decisiones de diseño](fuentes-y-diseno.md). El [experimento con OCI](../../PENDIENTES.md) sigue pendiente.

## Diagramas para leer y reutilizar

Los diagramas están integrados como imágenes PNG; pueden verse sin soporte de Mermaid. También están disponibles en un [PDF vectorial de dos páginas](output/pdf/diagramas.pdf) y como [fuente editable en LaTeX/TikZ](diagramas.tex).

Para regenerar el PDF y las imágenes, desde esta carpeta:

```bash
python3 compilar.py
```

Requisitos: LuaLaTeX, PGF/TikZ, standalone, fontspec, TeX Gyre Heros y Poppler (`pdfinfo` y `pdftoppm`). La compilación comprueba que haya dos páginas y que no se informen desbordamientos ni caracteres faltantes. Los archivos intermedios quedan en `build/`, ignorado por Git.
