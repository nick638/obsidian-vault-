---
created: 2026-04-28
updated: 2026-04-28
area: profissional
type: conversa
status: arquivado
tags: [openclaw, telegram, vps, setup, agente]
---

# 2026-04-28 — Setup OpenClaw no Telegram

## O que foi feito

- OpenClaw instalado no VPS Hetzner (hostname: `redebaixada`)
- Versão: OpenClaw 2026.4.26 (be8c246), Node 22.22.2
- Gateway rodando como systemd: `openclaw-gateway.service`
- Bot Telegram criado: `@jarvism6k_bot`
- Modelo configurado: `google/gemini-2.5-flash` (via jq no `/root/.openclaw/openclaw.json`)
- Workspace: `/root/.openclaw/workspace`
- Logs: `/tmp/openclaw/openclaw-2026-04-28.log`

## Estado final

- Bot **funcional** — respondeu no Telegram ✅
- Onboarding básico feito via chat: nome Nicholas Maier, timezone America/Sao_Paulo, "Senhor"
- SOUL.md **não configurado** — só onboarding raso via chat ⚠️
- Vault **não sincronizado** pro VPS ⚠️

## Problemas encontrados

- Disco VPS estava 95% cheio durante instalação
- Terminal Bitvise quebrava comandos (aspas, multiline)
- API DeepSeek sem crédito → trocou pra Gemini Flash
- Pairing Telegram expira a cada restart do gateway

## Fix do pairing (pendente confirmar)

```bash
jq '.channels.telegram.dmPolicy = "open"' /root/.openclaw/openclaw.json > /tmp/ocl.json && mv /tmp/ocl.json /root/.openclaw/openclaw.json
```

## Update 28/04 — 18:55

Bot **100% funcional**. Modelo final: `openrouter/deepseek/deepseek-v3.2`
- OpenRouter com $5 de crédito (nickaugaitis@gmail.com)
- ~$0.00 por sessão. $5 dura meses.
- Entende áudio via transcrição automática do Telegram
- Reporta tokens e custo em tempo real

## Próximos passos

1. Configurar SOUL.md com contexto completo do vault (Speed Run módulo 3)
2. Configurar memória (Speed Run módulo 4)
3. Sincronizar vault via git pro VPS
4. Instalar skills (git clone Bruno Okamoto repo)
5. Revogar chave Groq exposta no chat (console.groq.com)

---
[[03 - Memoria da IA/Stack]] | [[01 - Profissional/Projetos/Lara Comercial]]
