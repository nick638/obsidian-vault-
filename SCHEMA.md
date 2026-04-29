---
created: 2026-04-26
updated: 2026-04-26
type: schema
status: ativo
prioridade: alta
quando_ler: ao criar/editar qualquer arquivo do vault
tags: [schema, padrao, llm-native]
---

# SCHEMA.md — Padrão LLM-Native do Vault

> Regra única pra todo arquivo. Garante que qualquer LLM navega o vault
> em modo lazy-load: lê pouco, descobre rápido, puxa profundo só quando precisa.

---

## 1. PRINCÍPIO

**Um conceito = um arquivo.** Mistura quebra.

**Toda nota tem 3 camadas:**
1. Frontmatter (metadado pra LLM filtrar).
2. Sumário curto (3-5 linhas, primeiro bloco visível).
3. Detalhe (resto).

LLM lê só 1+2 na maioria das vezes. Desce ao 3 quando precisa.

## 2. FRONTMATTER PADRÃO

Todo arquivo do vault tem este header. Campos obrigatórios em **negrito**.

```yaml
---
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: <ver tipos abaixo>
status: <ativo|arquivado|rascunho|bloqueado>
prioridade: <maxima|alta|media|baixa>
quando_ler: <descrição curta de quando este arquivo é relevante>
tags: [tag1, tag2]
links_obrigatorios: [[Arquivo1]], [[Arquivo2]]   # opcional
projeto: <nome>                                    # se aplicável
area: <pessoal|profissional|pesquisa|memoria-ia|arquivo>
---
```

### Tipos válidos
- `kernel` — boot do sistema (só 1, KERNEL.md).
- `identidade` — quem é Nicholas, voz Jarvis, arquétipos.
- `perfil` — diagnóstico, persona, vulnerabilidade.
- `projeto` — frente de batalha (Lara, Bumblebee, Mapa da Alma...).
- `area` — domínio contínuo (estratégia, financeiro).
- `decisao` — registro de escolha + motivo.
- `insight` — descoberta nova.
- `pesquisa` — coletado externo (curso, expert, framework).
- `protocolo` — script de ação repetível (família, vendas...).
- `stack` — ferramenta, agente, automação, infra.
- `conversa` — log diário.
- `meta` — sobre o vault em si (kernel, schema, índice).

### Status
- `ativo` — em uso agora.
- `rascunho` — em construção.
- `bloqueado` — esperando algo externo.
- `arquivado` — histórico, não toca.

### Prioridade
- `maxima` — kernel, identidade, perfil. LLM lê em todo boot.
- `alta` — projetos ativos, decisões recentes.
- `media` — referência consultiva.
- `baixa` — histórico, contexto secundário.

## 3. ESTRUTURA INTERNA DA NOTA

```markdown
---
[frontmatter]
---

# Título

> Sumário em 1-3 linhas. O que é, por quê importa, quando consultar.

## Pointers (quando aplicável)
- [[Arquivo Relacionado 1]] — por quê linka
- [[Arquivo Relacionado 2]] — por quê linka

## [Seção 1]
Conteúdo profundo.

## [Seção N]
...

---
[[Pai]] | [[Irmão]] | [[Filho]]
```

**Regras:**
- Sumário no topo, depois do título. Nunca pula.
- Wiki-links explicados em 1 linha (`[[X]] — por quê`). Sem link nu.
- Footer com 2-4 wiki-links de navegação.
- Sem floreio, sem emoji decorativo. Emoji só se for sinal funcional (🔴 bloqueio).

## 4. ESTRUTURA DE PASTAS LLM-NATIVE

```
C:/jarvis/
├── KERNEL.md                       ← boot único
├── SCHEMA.md                       ← este arquivo
├── _INDEX.md                       ← gerado, mapa vivo
├── CLAUDE.md                       ← compat Claude Code
│
├── 00 - Pessoal/
│   ├── Identidade/                 ← arquétipo, voz, anti-padrão
│   ├── Perfil/                     ← diagnóstico, vulnerabilidades
│   ├── Familia/                    ← Lúcio, Elisangela, Tia Lu (1 arquivo cada)
│   ├── Insights/                   ← descobertas pontuais
│   ├── Diario/Conversas/           ← logs YYYY-MM-DD
│   └── Journaling/                 ← reflexões longas
│
├── 01 - Profissional/
│   ├── Projetos/                   ← 1 pasta por projeto
│   │   └── <projeto>/
│   │       ├── _MOC.md             ← entrada do projeto
│   │       ├── status.md           ← snapshot binário
│   │       ├── decisoes/           ← decisão por arquivo
│   │       └── ...
│   ├── Areas/                      ← Estratégia, Financeiro, Carreira
│   └── Prioridades da Semana.md    ← raiz
│
├── 02 - Pesquisas e Estudos/
│   ├── Ativas/STAGING/             ← entra cru, espera curadoria
│   ├── Frameworks/
│   ├── Experts/
│   └── Cursos/
│
├── 03 - Memoria da IA/
│   ├── Stack/                      ← N8N, Evolution, Supabase...
│   ├── Agentes/                    ← squads, comandos
│   ├── Automações/
│   └── Infra/
│
└── 04 - Arquivo/                   ← histórico inativo, intocável
```

## 5. REGRAS DE WIKI-LINK

- **Toda nota tem ≥ 2 links saindo.** Senão é órfã.
- **Hub não linka satélite.** Satélite linka hub. Direção: profundo → raso.
- **Peer-to-peer obrigatório.** Notas do mesmo tema linkam entre si, não só pro MOC.
- **Link explicado.** `[[X]]` nu = ruim. `[[X]] — porque Y` = bom.

## 6. COMO MIGRAR ARQUIVO ANTIGO

1. Lê arquivo. Identifica conceito principal.
2. Aplica frontmatter padrão (preenche todos os campos).
3. Adiciona sumário 1-3 linhas no topo.
4. Quebra em seções limpas. Remove floreio.
5. Adiciona wiki-links explicados (≥ 2).
6. Adiciona footer de navegação.
7. Se arquivo cobre 2+ conceitos → divide em 2+ arquivos.

## 7. ANTI-PADRÃO (NÃO FAZER)

- ❌ Arquivo sem frontmatter.
- ❌ Frontmatter sem `quando_ler`.
- ❌ Mistura 3 conceitos num arquivo só.
- ❌ Wiki-link nu sem explicação.
- ❌ Nota órfã (sem link saindo).
- ❌ Hub gigante linkando 50 satélites verticalmente sem peer-to-peer.
- ❌ Floreio, emoji decorativo, frase motivacional.
- ❌ Repetir info que já tá em outro arquivo (linka).

---
[[KERNEL]] | [[_INDEX]]
