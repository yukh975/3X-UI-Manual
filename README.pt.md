# 3X-UI Manual

🇸🇦 [العربية](README.ar.md) · 🇬🇧 [English](README.md) · 🇪🇸 [Español](README.es.md) · 🇮🇷 [فارسی](README.fa.md) · 🇮🇩 [Bahasa Indonesia](README.id.md) · 🇯🇵 [日本語](README.ja.md) · 🇧🇷 Português · 🇷🇺 [Русский](README.ru.md) · 🇹🇷 [Türkçe](README.tr.md) · 🇺🇦 [Українська](README.uk.md) · 🇻🇳 [Tiếng Việt](README.vi.md) · 🇨🇳 [简体中文](README.zh-CN.md) · 🇹🇼 [繁體中文](README.zh-TW.md)

Manual do usuário para o painel [3x-ui](https://github.com/MHSanaei/3x-ui) — um guia completo escrito para a versão **v3.4.2** do painel.

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

## O que há de novo na 3.4.2

A versão 3.4.2 é uma grande atualização: o WireGuard foi migrado para o modelo multicliente, o REALITY ganhou um scanner de destinos ao vivo, os balanceadores receberam as abas Observatory/Burst Observatory e foi adicionada a confirmação de configurações sensíveis com o código 2FA. A seguir, as alterações em relação à 3.4.1, agrupadas pelas seções do manual.

### Alterações na seção 1 — Introdução, requisitos e instalação

- No menu lateral (e na gaveta móvel) apareceu o botão **«Documentação»** (ícone de livro) — abre a documentação oficial `https://docs.sanaei.dev/`.
- A versão mínima do Xray para a qual o painel atualiza foi elevada para **26.6.27** (o núcleo Xray 26.6.27 vem incluído).

### Alterações na seção 2 — Acesso ao painel e segurança de acesso

- Com a 2FA ativada, a alteração de login/senha do administrador e a desativação da 2FA agora exigem **inserir o código atual** do aplicativo autenticador (confirmação de alterações sensíveis).
- LDAP: novo interruptor **«Pular verificação do certificado TLS»** (`ldapInsecureSkipVerify`) — desativa a verificação do certificado no LDAPS; disponível apenas quando «Usar TLS (LDAPS)» está ativado.

### Alterações na seção 3 — Visão geral / Dashboard

- O botão de versão do painel agora sempre abre a janela de atualização (veja a seção 16 — canal dev).
- Melhoria transversal de **acessibilidade**: rótulos aria para ícones e ativação de elementos por Enter/Space (para leitores de tela e navegação por teclado).

### Alterações na seção 4 — Inbounds: criação e parâmetros gerais

- A ação **«Exportar todos os links»** agora gera os links pelo motor de assinaturas — aplica o modelo de remark a cada cliente e prefere os endpoints Host gerenciados (antes havia um remark fixo `inbound-email`).

### Alterações na seção 5 — Protocolos

- **O WireGuard foi migrado para o modelo multicliente.** Os peers agora são clientes comuns (com atribuição automática de endereço no túnel, suporte a assinaturas, limites de tráfego/prazo e grupos); a lista inline «Peers» do formulário do inbound foi removida.
- No inbound WireGuard foi adicionado o campo configurável **DNS** (padrão `1.1.1.1, 1.0.0.1`) e um **cartão de configuração do cliente** — copiar/baixar/QR do `.conf` completo e do link `wireguard://`/`wg://`.

### Alterações na seção 6 — Transporte (Stream Settings)

- No XHTTP, para novos inbounds, o parâmetro `maxConnections` no **xmux** agora tem padrão **6** (era `0` — sem limite). Os inbounds existentes mantêm seu valor.

### Alterações na seção 7 — Segurança da conexão: TLS, XTLS e REALITY

- Foi adicionado um **scanner de destinos REALITY ao vivo**: os botões **«Escanear»** (verificar o destino atual «ao vivo») e **«Buscar destinos»** (escanear um domínio ou faixa **IP/CIDR** e selecionar destinos adequados pelos seus certificados). Os campos «Destino» e SNI agora ficam vazios na primeira seleção do REALITY.

### Alterações na seção 8 — Clientes

- A extensão de prazo/cota via `bulkAdjust` agora **reativa automaticamente** um cliente desativado apenas por esgotamento (prazo vencido ou cota excedida), se a extensão o devolver aos limites. Os desativados manualmente ou ainda esgotados permanecem desligados.

### Alterações na seção 9 — Grupos de clientes

- **«Zerar tráfego»** de um grupo agora zera **apenas o contador do próprio grupo**; os contadores, cotas e o estado dos clientes individuais não são afetados, e não é necessário reiniciar o Xray. Esta é uma mudança em relação ao comportamento anterior (antes, o tráfego de todos os clientes do grupo era zerado).

### Alterações na seção 10 — Assinaturas (Subscription)

- Nos **hosts gerenciados**, o campo **VLESS route** foi redefinido: agora é um único valor `0-65535` (e não uma lista de portas), que é realmente «embutido» no UUID de cada assinatura (raw/JSON/Clash).
- A variável `{{EMAIL}}` (e seu sinônimo `{{USERNAME}}`) no modelo de remark agora é exibida apenas no **primeiro link** do cliente — assim como o bloco de tráfego/prazo.

### Alterações na seção 11 — Xray: roteamento, outbounds, DNS e extensões

- **Balanceadores**: a página foi dividida nas abas **«Configurações do balanceador»** e **«Observatory»**; em vez de JSON bruto — formulários Observatory e Burst Observatory (no Burst foi adicionado o campo **«Método HTTP»**). Um balanceador Random/Round-robin com `fallbackTag` agora cria automaticamente um Burst Observatory.
- Ao excluir um outbound ou balanceador, o painel limpa por si só as referências relacionadas no roteamento e exibe uma **prévia das consequências** no diálogo de confirmação.
- Nas regras de roteamento, o critério de rede **L4** é gravado no config em minúsculas (`tcp`/`udp`) e exibido em maiúsculas na tabela.
- Os erros no formulário de adição/edição de balanceador agora são adiados até o primeiro toque no campo ou a tentativa de salvar.

### Alterações na seção 12 — Nós (multipainel, master/slave)

- A notificação «salvo localmente, nó offline — será sincronizado depois» agora só é exibida quando o nó está realmente offline ou desligado (antes — a cada salvamento em um nó online).

### Alterações na seção 16 — Operação: backups, logs, atualização, CLI

- Os nomes dos arquivos de backup agora contêm o endereço do servidor e a **data-hora**: `{host}_AAAA-MM-DD_HHMMSS.db` (`.dump` para PostgreSQL), por exemplo `panel.example.com_2026-06-27_000000.db` — tanto ao baixar do painel quanto nos backups enviados pelo bot do Telegram.
- É possível ativar o **canal dev** de atualizações a partir de uma build estável: o botão de versão sempre abre a janela de atualização, e apareceu o interruptor **«Canal Dev»** com aviso sobre instabilidade e ausência de rollback automático.

---

Criado a partir de uma análise dos arquivos-fonte do painel. Yuriy Khachaturian ([yukh.net](https://yukh.net))

_Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)._
