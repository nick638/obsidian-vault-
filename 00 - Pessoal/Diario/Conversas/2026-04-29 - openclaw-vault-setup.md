---
created: 2026-04-29
type: conversa
status: ativo
tags: [openclaw, vault, github, jarvis, setup]
---

# 2026-04-29 — Setup OpenClaw + Vault Compartilhado

## Decisões tomadas

- OpenClaw = Jarvis operacional (age sozinho, heartbeats, Gate 42 daemon)
- Claude Code = engenheiro (constrói, evolui, refina)
- Vault GitHub = cérebro compartilhado dos dois
- Repo: https://github.com/nick638/obsidian-vault-
- OpenClaw usa DeepSeek V3 (custo ~R$0,50/mês)
- Custo extra total: marginal (assinatura Claude já paga)

## O que foi construído hoje

- Git init do vault `C:\JARVIS` + push pro GitHub (258 arquivos)
- Estrutura `shared/` criada:
  - `user-profile.md` — perfil completo Nicholas
  - `project-state.md` — todos projetos com status e gates
  - `decisions-log.md` — decisões estratégicas
  - `pending.md` — itens aguardando input (OpenClaw cobra no heartbeat)
- Estrutura `Agent-OpenClaw/` criada:
  - `working-context.md`
  - `mistakes.md` (já com erros da análise inicial dele)
- OpenClaw clonou vault, configurou cron pull 1x/hora
- Vault bidirecional confirmado (OpenClaw editou project-state.md)
- Heartbeat das 11h disparou: gate crítico = Proposta Formalização pai

## Módulo 4 — status

Vault substitui sistema nativo do curso:
- decisions.md → shared/decisions-log.md ✅
- projects.md → shared/project-state.md ✅
- people.md → 00 - Pessoal/Areas/Família/ ✅
- lessons.md → 00 - Pessoal/Insights/ ✅
- pending.md → shared/pending.md ✅ criado hoje
- MEMORY.md → KERNEL.md ✅

Módulo 4 concluído. Próximo: Módulo 5 — Integrações & Crons.

## Sessão 2 — DeepSeek fix (29/04 tarde)

- DeepSeek key `sk-8b6e26f7...` salva em `~/.openclaw/auth-profiles.json` ✅
- Auth mode mudado de `api_key` → `token` no openclaw.json ✅
- Cron `Pull vault hourly` funcionando com DeepSeek V4 Flash direto ✅
- Telegram @jarvism6k_bot respondendo ✅
- HEARTBEAT.md criado em `Agent-OpenClaw/` ✅
- Jarvis confirmou via Telegram: "Funcionando. DeepSeek V4 Flash direto na API, fallback pro V3.2 no OpenRouter." ✅

## Sessão 3 — M05 Integrações (29/04 noite)

- Gmail Jarvis criado: jarvis.do.nick@gmail.com ✅
- Google Cloud OAuth configurado (projeto "jarvis", client criado) ✅
- client_id: 869852581603-06fl757vapgggpgthtiqhije66opnbteu.apps.googleusercontent.com
- gog CLI não instalado no VPS — Jarvis tentando instalar via Telegram
- WhatsApp descartado por agora (risco rate limit Meta)
- Integração Google Calendar/Gmail: próximo passo após gog instalado

## Pendências abertas

- Instalar gog CLI no VPS + fazer OAuth flow com jarvis.do.nick@gmail.com
- Criar cron heartbeat a cada 4h (HEARTBEAT.md ativo, só falta o cron)
- Criar conta GitHub própria pro OpenClaw (jarvis-openclaw)
- Revogar token temporário após migração
- Frontend Mapa da Alma — Gate: 1ª venda até 15/maio (16 dias restantes em 29/04)
- Conversa com mãe (3 perguntas qualificação Lara) — crítico
- Proposta Formalização pro pai via Revolucio — crítico

## Planejamento maio (urgente — começa amanhã)

Nicholas tem 24h para fazer planejamento completo de maio.
Contexto: R$1.500/mês atual → meta R$10k/mês fim 2026.
Gates críticos: Lara (mãe), Mapa da Alma (1ª venda 15/maio), Formalização (pai).

---
[[KERNEL]] | [[shared/project-state]] | [[shared/pending]]
