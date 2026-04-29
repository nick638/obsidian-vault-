---
created: 2026-04-22
updated: 2026-04-26
type: projeto
status: bloqueado
prioridade: maxima
quando_ler: "status Lara, gate de fechamento, próximos passos pra subir em produção, arquitetura N8N/GPT, bloqueio na conversa com Tia Lu"
tags: [projeto, lara, ia, holos, prioridade]
aliases: [Lara, Lara IA, Atendente Holos, Lara Comercial 2]
---

# Lara Comercial

> Agente IA de atendimento WhatsApp (Holos). Orquestradora + Tools + Supabase.

## 1. Status e Bloqueios (Gate 42)
- **Status:** ~90% pronta.
- **Ideia Pendente:** [[02 - Pesquisas e Estudos/Ativas/Pontes/2026-04-24 - connect - Lara x Funil Gamificado]] (qualificação gamificada).
- **Bloqueio (Gate 42):** "Nicholas constrói, não fecha." Travada na conversa com a tia sobre critérios de pré-qualificação.
- **Regra:** *Nenhuma feature nova antes de subir em produção.*

## 2. Gate de Fechamento (O Fim do Ciclo)
O projeto sai do status "ativo" no exato momento em que:
1. Os critérios de pré-qualificação forem validados com a Tia Lu.
2. A Lara rodar 1 atendimento real via Evolution API com o Supabase sendo alimentado.

## 3. Arquitetura
Detalhes técnicos de infra e prompts → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]]
```text
Lead envia mensagem (WhatsApp)
    ↓
Evolution API → N8N
    ↓
[Orquestradora] — agente principal (GPT-4o)
    ↓ (se precisar de info de produto)
[Tool: Busca de Produtos] — sub-workflow → sistema Holos (API)
    ↓
[Orquestradora] responde ao lead
    ↓
[Fluxo CRM] — IA preenche etapa, resumo, dados do lead → Supabase
```

## 4. Checklist de Operação (100%)
- [ ] Dashboard visual mostrando conversas em tempo real.
- [ ] Kanban de leads com etapas, resumo de conversa e dados do lead.
- [ ] Novos cursos/produtos adicionáveis pelo sistema — sem editar prompt.
- [ ] Pré-qualificação de leads funcionando.
- [ ] Testada e estável em produção.

## 5. Stakeholders e Histórico
- **Nicolas:** Arquiteto/Operador.
- **Tia (Holos):** Cliente final. Projeto pai → [[01 - Profissional/Projetos/Holos/Holos]]
- **Afonso Lopes:** Metodologia base. → [[02 - Pesquisas e Estudos/Ativas/Cursos/Método ERA - Afonso Lopes]]
- **Decisão (Abr/26):** Arquitetura orquestradora + tools escolhida para não depender de edição de prompt por produto. CRM construído com Vibe Coding + Supabase.
Prompt master → [[03 - Memoria da IA/Referencias/Prompts Completos]]

---
[[01 - Profissional/Projetos/Holos/Holos]] | [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] | [[03 - Memoria da IA/Referencias/Prompts Completos]]
