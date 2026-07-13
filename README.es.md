# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 Español · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 [Português](README.pt.md) · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Manual de usuario del panel [3x-ui](https://github.com/MHSanaei/3x-ui) — una guía de usuario completa escrita para la versión **v3.5.0** del panel.

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

## Qué hay de nuevo en 3.5.0

La versión 3.5.0 es un lanzamiento importante: MTProto se ha migrado al modelo multicliente (motor mtg-multi, secretos personales, cuotas y ad-tag), los hosts gestionados ahora son grupales (varios inbound y varias direcciones en un mismo registro), la restauración en un panel PostgreSQL acepta copias de seguridad de SQLite, los outbound han recibido «Target Strategy», la prueba «Real delay» y las columnas Egress/Country, y un balanceador puede usar otro balanceador como fallback. Se incluye el núcleo Xray 26.7.11. A continuación se enumeran los cambios respecto a 3.4.2 por secciones del manual.

### Cambios en la sección 1 — Introducción, requisitos e instalación

- El núcleo Xray se ha actualizado a **26.7.11**. Auto-migraciones asociadas: los cifrados Shadowsocks `none`/`plain` y VMess `none`/`zero` se han eliminado del núcleo (las configuraciones guardadas se reescriben automáticamente), y un outbound VLESS/Trojan sin cifrar hacia una dirección pública se rechaza al guardar.
- Nuevo comando **`x-ui pgclient [versión]`** y elemento **10. Install/Upgrade client tools (pg_dump/pg_restore)** en el menú PostgreSQL — instalación/actualización de las herramientas cliente de PostgreSQL.
- Correcciones de scripts: instalación de PostgreSQL y fail2ban en la familia RHEL (EPEL), Arch sin el `pacman -Syu` completo, nombre correcto del binario de Xray en ARM de 32 bits (`xray-linux-arm32`), confirmación del IPv4 detectado automáticamente antes de emitir el certificado por IP, y corrección del falso «Your input is invalid» al elegir el puerto ACME por defecto.

### Cambios en la sección 2 — Acceso al panel y seguridad

- Límite de IP: una conexión «muerta» ahora se bloquea **una sola vez**, y no en cada escaneo de 10 segundos — los contadores de fail2ban ya no se inflan y no hace falta aumentar `maxretry`.

### Cambios en la sección 4 — Inbounds: creación y parámetros generales

- En la lista de inbounds ha aparecido la **búsqueda** (por nota, puerto y protocolo), y las listas desplegables de nodos («Desplegar en», el filtro «Nodos») ahora admiten búsqueda.

### Cambios en la sección 5 — Protocolos

- **MTProto se ha migrado al modelo multicliente** (motor mtg-multi): los usuarios de MTProto ahora son clientes normales con su propio secreto, cuota, plazo, ad-tag y enlace personal `tg://proxy`. El campo «Secret» a nivel de inbound se ha eliminado (los inbounds existentes se convierten automáticamente), y «FakeTLS domain» pasa a ser el dominio por defecto para los nuevos secretos. Nuevos campos del inbound: **Max connections** (límite de conexiones) y **Public IPv4/IPv6** (para el ad-tag middle proxy). Los cambios de clientes se aplican «en caliente», sin tirar las sesiones de Telegram ajenas.
- WireGuard: el menú del inbound ha recibido el conjunto completo de acciones de clientes (Export All URLs, vinculación/desvinculación, grupos), la exportación se ha dividido en las pestañas **Config** y **Links**, el campo **«IPs permitidas WireGuard» ahora es editable** (varias entradas separadas por comas), y en la configuración de cliente de un inbound de nodo `Endpoint` ahora apunta a la dirección del nodo.

### Cambios en la sección 7 — Seguridad de la conexión: TLS, XTLS y REALITY

- La combinación **Finalmask + REALITY se rechaza** al guardar (provocaba la caída de Xray-core en la primera conexión); el texto de ayuda de minClientVer se ha actualizado a 26.3.27.
- Nuevo tipo de máscara TCP de Finalmask — **XMC (Minecraft)**: enmascara el flujo como tráfico de Minecraft (Hostname, Usernames, Password obligatorio con generación automática).

### Cambios en la sección 8 — Clientes

- Nueva columna **«Velocidad»** — velocidad en vivo de cada cliente (↑/↓, media móvil de ~5 segundos).
- La búsqueda de clientes vuelve a encontrar por **Telegram ID**; en el formulario del cliente los inbounds deshabilitados quedan ocultos de la lista de vinculación; corregida la acumulación de duplicados en la ventana «Desvincular».
- Los clientes MTProto tienen sus propios campos: **«MTProto secret»** (con regeneración) y **«Ad-tag (canal patrocinado)»** (32 caracteres hex); la cuota y el plazo ahora se aplican realmente a MTProto.

### Cambios en la sección 9 — Grupos de clientes

- En la ventana de información del cliente ahora se muestra su **grupo**.

### Cambios en la sección 10 — Suscripciones (Subscription)

