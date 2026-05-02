---
created: 2026-04-23
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "contas GitHub (nick638/Luciomaier), repos locais e donos, aviso token hardcoded .git/config, fluxo PR obrigatório"
tags: [github, git, infraestrutura]
---

# GitHub — Acesso e Fluxo

> Controle de versão local e remote. Regras de colaboração.

## 1. Mapeamento de Contas e Repositórios
| Repositório | Caminho Local | Conta Remote |
| :--- | :--- | :--- |
| `atendichat-hub-30` | `C:\Users\lugzi\atendichat-hub-30` | `Luciomaier` (Pai) |
| `redebaixada` | `C:\Users\lugzi\redebaixada` | `Luciomaier` (Pai) |
| `vende pró` | *Pendente confirmação* | `Luciomaier` (Pai) |
| `chakra-flow-builder`| *Pendente* | `nick638` (Nicolas) |

## 2. Autenticação Ativa
- **CLI Logged In:** Conta `nick638`.
- **Scopes Permitidos:** `repo`, `workflow`, `read:org`, `gist`.
> ⚠️ **RISCO CRÍTICO:** O token de acesso do pai (`ghp_...`) está hardcoded no `.git/config` dos repos locais `atendichat` e `redebaixada`. Vazamento de log = Vazamento de token de terceiros. **Plano de contingência:** Mudar para fluxo de colaborador e revogar token root.

## 3. Fluxo de PR Obrigatório
> **REGRA INEGOCIÁVEL:** Jamais commitar direto na `main`. Toda feature exige ramificação.
```text
Nicolas (Prompt) → Jarvis (Edição Local)
  ↓
git checkout -b nicolas/<feature>
git add + commit + push
  ↓
gh pr create (via nick638)
  ↓
Merge Review = Luciomaier
```

Deploy → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Stack Tecnológica]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/Stack Tecnológica]] | [[00 — Quem Sou Nicolas/Mapa do PC]]
