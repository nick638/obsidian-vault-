---
created: 2026-04-13
updated: 2026-04-26
type: sistema-tecnico
status: rascunho
prioridade: media
quando_ler: "KPIs da Lara (campos Supabase CRM_HOLOS), arquitetura N8N→Sheets→Edge Function, template relatório semanal"
tags: [holos, metricas, kpi, dashboard, analytics]
---

# Holos — Dashboard de Métricas

> O que não é medido não é gerenciado. Dashboard para a Lara Comercial 2.

## 1. Funil de Métricas (Lara)
| Métrica | Definição | Fonte (CRM_HOLOS) |
| :--- | :--- | :--- |
| **Leads Novos/Dia** | Volume de entrada no WhatsApp. | `Inicio do atendimento` |
| **Taxa Conversa** | Leads que responderam a Lara. | `Etapa do funil` |
| **Taxa Agendada** | Leads que marcaram experimental. | `aulas_experimentais` |
| **Taxa Matrícula** | Leads que fecharam (Matriculado). | `Etapa = matriculado` |
| **Follow-up Rate** | % que precisou de reengajamento. | `Follow UP 1/2/3` |

## 2. ROI e Performance
- **Conversão por Origem:** Instagram vs ZenPro vs Indicação.
- **Custo por Matrícula:** Investimento em Ads / Matrículas fechadas.
- **Velocidade:** Tempo médio entre `Inicio` e `Aula Experimental`.

## 3. Arquitetura de Dados
- **Implementação Inicial:** N8N Schedule Diário → Query Supabase → Google Sheets.
- **Escala Futura:** Edge Function → Lovable (Dashboard visual real-time).

## 4. Template Relatório Semanal (KPIs)
```text
📥 Leads novos: X
💬 Em conversa: X (X%)
🗓 Aulas agendadas: X (X%)
✅ Matriculados: X (X%)
📊 Origem Principal: [Nome]
⚡ Insights: [O que ajustar no prompt/campanha]
```

Schemas das tabelas → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] · Funil de conversão → [[01 - Profissional/Projetos/Holos/Holos - Modelo de Negócio]]

---
[[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] | [[01 - Profissional/Projetos/Lara Comercial]] | [[01 - Profissional/Projetos/Holos/Holos]]
