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
TO: jarvis-ceo
TASK: <descrição clara da missão>
CONTEXT: <contexto relevante>
PRIORITY: alta | normal | baixa
CREATED: YYYY-MM-DD HH:MM
```

## Tarefas

STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo
TASK: Criar criativo estático para massoterapia da Holos — imagem + copy principal para anúncio. Pesquisador pesquisa, copy-master escreve, designer faz briefing visual, executor salva. Usar novo formato chat-log: cada agente appenda no shared/outputs/cadeia-[timestamp].md. Público: mulheres 25-45 buscando nova carreira em massoterapia. Produto: Formação Massoterapia EAD 460h (Holos). Paleta Holos: roxo + laranja + dourado. Gerar: 1) copy versão A e B, 2) briefing visual completo (dimensões 1080x1080, 1080x1920, 1200x628), 3) arquivo final salvo em 00 - Jarvis/shared/holos-criativo-estatico.md. Priority: alta.
CONTEXT: PRIMEIRO TESTE do novo sistema chat-log (shared/outputs/cadeia-*.md). Missão real: criativo estático massoterapia Holos. Nicholas vai ler o chat-log como se fosse conversa de WhatsApp entre os agentes. Validar que o formato funciona.
PRIORITY: alta
CREATED: 2026-04-30 17:30
