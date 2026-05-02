---
created: 2026-04-24
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "sinergia Obsidian+Claude Code (Obsidian=memória/Claude=executor), todos os slash commands do vault (/context/today/close day/ghost/walk), hooks settings.json"
tags: [obsidian, claude-code, thinking-partner, jarvis-os]
---

# Obsidian + Claude Code — Thinking Partner

> Sinergia arquitetural: Obsidian (Memória) + Claude Code (Interpretador Ativo).

## 1. Princípio de Roteamento
- **Obsidian:** Banco de dados vetorial / markdown (Passivo).
- **Claude Code:** Raciocínio (Ativo). Lê, cruza e executa em `C:\Jarvis\`.
- Sem o Obsidian, a IA tem amnésia. Sem a IA, o Obsidian exige trabalho manual (fricção TDAH).

## 2. Slash Commands (Hooks)
Arquivados em: `C:\Jarvis\.claude\commands\*.md`.

### Gestão do Dia (Operação)
| Slash | Lê | Escreve / Ação |
| :--- | :--- | :--- |
| `/context` | `Perfil`, `Diagnóstico Real`, `Prioridades da Semana` | Injeta contexto base na sessão. |
| `/today` | `Prioridades da Semana` + Log semanal | `Diario/Conversas/<data> - today.md` |
| `/close day`| Chat atual + Vault | `Diario/Conversas/<data> - close-day.md` |

### Brainstorm / Vault Parsing
| Slash | Ação |
| :--- | :--- |
| `/ghost` | Simula output de "Nicholas Maier" via inferência de notas. |
| `/challenge`| Advogado do diabo contra histórico do vault. |
| `/emerge` | Clusterização latente de ideias desconexas. |
| `/ideas` | Extração de backlog acionável. |
| `/walk [path]`| Batch loop: Lê, faz 2-5 perguntas curtas, enriquece metadados. |

## 3. Template de Comando (Sintaxe Claude)
```markdown
---
name: <nome>
description: <o que faz em 1 linha>
---

# /<nome>
## Protocolo
1. ...
## Regras
- ...
```

## 4. Settings.json (Hooks Automáticos)
- **SessionStart:** Carrega `/context`.
- **PreToolUse:** Gatekeeping de sucesso.
- **PostAction:** Push para `jarvis-feedback-log`.
- **Stop:** Auto-commit + QA check.

Perfil → [[00 — Quem Sou Nicolas/Perfil]] · Arquitetura → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Arquitetura de Conhecimento]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Como Usar]] | [[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Arquitetura de Skills]] | [[_INDEX]]
