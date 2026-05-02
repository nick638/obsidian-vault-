---
created: 2026-04-30
type: conversa
status: concluido
tags: [escritorio, cron, task-scheduler, inbox, durable]
---

# 2026-04-30 — Cron Durable: Task Scheduler + claude -p

## O que foi feito

### Problema resolvido
Cron anterior era session-only — morria ao fechar Claude Code. Inbox ficava parado sem processar.

### Solução implementada
- `scripts/check-inbox.ps1` — script PowerShell que:
  1. `git pull`
  2. Lê `inbox.md` — tem PENDING?
  3. Se SIM → dispara `claude --dangerously-skip-permissions -p` com prompt jarvis-ceo
  4. Atualiza inbox (PENDING → DONE) + escreve outbox.md + `git push`
  5. Log em `scripts/inbox-monitor.log`

- **Windows Task Scheduler** registrado como `JarvisInboxMonitor`
  - Intervalo: 2 minutos
  - Estado: Ready
  - Sobrevive reboot, sem terminal aberto

### Fluxo final
```
Telegram → OpenClaw → inbox.md → git push
                                     ↓
                     Windows detecta (até 2min)
                                     ↓
                     claude -p processa cadeia
                                     ↓
                     outbox.md → git push
                                     ↓
                     OpenClaw lê → Telegram
```

## Arquivos
- `C:\JARVIS\scripts\check-inbox.ps1`
- `C:\JARVIS\scripts\inbox-monitor.log` (gerado em runtime)

## Próximos passos
- Testar com missão real pelo Telegram
- Validar que outbox chega no OpenClaw
- Módulo 8 OpenClaw: agents.list + TEAM.md no VPS
