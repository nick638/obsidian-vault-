---
created: 2026-04-22
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "instruções para AI operar n8n via MCP (Silent/Parallel Execution, Templates First, Multi-Level Validation, JSON payload patterns obrigatórios, top 20 nodes)"
tags: [stack, n8n, ia, automacao]
---

# N8N - Instruções Antigravity (n8n-MCP)

> Instruções de nível de sistema para AI Agents operando o n8n via MCP.

## 1. Princípios Core de Execução (Literais)
1. **Silent Execution:** Execute tools sem comentário. Responda APENAS após completar.
2. **Parallel Execution:** Execute operações independentes (ex: search_nodes) em paralelo.
3. **Templates First:** Sempre procure templates antes (2.709 base).
4. **Multi-Level Validation:** `validate_node(mode='minimal')` → `validate_node(mode='full')` → `validate_workflow`.
5. **Never Trust Defaults:** Parâmetros nativos geram runtime errors. Configure TUDO.

## 2. Padrões JSON Críticos (Mandar explícito)
### Operação Batch (Correto vs Errado)
```json
// ✅ GOOD - Batch operations
n8n_update_partial_workflow({
  id: "wf-123",
  operations: [
    {type: "updateNode", nodeId: "slack-1", changes: {...}},
    {type: "cleanStaleConnections"}
  ]
})
```

### addConnection Syntax (Obrigatório 4 strings)
```json
{
  "type": "addConnection",
  "source": "node-id-string",
  "target": "target-node-id-string",
  "sourcePort": "main",
  "targetPort": "main"
}
```

### Roteamento IF Node (branch param)
```json
// TRUE branch
{"type": "addConnection", "source": "if-node-id", "target": "success-handler", "sourcePort": "main", "targetPort": "main", "branch": "true"}
```

## 3. Workflow Process (API Reference)
1. `tools_documentation()`
2. `search_templates({searchMode: 'by_metadata', complexity: 'simple'})`
3. `search_nodes({query: 'trigger'})`
4. `get_node({nodeType, detail: 'standard'})`
5. `validate_node({nodeType, config, mode: 'minimal'})`
6. Expressions default: `$json`, `$node["NodeName"].json`
7. `n8n_create_workflow(workflow)`

## 4. Top 20 Nodes Referência
- `n8n-nodes-base.code` (JS/Python)
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.webhook`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.postgres`

Visão macro → [[03 - Memoria da IA/Referencias/N8N]] · Setup MCP → [[03 - Memoria da IA/Referencias/Antigravity - Setup n8n-MCP]]

---
[[03 - Memoria da IA/Referencias/N8N]] | [[03 - Memoria da IA/Referencias/Antigravity - Setup n8n-MCP]] | [[_INDEX]]
