---
created: 2026-04-30
updated: 2026-04-30
type: referencia
status: ativo
prioridade: alta
quando_ler: "qualquer agente antes de escrever no vault"
tags: [agentes, vault, protocolo, openclaw, jarvis-ceo]
---

# AGENTS.md — Protocolo de Escrita no Vault

> Regra única: vault é fonte de verdade. Cada agente escreve no lugar certo, na hora certa.
> Leia isso antes de criar qualquer arquivo.

## Onde cada coisa vai

### Conversas / Sessões do Telegram (OpenClaw)
- **Onde:** `00 - Jarvis/Agent-OpenClaw/daily/YYYY-MM-DD.md`
- **O quê:** só o essencial — decisões tomadas, tarefas delegadas, resultados recebidos
- **Não registrar:** conversa inteira, mensagens de triagem, confirmações simples

### Pesquisas

| Estágio | Onde | Formato |
|---|---|---|
| Em andamento (WIP) | `00 - Jarvis/shared/outputs/` | `01-pesquisador.md`, etc. |
| Finalizada + virou referência | `02 - Pesquisas e Estudos/Ativas/` | arquivo próprio com título claro |

### Decisões Estratégicas

| Tipo | Onde |
|---|---|
| Transversal (afeta múltiplos projetos) | `00 - Jarvis/shared/decisions-log.md` |
| Específica de projeto | `01 - Profissional/Projetos/[projeto]/` |

### Logs de Conversa (sessões Claude Code)
- **Onde:** `00 - Pessoal/Diario/Conversas/YYYY-MM-DD - <tema>.md`
- **Quando:** toda conversa substancial

### Resultados de Cadeia de Agentes
- **Onde:** `00 - Jarvis/shared/outputs/`
- Formato: `01-pesquisador.md`, `02-estrategista.md`, `03-copy-master.md`, `04-designer.md`, `05-final-jarvis-ceo.md`
- Cada agente escreve o próprio arquivo **antes** de passar pro próximo

## Regras gerais

1. **Nunca deletar** — mover pra `04 - Arquivo/` se ficar obsoleto
2. **Frontmatter obrigatório** — `created`, `type`, `status`, `tags` no mínimo
3. **Wiki-links** `[[Nota]]` pra referências internas
4. **Commit imediato** após escrever — `git add + commit + push`
5. **Nome de arquivo**: kebab-case ou `YYYY-MM-DD - tema.md` pra diários

## Agentes e seus papéis no vault

| Agente | Lê | Escreve |
|---|---|---|
| jarvis-ceo | inbox.md, qualquer arquivo | outbox.md, shared/outputs/05-final.md |
| pesquisador | vault + web | shared/outputs/01-pesquisador.md, 02 - Pesquisas (se finalizado) |
| estrategista | outputs do pesquisador | shared/outputs/02-estrategista.md, decisions-log.md |
| copy-master | outputs anteriores | shared/outputs/03-copy-master.md |
| designer | copy pronta | shared/outputs/04-designer.md |
| executor | outputs finais | arquivo de destino real no vault |
| openclaw | inbox.md, outbox.md | Agent-OpenClaw/daily/YYYY-MM-DD.md |

---
[[00 - Jarvis/Jarvis]] | [[KERNEL]] | [[00 - Jarvis/shared/prompts-agentes.md]]
