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

<!-- Claude Code local escreve aqui. OpenClaw lê e limpa após reportar. -->

_(vazio — nenhum resultado pendente)_
