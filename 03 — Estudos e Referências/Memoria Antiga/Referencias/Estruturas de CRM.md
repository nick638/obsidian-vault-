---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "schema Supabase universal (campos snake_case), extensões por segmento (barbearia/imobiliária/advocacia/SaaS), CronJob follow-up 20min/24h/72h"
tags: [crm, supabase, banco-de-dados]
---

# Estruturas de CRM

> Dicionário de dados base para clientes (Supabase).
> Checklist de implantação para mapeamento de entidades.

## 1. CRM Universal (Atributos Core)
| Campo | Tipo / Descrição |
| :--- | :--- |
| `identificador_usuario` | PK ou UUID do Lead. |
| `nome` | Nome extraído. |
| `whatsapp` | Chave de roteamento Evolution. |
| `status` | ENUM: novo, em_conversa, interessado, convertido, perdido. |
| `resumo_conversa` | Payload IA. |
| `timestamp_ultima_msg` | Trigger de CronJob. |
| `follow_up_1` | Flag: 20 min. |
| `follow_up_2` | Flag: 24 horas. |
| `follow_up_3` | Flag: 72 horas. |
| `id_conta_chatwoot` | FK. |
| `id_conversa_chatwoot` | FK. |
| `id_lead_chatwoot` | FK. |
| `inbox_id_chatwoot` | FK. |

## 2. Dicionários Específicos (Extensões)
- **Barbearia:** `servicos`, `valor_servico`, `data_hora_agendada`, `barbeiro`, `id_agendamento`, `marcou_no_grupo`.
- **Imobiliária:** `tipo_imovel`, `finalidade`, `bairro_desejado`, `data_visita`, `id_agendamento`.
- **Advocacia:** `tipo_caso`, `objetivo_lead`, `data_consulta`.
- **SaaS (Unimasso):** `especialidade`, `tempo_atuacao`, `interesse`, `principal_duvida`, `principal_objecao`, `proximo_passo`.

## 3. CronJob de Follow-Up (Orquestração)
```text
Cronjob: Intervalo 10m
        ↓
Query: (timestamp_ultima_msg + delay) < agora
        ↓
Condition: Se (follow_up_1 = false) AND (> 20m) → Executa e = true
Condition: Se (follow_up_2 = false) AND (> 24h) → Executa e = true
Condition: Se (follow_up_3 = false) AND (> 72h) → Executa e = true
```
> **KPI:** Recuperação de 20-30% de leads perdidos.

Campos Lara → [[01 - Profissional/Projetos/Lara Comercial]] · CronJobs → [[03 - Memoria da IA/Referencias/N8N - Instruções Antigravity]]

---
[[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] | [[03 - Memoria da IA/Referencias/N8N]] | [[01 - Profissional/Projetos/Lara Comercial]]
