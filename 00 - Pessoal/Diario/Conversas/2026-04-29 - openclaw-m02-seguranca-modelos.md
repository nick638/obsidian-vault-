---
created: 2026-04-29
updated: 2026-04-29
area: profissional
type: conversa
status: em-andamento
tags: [openclaw, seguranca, ufw, fail2ban, llm, openrouter, modelos]
---

# 2026-04-29 — OpenClaw M02 Segurança + Comparativo de Modelos

## M02 Concluído — Segurança VPS

Bot (@jarvism6k_bot) executou e concluiu os 3 pilares de segurança do Módulo 2:

### 1. UFW (Firewall)
- Portas abertas: **22** (SSH), **80** (HTTP), **443** (HTTPS)
- Todo o restante bloqueado por padrão
- Justificativa: todos os serviços (N8N, Evolution, etc.) passam pelo Cloudflare proxy — só essas 3 necessárias

### 2. Fail2ban
- Ativo e funcionando
- **9 IPs banidos** na primeira rodada — confirma que o VPS estava sendo atacado ativamente
- Protege SSH contra brute force

### 3. dmPolicy — Allowlist Telegram
- `dmPolicy` alterado de `"open"` → `"allowlist"`
- Telegram ID autorizado: `5337782017` (Nicholas)
- Qualquer outro usuário → ignorado pelo bot
- Gateway reiniciado para aplicar config

## Incidente — Bot em Loop

Entre meia-noite e manhã de 29/04, bot travou em loop executando:
```
readlink -f /proc/2394147/exe → /usr/bin/node
```
Loop infinito sem progresso. Resolvido com `systemctl restart openclaw-gateway.service`.

**Causa provável:** tarefa complexa sem checkpoint — bot ficou verificando processo sem critério de saída.

## Comparativo de Modelos LLM (OpenRouter)

Pesquisa realizada para otimizar custo do bot:

| Modelo | Input/1M | Output/1M | Capacidade |
|--------|----------|-----------|------------|
| Qwen3 235B | Grátis | Grátis | ⭐⭐⭐⭐ — preview |
| Kimi K2 | Grátis | Grátis | ⭐⭐⭐⭐ — forte em código |
| DeepSeek V3.2 | $0.28 | $1.20 | ⭐⭐⭐⭐ — melhor custo pago |
| Gemini Flash Lite | $0.25 | $1.50 | ⭐⭐⭐ |
| Claude Sonnet 4.6 | ~$3 | ~$15 | ⭐⭐⭐⭐⭐ |
| GPT-5.4 | $2.50 | $15 | ⭐⭐⭐⭐⭐ — caro |

**Decisão:** manter DeepSeek V3.2 por ora. Testar Kimi K2 / Qwen3 235B (grátis) nos próximos módulos.

**Nota:** Claude Pro ≠ créditos de API. São produtos separados. API Anthropic = console.anthropic.com, cobrado por token.

## Estado do Bot (fim do M02)

- ✅ VPS seguro (UFW + fail2ban)
- ✅ Bot privado (dmPolicy allowlist)
- ✅ Modelo: `openrouter/deepseek/deepseek-v3.2`
- ⚠️ Gateway reiniciado — verificar se dmPolicy aplicou via Telegram
- 🔜 M03: SOUL.md (identidade do agente)
- 🔜 M04: Memória (decisions.md, lessons.md)

## Próximos Passos

1. Confirmar no Telegram que só ID `5337782017` consegue resposta
2. Iniciar M03 — configurar SOUL.md com contexto completo do vault
3. Sincronizar vault via git pro VPS (pendente desde 28/04)
4. Instalar skills do repositório Bruno Okamoto

---
[[2026-04-28 - openclaw-setup-telegram]] | [[03 - Memoria da IA/Stack]] | [[01 - Profissional/Projetos/Lara Comercial/instrucoes-ia]]
