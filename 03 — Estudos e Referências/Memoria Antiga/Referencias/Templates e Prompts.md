---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: rascunho
prioridade: alta
quando_ler: "templates N8N para deploy rápido de agentes (arquitetura WhatsApp→Secretária→Subagente→CRM), prompts literais quebrar_mensagem e Agente CRM, segmentos (barbearia/advocacia/imobiliária)"
tags: [recurso, templates, prompts]
---

# Templates e Prompts

> Produto padronizado. Base para deploy rápido (2 dias) de agentes comerciais N8N.
> Local: `C:\Users\lugzi\Downloads\Projetos\`

## 1. Arquitetura Padrão N8N (Flow)
```text
WhatsApp → N8N → Secretária (agente principal)
                      ↓ aciona tool
              Subagente de conhecimento
                      ↓ retorna info
              Secretária monta resposta
                      ↓
              quebrar_mensagem (formata pro WhatsApp)
                      ↓
              Envia em partes pro cliente
                      ↓ (fluxo paralelo)
              CRM → atualiza Supabase
                      ↓ (fluxo separado, roda a cada 10min)
              Follow-up → 20min · 24h · 72h
```

## 2. Prompts Estruturais (Literais)
### quebrar_mensagem
```text
## Quem é você
Assistente de formatação de mensagens no N8N.
Quebra mensagens longas em partes menores sem alterar o conteúdo.

## Regras
1. Não modifique o texto — apenas divida
2. Mantenha frases completas, nunca corte no meio de uma ideia
3. Limite: máximo 80 caracteres por parte
4. Use \n entre os trechos
5. Remova completamente qualquer formatação Markdown
6. Se < 80 caracteres, não divide
7. Listas: cada item em linha separada
8. Nunca corte depois de vírgula
9. Nunca adicione comentários extras
```

### Agente CRM
```json
Analise o histórico da conversa e extraia em JSON:
{
  "nome": "",
  "telefone": "",
  "interesse": "",
  "status": "novo|em_conversa|interessado|convertido|perdido",
  "principal_duvida": "",
  "principal_objecao": "",
  "resumo": "2 linhas",
  "proximo_passo": ""
}
Retorne APENAS o JSON. Sem explicações.
```

### Secretária (Frame Base 4 Camadas)
1. **Identidade:** Nome + Empresa. Nunca admitir IA.
2. **Tom de Voz:** Leve, informal. Zero jargão ("prezado").
3. **Fluxo:** Apresentação → Necessidade → Rapport (2 qs) → Tool Conhecimento → Call to Action.
4. **Tools:** Tool de Info e Agendamento. Restrição de halucinação.

## 3. Instâncias / Segmentos
| Template | Segmento | Pasta Base |
| :--- | :--- | :--- |
| **Template Base** | Genérico | `TEMPLATE--BASE--(atual)` |
| **Barbearia** | Barão da Navalha | `BARBEARIA` |
| **Advocacia** | Aurora Advocacia | `Workflow--advogado` |
| **Imobiliária** | Morada One | `ImobiFlow` |

Prompts → [[03 - Memoria da IA/Referencias/Prompts Completos]] · Deploy → [[01 - Profissional/Projetos/Clientes Externos/Metodologia de Captação]]

---
[[03 - Memoria da IA/Referencias/Prompts Completos]] | [[01 - Profissional/Projetos/Clientes Externos/Metodologia de Captação]] | [[_INDEX]]
