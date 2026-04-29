---
created: 2026-04-21
updated: 2026-04-26
type: arquitetura
status: ativo
tags: [jarvis, orquestrador, ia, arquitetura]
---

# Arquitetura Jarvis OS

> Diagrama mestre do orquestrador. Referência visual de roteamento.

## 1. Topologia do Sistema
```text
┌─────────────────────────────────────────────────────────────┐
│                         NICOLAS                              │
│                            │                                 │
│                            ▼                                 │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  CAMADA 1 — JARVIS (você fala só com ele)           │    │
│  │  • Lê CLAUDE.md + Prioridades da Semana             │    │
│  │  • Decide se precisa de Chief of Staff ou não       │    │
│  │  • Aciona roteador direto em tarefas simples        │    │
│  └─────────────────────────────────────────────────────┘    │
│                            │                                 │
│          ┌─────────────────┴─────────────────┐               │
│          ▼                                   ▼               │
│  ┌───────────────┐              ┌──────────────────────┐    │
│  │ Tarefa simples │              │ 3+ sub-tarefas       │    │
│  │ (1 roteador)  │              │ ou paralelismo real  │    │
│  └───────┬───────┘              └──────────┬───────────┘    │
│          │                                  │                │
│          │                                  ▼                │
│          │                   ┌──────────────────────────┐    │
│          │                   │ CHIEF OF STAFF (ad-hoc)  │    │
│          │                   │ Decompõe + paraleliza    │    │
│          │                   │ Consolida e reporta      │    │
│          │                   └──────────┬───────────────┘    │
│          │                              │                    │
│          ▼                              ▼                    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  CAMADA 2 — 4 ROTEADORES                            │    │
│  ├─────────────┬─────────────┬─────────────┬───────────┤    │
│  │ STRATEGIST  │  CREATOR    │  BUILDER    │  KEEPER   │    │
│  │ decisões    │  copy/oferta│  sistemas   │  memória  │    │
│  │ matemática  │  conteúdo   │  deploy     │  pesquisa │    │
│  └──────┬──────┴──────┬──────┴──────┬──────┴──────┬────┘    │
│         │             │             │             │          │
│         ▼             ▼             ▼             ▼          │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  CAMADA 3 — RECURSOS                                │    │
│  │  Skills (/copy-master, /hormozi, /holos-lara...)    │    │
│  │  Personas (@rafael, @afonso, @hormozi...)           │    │
│  │  MCPs (supabase, youtube, trigger, gdrive)          │    │
│  │  Vault (CONHECIMENTO, NEGÓCIOS, DEV, ESTRATÉGIA)    │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 2. Filtros Operacionais (Inegociáveis)
1. **Filtro Rafael Melgaço:** Ativar o pronto > Construir do zero.
2. **Filtro R$ 10k:** Serve à meta de 2026?
3. **Filtro Lei 3:** Travado por excesso de importância?
4. **Filtro 3Ps:** Pessoa → Problema → Produto.
5. **Filtro Matemática:** Meta sem número = Distração.

## 3. Hooks de Automação
- **SessionStart:** Busca memória + lê `Prioridades da Semana`.
- **PreToolUse:** Pergunta critério de sucesso.
- **PostAction:** Keeper salva aprendizado.
- **Stop:** "Funcionou? O que ajustar?" + commit.

Como usar o orquestrador → [[03 - Memoria da IA/Referencias/Claude Code - Como Usar]] · Arquivo de boot → [[01 - Profissional/Areas/Estrategia/Prioridades da Semana]]

---
