---
created: 2026-04-23
updated: 2026-04-26
type: recurso
status: ativo
prioridade: media
quando_ler: "conexão Claude Code→N8N via MCP, diretório C:\\Users\\lugzi\\n8n-mcp\\, arquivos mapeados (.mcp.json), regra: nunca via FileSystem direto"
tags: [mcp, n8n, claude-code]
---

# n8n-mcp

> Conexão nativa do Claude Code com o Engine N8N via MCP Server.
> Edição de nodes/workflows via prompt CLI.

## 1. Diretório Core
`C:\Users\lugzi\n8n-mcp\`
> **REGRA CRÍTICA:** Jarvis acessa restritamente via protocolo MCP, nunca via FileSystem direto. Paths fixos absolutos em produção.

## 2. Mapa de Registros (.mcp.json)
| Arquivo | Função Contextual |
| :--- | :--- |
| `CLAUDE.md` | Instruções sistêmicas do próprio MCP. |
| `ANALYSIS_QUICK_REFERENCE.md` | Guia de referência tática de API. |
| `MEMORY_N8N_UPDATE.md` | Logs de estado. |
| `Dockerfile.railway` | Build de container. |

Deploy N8N → [[03 - Memoria da IA/Referencias/Stack Tecnológica]] · Scripts → [[03 - Memoria da IA/Referencias/Scripts Locais - dev]]

---
[[03 - Memoria da IA/Referencias/N8N]] | [[03 - Memoria da IA/Referencias/Stack Tecnológica]]
