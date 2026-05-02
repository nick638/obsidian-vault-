---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: media
quando_ler: "quando usar Lovable vs Claude Code vs WordPress, casos em produção (ZenPro/Holos Connect), guardrail de prompt padrão"
tags: [vibe-coding, lovable, deploy]
---

# Vibe Coding

> Desenvolvimento guiado por linguagem natural (Lovable).

## 1. Pipeline de Interface (Zero-Code Frontend)
- **Engine:** Lovable.dev
- **Deploy:** Lovable.app
- **Casos Produção:** ZenPro (CRM+Massa), Lara Holos, Holos Connect (Área de Membros), Templates de Cliente.
- **Risco Técnico:** Output = Single Page Applications (SPA). **Não indexa no Google**. SEO = WP.

## 2. Roteamento de Tech Stack
| Situação | Stack Primária |
| :--- | :--- |
| **Deploy Externo (Cliente)** | Lovable |
| **Painel / Dashboard Cliente** | Lovable |
| **Ferramenta Interna (Scripts, Plugins)** | Claude Code + React/Vite (Local) |
| **Indexação / Blog SEO** | WordPress (Nunca Lovable) |

## 3. Protocolos de Prompto
> "Não altere páginas existentes. Concentre mudanças apenas no módulo novo."
*(Guardrail padrão para atualizações sistêmicas)*

Benchmark → [[01 - Profissional/Projetos/ZenPro/ZenPro]] · Matriz ferramentas → [[03 - Memoria da IA/Referencias/Ferramentas de IA]]

---
[[01 - Profissional/Projetos/ZenPro/ZenPro]] | [[01 - Profissional/Projetos/Holos/Holos - Site 2.0]] | [[03 - Memoria da IA/Referencias/Stack Tecnológica]]
