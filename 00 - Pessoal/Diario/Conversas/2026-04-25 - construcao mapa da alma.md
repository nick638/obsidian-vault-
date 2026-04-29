---
created: 2026-04-25
updated: 2026-04-25
type: conversa
status: rascunho
tags: [conversa, projeto, mapa-da-alma, build, squads]
projeto: Mapa da Alma
---
# 2026-04-25 — Construção Mapa da Alma

> Conversa substancial: Nicholas pediu pra construir Mapa da Alma completo usando squads + Jarvis. Sistema entregue funcional (mock), pronto pra integração.

## Contexto
Nicholas trouxe prompt da Titia Dark (preparado pra v0.dev). Em vez de jogar no v0, decidiu testar capacidade do Jarvis de construir tudo direto + squads validando estratégia.

## Decisões
- **Stack:** Next.js 14 + Supabase + N8N + OpenAI + Vercel
- **Local repo:** `C:/Users/lugzi/dev/projetos/mapa-da-alma`
- **Modelo de oferta:** híbrido (Free → R$67 one-time → R$27/mês). Definido pelo hormozi-squad.
- **Posicionamento:** Sage + Magician. Tagline "O manual que ninguém te entregou." Definido pelo brand-squad.
- **Quiz:** 16 perguntas situacionais (cenários sem resposta errada). 4 metodologias cruzadas: Numerologia, HD, Arquétipos, Eneagrama.

## Squads acionados
1. `brand-squad` → posicionamento, paleta, tipografia, anti-posição
2. `copy-master` → landing completa + microcopy + 3 emails
3. `hormozi-squad` → oferta + créditos + projeção R$10k

Todos retornaram em 1 turno paralelo. Outputs integrados no código direto.

## Entregue
- 38 arquivos no repo
- Build OK (next build passou)
- Typecheck OK (zero erros)
- Mock 100% funcional sem env vars
- Schema Supabase + 2 workflows N8N exportáveis
- Doc arquitetura completa

## Pendências (ele faz)
1. Aplicar `supabase/schema.sql` em projeto Supabase
2. Importar 2 JSONs no N8N (`n8n.m6k.com.br`)
3. Configurar credenciais OpenAI + Supabase nos workflows
4. Setar `.env.local`
5. Deploy Vercel (Nicholas tentou Netlify primeiro)

## Sinais sobre Nicholas (pra futuras conversas)
- Confiou autonomia total ("use tudo que faça sentido", "quero algo melhor do que falei")
- Quer ver primeiro funcionando, depois refina
- Se não tiver clareza do que falta, pergunta direto ("organizado, sem ponta solta")
- Preocupação com vault organizado é constante
- Comunicação atrabalhada quando entusiasmado (frases longas, sem pontuação) — mas pedido é claro

## Próximo passo
Gate de Fechamento atualizado: deploy + 1ª venda paga até **15 de maio**.
Subgate imediato: rodar local + decidir se próximo é integração Supabase ou polimento visual.

## Conexões
- [[Mapa da Alma]]
- [[Prioridades da Semana]]
- [[Unimasso]]
