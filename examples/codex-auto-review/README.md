# Menos interrupciones al desarrollar y evaluar agentes

Ejemplo educativo personal para Codex CLI y ejecución local compatible desde la app. No representa una configuración corporativa ni demuestra conformidad con una política empresarial. Consulta de fuentes: 5 de noviembre de 2026.

[config.toml](config.toml) es una configuración de ejemplo independiente; no es una copia de la configuración personal. Conserva el ajuste genérico de esfuerzo `medium`, añade revisión automática y un perfil de laboratorio. Omite identidad, modelo, proyectos confiables, plugins, MCP, hooks y rutas personales.

## Qué hace y qué requiere

1. Permite editar el workspace y usar temporales, heredando `:workspace` y sus rutas protegidas. Limita otras lecturas a las rutas mínimas del runtime. Python, Conda, cachés o herramientas instaladas en otras carpetas pueden necesitar permisos locales concretos.
2. Activa el proxy y permite cuatro destinos públicos de ejemplo para API y paquetes. Elimina los registros que no uses y añade únicamente los endpoints autorizados de otros proveedores en una copia privada. Red habilitada sin proxy no aplica esta lista de dominios.
3. Mantiene `on-request` y selecciona `auto_review`: las solicitudes elegibles se revisan automáticamente. No se garantiza aprobarlas ni eliminar toda intervención humana.
4. Conserva la política de revisión existente. El bloque de criterios personales está comentado porque no se identificó la política vigente completa. El marcador NO es una política utilizable. Para personalizar, preservar primero el texto vigente completo en una copia privada; no publicar políticas internas.

Los perfiles de permisos son beta y las reglas experimentales pueden cambiar. La sintaxis se contrastó con la documentación vigente; no se ha activado ni verificado su aislamiento en terminal o app. La versión de referencia inspeccionada fue Codex CLI 0.166.0; la versión de la app no se verificó. Los requisitos administrados pueden impedir seleccionar el perfil o sustituir la política personal.

## Qué automatizar y con qué límites

| Actividad | Recomendación | Límite práctico |
| --- | --- | --- |
| Tests, lint y builds | Ejecutarlos dentro del workspace | Los scripts ejecutan código: revisar dependencias y cambios en los comandos |
| Dependencias | Entorno virtual o instalación local y versiones fijadas | Un registro permitido no garantiza paquetes seguros; evitar instalaciones globales |
| Internet y APIs | Lista corta de destinos aprobados y datos sintéticos | Un dominio permitido también puede aceptar uploads y generar consumo |
| Carpetas adicionales | Añadir solo una raíz de laboratorio en la copia privada | Cada carpeta adicional puede modificarse o borrarse; no incluir todo el home |
| Docker | Daemon de laboratorio aislado, con mounts, imágenes y privilegios revisados | El daemon actúa fuera del sandbox del cliente; sus contenedores no heredan automáticamente el proxy ni la lista de archivos |
| Publicación y despliegue | Autorización específica, con destino y efectos definidos | Tener acceso técnico no es autorización de negocio |

El ejemplo no permite sockets Docker automáticamente: OpenAI los considera una vía de escape local. Evitar una regla amplia `allow` para `docker`, `python`, shells o `curl`: puede ejecutar fuera del sandbox sin pasar por el revisor. Si hace falta revisión para una acción sensible ya permitida, usar una regla precisa `decision = "prompt"` o el control de aprobación de la herramienta; no basta con describirlo en la política del revisor.

Para Docker frecuente, preparar primero un entorno desechable separado de otros trabajos y credenciales. Después revisar una receta concreta de contenedor. Este paquete no crea ese entorno ni garantiza seguridad de Docker Desktop.

## Uso en terminal y app

1. Revisar el archivo sin ejecutarlo. No copiarlo sobre la configuración personal completa: se perderían otros ajustes.
2. Integrar las claves necesarias en una copia privada de `~/.codex/config.toml` o en `.codex/config.toml` de un proyecto confiable. Evitar mezclar `default_permissions` con `sandbox_mode` o `[sandbox_workspace_write]` en cualquier capa activa; no cambiar requisitos empresariales para hacerlo funcionar.
3. Para CLI, abrir una nueva sesión en el proyecto. Para app con ejecución local compatible, abrir una nueva conversación en ese proyecto y revisar el selector/perfil efectivo. Seleccionar otro modo en la interfaz puede cambiar la configuración de esa sesión.
4. Comprobar en cada cliente el perfil activo, el revisor y los límites efectivos antes de trabajar. No dar por hecho que compartir el archivo hace idénticas las dos sesiones.
5. Ensayar por separado una escritura permitida y una denegada en archivos sintéticos propios. Si se valida red, usar destinos públicos autorizados y peticiones sin datos sensibles. Registrar si hay bloqueo, solicitud o revisión y su resultado; no inferir el aislamiento a partir de la configuración.

