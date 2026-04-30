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
TO: jarvis-ceo
TASK: <descrição clara da missão>
CONTEXT: <contexto relevante>
PRIORITY: alta | normal | baixa
CREATED: YYYY-MM-DD HH:MM
```

## Tarefas

STATUS: DONE
FROM: openclaw
TO: executor
TASK: Implementar sistema shared/outputs/ — criar estrutura de pastas e arquivos para cada agente depositar resultado parcial durante execução da cadeia. Estrutura: 00 - Jarvis/shared/outputs/01-pesquisador.md, 02-estrategista.md, 03-copy-master.md, 04-designer.md, 05-final-jarvis-ceo.md. Cada arquivo deve ter template com: agente, etapa, input recebido, output gerado, timestamp. Também atualizar os agentes para escreverem seus resultados parciais nesses arquivos ANTES de passar pro próximo agente na cadeia.
CONTEXT: Nicholas quer transparência do raciocínio de cada agente. O Pixel Agents mostra os terminais em tempo real, mas com shared/outputs/ ele pode ler o resultado de cada etapa mesmo depois de finalizada. Deve funcionar como trilha de auditoria da cadeia. Prioridade: alta — implementar AGORA, antes da missão do criativo estático começar a rodar.
PRIORITY: alta
CREATED: 2026-04-30 15:52

STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo
TASK: Criar criativo estático para massoterapia da Holos — vertente visual de anúncio estático (imagem + copy principal). Pesquisar referências de mercado primeiro, depois gerar copy + briefing visual para o designer produzir o criativo final. IMPORTANTE: primeiro garantir que o sistema shared/outputs/ foi implementado. Cada etapa da cadeia deve escrever o resultado parcial em shared/outputs/ antes de passar pro próximo agente.
CONTEXT: Holos Escola de Terapias. Produto: Formação Massoterapia EAD 460h. Público: pessoas buscando nova carreira em massoterapia, trocar emprego ruim por independência financeira, maioria mulheres 25-45. Diferenciar do criativo anterior (que focou no funil completo + lançamento) — agora queremos o criativo ESTÁTICO em si: a arte visual + copy que vai no anúncio. Pesquisar referências visuais que convertem no nicho. Usar paleta da Holos (roxo + laranja + dourado). Tom profissional mas acolhedor. Briefing deve ser específico o suficiente pro designer gerar a arte (dimensões: 1080x1080 feed, 1080x1920 story, 1200x628 link ad). Gate: Tia Luciana precisa aprovar — apresentar valor primeiro, surpresa nunca.
PRIORITY: alta
CREATED: 2026-04-30 15:53
