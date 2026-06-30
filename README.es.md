# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 Español · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Manual de usuario del panel [3x-ui](https://github.com/MHSanaei/3x-ui) — una guía de usuario completa escrita para la versión **v3.4.2** del panel.

> **Espejo de solo lectura.** Este repositorio de GitHub es un espejo unidireccional — el código fuente del manual reside en un GitLab privado y se publica aquí automáticamente, por lo que siempre está actualizado. ¿Encontraste un error o inexactitud? Por favor, [abre un Issue](https://github.com/yukh975/3X-UI-Manual/issues). **No se aceptan Pull Requests** (se cierran automáticamente) — las correcciones se realizan en el origen.

## Contenido

| Archivo | Idioma | Formato |
| --- | --- | --- |
| **[3X-UI-MANUAL.ar.md](3X-UI-MANUAL.ar.md)** · [PDF](pdf/3X-UI-MANUAL.ar.pdf) | 🇸🇦 العربية | Markdown + PDF |
| **[3X-UI-MANUAL.en.md](3X-UI-MANUAL.en.md)** · [PDF](pdf/3X-UI-MANUAL.en.pdf) | 🇬🇧 English | Markdown + PDF |
| **[3X-UI-MANUAL.es.md](3X-UI-MANUAL.es.md)** · [PDF](pdf/3X-UI-MANUAL.es.pdf) | 🇪🇸 Español | Markdown + PDF |
| **[3X-UI-MANUAL.fa.md](3X-UI-MANUAL.fa.md)** · [PDF](pdf/3X-UI-MANUAL.fa.pdf) | 🇮🇷 فارسی | Markdown + PDF |
| **[3X-UI-MANUAL.id.md](3X-UI-MANUAL.id.md)** · [PDF](pdf/3X-UI-MANUAL.id.pdf) | 🇮🇩 Bahasa Indonesia | Markdown + PDF |
| **[3X-UI-MANUAL.ja.md](3X-UI-MANUAL.ja.md)** · [PDF](pdf/3X-UI-MANUAL.ja.pdf) | 🇯🇵 日本語 | Markdown + PDF |
| **[3X-UI-MANUAL.pt.md](3X-UI-MANUAL.pt.md)** · [PDF](pdf/3X-UI-MANUAL.pt.pdf) | 🇧🇷 Português | Markdown + PDF |
| **[3X-UI-MANUAL.ru.md](3X-UI-MANUAL.ru.md)** · [PDF](pdf/3X-UI-MANUAL.ru.pdf) | 🇷🇺 Русский | Markdown + PDF |
| **[3X-UI-MANUAL.tr.md](3X-UI-MANUAL.tr.md)** · [PDF](pdf/3X-UI-MANUAL.tr.pdf) | 🇹🇷 Türkçe | Markdown + PDF |
| **[3X-UI-MANUAL.uk.md](3X-UI-MANUAL.uk.md)** · [PDF](pdf/3X-UI-MANUAL.uk.pdf) | 🇺🇦 Українська | Markdown + PDF |
| **[3X-UI-MANUAL.vi.md](3X-UI-MANUAL.vi.md)** · [PDF](pdf/3X-UI-MANUAL.vi.pdf) | 🇻🇳 Tiếng Việt | Markdown + PDF |
| **[3X-UI-MANUAL.zh-CN.md](3X-UI-MANUAL.zh-CN.md)** · [PDF](pdf/3X-UI-MANUAL.zh-CN.pdf) | 🇨🇳 简体中文 | Markdown + PDF |
| **[3X-UI-MANUAL.zh-TW.md](3X-UI-MANUAL.zh-TW.md)** · [PDF](pdf/3X-UI-MANUAL.zh-TW.pdf) | 🇹🇼 繁體中文 | Markdown + PDF |

## Qué hay de nuevo en 3.4.2

La versión 3.4.2 es una actualización importante: WireGuard se ha migrado al modelo multicliente, REALITY incorpora un escáner de objetivos en vivo, los balanceadores ganan las pestañas Observatory/Burst Observatory y se ha añadido la confirmación de ajustes sensibles con el código 2FA. A continuación se enumeran los cambios respecto a 3.4.1, agrupados por secciones del manual.

### Cambios en la sección 1 — Introducción, requisitos e instalación

- En el menú lateral (y en el panel deslizante móvil) ha aparecido el botón **«Documentación»** (icono de libro) — abre la documentación oficial `https://docs.sanaei.dev/`.
- La versión mínima de Xray a la que se actualiza el panel se ha elevado a **26.6.27** (se incluye el núcleo Xray 26.6.27).

### Cambios en la sección 2 — Acceso al panel y seguridad

- Con 2FA activado, cambiar el usuario/contraseña del administrador y desactivar 2FA ahora requieren **introducir el código actual** de la aplicación de autenticación (confirmación de cambios sensibles).
- LDAP: nuevo interruptor **«Omitir la verificación del certificado TLS»** (`ldapInsecureSkipVerify`) — desactiva la verificación del certificado en LDAPS; disponible solo si está activado «Usar TLS (LDAPS)».

### Cambios en la sección 3 — Resumen / Dashboard

- El botón de versión del panel ahora siempre abre la ventana de actualización (véase la sección 16 — canal dev).
- Mejora transversal de **accesibilidad**: etiquetas aria para los iconos y activación de elementos con Enter/Espacio (para lectores de pantalla y navegación con teclado).

### Cambios en la sección 4 — Inbounds: creación y parámetros generales

- La acción **«Exportar todos los enlaces»** ahora genera los enlaces a través del motor de suscripciones — aplica la plantilla de remark a cada cliente y prefiere los endpoints de Host gestionados (antes había un remark fijo `inbound-email`).

### Cambios en la sección 5 — Protocolos

- **WireGuard se ha migrado al modelo multicliente.** Los peers ahora son clientes normales (con asignación automática de dirección en el túnel, soporte de suscripciones, límites de tráfico/plazo y grupos); se ha eliminado la lista inline «Peers» del formulario del inbound.
- En el inbound WireGuard se ha añadido un campo **DNS** configurable (por defecto `1.1.1.1, 1.0.0.1`) y una **tarjeta de configuración del cliente** — copiar/descargar/QR del `.conf` completo y del enlace `wireguard://`/`wg://`.

### Cambios en la sección 6 — Transporte (Stream Settings)

- En XHTTP, para los inbounds nuevos el parámetro `maxConnections` en **xmux** ahora es por defecto **6** (antes `0` — sin límite). Los inbounds existentes conservan su valor.

### Cambios en la sección 7 — Seguridad de la conexión: TLS, XTLS y REALITY

- Se ha añadido un **escáner de objetivos REALITY en vivo**: los botones **«Escanear»** (comprobar el objetivo actual «en vivo») y **«Buscar objetivos»** (escanear un dominio o un rango **IP/CIDR** y seleccionar objetivos aptos según sus certificados). Los campos «Destino» y SNI ahora quedan vacíos al seleccionar REALITY por primera vez.

### Cambios en la sección 8 — Clientes

- La ampliación de plazo/cuota mediante `bulkAdjust` ahora **activa automáticamente** al cliente desactivado solo por agotamiento (plazo vencido o cuota superada), si la ampliación lo devuelve dentro de los límites. Los desactivados manualmente o todavía agotados permanecen desactivados.

### Cambios en la sección 9 — Grupos de clientes

- **«Reiniciar tráfico»** de un grupo ahora pone a cero **solo el contador del propio grupo**; los contadores, cuotas y estado de cada cliente no se ven afectados, y no se requiere reiniciar Xray. Este es un cambio respecto al comportamiento anterior (antes se reiniciaba el tráfico de todos los clientes del grupo).

### Cambios en la sección 10 — Suscripciones (Subscription)

- En los **hosts gestionados**, el campo **VLESS route** se ha redefinido: ahora es un único valor `0-65535` (en lugar de una lista de puertos) y se «incrusta» realmente en el UUID de cada suscripción (raw/JSON/Clash).
- La variable `{{EMAIL}}` (y su sinónimo `{{USERNAME}}`) en la plantilla de remark ahora se muestra solo en el **primer enlace** del cliente — al igual que el bloque de tráfico/plazo.

### Cambios en la sección 11 — Xray: enrutamiento, outbounds, DNS y extensiones

- **Balanceadores**: la página se ha dividido en las pestañas **«Configuración del balanceador»** y **«Observatory»**; en lugar de JSON en bruto, ahora hay formularios de Observatory y Burst Observatory (en Burst se ha añadido el campo **«Método HTTP»**). Un balanceador Random/Round-robin con `fallbackTag` ahora crea automáticamente un Burst Observatory.
- Al eliminar un outbound o un balanceador, el panel limpia automáticamente las referencias relacionadas en el enrutamiento y muestra una **vista previa de las consecuencias** en el diálogo de confirmación.
- En las reglas de enrutamiento, el criterio de red **L4** se escribe en la configuración en minúsculas (`tcp`/`udp`) y en la tabla se muestra en mayúsculas.
- Los errores en el formulario de añadir/editar balanceador ahora se posponen hasta el primer toque del campo o el intento de guardar.

### Cambios en la sección 16 — Operación: copias de seguridad, registros, actualización, CLI

- Los nombres de los archivos de copia de seguridad ahora contienen la dirección del servidor y la **fecha-hora**: `{host}_AAAA-MM-DD_HHMMSS.db` (`.dump` para PostgreSQL), por ejemplo `panel.example.com_2026-06-27_000000.db` — tanto al descargarlos desde el panel como en las copias enviadas por el bot de Telegram.
- Se puede activar el **canal dev** de actualizaciones desde una compilación estable: el botón de versión siempre abre la ventana de actualización, y ha aparecido el interruptor **«Canal Dev»** con una advertencia sobre la inestabilidad y la ausencia de reversión automática.

---

Creado a partir del análisis de los archivos fuente del panel. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
