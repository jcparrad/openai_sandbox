# Lectura complementaria: sandbox y permisos en Codex

Este texto conserva los temas especializados de la presentación anterior. La
charla vigente es [OpenAI y sandbox](../../presentation/openai-y-sandbox/README.md).
Los ejemplos de Codex no se trasladan automáticamente a cualquier servicio API.

## Alcance y revisión

El sandbox restringe accesos de los comandos. La política de aprobación define
cuándo una acción requiere revisión. El revisor puede ser una persona o, para
solicitudes elegibles, Auto-review. Cambiar el revisor no amplía por sí mismo las
rutas de escritura. Una denegación explícita se respeta; un fallo técnico del
revisor no equivale a una decisión de seguridad.

Ejemplo ilustrativo: guardar el informe dentro del proyecto puede estar permitido;
exportarlo fuera puede requerir una excepción si las políticas la admiten. Una
ubicación externa podría estar ya autorizada: hay que observar el alcance efectivo.
La lectura, la escritura y la red tienen dimensiones distintas.

## Configuración didáctica

Se conserva [ejemplo-config.toml](ejemplo-config.toml), sin activarlo. Muestra la
familia tradicional de configuración: `sandbox_mode`, `approval_policy`,
`approvals_reviewer` y `sandbox_workspace_write`. La demo histórica usa perfiles
`default_permissions`; no combinar ambas familias como si fueran una plantilla única.

- `read-only`: escrituras restringidas bajo los controles efectivos.
- `workspace-write`: escritura en raíces autorizadas y temporales según el entorno.
- `danger-full-access`: sin las fronteras del sandbox de Codex; permanecen permisos del sistema.
- `writable_roots`: puede añadir ubicaciones de escritura en el esquema tradicional.
- `network_access`: afecta la red de comandos de ese sandbox, no toda conexión del cliente o de conectores.

`workspace-write` no implica que todas las lecturas estén confinadas al proyecto.
La configuración efectiva depende de cliente, confianza y políticas administradas.
Consultar `/status` y `/permissions` en el CLI compatible. Los requisitos de la
organización pueden limitar qué preferencias se admiten.

La [captura histórica del selector](assets/selector-permisos.png) pertenece al
material aportado para la charla original. No garantiza opciones idénticas en
una cuenta o versión actual.

## Ejecución local y otras herramientas

Los comandos locales usan controles del sistema compatibles con el cliente.
No todo sandbox es una VM o contenedor. Navegación, búsqueda y conectores tienen
sus propios controles; no atribuirles automáticamente los del shell.

El [perfil de laboratorio general](../../examples/codex-auto-review/README.md)
explica otro ejemplo de configuración. No modifica la configuración personal por
estar guardado en el repositorio. La [demo manual/automática](../../examples/demo-sandbox/README.md)
conserva instrucciones y resultados específicos de su comparación.

## Límites de la conclusión

Una acción puede estar permitida y aun así modificar el archivo equivocado o
guardar un resultado incorrecto. Se revisan permisos, autorización de la tarea y
contenido del resultado. El sandbox no garantiza exactitud, seguridad integral ni
reversión automática.

Fuentes oficiales para contrastar al aplicar configuraciones:
[seguridad y aprobaciones](https://learn.chatgpt.com/docs/agent-approvals-security),
[Auto-review](https://learn.chatgpt.com/docs/sandboxing/auto-review),
[configuración](https://learn.chatgpt.com/docs/config-file/config-reference),
[requisitos administrados](https://learn.chatgpt.com/docs/enterprise/managed-configuration).
La explicación conceptual se revisó el 17 de noviembre de 2026; verificar cliente
y documentación al aplicar un perfil real.
