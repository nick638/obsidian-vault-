---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "integração bidirecional Claude↔N8N (N8N→Claude API, Claude→webhook POST, curl de acionamento), auth Anthropic API, backlog de endpoints a implementar"
tags: [ia, automacao, claude, webhook]
---

# Claude + N8N — Integração

> A ponte conversacional bi-direcional. Acesso direto a workflows via CLI.

## 1. Topologias de Acionamento
| Direção | Flow Operacional |
| :--- | :--- |
| **N8N → Claude** | N8N roteia payloads complexos para a API da Anthropic processar/classificar. |
| **Claude → N8N** | Claude Code CLI dispara webhooks `POST` para N8N executar side-effects locais. |
| **Bidirecional** | Claude usa o webhook N8N para fazer `GET` no Supabase CRM. |

## 2. Triggering via Claude Code CLI (Webhook POST)
Executável via bash tool interno do agente local.
```bash
curl -X POST https://nwh.m6k.com.br/webhook/XXXX \
  -H "Content-Type: application/json" \
  -d '{"acao": "criar_followup", "lead": "João", "mensagem": "..."}'
```

## 3. Triggering via WhatsApp (Webhook N8N → Claude API)
```text
WhatsApp → N8N → HTTP Request (Claude API) → Classifica Intenção → N8N Roteia
```
**Autenticação do Node HTTP (N8N):**
- URL: `https://api.anthropic.com/v1/messages`
- Headers: `x-api-key: sk-ant-...`, `anthropic-version: 2023-06-01`

## 4. Backlog de Implantação
- [ ] Criar webhook simples no N8N que insere log no Supabase.
- [ ] Testar curl do Claude Code apontando pro webhook.
- [ ] Expandir para endpoints `follow_up` e `lead_update`.

MCP técnico → [[03 — Estudos e Referências/Memoria Antiga/Referencias/N8N - Instruções Antigravity]] · Classificação → [[Projetos/Lara Comercial]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/N8N]] | [[03 — Estudos e Referências/Memoria Antiga/Referencias/N8N - Instruções Antigravity]] | [[_INDEX]]
