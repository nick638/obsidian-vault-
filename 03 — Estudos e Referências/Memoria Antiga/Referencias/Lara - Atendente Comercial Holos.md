---
created: 2026-04-24
updated: 2026-04-26
type: recurso
status: ativo
prioridade: maxima
quando_ler: "SDR comercial Holos (SPIN Selling, triagem, qualificação), topologia N8N+GPT-4o/mini+Evolution+Supabase, regras de ouro, escopo Lara vs Jarvis"
tags: [agente, comercial, whatsapp, holos]
---

# Lara — Atendente Comercial Holos (SDR)

> SDR Conversacional. Foco: Triagem, SPIN Selling e qualificação para CRM.

## 1. Topologia Tecnológica
| Layer | Tecnologia |
| :--- | :--- |
| **Orquestração** | N8N |
| **Cognição** | GPT-4o (Supervisor) + GPT-4.1-mini (Tool Execution) |
| **Rede/Canal** | WhatsApp (Evolution API + Chatwoot) |
| **Dados/Estado**| Supabase (PostgreSQL) |

## 2. Regras de Ouro
1. **Prioridade de Triagem:** SPIN Selling puro (Situação → Problema → Implicação → Necessidade). Qualificação antecede a oferta.
2. **Tool Integrity:** Vetado alucinação de curso. Sem fallback em DB, escala para um Humano via inbox.
3. **Escopo vs Jarvis:** Lara é Vendas/Front-End B2C. Jarvis é OS Executivo B2B.

Projeto → [[Projetos/Lara Comercial]] · Sistema → [[Projetos/Holos/Holos - Sistema Técnico]] · Framework → [[03 — Estudos e Referências/Ativas/Frameworks/SPIN Selling]]

---
[[_INDEX]]
