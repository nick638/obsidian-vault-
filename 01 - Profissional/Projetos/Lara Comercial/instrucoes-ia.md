---
type: instrucoes-ia
summary: "Como IA deve operar no projeto Lara Comercial — gates, arquitetura, restrições"
tags: [lara, instrucoes-ia, config, ia-agente]
---

# Instruções para IA — Lara Comercial

## Contexto
Agente IA de atendimento WhatsApp (Holos). Status: ~90% pronta. Bloqueada na conversa com Tia Lu sobre pré-qualificação.
Arquitetura: Evolution API → N8N → Orquestradora (GPT-4o) → Tools (Busca Produtos, CRM) → Supabase.

## Gate de Fechamento (prioridade máxima)
Projeto fecha quando:
1. Critérios de pré-qualificação validados com Tia Lu
2. Lara roda 1 atendimento real via Evolution API com Supabase sendo alimentado

**Qualquer sugestão deve ser filtrada por este gate. Se não avança o gate → não priorizar.**

## Restrições absolutas
- **Zero features novas antes de subir em produção.** Se usuário pedir nova feature → redirecionar para gate.
- Mudanças de prompt master → checar [[03 - Memoria da IA/Referencias/Prompts Completos]] primeiro
- Alterações de infra → checar [[Holos - Sistema Técnico]]

## Como operar

### Debug / ajuste técnico
1. Identificar em qual nó do fluxo está o problema (Evolution → N8N → Orquestradora → Tool → Supabase)
2. Isolar antes de propor solução
3. Output: código N8N (JavaScript) ou query Supabase, sempre com explicação do porquê

### Avanço do gate (conversa com Tia Lu)
1. Ler [[Familia/Dinâmica Familiar]] — protocolo com Tia Lu
2. Preparar script de conversa: contexto → proposta → validação (nunca surpresa)
3. Critérios de qualificação = perguntas que a Lara faz antes de apresentar oferta

### Checklist de produção (o que falta)
- [ ] Dashboard visual conversas em tempo real
- [ ] Kanban de leads com etapas + resumo + dados
- [ ] Produtos adicionáveis sem editar prompt
- [ ] Pré-qualificação funcionando
- [ ] Testada e estável em produção

## Formato de output padrão
- Sempre iniciar com: status do gate (aberto/fechado)
- Sugestões técnicas: formato de workflow N8N ou SQL Supabase
- Se detectar feature creep → bloquear e redirecionar

## Arquivos-chave
- [[Holos - Sistema Técnico]] — infra completa
- [[03 - Memoria da IA/Referencias/Prompts Completos]] — prompt master Lara
- [[Familia/Dinâmica Familiar]] — como falar com Tia Lu
- [[Holos]] — contexto pai
