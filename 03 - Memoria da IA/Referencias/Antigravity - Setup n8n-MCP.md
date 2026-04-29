---
created: 2026-04-22
updated: 2026-04-26
type: recurso
status: ativo
prioridade: media
quando_ler: "setup MCP n8n-mcp (instalação npm, config JSON path, 7 camadas n8n-skills, regras de execução para Antigravity)"
tags: [stack, ia, n8n, mcp]
---

# Antigravity + n8n Setup Guide (MCP)

> Configuração crítica do servidor MCP e n8n-Skills para o agente Antigravity.

## 1. Stack
- **n8n-MCP:** [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)
- **n8n-Skills:** [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills)

## 2. Setup do Servidor MCP
### Instalação Global
```bash
npm install -g n8n-mcp
```

### Config JSON
Caminho: `C:\Users\<SEU_USUARIO>\.gemini\antigravity\mcp_config.json`
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "node",
      "args": [
        "C:\\Users\\<SEU_USUARIO>\\AppData\\Roaming\\npm\\node_modules\\n8n-mcp\\dist\\mcp\\index.js"
      ],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true",
        "N8N_API_URL": "http://localhost:5678",
        "N8N_BASE_URL": "http://localhost:5678",
        "N8N_API_KEY": "<SUA_API_KEY>"
      }
    }
  }
}
```

## 3. n8n-Skills (7 Camadas)
Instalação: Clone e copie para `~/.gemini/antigravity/skills/`.
```bash
git clone https://github.com/czlonkowski/n8n-skills.git
```
Skills englobadas: Expression Syntax, Tools Expert, Workflow Patterns, Validation Expert, Node Config, Code JS, Code Python.

## 4. AGENTS.md (Regras de Execução)
- **Parallel Execution:** Obrigatório.
- **Templates First:** 2.709 disponíveis.
- **Multi-level Validation:** Obrigatório.
- **Explicit Parameters:** Zero confiança em defaults.

Instruções IA → [[03 - Memoria da IA/Referencias/N8N - Instruções Antigravity]] · Em produção → [[01 - Profissional/Projetos/Lara Comercial]]

---
[[03 - Memoria da IA/Referencias/N8N - Instruções Antigravity]] | [[03 - Memoria da IA/Referencias/N8N]] | [[_INDEX]]
