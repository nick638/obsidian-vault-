---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "arquitetura de skills Claude Code (nativas/projeto/globais), triggers por keyword, backlog de skills a implementar (vault-search, lara-context, deploy-holos)"
tags: [tecnico, claude-code, skills, produtividade]
---

# Claude Code — Arquitetura de Skills

> Memória permanente do time de IA. Elimina repetição de contexto via rotinas salvas.

## 1. Topologia de Skills
1. **Nativas (built-in):** Globais automáticas.
   - `/batch` (Paraleliza tarefas)
   - `/model` (Opus/Sonnet)
   - `/compact` (Economia token)
2. **De Projeto:** Específicas. Path: `meu-projeto/.claude/skills/`.
3. **Globais (Usuário):** Todas as máquinas. Path: `~/.claude/skills/`.

## 2. Automação por Keyword (Triggers)
Skills ativam via regex/texto livre.
- Trigger "deploy" → `npm run build` → Upload VPS Hetzner.
- Trigger "vídeo para Holos" → Carrega Branding (#2dd4bf, Maria Clara).

## 3. Estrutura Padrão (Criação via Prompt)
```markdown
# Skill: deploy-vps
Quando: usuário mencionar "subir", "deploy", "publicar"
Fazer:
1. Identificar projeto atual
2. Rodar `npm run build`
3. Upload VPS via rsync/scp
4. Confirmar domínio
```

## 4. Backlog de Implementação (Roadmap)
- `holos-video`: Injeta brandbook Holos para IA de edição.
- `vault-search`: Roda `python C:/Users/lugzi/dev/search-memory.py "query"`.
- `deploy-holos`: CI/CD de 1 click via Hetzner.
- `lara-context`: Injeta N8N + Supabase + Chatwoot + CRM_HOLOS.
- `checkin-diario`: Grava tabela `daily_checkin`.

## 5. Auditoria de Status
```bash
# Skills globais
ls ~/.claude/skills/

# Skills locais
ls .claude/skills/

# Hooks
cat ~/.claude/settings.json | grep -A 5 "hooks"
```

Arsenal ativo → [[03 - Memoria da IA/Referencias/Skills e MCPs]] · Contexto lara-context → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]]

---
[[03 - Memoria da IA/Referencias/Claude Code - Como Usar]] | [[03 - Memoria da IA/Referencias/Skills e MCPs]] | [[_INDEX]]
