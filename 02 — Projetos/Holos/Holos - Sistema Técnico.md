---
created: 2026-04-22
updated: 2026-04-26
type: sistema-tecnico
status: ativo
prioridade: alta
quando_ler: "infra VPS Hetzner/EasyPanel, schema Supabase CRM_HOLOS, fluxos N8N Lara, guardrail de saúde, estado real do sistema (o que está ativo vs bloqueado)"
tags: [projeto, familia, tecnico, prioridade, holos]
---

# Holos — Sistema Técnico

> Infraestrutura e Prompts da Lara Comercial 2. Conectado: [[Holos/Holos]] · [[03 — Estudos e Referências/Ativas/Frameworks/SPIN Selling]] · [[03 — Estudos e Referências/Memoria Antiga/Referencias/N8N]].

## 1. Infraestrutura (VPS)
| Camada | Serviço | Função |
|--------|---------|--------|
| Servidor (VPS) | **Hetzner** | Onde tudo roda fisicamente |
| Painel de gestão | **EasyPanel** | Gerencia containers/apps dentro do Hetzner |
| DNS / domínio | **Cloudflare** | DNS + proteção de rede na frente do Hetzner |

> N8N, Chatwoot e Evolution API rodam em containers EasyPanel.

## 2. Guardrail de Saúde
O prompt **DEVE** conter explicitamente:
```
Nunca recomendar tratamentos, técnicas terapêuticas ou indicações de saúde.
Sempre redirecionar para a equipe humana da Holos quando o lead fizer perguntas clínicas.
```

## 3. Estado Real do Sistema (Abril 2026)
| Componente | Status real |
|------------|-------------|
| N8N | ✅ Instalado na VPS Hetzner |
| Lara (fluxos N8N) | ⚠️ Ativo apenas no número EAD (teste) |
| Cursos no banco | ⚠️ **CRÍTICO: 73 cursos no site, apenas 2 no Supabase.** |
| Chatwoot + Evolution API | ✅ Instalados na VPS |
| Supabase (CRM_HOLOS) | ✅ Existe — dados de teste |
| Comercial 2 | ❌ Ainda não conectado — aguarda ajustes + aprovação |

## 4. Supabase — Schema Literal
**Projeto:** `pjpircjhlryoccdksrmo.supabase.co`

### CRM_HOLOS (Campos)
id (text), Whatsapp (bigint), Nome (text), email (text), Curso de interesse (text), codigo_curso (text), turma_id (text), Etapa do funil (text), UTM Source (text), UTM Campaign (text), origem (text), Resumo da conversa (text), Data aula experimental (text), Status aula experimental (text), Follow UP 1/2/3 (text), minutos_sem_resposta (integer), Timestamp ultima msg (timestamptz), Inicio do atendimento (timestamptz).

### cursos (Campos)
id (uuid), codigo_curso (text), nome (text), descricao (text), grade_curricular (text), categoria (text), modalidade (text), nivel (text), carga_horaria (integer), duracao_texto (text), turno (text), preco (numeric), preco_promocional (numeric), proximo_inicio (date), vagas_disponiveis (integer), certificado (boolean), entidades_reconhecimento (text), prerequisitos (text), instrutor (text), imagens (ARRAY), capa_url (text), link_pagamento (text), url_publica (text), destaque (boolean), publicado (boolean), turmas_texto (text).

## 5. Fluxos N8N
| Arquivo | Função |
| --------------------------------- | --------------------------------------------------- |
| `1- Assistente Holos.json` | Lara — SDR principal, recebe do Chatwoot |
| `2- CRM _ Holos.json` | Cria/atualiza lead no Supabase + resumo GPT-4o-mini |
| `3- cursos_tool _ Holos.json` | Subagente que busca cursos via Edge Function |
| `1- Follow UP de 20 minutos.json` | Follow-up automático 20min |
| `2- Follow Up de 24 horas.json` | Follow-up automático 24h |

## 6. Script de Qualificação (Conversa com a Mãe)
1. **O que é um lead quente?** (Sinais de compra).
2. **Quais info precisa no 1º contato?** (Campos para Lara coletar).
3. **Como diferencia comprador de curioso?** (Critério de funil).

---
[[Holos/Holos]] | [[Lara Comercial]] | [[03 — Estudos e Referências/Memoria Antiga/Referencias/Prompts Completos]]
