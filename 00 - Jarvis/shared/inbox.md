---
updated: 2026-04-30
type: shared
purpose: bridge openclaw → local agents
---

# Inbox — OpenClaw → Escritório Local

> OpenClaw escreve aqui quando precisa delegar tarefa pros agentes locais (jarvis-ceo, pesquisador, executor).
> Claude Code local monitora, executa, escreve resultado em outbox.md.

## Como usar (OpenClaw)

```
STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo | pesquisador | executor
TASK: <descrição clara da tarefa>
CONTEXT: <contexto necessário>
PRIORITY: alta | normal | baixa
CREATED: YYYY-MM-DD HH:MM
```

## Tarefas

STATUS: DONE
FROM: openclaw
TO: executor
TASK: Criar arquivo shared/teste-bridge.md com conteúdo "Bridge OpenClaw ↔ Escritório Local operacional. Data: 2026-04-30."
COMPLETED: 2026-04-30 15:01

STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo
TASK: Criar criativo completo para massoterapia da Holos — funil, copy, criativos visuais (briefing para designer/IA), e plano de lançamento.
CONTEXT: Holos é uma escola de terapias da tia Luciana. Já tem funil de captura pronto, site, plataforma EAD e agente comercial Lara. Agora precisa de um criativo focado em massoterapia (curso de massagem terapêutica). Nicho: saúde/terapias alternativas. Público: pessoas interessadas em formação profissional em massoterapia. Modelo de negócio: venda de curso online (EAD). Precisa incluir: 1) Estrutura de funil (captura → aquecimento → venda); 2) Copy para anúncio (Facebook/Instagram); 3) Briefing para criativo visual (imagem/vídeo); 4) Plano de conteúdo para aquecimento (3-5 posts/emails); 5) Sugestão de oferta (lançamento). Levar em conta que a tia Luciana precisa aprovar — então tom profissional mas acolhedor, sem jargão técnico abrupto.
PRIORITY: alta
CREATED: 2026-04-30 15:00

STATUS: PENDING
FROM: openclaw
TO: pesquisador
TASK: Pesquisar referências de anúncios e funis de venda para cursos de massoterapia no Brasil. Identificar: gatilhos emocionais mais usados, objeções comuns do público, ofertas que converteram, faixa de preço praticada. Buscar também exemplos de criativos visuais (paletas, estilos de imagem) que funcionam no nicho de terapias holísticas/formação profissional.
CONTEXT: Subalimentação do jarvis-ceo com dados de mercado reais para embasar o criativo da Holos massoterapia.
PRIORITY: alta
CREATED: 2026-04-30 15:00
