---
created: 2026-04-19
updated: 2026-04-26
type: recurso
status: ativo
prioridade: media
quando_ler: "mapa hierárquico Claude Code (Skill<MCP<Squad<Agente<Sub-agente), topologia multi-agente, matriz de maturidade Nicholas (Skills Intermediário, Squads Avançado)"
tags: [tecnico, claude, ia, aprendizado]
---

# Claude Code — Arquitetura de Conhecimento

> Mapa ontológico do Claude Code. Níveis de proficiência e custo/poder.

## 1. Blocos Operacionais
| Camada | Custo | Código Real? | O que é | Exemplo |
| :--- | :---: | :---: | :--- | :--- |
| **Skill** | Baixo | Não | Regra de comportamento / Prompt injetado. | `/cost-mode` |
| **MCP** | Baixo | Sim | Servidor externo acessando APIs/DB. | Supabase MCP |
| **Squad / XQuad** | Alto | Não | Multi-persona (halbert + ogilvy). | `/copy-master` |
| **Agente** | Alto | Sim | Thread paralela independente. | `@dev` |
| **Sub-agente** | Alto | Sim | Agente lançado por outro agente. | Auto-orquestração |

## 2. Topologia Multi-Agente (ASCII)
```text
Usuário → Agente Orquestrador
              ↓
    ┌─────────┴──────────┐
    ↓                    ↓
Sub-agente 1       Sub-agente 2
(pesquisar)        (escrever código)
    ↓                    ↓
    └─────────┬──────────┘
              ↓
    Resultado consolidado → Usuário
```

## 3. Matriz de Maturidade Atual (Nicolas)
- **Skills:** 🟡 Intermediário (Uso passivo, falta criação ativa).
- **MCPs:** 🟡 Intermediário (Instalação OK, falta debug).
- **Squads:** 🟢 Avançado (Orquestração ativa).
- **Agentes:** 🔴 Iniciante (Conceito estático).

Como usar → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Como Usar]] · Arsenal → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Skills e MCPs]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Como Usar]] | [[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Arquitetura de Skills]] | [[_INDEX]]
