---
created: 2026-04-30
type: conversa
status: concluido
tags: [escritorio, antigravity, pixel-agents, stack, openclaw, alinhamento]
---

# 2026-04-30 — Stack Final: Antigravity + Escritório de Agentes

## Decisões fechadas hoje

### Stack final aprovada (Claude Code + OpenClaw alinhados)
```
ANTIGRAVITY (IDE principal)
├── Terminal → Claude Code Pro (trabalho pesado)
├── Pixel Agents → escritório visual dos agentes
├── Painel lateral → Gemini/outros (tarefas leves, grátis)
└── Vault JARVIS aberto

TELEGRAM → OpenClaw (VPS, 24/7, mobile)

GITHUB (vault) → ponte entre os dois mundos
└── shared/outputs/cadeia-YYYY-MM-DD-HHMM.md → chat-log por missão
```

### PowerShell substituído pelo terminal do Antigravity
### Pixel Agents instalado e funcionando no Antigravity (Instant Detection ON)

## Arquitetura do escritório

### Agentes criados (~/.claude/agents/)
jarvis-ceo · pesquisador · estrategista · copy-master · designer · executor

### Chat-log por missão (implementado)
Cada missão gera `shared/outputs/cadeia-YYYY-MM-DD-HHMM.md`
Cada agente appenda 1 linha: `[timestamp] agente: "mensagem"`
Leitura = histórico de WhatsApp dos agentes

### AGENTS.md criado
`00 - Jarvis/AGENTS.md` — protocolo único de escrita no vault pra todos os agentes

## Regra de uso dos tokens
- Missões pesadas → Claude Code (Pro, ilimitado)
- Missões leves/mobile → OpenClaw (paga por token, usar com parcimônia)
- Tarefas leves no PC → Gemini no painel lateral do Antigravity (grátis)

## O que falta (próximo mês)
- [ ] Cron durable sem janela visível
- [ ] Agentes nativos OpenClaw na VPS (Fase 1)
- [ ] Dashboard visual (Fase 2)
- [ ] Comando /status no OpenClaw (status mobile do escritório)
- [ ] Pixel Agents: abrir agentes via botão + Agent (um terminal por agente)

## Contexto importante desta sessão

### Task Scheduler — REMOVIDO
JarvisInboxMonitor foi removido pois abria janela de terminal visível a cada 2min.
Reconfigurar na próxima sessão: modo hidden (sem janela).

### Antigravity = IDE principal confirmado
Pixel Agents instalado e funcionando no Antigravity (Instant Detection ON via Claude Code Hooks).
Claude Code Pro rodando no terminal do Antigravity — substitui PowerShell.

### Sessões Claude Code são isoladas
Cada `claude` novo = instância nova, sem histórico de chat.
Contexto vem do vault (SessionStart lê KERNEL + Jarvis OS + prioridades + última conversa).
Não é bug — é o comportamento correto.

### Alinhamento Claude Code + OpenClaw concluído
Ambos leram AGENTS.md. Protocolo de escrita no vault sincronizado nos dois lados.

## Próximas sessões — por onde começar

1. **Gargalo real da semana:** escopo Holos + proposta formalização (prazo: dia 5/mai)
2. **Task Scheduler:** reconfigurar sem janela visível
3. **Bumblebee 2.0:** conectar no WordPress Holos
4. **OpenClaw Fase 1:** agentes nativos na VPS (jarvis-ceo, pesquisador, executor)
5. **Dashboard visual:** Fase 2 — ler shared/outputs/cadeia-*.md como chat

## Como retomar próxima sessão
Abrir Antigravity → terminal → `claude` → vault carrega automaticamente via SessionStart
Dizer: "retoma o escritório" — contexto completo carregado do vault
