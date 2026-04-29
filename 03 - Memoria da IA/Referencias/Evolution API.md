---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "conector WhatsApp (instância HolosEAD), rate limit 15s crítico (banimento), posição topologia, risco operacional"
tags: [whatsapp, automacao, api]
---

# Evolution API

> O conector de end-user. The last mile. Entrega e recebe mensagens no WhatsApp.

## 1. Posição na Topologia
```text
WhatsApp Cliente ↔ Evolution API ↔ N8N ↔ Agente IA
```
- **Taxa de Conversão Base:** WhatsApp = 90%+ abertura (vs E-mail 20%, Meta Ads 5-10%). 
- Sem a API, a inteligência da Lara (SPIN Selling, CRM) não encontra o lead.

## 2. Instâncias Ativas (EasyPanel VPS)
| Instância | Aplicação Operacional |
| :--- | :--- |
| **HolosEAD** | Gateway de disparo em massa (ZenPro). |
| *Outras* | *Pendente mapeamento do backend*. |

## 3. Risco Operacional Crítico
> ⚠️ **CRITICAL:** Banimento de WhatsApp.
O disparo da HolosEAD processa base de 5.768 contatos. Cadência de disparo hardcoded: **15s entre envios**. Romper esse rate-limit = bloqueio instantâneo do Meta = quebra de toda a pipeline de vendas ativas.

Disparos → [[01 - Profissional/Projetos/ZenPro/ZenPro]] · Inbox → [[03 - Memoria da IA/Referencias/Chatwoot]]

---
[[03 - Memoria da IA/Referencias/N8N]] | [[01 - Profissional/Projetos/ZenPro/ZenPro]] | [[03 - Memoria da IA/Referencias/Chatwoot]]
