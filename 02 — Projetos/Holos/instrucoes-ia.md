---
type: instrucoes-ia
summary: "Como IA deve operar no projeto Holos — tom, contexto, restrições, fluxos"
tags: [holos, instrucoes-ia, config]
---

# Instruções para IA — Holos

## Contexto
Projeto da Tia Luciana. Nicolas = CTO/Estrategista. Renda atual: R$1.500/mês.
Stack: Evolution API → N8N → Chatwoot → Supabase (CRM_HOLOS) → GPT-4.1-mini.
Base: 900 alunos ativos (Holos Connect) + 8.700 contatos ZenPro.

## Stakeholders — protocolo de comunicação
- **Tia Lu (Luciana):** onboarding suave. Nunca entregar por surpresa. Validar antes de mostrar.
- **Giovanna:** futura substituta da mãe no comercial. Lara a suporta hoje.
- **Nicolas:** arquiteto. Não executar nos 10% finais sem pressão externa (Gate 42).

## Como operar nesta pasta

### Tasks técnicas (N8N, Supabase, prompts)
1. Ler [[Holos - Sistema Técnico]] antes de qualquer mudança de infra
2. Checar [[Lara Comercial]] para status da Lara antes de sugerir features
3. **Regra absoluta:** nenhuma feature nova na Lara antes de subir em produção
4. Sugestões de código → N8N workflow ou Supabase query, nunca mudança direta em produção

### Tasks estratégicas (funil, copy, oferta)
1. Ler [[Holos - Estratégia 90 Dias]] para contexto de prioridades
2. Tom: transformação de identidade + semipresencial (diferencial vs. EAD puro)
3. Concorrentes para não imitar: Aprenda Massoterapia, Instituto Lis, Widom

### Tasks familiares / stakeholders
1. Ler [[Familia/Dinâmica Familiar]] antes de qualquer comunicação com tia ou pai
2. Crítica à Tia Lu = reconhecimento ANTES da correção. Nunca seco.

## Formato de output padrão
- Diagnóstico em bullets curtos
- Próximo passo único e acionável
- Se detectar bloqueio Gate 42 → sinalizar explicitamente

## Arquivos-chave nesta área
- [[Holos]] — contexto geral
- [[Holos - Sistema Técnico]] — infra e prompts
- [[Holos - Estratégia 90 Dias]] — prioridades
- [[Lara Comercial]] — agente IA
- [[Familia/Dinâmica Familiar]] — stakeholders
