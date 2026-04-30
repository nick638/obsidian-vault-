---
updated: 2026-04-30
type: shared
purpose: bridge local agents → openclaw
---

# Outbox — Escritório Local → OpenClaw

> Claude Code local escreve resultados aqui após executar tarefas do inbox.
> OpenClaw lê no próximo pull e reporta ao Nicholas via Telegram.

## Formato de resultado

```
TASK_ID: <mesmo id do inbox>
STATUS: completed | partial | blocked
AGENT: jarvis-ceo | pesquisador | executor
RESULT: <resultado resumido>
FILES: <arquivos criados/modificados, se houver>
COMPLETED: YYYY-MM-DD HH:MM
```

## Resultados

TASK_ID: teste-bridge
STATUS: completed
AGENT: executor
RESULT: Arquivo de teste criado com sucesso. Bridge OpenClaw ↔ Escritório Local operacional.
FILES: 00 - Jarvis/shared/teste-bridge.md
COMPLETED: 2026-04-30 15:01
