---
created: 2026-04-24
updated: 2026-04-24
area: pesquisa
type: staging
status: rascunho
tags: [obsidian-cli, infra, automacao, claude-code, ferramentas]
---
# Obsidian CLI — Plugin Oficial (v1.6.0+)

> **Fonte:** https://obsidian.md/cli
> **Data de Captura:** 2026-04-24

## 1. Tese Central
O Obsidian CLI é um **plugin oficial nativo** que expõe o vault inteiro via terminal. Diferente de ler os `.md` diretamente (o que o Jarvis já faz), ele usa o índice e o motor interno do Obsidian — possibilitando buscas semânticas, criação com templates, export estruturado em JSON e integração com agentes de IA.

## 2. Comandos-Chave

```bash
# Busca usando o índice real do Obsidian
obsidian search query="Lara Comercial"

# Adiciona uma tarefa à nota diária de hoje
obsidian daily:append content="[ ] Revisar proposta formalização"

# Cria nota usando um template configurado
obsidian create name="2026-04-24 - Reunião Pai" template="Nota de Reunião"

# Exporta o vault inteiro como JSON (para processar externamente)
obsidian vault:export format=json

# Lê o conteúdo do arquivo atualmente aberto no Obsidian
obsidian read

# Abre o TUI interativo com autocomplete
obsidian
```

## 3. Como Ativar
1. Obsidian ≥ **1.6.0**
2. `Settings > Core Plugins > CLI` → ativar
3. Registrar no PATH do sistema (Windows: variável de ambiente)

## 4. O que muda para o Jarvis OS

| Hoje (acesso direto) | Com Obsidian CLI |
|---|---|
| Lê/escreve `.md` diretamente | + Busca usando índice real do vault |
| Precisa saber o path exato | + Pode usar nome da nota diretamente |
| Cria nota do zero | + Cria usando templates do Obsidian |
| Grep manual | + `obsidian search` com índice semântico |
| — | + Integração com plugins ativos do Obsidian |

## 5. Próximo Passo
- [ ] Verificar versão atual do Obsidian (precisa ser ≥ 1.6.0)
- [ ] Ativar plugin CLI em `Settings > Core Plugins`
- [ ] Registrar no PATH do Windows
- [ ] Testar: `obsidian search query="Lara Comercial"` no terminal

---
*Conecta com: [[N8N - Instruções Antigravity]] · [[Stack]] · [[Jarvis OS]] · [[Greg Isenberg - Obsidian e Claude Code]]*
