---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: baixa
quando_ler: "features Obsidian (Canvas Ctrl+N, Quick Switcher, Templater, Dataview queries), atalhos de teclado, automação de frontmatter"
tags: [obsidian, produtividade, interface]
---

# Obsidian — Features Avançadas

> Operação fluida do co-piloto estrutural. Redução de fricção TDAH.

## 1. Ferramentas Nativas
| Feature | Atalho | Aplicação |
| :--- | :--- | :--- |
| **Canvas** | `Ctrl+N` | Arquitetura visual de funil (Lara, Flywheel). |
| **Quick Switcher** | `Ctrl+O` | Acesso instantâneo a nós. |
| **Command Palette**| `Ctrl+P` | Invocação global de plugins. |

## 2. Automação de Estrutura
- **Templates Nativos (`Ctrl+T`):** Path `Templates/`. Arquivos base (`novo-projeto.md`, `novo-cliente.md`).
- **Templater (Plugin Dinâmico):** Scripts de frontmatter automático.
  ```text
  ---
  data: <% tp.date.now("YYYY-MM-DD") %>
  ---
  ```

## 3. Banco de Dados Interno (Dataview)
Queries locais para consolidar métricas de projetos.
```dataview
TABLE status, fonte_de_renda
FROM "Projetos"
WHERE status = "Ativo"
```

Canvas funil → [[Projetos/Holos/Holos - Funil Digital]] · Templater check-in → [[Arquivo não encontrado — ver conteúdo migrado]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/Obsidian + Claude Code - Thinking Partner]] | [[_INDEX]]
