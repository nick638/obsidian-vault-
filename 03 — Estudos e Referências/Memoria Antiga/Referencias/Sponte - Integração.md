---
created: 2026-04-19
updated: 2026-04-26
type: recurso
status: rascunho
prioridade: media
quando_ler: "integração ERP Sponte (Holos), 3 APIs (Integração/BI/Indicadores), endpoints críticos, fluxo N8N schedule 30min→Supabase, Pull-Only sem webhooks"
tags: [api, integracao, sponte, holos]
---

# Sponte — Integração

> Sistema de ERP e Gestão Escolar (Holos). Dependência fase 2 (pós-Lara CRM).

## 1. Topologia de APIs (Limitações: Pull-Only)
| API | Base URL | Limitações |
| :--- | :--- | :--- |
| **Integração** | `https://integracao.sponteweb.net.br` | Principal. |
| **BI** | `https://sponte-bi.sponteweb.com.br` | Rate limit: `1.000 req/min`. Lag: D-1. |
| **Indicadores**| `https://apiindicadores.sponte.com.br` | Métricas puras. |

## 2. Endpoints Críticos (API Integração)
> **Requisito Global:** Parâmetro `CodCliSponte` obrigatório.
- `POST /api/v1/login` → Retorna Bearer JWT.
- `GET /api/v1/alunos` → (Nome, Email, CPF, Status)
- `GET /api/v1/turmas` → (Curso, Matrículas, Vagas Livres)
- `GET /api/v1/matriculas` → (Estágio, Turma, Pagamento)
- `GET /api/v1/aulas`
- `GET /api/v1/contasReceber`
- `GET /api/v1/followups`

## 3. Fluxo Proposto (N8N Sincronizador)
Como a API não possui webhooks (Push), a sincronização exige rotina de Schedule.
```text
N8N Schedule (CronJob: 30min)
        ↓
POST /api/v1/login → (Auth: Bearer JWT)
        ↓
GET /api/v1/turmas → (vagas_total - vagas_ocupadas = Scarcity Real)
GET /api/v1/matriculas → (leads convertidos)
        ↓
Upsert Supabase → Tabela de Turmas
Upsert CRM_HOLOS → (etapa: matriculado)
```

CronJob N8N → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] · Consumidor → [[01 - Profissional/Projetos/Lara Comercial]]

---
[[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] | [[03 - Memoria da IA/Referencias/Estruturas de CRM]] | [[_INDEX]]