El perfil gobierna comandos locales. Browser, Computer Use, búsqueda web, MCP, conectores y ejecuciones cloud tienen controles propios. Las aprobaciones de aplicaciones de Computer Use pueden seguir requiriendo intervención directa del usuario.

## Evaluaciones con APIs sin pedir permiso para cada llamada

Autorizar un lote finito antes de comenzar. Ejemplo de alcance que el usuario debe completar y aprobar: «Evalúa 10 casos sintéticos contra un endpoint y modelo aprobados; máximo 12 solicitudes totales contando reintentos, 500 tokens de salida por solicitud, concurrencia 1 y sin subir archivos». Son cantidades ilustrativas, no una autorización para ejecutar este ejemplo.

El ejecutor debe imponer esos contadores, límites de tokens, timeouts y parada. No son claves de `config.toml` ni límites económicos garantizados por Auto-review. Un test dentro del sandbox con acceso a API permitido puede generar cargos sin revisión adicional. Usar credenciales de prueba de mínimo privilegio y proyecto separado; obtener secretos del mecanismo autorizado y no imprimirlos ni incluirlos en prompts, trazas o salidas. El perfil de ejemplo no deniega ni administra las variables de entorno; controlar qué credenciales hereda el proceso por separado.

Configurar también rate limits y avisos de consumo en el proveedor. En OpenAI, las alertas de gasto descritas en la fuente no detienen las solicitudes: no tratarlas como corte de gasto. Un límite de solicitudes tampoco equivale por sí solo a un importe máximo garantizado; estimar el coste por modelo y entrada y usar controles de consumo efectivos del proveedor cuando existan.

## Preparación para GitHub público

Publicar el ejemplo saneado y su explicación; conservar en privado la política efectiva, los endpoints de trabajo, IDs de cuentas y proyectos, claves, wallets, nombres de clientes y datos de pruebas internas. No trasladar el `config.toml` personal, archivos de autenticación ni transcripciones completas de sesiones al repositorio.

Revisar el diff, los archivos nuevos y el historial antes de publicar. `.gitignore` no elimina contenido ya versionado. Activar push protection donde esté disponible y atender secret scanning; un escaneo sin alertas no demuestra ausencia de información corporativa. Si se expone una clave, revocarla o rotarla. Revisar manualmente también capturas, notas y PDFs.

Este ejemplo no autoriza publicar el repositorio completo: la revisión pública debe cubrir todos sus archivos e historial, no solo esta carpeta. No se ha realizado esa auditoría global.

## Fuentes y verificación

- [OpenAI: Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review): solicitudes elegibles, límites y reemplazo completo de política.
- [OpenAI: permisos](https://learn.chatgpt.com/docs/permissions): perfiles beta, herencia, proxy, límites de cobertura y sockets.
- [OpenAI: reglas](https://learn.chatgpt.com/docs/agent-configuration/rules): diferencia entre `allow`, `prompt` y `forbidden`.
- [OpenAI: configuración](https://learn.chatgpt.com/docs/config-file/config-basic): ubicaciones y prioridades.
- [OpenAI: requisitos administrados](https://learn.chatgpt.com/docs/enterprise/managed-configuration#configure-automatic-review-policy): política corporativa frente a personal.
- [OpenAI: rate limits y alertas](https://developers.openai.com/api/docs/guides/terraform/rate-limits-and-spend): alertas sin corte de solicitudes.
- [Docker: seguridad del daemon](https://docs.docker.com/engine/security/#docker-daemon-attack-surface): controlar el daemon puede permitir modificar archivos del host.
- [GitHub: secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning): revisión del historial y respuesta ante filtraciones.

Comprobaciones realizadas: parseo TOML, coherencia de claves con documentación y revisión del contenido nuevo para excluir valores personales y secretos reconocibles. No se instalaron dependencias, activó la configuración, ejecutó Docker ni realizaron llamadas a APIs de evaluación. No se probó una decisión del revisor con estos criterios.
