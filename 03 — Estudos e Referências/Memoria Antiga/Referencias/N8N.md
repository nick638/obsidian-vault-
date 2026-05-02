---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "topologia N8N (WhatsApp→IA→CRM→Evolution), fluxos mapeados (Lara/ZenPro/Bumblebee/Follow-up), curl de acionamento via Claude Code"
tags: [n8n, orquestracao, automacao]
---

# N8N

> O Kernel do ambiente operacional em nuvem. Cola todas as APIs. Self-hosted EasyPanel.

## 1. Topologia Core (Lara / Uni Padrão)
```text
WhatsApp → N8N → Agente IA (OpenAI)
                      ↓
              Subagente de conhecimento
                      ↓
              quebrar_mensagem
                      ↓
              Evolution API → envia resposta
                      ↓ (paralelo)
              Supabase → atualiza CRM
                      ↓ (fluxo separado)
              Follow-up automático
```

## 2. Integrações de Backplane
- **Modelos:** OpenAI (`gpt-4.1-mini`, `gpt-4o`).
- **DB:** Supabase (`PostgreSQL`).
- **Gateway:** Evolution API, Chatwoot.
- **Queue/Buffer:** Redis / Upstash.
- **Externos:** Sponte (REST API), WP, Google Sheets.

## 3. Operações Mapeadas
| Operação | Lógica no N8N |
| :--- | :--- |
| **Holos Lara** | Webhook → IA → CRM → Whatsapp. |
| **ZenPro** | Webhook local → Evolution API. |
| **Bumblebee** | Cron → GPT → WP POST. |
| **Follow-up** | Cron 10m → Regra (20m/24h/72h). |

## 4. Claude Code CLI Integration (Remote Call)
Claude executando N8N flow via `bash`:
```bash
curl -X POST https://nwh.m6k.com.br/webhook/XXXX \
  -d '{"acao": "criar_followup", "lead_whatsapp": "11999999999"}'
```

Schemas → [[03 - Memoria da IA/Referencias/N8N - Instruções Antigravity]] · Fluxos Holos → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]]

---
[[03 - Memoria da IA/Referencias/Stack Tecnológica]] | [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] | [[03 - Memoria da IA/Referencias/N8N - Instruções Antigravity]]