- **Los hosts gestionados ahora son grupales**: un registro abarca **varios inbound** (selección múltiple) y **varias direcciones** (etiquetas; cada entrada puede llevar su propio `:puerto`; autocompletado de direcciones; vacío — se hereda la dirección del inbound). Las columnas de la lista muestran chips de direcciones e inbounds (con «+N»), las acciones y la API trabajan con grupos (`groupId`), y ha aparecido el endpoint masivo `POST /panel/api/hosts/bulk/add`. La ordenación de hosts ahora es global (por orden y luego por nota).
- El texto del **anuncio** (`subAnnounce`) ahora se muestra como banner en la página de información de la suscripción; en las plantillas personalizadas está disponible la variable `announce`.
- La página de información en el navegador ahora se abre también con los **enlaces JSON/Clash** (no solo con el principal).
- Los ajustes de host **Final Mask** y **Allow insecure** ahora actúan también en los enlaces raw (`fm=`) y para **Hysteria2** (`insecure=1` / `skip-cert-verify: true`) respectivamente.
- El rango de «Intervalos de actualización» (`subUpdates`) se ha corregido a **0–525600** (el anterior límite de la interfaz, 168, bloqueaba el guardado de la configuración tras actualizar desde 2.x).
- Los clientes de **WireGuard nativo ahora entran en las suscripciones Clash y JSON** (antes — solo en raw).

### Cambios en la sección 11 — Xray: enrutamiento, outbounds, DNS y extensiones

- Editor de outbound: nuevo campo **«Target Strategy»** (11 valores de `AsIs` a `ForceIPv4`), modo de prueba **«Real delay»** (tiempo completo con establecimiento del túnel; el modo HTTP ahora se mide sobre una conexión «caliente»), columnas **Egress** (IP de salida oculta tras un «ojo») y **Country** (bandera + país, etiqueta WARP) tras una prueba HTTP/Real.
- **El fallback de un balanceador puede apuntar a otro balanceador**: el panel construye por sí mismo un objeto loopback oculto (`_bl_…`), protege contra ciclos y contra la eliminación de un balanceador en uso; el prefijo `_bl_` queda reservado.
- La pestaña «Enrutamiento básico» ha recibido el selector **«Default Outbound»** — qué outbound procesa el tráfico que no coincide con ninguna regla (el seleccionado se mueve a la primera posición).
- Los servidores DNS con IP privadas ya no quedan bloqueados por la regla `geoip:private` — el panel mantiene por sí mismo una regla allow gestionada.
- Happy Eyeballs en la configuración de dial (sockopt) ahora se activa de verdad; «Try delay» por defecto 250 ms, el 0 explícito se conserva.
- Importación de suscripciones de outbound: en los enlaces `ss://` con `?plugin=`/`/` final el puerto se analiza correctamente.

### Cambios en la sección 12 — Nodos (multipanel, master/slave)

- Paquete de correcciones: guardar un cliente sin cambios ya no rompe el tráfico en vivo de los inbounds de nodo; las sobreescrituras de Host del nodo se aceptan en el maestro en la primera aceptación; la renovación automática abre una ventana de cuota nueva; la eliminación de un cliente en el maestro lo elimina por completo en los nodos; los inbounds del nodo no se barren antes de la primera aceptación; un inbound incorrecto no detiene la sincronización de tráfico del nodo; la comprobación de conflicto de puertos se limita al propio nodo.

### Cambios en la sección 14 — Bot de Telegram

- Al menú de comandos del bot se han añadido **`/usage`**, **`/inbound`**, **`/restart`** y el nuevo comando de administrador **`/clearall`** (restablecimiento del tráfico de todos los clientes, con confirmación).
- La lista de clientes en línea se rotula como `email - nota del inbound`; los mensajes de copia de seguridad y del registro de baneos incluyen el nombre del host; la búsqueda por Telegram ID funciona con independencia del formato de la configuración.

### Cambios en la sección 16 — Operaciones: copias de seguridad, registros, actualización, CLI

- **La restauración en un panel PostgreSQL acepta archivos SQLite**: una copia de seguridad normal `.db` o un `.dump` de migración se importan directamente en PostgreSQL (en una sola transacción, con comprobaciones antes de detener Xray). El diálogo de selección de archivo acepta `.dump,.db` en ambos SGBD; «Descargar archivo de migración» queda solo en los paneles PostgreSQL.
- Antes de restaurar un archivo `pg_dump`, el panel comprueba la legibilidad del volcado y, si las versiones no coinciden, sugiere el comando exacto `x-ui pgclient <versión>`.
- Reparaciones automáticas al arrancar: los contadores de tráfico desbordados se acotan y se restauran; se elimina la obsoleta restricción UNIQUE del puerto del inbound (estorbaba al multi-node).
- Logs de Xray: una nueva tarea cada 10 minutos recorta el access-log y el error-log cuando superan **64 MiB**; la limpieza diaria ahora limpia ambos.
- Docker: reparada la renovación automática de certificados (crond se inicia y el estado de acme.sh se conserva en un volumen).

---

Creado a partir del análisis de los archivos fuente del panel. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
