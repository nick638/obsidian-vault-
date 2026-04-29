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

## Pendências abertas

- Configurar compactação no OpenClaw (contextTokens 160k, reserveTokensFloor 30k)
- Criar conta GitHub própria pro OpenClaw (jarvis-openclaw)
- Revogar token temporário após migração
- Definir canal heartbeat: WhatsApp (Evolution API) ou Telegram

---
[[KERNEL]] | [[shared/project-state]] | [[shared/pending]]
