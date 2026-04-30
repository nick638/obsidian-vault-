---
created: 2026-04-30
updated: 2026-04-30
type: sistema
status: ativo
tags: [agentes, escritorio, pixel-agents, gsd, jarvis]
---

# Escritório de Agentes

> Sistema de múltiplos agentes IA operando em paralelo, visualizados pelo Pixel Agents.

## Agentes ativos

| Agente | Arquivo | Papel |
|---|---|---|
| Jarvis CEO | `~/.claude/agents/jarvis-ceo.md` | Orquestrador, estratégia, delegação |
| Pesquisador | `~/.claude/agents/pesquisador.md` | Busca, análise, síntese |
| Executor | `~/.claude/agents/executor.md` | Código, deploys, arquivos |
| OpenClaw | VPS Hetzner | Heartbeat 24/7, Gate 42 daemon |

## Como usar no dia a dia

### Abrir o escritório
1. Abrir VS Code na pasta `C:/projetos/escritorio-agentes`
2. Pixel Agents abre automaticamente no painel lateral
3. Clicar **+ Agent** 3x → 3 terminais (Jarvis, Pesquisador, Executor)
4. Cada terminal: digitar o papel do agente como primeiro prompt

### Iniciar projeto com GSD
```
/gsd-new-project
```
Jarvis orquestra, delega para Pesquisador e Executor conforme fases.

### Prompt de entrada por agente
- **Jarvis:** "Você é o Jarvis CEO. Leia o vault e me diga o gargalo do dia."
- **Pesquisador:** "Você é o Pesquisador. Aguarde tarefas do Jarvis."
- **Executor:** "Você é o Executor. Aguarde tarefas do Jarvis."

## Projeto base
`C:/projetos/escritorio-agentes/`
- `.planning/PROJECT.md` — visão
- `.planning/ROADMAP.md` — fases

## Próximo passo
Fase 1.2 — rodar primeiro projeto real (escopo Holos) com os 3 agentes.
