---
updated: 2026-04-30
type: shared
purpose: bridge openclaw → local agents
---

# Inbox — OpenClaw → Escritório Local

> OpenClaw escreve aqui quando precisa delegar tarefa pros agentes locais (jarvis-ceo, pesquisador, executor).
> Claude Code local monitora, executa, escreve resultado em outbox.md.

## Como usar (OpenClaw)

```
STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo | pesquisador | executor
TASK: <descrição clara da tarefa>
CONTEXT: <contexto necessário>
PRIORITY: alta | normal | baixa
CREATED: YYYY-MM-DD HH:MM
```

## Tarefas

STATUS: DONE
FROM: openclaw
TO: executor
TASK: Criar arquivo shared/teste-bridge.md com conteúdo "Bridge OpenClaw ↔ Escritório Local operacional. Data: 2026-04-30."
COMPLETED: 2026-04-30 15:01

STATUS: DONE
FROM: openclaw
TO: jarvis-ceo
TASK: Criativo completo massoterapia Holos
COMPLETED: 2026-04-30 15:10

STATUS: DONE
FROM: openclaw
TO: pesquisador
TASK: Pesquisa mercado massoterapia Brasil
COMPLETED: 2026-04-30 15:10
