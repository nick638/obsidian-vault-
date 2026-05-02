---
updated: 2026-04-22
status: rascunho
tags: [projeto, produto, futuro, saas]
---
# WhatsApp Unificado

> **O produto que realiza a autonomia total.** R$200/empresa × 50 empresas = R$10k/mês sem uma hora extra de trabalho de Nicolas. É a diferença entre vender tempo (prestador de serviço) e vender sistema (dono de produto). Só construir depois que Holos + Unimasso estiverem provados — porque o produto é a abstração do que já funciona.

**Status:** Conceito documentado · Execução após R$10k/mês  
*Última atualização: 2026-04-13*

---

## O que é

Um produto/sistema que centraliza o atendimento WhatsApp de múltiplas empresas (Unimasso, Holos, e futuros clientes) com:

- **Dashboard visual** para cada empresa
- **Kanban** de atendimentos
- **Cadastro de produtos** → atendente IA responde com base no catálogo sem precisar alterar prompt
- **Gestão de contexto** por empresa (cada uma tem sua identidade, produtos e fluxo)

---

## Por que isso importa — a visão de longo prazo

Hoje cada sistema novo que Nicolas cria exige:
1. Alterar prompt manualmente
2. Criar novo fluxo no N8N
3. Configurar novo ambiente

Com o WhatsApp Unificado: **cadastra empresa → define produtos → IA já atende**.

Mas o que realmente importa vai além da eficiência técnica:

**Este é o produto que realiza a autonomia.** Holos paga R$1.500/mês. Unimasso paga participação futura. Clientes externos pagam R$2–3k/mês cada. Mas o WhatsApp Unificado como SaaS significa receita que não depende de mais tempo de Nicolas — ele opera sem ele. R$200/empresa × 50 empresas = R$10k/mês sem uma hora a mais de trabalho.

**É a diferença entre ser prestador de serviço (vende tempo) e ser dono de produto (vende sistema).** Erico Rocha, ERA, Jesus multiplicação — todos apontam para isso. O WhatsApp Unificado é onde o princípio "construir uma vez, distribuir infinito" se torna produto real.

**Quando construir:** depois que Lara + Uni estiverem rodando e provados. O WhatsApp Unificado é a generalização dos sistemas que já funcionam — não é uma ideia nova, é a abstração do que já foi construído.

---

## Visão do produto

```
Empresa cadastrada
    → Produtos/serviços cadastrados no sistema
    → IA lê os produtos e monta o atendimento
    → Atendente responde com base no catálogo dinâmico
    → Dashboard mostra funil de cada empresa
    → Kanban organiza os atendimentos
```

---

## Diferencial

- Não precisa mexer em prompt para adicionar produto/serviço
- Multi-empresa em um único painel
- Pode virar SaaS (cobrado por empresa/número)

---

## Stack provável

- **N8N** — orquestração dos fluxos
- **Supabase** — dados (empresas, produtos, conversas, CRM)
- **Lovable** — dashboard visual
- **Evolution API** — camada WhatsApp
- **OpenAI** — IA das atendentes

---

## Próximos passos

- [ ] Validar conceito — qual empresa testar primeiro?
- [ ] Mapear estrutura de dados (empresas → produtos → conversas)
- [ ] Prototipar dashboard no Lovable

---

Caso 1 → [[Holos/Holos]] · Caso 2 → [[Unimasso/Unimasso]] · Escala para clientes → [[Clientes Externos/Metodologia de Captação]]
