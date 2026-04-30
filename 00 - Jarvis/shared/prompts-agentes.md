---
created: 2026-04-30
actor: jarvis-claude
type: referencia
---

# Prompts dos Agentes — Escritório Local

> Referência dos agentes configurados em `~/.claude/agents/` na máquina local.
> Usados via Claude Code Agent tool. Não rodam no VPS — rodam no PC quando Claude Code está aberto.

## Arquitetura

```
OpenClaw (VPS/Telegram) → inbox.md → git push
                                          ↓
                               Cron local (2min) detecta
                                          ↓
                               jarvis-ceo orquestra cadeia
                                          ↓
         pesquisador → estrategista → copy-master → designer → executor
                                          ↓
                               outbox.md → git push
                                          ↓
                               OpenClaw lê → reporta no Telegram
```

## Agentes disponíveis

### jarvis-ceo
**Papel:** Orquestrador puro. Recebe missão do inbox, monta cadeia, executa, consolida.
**Cadeia padrão (criativo/campanha):** pesquisador → estrategista → copy-master + designer → executor
**Cadeia técnica:** pesquisador (se necessário) → executor

### pesquisador
**Papel:** Dados de mercado, busca no vault, pesquisa externa.
**Entrega:** resposta direta + fontes + gaps identificados.

### estrategista
**Papel:** Oferta, precificação, plano de lançamento, projeção de receita.
**Input esperado:** resultado do pesquisador + briefing do produto.

### copy-master
**Papel:** Copy de qualquer formato — anúncio FB/IG, email, VSL, WhatsApp, página de vendas.
**Input esperado:** estratégia definida + briefing de produto + público.

### designer
**Papel:** Briefing visual, paleta, prompt IA, especificação por canal.
**Input esperado:** copy pronta + tom definido + identidade visual do projeto.

### executor
**Papel:** Cria/edita arquivos no vault, código, deploy, commit git.
**Input esperado:** conteúdo final pronto pra ser escrito em arquivo.

## Formato do inbox (como OpenClaw deve escrever)

```
STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo
TASK: <descrição clara da missão>
CONTEXT: <contexto relevante — projeto, público, objetivo, restrições>
PRIORITY: alta | normal | baixa
CREATED: YYYY-MM-DD HH:MM
```

**Regra:** sempre mandar `TO: jarvis-ceo` para missões complexas. Ele decide a cadeia.
Usar outros agentes direto só para tarefas simples e específicas.

## Limitações importantes

- Cron é **session-only** — morre quando Claude Code fecha. PC precisa estar ligado e Claude Code aberto.
- Não há shared/outputs/ por agente ainda — contexto passa direto na memória do jarvis-ceo.
- Delay médio: 2min (cron) + tempo de execução dos agentes (3-15min dependendo da cadeia).
