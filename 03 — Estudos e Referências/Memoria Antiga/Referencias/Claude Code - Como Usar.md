---
created: 2026-04-19
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "arquitetura local Claude Code (CLAUDE.md/memory/skills), scripts Python Supabase, custo R$110/mês, integração Obsidian via MCP"
tags: [tecnico, claude, ia, orquestrador]
---

# Claude Code — Operação Macro

> Cérebro técnico local. Executa código, acessa Supabase, interage com o Vault via MCPs.
> Custo operacional: R$ 110/mês.

## 1. Arquitetura Local
| Componente | Função |
| :--- | :--- |
| `CLAUDE.md` | Contexto primário. |
| `memory/` | Memória persistente entre sessões (perfil, insights). |
| `settings.json` | Hooks self-healing e roteadores. |
| `skills/` | Cost-mode, scripts complementares. |

## 2. Xquads (Agentes Acionáveis)
- `/copy-master` (Prompt Lara, Ads)
- `/hormozi-squad` (Ofertas EAD, Funis)
- `/brand-squad` (Identidade Visual)
- `/design-squad` (UI React / Dashboard)
- `/advisory-board` (Decisão estratégica em Y)

## 3. Gestão de Contexto (Supabase / Vector DB)
Vault indexado via Embeddings.
```bash
# Buscar memória semântica
python C:/Users/lugzi/dev/search-memory.py "query"

# Atualizar indexação do Vault
python C:/Users/lugzi/dev/populate-memory.py
```
- **Tabelas DB:** `memories` (70 arquivos vetoriais), `daily_checkin`.

## 4. Integração Obsidian (Métodos)
1. **Path Direto:** Já ativo.
2. **MCP via REST API:** Auto-discovery + Pesquisa sem path.
   ```bash
   export OBSIDIAN_API_KEY="sua-key-aqui"
   claude mcp add obsidian -- bunx -y @oleksandrkucherenko/mcp-obsidian
   ```
3. **Claudian Plugin:** Executa Code via sidebar do app.

Add-ons → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Skills e MCPs]] · Conceitual → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Obsidian + Claude Code - Thinking Partner]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/Skills e MCPs]] | [[03 — Estudos e Referências/Memoria Antiga/Referencias/Stack Tecnológica]] | [[00 — Quem Sou Nicolas/Mapa do PC]]
