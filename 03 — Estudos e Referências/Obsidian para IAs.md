# Obsidian para IAs — Guia Completo

## Propósito
Tudo que você precisa saber sobre como estruturar um vault Obsidian para ser lido e mantido por IAs (Claude Code, agentes, OpenClaw). Baseado em pesquisas de 2025-2026.

---

## 1. Princípio central: Vault AI-Native

Um vault pra IA não é organizado igual um vault pra humanos. A IA não navega visualmente — ela **lê arquivos em ordem.** O design muda de "visual bonito" pra "hierarquia clara e previsível."

**Regra de ouro:** Uma IA deve conseguir entender seu vault inteiro lendo **3-5 arquivos** no máximo.

## 2. Arquitetura Recomendada (Karpathy LLM Wiki)

```
meu-vault/
├── CLAUDE.md          ← Instruções pra IA (lê primeiro)
├── _INDEX.md          ← Mapa do vault (lê segundo)
├── 00 — Núcleo/       ← Perfil, diagnóstico, identidade
├── 01 — Metodologia/  ← Como você faz as coisas
├── 02 — Projetos/     ← Onde você aplica
├── 03 — Estudos/      ← Referências, cursos
└── 04 — Agentes/      ← Prompts, logs, shared
```

### Arquivos-chave que a IA sempre lê:
| Arquivo | Função |
|---|---|
| `CLAUDE.md` | Instruções de como interagir com o vault |
| `_INDEX.md` | Mapa: onde está cada coisa |
| `_SCHEMA.md` | Template/padrão de cada tipo de arquivo |

## 3. Estrutura de cada arquivo

**Padrão para IA:**

```markdown
# Título

## Propósito
Por que esse arquivo existe (a IA precisa disso pra saber se deve ler)

## Conteúdo
- Tópicos
- Subtópicos

## Links
[[arquivo-relacionado]]
```

- **Propósito primeiro** — IA decide se precisa ler o resto baseado nisso
- Links `[[assunto]]` no final — IA segue ou ignora conforme necessidade

## 4. O que NÃO versionar no Git

| Ignorar | Motivo |
|---|---|
| `.obsidian/workspace.json` | Layout de janela (local) |
| `.obsidian/workspace-mobile.json` | Layout mobile |
| `.obsidian/plugins/` | Binários dos plugins |
| `.obsidian/graph.json` | Estado visual do grafo |
| `.trash/` | Lixo |
| `*.ps1`, `*.bat`, `*.py`, `*.log` | Scripts de sistema |

**Versionar:** `app.json`, `appearance.json`, `core-plugins.json`, `community-plugins.json`

## 5. Plugins essenciais para AI

| Plugin | Função |
|---|---|
| **Iconic** | Cores e ícones nas pastas (visual) |
| **Obsidian Git** | Auto commit/sync automático |
| **Smart Connections** | Similaridade semântica entre notas |
| **Dataview** | Queries SQL-like no vault |
| **Templater** | Templates com variáveis |
| **Obsidian Web Clipper** | Salvar páginas web como notas |

## 6. Claude Code + Obsidian

**Estratégias de integração:**

1. **Vault é o diretório de trabalho** — Claude Code roda dentro do vault. `CLAUDE.md` no raiz serve pros dois. → É o que você usa.

2. **Symlinks** — Cria links simbólicos de pastas específicas do vault dentro do repositório do Claude.

3. **MCP Bridge** — Claude Code consulta o vault via MCP sem precisar estar dentro dele.

**Sua setup atual:** Estratégia 1 (vault = diretório de trabalho) + GitHub como ponte pro OpenClaw.

## 7. Melhores práticas compiladas

**✅ Faz:**
- Propósito no início de cada arquivo
- `_INDEX.md` atualizado
- Links entre arquivos relacionados
- Pastas numeradas (00, 01, 02...) pra ordem previsível
- Manter arquivos < 200 linhas (IA processa melhor)

**❌ Não faz:**
- README.md em cada pasta (polui)
- Arquivos soltos na raiz
- Links quebrados apontando pro nada
- Conteúdo duplicado em lugares diferentes
- Informação que não serve pra IA nem pra você

## Fontes
- Karpathy LLM Wiki (abril/2026)
- Obsidian Forum — "Design your vault for AI orientation"
- Starmorph — "Obsidian + Claude Code: Complete Integration Guide"
- Rafael Melgaço — Método Claude Code + Obsidian
