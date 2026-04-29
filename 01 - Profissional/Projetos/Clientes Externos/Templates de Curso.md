---
updated: 2026-04-22
status: rascunho
tags: [cliente, templates, produto]
---
# Templates de Curso — Entregáveis por Segmento

> **O produto pronto na prateleira.** Quatro templates completos testados em produção. Barbearia, advocacia, imobiliária, estética — cada um com prompt, CRM, follow-up e integração N8N prontos. Um novo cliente desses segmentos está rodando em 2 dias.

*Última atualização: 2026-04-13*

---

## O que é um "template de curso"

Cada template é um sistema completo de automação já montado e testado em produção. Quando um novo cliente entra, Nicolas:

1. Copia o template base
2. Adapta o prompt da secretária para o segmento
3. Configura a tabela CRM no Supabase
4. Conecta N8N + Evolution API + Chatwoot
5. Entrega funcionando em ~2 dias

---

## Templates disponíveis (prontos para entregar)

| Template | Segmento | Agente | Arquivo N8N |
|----------|----------|--------|-------------|
| Barão da Navalha | Barbearia | Bia | `Downloads/Projetos/BARBEARIA` |
| Aurora Advocacia | Advocacia/Direito | Camila | `Downloads/Projetos/Workflow--advogado` |
| Morada One | Imobiliária | Caique | `Downloads/Projetos/ImobiFlow` |
| Instituto Essenza | Clínica estética | Renata | `Downloads/Projetos/estética` |
| Template Base (genérico) | Qualquer segmento | — | `Downloads/Projetos/TEMPLATE--BASE--(atual)` |

> Prompts completos de cada agente em: [[03 - Memoria da IA/Referencias/Prompts Completos]]

---

## O que cada entrega inclui

```
Sistema completo:
├── Fluxo N8N (secretária + subagente de conhecimento + CRM + follow-up)
├── Tabela Supabase (CRM estruturado por segmento)
├── Prompt da secretária (com SPIN Selling adaptado)
├── 3 follow-ups automáticos (20min · 24h · 72h)
└── Conexão Evolution API + Chatwoot
```

**Opcional (quando cliente pede):**
- Blog SEO automático (Bumblebee 2.0 conectado ao WordPress)
- Dashboard Lovable espelhando o CRM

---

## Campos CRM por segmento

| Segmento | Campos extras além do universal |
|----------|---------------------------------|
| Barbearia | servico · barbeiro · data_hora_agendada · id_agendamento |
| Advocacia | tipo_caso · objetivo_lead · data_consulta |
| Imobiliária | tipo_imovel · finalidade · bairro_desejado · data_visita |
| Estética | procedimento_interesse · queixa_principal |
| SaaS (Unimasso) | especialidade · tempo_atuacao · interesse_plano · objecao |

> Campos universais em: [[03 - Memoria da IA/Referencias/Estruturas de CRM]]

---

## Precificação (referência de mercado)

| Entregável | Valor que o mercado cobra |
|-----------|--------------------------|
| Sistema completo (secretária + CRM + follow-up) | R$3.000–8.000 projeto + R$500–1.500/mês manutenção |
| Só o fluxo de aquecimento (N8N) | ~R$30.000 (valor percebido Leo Soares) |
| Clone de IA especialista | ~R$8.000 |
| Dashboard comportamental de avatar | ~R$40.000 |

> Modelo ERA: cobrar **recorrência**, não projeto único — cliente paga pelo ecossistema rodando, não pela entrega inicial.

---

## Próximos segmentos a prospectar

| Segmento | Por que | Template base |
|----------|---------|--------------|
| Barbearia | Template pronto · mercado grande · dor clara (atendimento) | Barão da Navalha |
| Advocacia | Alta margem · diferencial alto · Camila já pronta | Aurora |
| Clínicas (odonto, estética, fisio) | Alto volume de leads · agendamento recorrente | Essenza adaptado |
| Imobiliária | Lead qualificado vale muito · Caique já pronto | Morada One |
| Escolas e cursos | Case Holos como prova social | Template Holos adaptado |

---

## Como fechar o primeiro cliente externo

```
1. Case Holos funcionando (Lara no ar)
2. Branding pessoal definido (/brand-squad)
3. Presença digital básica (LinkedIn + portfólio)
4. Abordagem direta: "Tenho um sistema pronto para [segmento]"
5. Demo → proposta → fechamento → 2 dias de entrega
```

---

## Por que isso importa — 5 templates prontos = 5 segmentos de mercado acessíveis hoje

A maioria dos especialistas em automação vende "sob medida" — cada cliente é um projeto do zero. Nicolas tem 5 sistemas prontos em 5 segmentos diferentes. Isso muda a conversa de venda completamente.

"Tenho um sistema pronto para barbearia que instalo em 2 dias" é diferente de "posso construir um sistema para você". A primeira é produto. A segunda é serviço. Produto fecha mais rápido, tem margem maior, e escala.

**A escada do produto:** hoje Nicolas entrega por cliente. O passo seguinte (WhatsApp Unificado) é entregar como plataforma — o cliente entra, configura o número, e usa o template diretamente. A receita multiplica sem que a carga de trabalho multiplique proporcional.

**Precificação recomendada ERA:** não cobrar setup + projeto. Cobrar recorrência desde o início. R$1.500–3.000/mês por 12 meses = R$18k–36k por cliente vs R$5k de projeto único. O template torna a recorrência viável porque manutenção é mínima.

---

Prompts → [[03 - Memoria da IA/Referencias/Prompts Completos]] · Arquitetura → [[03 - Memoria da IA/Referencias/Templates e Prompts]] · CRM → [[03 - Memoria da IA/Referencias/Estruturas de CRM]] · Metodologia → [[01 - Profissional/Projetos/Clientes Externos/Metodologia de Captação]] · Case → [[01 - Profissional/Projetos/Holos/Holos]] · Evolução SaaS → [[01 - Profissional/Projetos/WhatsApp Unificado/WhatsApp Unificado]]

---
