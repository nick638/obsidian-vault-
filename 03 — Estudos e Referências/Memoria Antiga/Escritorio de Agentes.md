---
created: 2026-04-30
updated: 2026-05-01
type: sistema
status: ativo
tags: [agentes, escritorio, pixel-agents, gsd, jarvis]
---

# Escritório de Agentes

> Sistema de múltiplos agentes IA operando em paralelo. Cada agente = instância separada de Claude Code com vault próprio.

## Arquitetura

```
Nicholas
    ↓ abre terminal por agente
[Agente X] — lê proprio vault/inbox.md
    ↓ executa
[Agente X] — escreve resultado em outbox.md
    ↓ delega
[Agente Y] — recebe em Y/inbox.md
```

Comunicação: agentes escrevem na `inbox.md` do próximo. Não há chamada direta — só arquivos.

## Agentes de Infraestrutura

| Agente | Arquivo | Papel |
|---|---|---|
| Jarvis CEO | `.claude/agents/jarvis-ceo.md` | Orquestrador, estratégia, delegação |
| Pesquisador | `.claude/agents/pesquisador.md` + skills | Busca, análise, síntese |
| Executor | `.claude/agents/executor.md` | Código, deploys, arquivos |
| OpenClaw | VPS Hetzner | Heartbeat 24/7, Gate 42 daemon |

## Agentes de Negócio (novo — mai/26)

| Agente | Arquivo | Vault | Papel |
|---|---|---|---|
| Comercial | `.claude/agents/comercial.md` | `Escritorio/comercial/` | Prospecção, propostas, fechamento — Gate 42 |
| Criativo | `.claude/agents/criativo.md` | `Escritorio/criativo/` | Assets visuais via nano-banana |
| Copy | `.claude/agents/copy.md` | `Escritorio/copy/` | Copy de resposta direta para todos os projetos |
| Campanhas | `.claude/agents/campanhas.md` | `Escritorio/campanhas/` | Análise Meta Ads Library + estratégia tráfego |
| Produto | `.claude/agents/produto.md` | `Escritorio/produto/` | Gate 42 — força fechamento de projetos travados |

## Como usar cada agente

### Abrir agente de negócio
```
# No terminal, abrir Claude Code com contexto do vault:
claude --add-dir "C:/Jarvis/03 - Memoria da IA/Escritorio/[agente]"
# Primeiro prompt:
"Você é o agente [nome]. Leia seu inbox.md e memoria.md. Me diga o que está pendente."
```

### Fluxo completo (exemplo: criar criativo para Holos Natureza)
1. Abrir terminal `copy`: "Escreva 5 copies para anúncio frio Holos Natureza"
2. Copy entrega → escreve em `criativo/inbox.md`
3. Abrir terminal `criativo`: "Leia seu inbox. Gere os criativos."
4. Criativo entrega → escreve em `campanhas/inbox.md`
5. Abrir terminal `campanhas`: "Leia seu inbox. Monte estrutura de campanha."

### Prompt de boot por agente
- **comercial:** "Você é o Comercial. Leia vault. Qual o próximo lead para avançar?"
- **criativo:** "Você é o Criativo. Leia vault. O que está no inbox para gerar?"
- **copy:** "Você é o Copy. Leia vault. O que está pendente de entrega?"
- **campanhas:** "Você é Campanhas. Leia vault. Analise [URL] da biblioteca de anúncios."
- **produto:** "Você é Produto. Leia vault. Qual o projeto mais vermelho? Execute próxima ação atômica."

## Referência de pesquisa
Modelo baseado em: [[03 — Estudos e Referências/Ativas/2026-05-01 - Escritório Virtual Multiagentes Claude Code]]
Fonte: MGTInc / Marcelo — Pixel Agents (live abr/26)
