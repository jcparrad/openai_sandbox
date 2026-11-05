# Una tarea, el mismo sandbox y dos revisores

**Pregunta:** ¿cuántas veces interviene una persona para que Codex termine la misma tarea con revisión manual o Auto-review?

Codex ejecutará seis casos sintéticos, verificará un informe y exportará una copia a una carpeta hermana. El evaluador es determinista y usa Python estándar: es una carga de trabajo de laboratorio. Codex es el agente observado; no se prueban Agents SDK, APIs alojadas ni calidad de modelos.

## 1. Preparar desde tu terminal

Requisitos: Python 3.11 o posterior y Codex CLI compatible con los perfiles de permisos, `auto_review` y las opciones del lanzador. El lanzador se contrastó con la ayuda de CLI 0.166.0. Ambos modos deben estar permitidos por la cuenta y los requisitos administrados. No se instalan dependencias ni se modifican configuraciones globales.

Desde la raíz de este repositorio, ejecuta:

```bash
codex --version
python3 examples/demo-sandbox/laboratorio.py preparar --lab "$HOME/codex-sandbox-demo-01"
```

El segundo comando crea una carpeta **nueva**, con esta estructura:

```text
codex-sandbox-demo-01/
  manual/proyecto/       Scripts y datos; raíz de trabajo de A
  manual/entregas/       Destino externo a esa raíz
  automatico/proyecto/   Copia inicial idéntica; raíz de trabajo de B
  automatico/entregas/   Destino externo equivalente
```

No abrir la carpeta padre como workspace ni ubicar el laboratorio en un temporal. No reutilizar carpetas con evidencia: cambia el sufijo a `02`, por ejemplo. Preparar el laboratorio no inicia Codex ni mide aprobaciones.

## 2. Abrir la sesión manual

```bash
python3 examples/demo-sandbox/laboratorio.py iniciar --lab "$HOME/codex-sandbox-demo-01" --modo manual --modelo gpt-6.1-sol
```

Sustituye el modelo por uno disponible si corresponde, usando **el mismo en ambas sesiones**. El lanzador abre una sesión interactiva nueva y entrega el [prompt fijo](prompt.txt). Cuando corresponda, responde a cada solicitud de permisos. Elige aprobación para esa acción, sin recordar nuevas reglas para el futuro. Cuenta también las denegaciones como intervenciones.

Antes de ejecutar, Codex debe informar qué entorno y permisos declara e inspeccionar las rutas reales, incluidos enlaces, para comprobar que `../entregas` esté fuera de **todas** las raíces escribibles y temporales. El modelo o revisor pueden no estar expuestos al agente: se registran como no verificables desde el chat y se continúa. Su ausencia como metadato no demuestra indisponibilidad. El tipo de revisor se respalda con la invocación solicitada y el comportamiento visible del cliente, sin atribuir decisiones automáticas no observadas. Si se detecta una regla previa que permite exportar sin revisión, no se podrá medir ese contraste. No elimines reglas corporativas ni cambies límites para forzar resultados.

Los ajustes del ejemplo no se suman a `sandbox_mode` o `sandbox_workspace_write`. Si alguna capa activa usa esos ajustes tradicionales, puede prevalecer sobre el perfil. Si se observa que el perfil no es efectivo o el cliente informa que el revisor solicitado no está disponible, registra esa limitación y detén la comparación. El lanzador no inspecciona ni modifica la política de tu organización.

Al terminar, registra las solicitudes visibles y sal con `/exit`. No cuentes confirmaciones de confianza, preparación o aclaraciones como permisos de la tarea; anótalas aparte.

## 3. Abrir la sesión automática

```bash
python3 examples/demo-sandbox/laboratorio.py iniciar --lab "$HOME/codex-sandbox-demo-01" --modo automatico --modelo gpt-6.1-sol
```

La [configuración manual](manual.config.toml) y la [automática](automatico.config.toml) solo difieren en `approvals_reviewer`. El lanzador las convierte en overrides `--config` de esa ejecución; no copia archivos a `~/.codex` ni `.codex`. Conserva la política de revisión existente. Añadir `--mostrar` al comando permite revisar la invocación sin abrir la sesión.

El sandbox permite escribir en el proyecto y temporales; la red de sus comandos está deshabilitada. Las conexiones del cliente con el servicio de Codex son independientes: esta demo sí utiliza tu acceso habitual a Codex, aunque el evaluador no llama APIs externas.

Si Auto-review deniega, falla o no está disponible, registra lo observado. No uses otro comando, otra ruta o `/approve` para eludir la denegación durante la medición.

## Los cuatro comandos de la tarea

El prompt solicita ejecutarlos por separado, desde `proyecto/`:

```bash
python3 evaluar.py evaluar --output informe.json
python3 evaluar.py verificar --input informe.json
python3 evaluar.py exportar --input informe.json --dest ../entregas/informe.json
python3 evaluar.py verificar --input ../entregas/informe.json
```

La referencia está en `casos.json`. El verificador usa los valores esperados, sin volver a ejecutar la lógica de cálculo. Generar/exportar no sobrescribe archivos. Una exportación exitosa comprueba contenido y SHA-256 de la copia.

Ejecutar estos comandos directamente en tu terminal permite comprobar el programa, pero **no mide el sandbox ni el revisor de Codex**. Tampoco basta un fallo de escritura para atribuirlo a Auto-review.

## Qué registrar

Completa una copia local del [registro comparativo](../../results/comparacion-aprobaciones.md). Cuenta prompts que exigieron respuesta humana, solicitudes elegibles observables, revisión/decisión y verificación final. Un prompt agrupado cuenta una vez. Si no se expone la revisión automática, escribe «no observable».

**Cero solicitudes no demuestra una ventaja de Auto-review:** puede significar que todo estaba permitido. Una tarea bloqueada con menos intervenciones no se presenta como mejora. La comparación solo es válida si el preflight confirma condiciones equivalentes y se conoce si ambas tareas terminaron.

Una pasada por modo es una demostración exploratoria. No es un benchmark de seguridad ni demuestra iguales resultados en la app u otros entornos.

## Si cambió el prompt durante un intento

Usar exactamente la misma versión del prompt en los dos modos. Si se corrigió después de abrir una sesión, salir con `/exit`, conservar el laboratorio anterior y preparar otro con un nombre libre, por ejemplo `codex-sandbox-demo-02`. Repetir A y B en sesiones nuevas desde ese laboratorio. No añadir aclaraciones diferentes a mitad de cada recorrido ni reemplazar los archivos del intento anterior. El lanzador rechaza copias que no coincidan con la versión actual.

## Estado y fuentes

El programa se comprobó localmente con generación, verificación, exportación, rechazo de duplicados y detección de un informe alterado. **Ambas sesiones interactivas completaron la tarea y entregaron informes idénticos.** En el manual se observaron cuatro solicitudes (tres de inspección y una de exportación); en el automático, el usuario confirmó cero intervenciones. No se atribuye una decisión automática concreta a partir del resumen ni se generaliza este resultado a otras tareas. Ver el registro para los detalles y límites de lo observado.

Documentación consultada el 5 de noviembre de 2026: [Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review), [perfiles de permisos](https://learn.chatgpt.com/docs/permissions) y [overrides de CLI](https://learn.chatgpt.com/docs/config-file/config-advanced#one-off-overrides-from-the-cli). Los perfiles son beta. Las reglas persistentes pueden evitar prompts aunque abras una sesión nueva: [reglas](https://learn.chatgpt.com/docs/agent-configuration/rules).
