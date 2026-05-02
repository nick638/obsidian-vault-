---
created: 2026-04-25
updated: 2026-04-26
type: projeto
status: ativo
prioridade: alta
quando_ler: "status do deploy, gate de fechamento (1ª venda 15/maio), preços (R$67/R$27), stack Next.js+N8N+Supabase, decisões pendentes (domínio, pagamento)"
tags: [projeto, produto, ia, wellbeing, unimasso]
---

# Mapa da Alma

> Quiz situacional → mapa visual cruzando 4 metodologias (Numerologia + Human Design + Arquétipos + Eneagrama) → chat IA com contexto pessoal.

## Posição (validado por brand-squad)

**Tagline:** *"O manual que ninguém te entregou."*
**Headline landing:** *"Você não é complicado. Você nunca foi traduzido."*
**Arquétipo:** Sage (sabedoria) + sombra Magician (transformação ritualística)
**Tom:** Lúcido · Íntimo · Reverente
**Anti-posição:** não é horóscopo · não é app gamificado · não é guru

---

## Identidade visual

| Elemento | Valor |
|---|---|
| Noite Profunda | `#0E0B16` (background) |
| Pergaminho | `#F4EDE0` (texto) |
| Ouro Velho | `#C9A96E` (acentos) |
| Violeta Crepúsculo | `#7B5EA7` (ritual) |
| Vermelho Sangue Seco | `#E85A4F` (CTA) |
| Display | Cormorant Garamond |
| Sans | Inter |
| Mono | DM Mono |

Estética: *códex digital* (livro místico encontrado num arquivo + interface conversacional).

---

## Oferta (validado por hormozi-squad)

| Tier | Preço | Inclui |
|---|---|---|
| Free | R$0 | Quiz + mapa básico + 3 perguntas chat |
| **Mapa Completo** | **R$67 one-time** | Mapa completo (8 seções) + 30 créditos chat + garantia 7d |
| Alma+ premium | R$27/mês | Chat ilimitado + atualização anual + sinastria |

**Pacotes de créditos avulsos:** 20/R$19 · 60/R$39 · 200/R$89

**Garantia:** condicional 7 dias — "use 10 créditos e se não disser 'me descreveu melhor que terapia', devolve."

**Meta R$10k/mês:** ~110 clientes/mês com 8% conversão visita→quiz→pago. CPA máx R$30.

---

## Stack técnica

```
Next.js 14 (App Router) · TypeScript · Tailwind · Framer Motion · Recharts
Supabase (Auth + Postgres + RLS)
N8N (2 workflows: gerar mapa + chat)
OpenAI GPT-4o-mini (custo ~R$0,003/leitura, ~R$0,001/chat)
Vercel (front) + Hetzner/EasyPanel (N8N self-hosted)
```

**Custo total até 1k usuários/mês:** ~R$40

---

## Estado atual (2026-04-25)

### ✅ Pronto
- **Frontend Next.js completo em `C:/Users/lugzi/dev/projetos/mapa-da-alma`**
  - Landing de vendas (copy hormozi + brand validados)
  - Auth signup/login (Supabase ou mock)
  - Quiz situacional 16 perguntas (sem certo/errado, captura sinais HD/Eneagrama/Arquétipo + nome/data pra numerologia)
  - Loading narrativo com 5 mensagens + polling
  - Mapa visual com Recharts radar + 8 seções colapsáveis + chat fixo bottom
  - Admin com busca + modal de detalhes
- **Schema Supabase completo** (`supabase/schema.sql`) — profiles, quiz_responses, mapas, chat_history, credits_transactions + RLS + triggers + função `use_credit`
- **N8N workflows exportáveis** (`n8n/workflow.json` + `workflow-chat.json`)
- **Numerologia Pitagórica em TypeScript** (`lib/numerology.ts`) — Caminho de Vida + Expressão + Alma
- **APIs mock** rodando 100% sem env vars (test-drive já)
- **Documentação** completa (`docs/ARCHITECTURE.md`)

### ✅ Backend integrado (2026-04-26)
- Supabase project `ismybhrgiehsoxqpjctk` (mapa-da-alma, sa-east-1) criado + schema aplicado + trigger profile.has_mapa
- N8N workflows ATIVOS:
  - `TfXFDAW78opySeWu` → `https://n8n.m6k.com.br/webhook/mapa-da-alma`
  - `8XgF7YsIwnwFGUJ7` → `https://n8n.m6k.com.br/webhook/mapa-da-alma-chat`
- LLM: OpenRouter `openai/gpt-4o-mini` (chave em `C:/Users/lugzi/dev/jarvis/.env`)
- E2E testado: quiz → mapa salvo Supabase ✅ · chat → resposta personalizada cruzando mapa ✅
- `.env.local` configurado com URLs + secret

### ⏳ Falta só
1. `npm run dev` local pra ver tudo conectado
2. Configurar env vars no Netlify (Site settings → Environment variables) com mesmo conteúdo do `.env.local`
3. Redeploy Netlify
4. Domínio (sugestão: `mapadalma.holos.com.br`)
5. Pixel Meta + GA + tracking

### ⚠️ Decisões pendentes
- Conectar com Unimasso Plus desde dia 1 ou rodar standalone primeiro? Destino final → [[Unimasso/Unimasso]]
- Domínio próprio ou subdomínio Holos? Canal de distribuição → [[Holos/Holos]]
- Pagamento: Stripe Brasil, Mercado Pago ou Asaas?
Contexto flywheel → [[02 — Projetos/Familia/Flywheel Holos x Unimasso]]

---

## N8N — fluxos exportáveis

**Webhook gerar mapa:** `POST /webhook/mapa-da-alma`
- Header obrigatório: `x-webhook-secret`
- Body: `{ uid, answers }`
- Fluxo: validar secret → calcular numerologia (Code node) → OpenAI gerar leitura JSON → mesclar → salvar Supabase → responder

**Webhook chat:** `POST /webhook/mapa-da-alma-chat`
- Body: `{ uid, message }`
- Fluxo: buscar mapa → buscar histórico → OpenAI com mapa como system prompt → salvar conversa → debitar crédito (RPC) → responder

JSONs prontos pra importar em `C:/Users/lugzi/dev/projetos/mapa-da-alma/n8n/`.

---

## Quiz — 16 perguntas situacionais

Estrutura: nome (numerologia) + data (numerologia) + 14 cenários (HD + Eneagrama + Arquétipo).

Cada cenário tem 4 opções. Cada opção tem `signals` que somam pesos pra cada metodologia. No N8N, IA recebe o tally final + numerologia já calculada e gera leitura cruzada.

Categorias: identidade, energia, decisão, vínculo, ambiente, padrão, sombra, futuro.

Arquivo completo: `lib/quiz-questions.ts` no projeto.

---

## Status (2026-05-02)

**Não é prioridade agora.** Sistema completo construído e backend integrado. Em pausa até voltar ao radar.

Gate anterior era 1ª venda até 15/mai — não perseguido ativamente.

---

---
[[Unimasso/Unimasso]] | [[Holos/Holos]] | [[Arquivo não encontrado — ver conteúdo migrado]]
