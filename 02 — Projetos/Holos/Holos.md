---
created: 2026-04-13
updated: 2026-04-26
type: projeto
status: ativo
prioridade: maxima
quando_ler: "contexto de renda atual (R$1.5k), estrutura comercial Holos, números WhatsApp, arquitetura Lara, base de alunos, stakeholders familiares"
tags: [projeto, familia, prioridade, ativo, holos]
---

# Holos

> Laboratório central. 100% da renda atual (R$ 1.500/mês). Case real para clientes de R$ 10k.

## 1. Visão Geral
- **Dona:** Tia Luciana Maier.
- **Papel:** Nicolas (CTO/Estrategista).
- **Conexão:** [[01 - Profissional/Projetos/Familia/Flywheel Holos x Unimasso]].

## 2. Desbloqueio (Diagnóstico Real)
- **Bloqueio:** TDAH nos 10% finais (Lara 90%). Falta de dopamina na fase chata (testes/ajustes).
- **Proteção:** "Lara que não subiu não falha".
- **Ação:** Subir imperfeita hoje > Perfeita parada.

## 3. Funil e Mercado (Abril 2026)
```
Tráfego pago → Páginas → WhatsApp → Conversão
```
- **Diferencial:** Transformação de identidade + semipresencial.
- **Concorrentes:** Aprenda Massoterapia (EAD puro), Instituto Lis (Genérico), Widom (Frio).

### Estrutura de Números
| Número      | Nome              | Responsável           | Função                                                      |
| ----------- | ----------------- | --------------------- | ----------------------------------------------------------- |
| Comercial 1 | (11) 97637-8429   | Equipe da tia         | Atende leads de massoterapia + imersões importantes         |
| Comercial 2 | Número geral      | Lara Comercial 2 (IA) | Vende cursos livres + outros cursos (às vezes massoterapia) |
| EAD         | Número do Nicolas | Nicolas               | Zero ativo — só para testes                                 |

## 4. Arquitetura Técnica (Resumo)
```
Chatwoot (WhatsApp) → Assistente Holos (Lara)
                               ↓ aciona tools
               ┌───────────────┼───────────────┐
          cursos_tool     agenda_tool        CRM
               ↓               ↓               ↓
      Supabase Edge      Supabase Edge    Supabase DB
      /api/v1/cursos  /api/v1/aulas-exp  CRM_HOLOS table
               ↓               ↓               ↓
          GPT-4.1-mini   GPT-4.1-mini    GPT-4o-mini
          (+ memória)    (+ memória)     (resumo)
```

## 5. Sistemas e Equipe
- **Métrica:** Alunos ativos (Holos Connect): 900. Contatos ZenPro: ~8.700.
- **Movimento:** Lara suporta Giovanna → Giovanna substitui mãe no comercial.
Infra e prompts → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] · Ações táticas → [[01 - Profissional/Projetos/Holos/Holos - Estratégia 90 Dias]] · Stakeholders familiares → [[01 - Profissional/Projetos/Familia/Dinâmica Familiar]]

---
[[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] | [[01 - Profissional/Projetos/Lara Comercial]] | [[01 - Profissional/Projetos/Holos/Holos - Estratégia 90 Dias]]
