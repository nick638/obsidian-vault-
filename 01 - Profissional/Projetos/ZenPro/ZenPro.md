---
created: 2026-04-13
updated: 2026-04-26
type: projeto
status: ativo
prioridade: alta
quando_ler: "disparo em massa (5.768 leads), webhook N8N literal, rate limits (15s/2MB), integração Lara na Fase 1 Holos (CAC zero)"
tags: [crm, familia, zenpro, ativos, automacao]
---

# ZenPro

> Ativo vivo: 5.768 contatos. CRM Multi-conta. Sistema pai para disparos em massa.

## 1. Infraestrutura e Status
- **Criador:** Pai do Nicolas. Hub do pai → [[01 - Profissional/Projetos/Familia/Revolucio — Sistema do Pai]]
- **Organização:** Holos Cursos e Terapias Ltda + Edificar.
- **Stack:** Evolution API + Lovable + Vercel.
- **Status:** Em Produção.

## 2. Especificações do Webhook e Disparo (Literais)
- **Base Total:** 5.768 contatos cadastrados.
- **Instância Ativa:** HolosEAD.
- **Webhook Destino (N8N):** `https://nwh.m6k.com.br/webhook/0f793393-9201-4398-96f6-7d1eaa5585ff`
- **Rate Limit:** 15s entre envios.
- **Limites de Mídia:** Editor de mensagem 2000 caracteres, Anexos JPG/PNG/WebP até 2MB.

## 3. O Gap Estratégico
ZenPro dispara *blasts* genéricos. A integração com a **Lara Comercial 2** converte isso em funil ativo:
1. ZenPro faz o disparo em massa para 5.768 leads (Fase 1 Holos). Motor da Fase 1 (CAC Zero) → [[01 - Profissional/Projetos/Holos/Holos - Estratégia 90 Dias]]
2. Lead responde.
3. Lara qualifica e registra no CRM_HOLOS. Oferta atrelada → [[01 - Profissional/Projetos/Holos/Holos - Cursos]]

---
[[01 - Profissional/Projetos/Holos/Holos - Estratégia 90 Dias]] | [[01 - Profissional/Projetos/Lara Comercial]] | [[01 - Profissional/Projetos/Familia/Revolucio — Sistema do Pai]]
