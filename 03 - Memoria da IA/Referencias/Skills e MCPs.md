---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "MCPs instalados (Chatwoot/21st.dev/N8N/NanoBanana/Trigger.dev), skills (self-healing/Stitch/Cost-mode), comandos manutenção CLI"
tags: [tecnico, mcp, claude, ia]
---

# Skills e MCPs — Arsenal do Claude Code

> Eliminação de restrições via servidores externos (MCP) e hooks locais.

## 1. MCPs Instalados (Ativos)
### Chatwoot MCP (`chatwoot.m6k.com`)
- **Git:** `github.com/hugoblanc/chatwoot-mcp`
- **Uso:** Debug da Lara Comercial 2. Acesso direto a conversas via Claude sem abrir navegador.
- **Ferramentas:** `chatwoot_list_conversations`, `chatwoot_get_conversation`, `chatwoot_create_message`.

### 21st.dev Magic MCP
- **Package:** `@21st-dev/magic`
- **Uso:** UI React local (Editor de Vídeo, Dashboard). Substitui Lovable para deploy local.
- **Ferramentas:** `21st_magic_component_builder`, `logo_search`.

### N8N MCP
- **Path:** `C:\Users\lugzi\n8n-mcp` | **Git:** `github.com/czlonkowski/n8n-mcp`
- **Uso:** Arquitetura direta via API. Docs de custom nodes.

### NanoBanana (Google Imagen 3)
- **Path:** `C:\Users\lugzi\nano-banana-2-skill`
- **Custo:** ~R$0,20/img. Chave em `~/.nano-banana/.env`
- **Uso:** Editor de Vídeo Local (criação programática de frames).

### Trigger.dev MCP
- **Package:** `trigger.dev`
- **Uso:** Background jobs confiáveis para tarefas de duração longa.

## 2. Skills Instaladas (Hooks)
### Self-Healing Claude
- **Hook:** `PostToolUse` + `SessionStart`
- **Repo:** `github.com/pandnyr/self-healing-claude`
- **Database:** `~/.claude/self-healing/` (30 padrões pre-load).
- **Comando Limpeza:** `bash ~/.claude/skills/self-healing/scripts/cleanup.sh`

### Google Stitch
- **Repo:** `github.com/google-labs-code/stitch-skills`
- **Comandos:** `/stitch-design`, `/stitch-loop`. Gera Design Systems alta fidelidade.

### Cost Mode
- **Repo:** `github.com/Sagargupta16/claude-cost-optimizer`
- **Comando:** `/cost-mode` (Lite, Standard, Strict). Output reduzido em 40-70%.

## 3. Comandos de Manutenção CLI
```bash
claude mcp list
```

Como usar → [[03 - Memoria da IA/Referencias/Claude Code - Como Usar]] · Arquitetura → [[03 - Memoria da IA/Referencias/Claude Code - Arquitetura de Skills]]

---
[[03 - Memoria da IA/Referencias/Claude Code - Como Usar]] | [[03 - Memoria da IA/Referencias/Claude Code - Arquitetura de Skills]] | [[00 - Pessoal/Mapa do PC]]
