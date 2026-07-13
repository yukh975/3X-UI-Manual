# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 Português · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Manual do usuário para o painel [3x-ui](https://github.com/MHSanaei/3x-ui) — um guia completo escrito para a versão **v3.5.0** do painel.

> **Repositório somente leitura.** Este repositório no GitHub é um espelho unidirecional — o código-fonte do manual está em um GitLab privado e é enviado aqui automaticamente, portanto está sempre atualizado. Encontrou um erro ou imprecisão? Por favor, [abra uma Issue](https://github.com/yukh975/3X-UI-Manual/issues). **Pull requests não são aceitos** (são fechados automaticamente) — as correções são feitas na fonte.

## Conteúdo

| Arquivo | Idioma | Formato |
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

## O que há de novo na 3.5.0

A versão 3.5.0 é um grande lançamento: o MTProto foi migrado para o modelo multicliente (motor mtg-multi, segredos pessoais, cotas e ad-tag), os hosts gerenciados tornaram-se grupais (vários inbound e endereços em um único registro), a restauração no painel PostgreSQL aceita backups SQLite, os outbound ganharam «Target Strategy», o teste «Real delay» e as colunas Egress/Country, e um balanceador pode usar outro balanceador como fallback. O núcleo Xray 26.7.11 vem incluído. A seguir, as alterações em relação à 3.4.2 pelas seções do manual.

### Alterações na seção 1 — Introdução, requisitos e instalação

- O núcleo Xray foi atualizado para **26.7.11**. Migrações automáticas associadas: as cifras Shadowsocks `none`/`plain` e VMess `none`/`zero` foram removidas do núcleo (as configurações salvas são reescritas automaticamente), e um outbound VLESS/Trojan sem criptografia para um endereço público é rejeitado ao salvar.
- Novo comando **`x-ui pgclient [versão]`** e item **10. Install/Upgrade client tools (pg_dump/pg_restore)** no menu PostgreSQL — instalação/atualização das ferramentas de cliente do PostgreSQL.
- Correções de scripts: instalação do PostgreSQL e do fail2ban na família RHEL (EPEL), Arch sem o `pacman -Syu` completo, nome correto do binário do Xray no ARM de 32 bits (`xray-linux-arm32`), confirmação do IPv4 autodetectado antes da emissão do certificado de IP, e corrigido o falso «Your input is invalid» ao escolher a porta ACME padrão.

### Alterações na seção 2 — Acesso ao painel e segurança

- Limite de IP: uma conexão «morta» agora é banida **uma única vez**, e não a cada varredura de 10 segundos — os contadores do fail2ban não são mais inflados, e não é preciso aumentar o `maxretry`.

### Alterações na seção 4 — Inbounds: criação e parâmetros gerais

- A lista de inbound ganhou uma **pesquisa** (por observação, porta e protocolo), e as listas suspensas de nós («Implantar em», filtro «Nós») tornaram-se pesquisáveis.

### Alterações na seção 5 — Protocolos

- **O MTProto foi migrado para o modelo multicliente** (motor mtg-multi): os usuários do MTProto agora são clientes comuns, com seu próprio segredo, cota, prazo, ad-tag e link pessoal `tg://proxy`. O campo «Secret» no nível do inbound foi removido (os inbound existentes são convertidos automaticamente), e o «FakeTLS domain» tornou-se o domínio padrão para os novos segredos. Novos campos do inbound: **Max connections** (limitação de conexões), **Public IPv4/IPv6** (para o ad-tag middle proxy). As alterações de clientes são aplicadas «a quente», sem derrubar as sessões do Telegram dos demais.
- WireGuard: o menu do inbound ganhou o conjunto completo de ações de clientes (Export All URLs, vincular/desvincular, grupos), a exportação foi dividida nas abas **Config** e **Links**, o campo **«IPs permitidos WireGuard» tornou-se editável** (várias entradas separadas por vírgula), e no config do cliente de um inbound de nó o `Endpoint` agora aponta para o endereço do nó.

### Alterações na seção 7 — Segurança da conexão: TLS, XTLS e REALITY

- A combinação **Finalmask + REALITY é rejeitada** ao salvar (ela levava à queda do Xray-core na primeira conexão); o placeholder do minClientVer foi atualizado para 26.3.27.
- Novo tipo de máscara TCP do Finalmask — **XMC (Minecraft)**: mascaramento do fluxo como tráfego de Minecraft (Hostname, Usernames, Password obrigatório com geração automática).

### Alterações na seção 8 — Clientes

- Nova coluna **«Velocidade»** — velocidade ao vivo de cada cliente (↑/↓, média móvel de ~5 segundos).
- A pesquisa de clientes volta a encontrar por **Telegram ID**; no formulário do cliente, os inbound desativados ficam ocultos da lista de vinculação; corrigido o acúmulo de duplicatas na janela «Desvincular».
- Os clientes MTProto têm campos próprios: **«MTProto secret»** (com regeneração) e **«Ad-tag (canal patrocinador)»** (32 caracteres hex); a cota e o prazo agora são realmente aplicados ao MTProto.

### Alterações na seção 9 — Grupos de clientes

- A janela de informações do cliente agora mostra o seu **grupo**.

### Alterações na seção 10 — Assinaturas (Subscription)

- **Os hosts gerenciados tornaram-se grupais**: um único registro abrange **vários inbound** (seleção múltipla) e **vários endereços** (tags, cada entrada pode ter seu próprio `:porta`; autocompletar de endereços; vazio — herda o endereço do inbound). As colunas da lista mostram chips de endereços e de inbound (com «+N»), as ações e a API trabalham com grupos (`groupId`), e surgiu o endpoint em massa `POST /panel/api/hosts/bulk/add`. A ordenação dos hosts agora é global (pela ordem, depois pela observação).
- O texto do **aviso** (`subAnnounce`) agora é exibido como banner na página de informações da assinatura; nos modelos personalizados está disponível a variável `announce`.
- A página de informações no navegador agora abre também pelos **links JSON/Clash** (e não apenas pelo principal).
- As configurações de host **Final Mask** e **Allow insecure** agora atuam também nos links raw (`fm=`) e para o **Hysteria2** (`insecure=1` / `skip-cert-verify: true`), respectivamente.
- O intervalo de «Intervalos de atualização» (`subUpdates`) foi corrigido para **0–525600** (o antigo limite de 168 da interface bloqueava o salvamento das configurações após o upgrade da 2.x).
- Os **clientes WireGuard nativos agora entram nas assinaturas Clash e JSON** (antes — apenas na raw).

### Alterações na seção 11 — Xray: roteamento, outbounds, DNS e extensões

- Editor de outbound: novo campo **«Target Strategy»** (11 valores de `AsIs` a `ForceIPv4`), modo de teste **«Real delay»** (tempo completo com estabelecimento do túnel; o modo HTTP agora é medido em uma conexão «aquecida»), colunas **Egress** (IP de saída atrás do «olho») e **Country** (bandeira + país, rótulo WARP) após o teste HTTP/Real.
- **O fallback do balanceador pode apontar para outro balanceador**: o painel constrói por conta própria um objeto loopback oculto (`_bl_…`), protege contra ciclos e contra a exclusão de um balanceador em uso; o prefixo `_bl_` é reservado.
- A aba «Roteamento básico» ganhou o seletor **«Default Outbound»** — qual outbound processa o tráfego que não corresponde a nenhuma regra (o selecionado é movido para a primeira posição).
- Servidores DNS em IPs privados não são mais bloqueados pela regra `geoip:private` — o painel mantém por conta própria uma regra allow gerenciada.
- O Happy Eyeballs nas configurações de dial (sockopt) agora é realmente ativado; o «Try delay» padrão é 250 ms, e um 0 explícito é preservado.
- Importação de assinaturas de outbound: nos links `ss://` com `?plugin=`/`/` final, a porta é analisada corretamente.

### Alterações na seção 12 — Nós (multipainel, master/slave)

- Pacote de correções: salvar um cliente sem alterações não derruba mais o tráfego ao vivo dos inbound de nó; as sobrescritas de Host do nó são aceitas no master na primeira aceitação; a renovação automática abre uma janela de cota nova; a exclusão de um cliente no master o exclui completamente nos nós; os inbound do nó não são varridos antes da primeira aceitação; um único inbound incorreto não interrompe a sincronização de tráfego do nó; a verificação de conflito de portas é limitada ao próprio nó.

### Alterações na seção 14 — Bot do Telegram

- Ao menu de comandos do bot foram adicionados **`/usage`**, **`/inbound`**, **`/restart`** e o novo comando de administrador **`/clearall`** (reset de tráfego de todos os clientes, com confirmação).
- A lista de clientes online é rotulada como `email - observação do inbound`; as mensagens de backup e do log de banimentos contêm o nome do host; a busca por Telegram ID funciona independentemente da formatação das configurações.

### Alterações na seção 16 — Operação: backups, logs, atualização, CLI

- **A restauração no painel PostgreSQL aceita arquivos SQLite**: um backup comum `.db` ou um `.dump` de migração é importado diretamente no PostgreSQL (em uma única transação, com verificações antes de parar o Xray). O diálogo de seleção de arquivo aceita `.dump,.db` em ambos os SGBDs; «Baixar arquivo de migração» permaneceu apenas nos painéis PostgreSQL.
- Antes de restaurar um arquivo `pg_dump`, o painel verifica a legibilidade do dump e, em caso de divergência de versões, sugere o comando exato `x-ui pgclient <versão>`.
- Autocorreções na inicialização: contadores de tráfego transbordados são limitados e restaurados; a restrição UNIQUE obsoleta na porta do inbound é removida (atrapalhava o multi-node).
- Logs do Xray: um novo job a cada 10 minutos trunca o access-log e o error-log quando excedem **64 MiB**; a limpeza diária agora limpa ambos.
- Docker: a renovação automática de certificados foi consertada (o crond é iniciado e o estado do acme.sh é preservado em um volume).

---

Criado a partir de uma análise dos arquivos-fonte do painel. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
