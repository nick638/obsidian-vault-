---
type: instrucoes-ia
summary: "Como IA deve operar no projeto Mapa da Alma — gates, stack, tom, decisões pendentes"
tags: [mapa-da-alma, instrucoes-ia, config, produto]
---

# Instruções para IA — Mapa da Alma

## Contexto
Produto SaaS: quiz situacional → mapa visual (Numerologia + HD + Arquétipos + Eneagrama) → chat IA personalizado.
Stack: Next.js 14 + Supabase (`ismybhrgiehsoxqpjctk`) + N8N (m6k.com.br) + GPT-4o-mini via OpenRouter.
Código em: `C:/Users/lugzi/dev/projetos/mapa-da-alma`

## Gate de Fechamento
**1ª venda paga até 15 de maio de 2026.**

Subgates:
1. ~~Rodar localmente e validar visual~~ — fazer se ainda não feito
2. ~~Integrar Supabase + importar N8N~~ ✅ feito
3. Deploy Vercel (até 05/maio)
4. 1ª venda (círculo próximo, até 15/maio)

**Qualquer sugestão deve acelerar o deploy. Não adicionar features antes da 1ª venda.**

## Tom e identidade (não mudar sem justificativa)
- Tagline: *"O manual que ninguém te entregou."*
- Arquétipo: Sage + sombra Magician
- Tom: Lúcido · Íntimo · Reverente
- Anti-posição: não é horóscopo, não é app gamificado, não é guru
- Estética: códex digital (livro místico + interface conversacional)

## Oferta (validada, não alterar)
| Tier | Preço |
|---|---|
| Free | R$0 — quiz + mapa básico + 3 perguntas |
| Mapa Completo | R$67 one-time |
| Alma+ | R$27/mês |

Meta: 110 clientes/mês com 8% conversão, CPA máx R$30.

## Como operar

### Tasks de desenvolvimento
1. Verificar se já existe em `C:/Users/lugzi/dev/projetos/mapa-da-alma` antes de criar
2. N8N webhooks ativos:
   - Gerar mapa: `https://n8n.m6k.com.br/webhook/mapa-da-alma`
   - Chat: `https://n8n.m6k.com.br/webhook/mapa-da-alma-chat`
3. Env vars em `C:/Users/lugzi/dev/jarvis/.env` — nunca comitar
4. Output de código: TypeScript/Next.js App Router, sem comentários desnecessários

### Deploy (próximo gate crítico)
1. Configurar env vars Netlify (mesmo conteúdo do `.env.local`)
2. Redeploy
3. Testar fluxo completo: quiz → mapa → chat → crédito debitado

### Decisões pendentes (não resolver sem Nicholas)
- Domínio: `mapadalma.holos.com.br` ou domínio próprio?
- Pagamento: Stripe Brasil, Mercado Pago ou Asaas?
- Integrar Unimasso desde dia 1 ou standalone primeiro?

### Copy / marketing
- Seguir tom do brand-squad e hormozi-squad já validados
- Não reescrever landing sem justificativa — copy já validada
- Distribuição inicial: círculo próximo → base ZenPro (8.700 contatos)

## Formato de output padrão
- Iniciar com: status do próximo subgate
- Código: TypeScript, App Router, sem boilerplate
- Decisões pendentes → sempre perguntar antes de assumir

## Arquivos-chave
- [[Mapa da Alma]] — estado completo do projeto
- [[Unimasso/Unimasso]] — destino final do produto
- [[Familia/Flywheel Holos x Unimasso]] — contexto estratégico
- [[Areas/Financeiro]] — metas de receita
