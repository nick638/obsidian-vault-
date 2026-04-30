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

STATUS: PENDING
FROM: openclaw
TO: pesquisador
TASK: EXECUTAR E REGISTRAR RESULTADO EM shared/outputs/01-pesquisador.md: Pesquisar Pixel Agents, ferramentas concorrentes (CrewAI, AutoGen, n8n AI agents, etc), e plataformas de multi-agentes visuais. Para cada ferramenta: o que faz, como mostra os agentes, se permite ver conversas entre eles, se roda 24/7, se é open source, preço. A pesquisa deve ser registrada no template 01-pesquisador.md com formato chat: timestamp, agente, mensagem. Exemplo: "[17:20] pesquisador: Iniciei pesquisa sobre...".
CONTEXT: Nicholas quer saber qual ferramenta permite agentes 24/7 com conversa visível entre eles, para escalar o escritório no futuro. Precisamos comparar opções.
PRIORITY: alta
CREATED: 2026-04-30 17:22

STATUS: PENDING
FROM: openclaw
TO: jarvis-ceo
TASK: Responder às perguntas de alinhamento de vault entre OpenClaw (VPS) e escritório local (Claude Code). Registrar resposta em shared/outputs/02-estrategista.md no formato chat-log. Perguntas:
1) Qual a estrutura de pastas do vault que você considera "fonte da verdade" pra nicho (OpenClaw)?
2) Onde cada um escreve logs diários? Eu uso /root/.openclaw/workspace/memory/YYYY-MM-DD.md. Onde você escreve?
3) Temos shared/pending.md, shared/decisions-log.md, shared/project-state.md — você também mantém eles atualizados? Qual a frequência?
4) Quando eu crio um arquivo no vault via inbox, onde você salva? Tem um padrão?
5) Qual a regra pra arquivos que só eu (OpenClaw) devo mexer vs arquivos que só você (escritório local) mexe?
6) Precisamos de um SCHEMA.md ou equivalente que ambos consultem pra saber onde por cada coisa.
CONTEXT: Nicholas quer que eu (OpenClaw VPS) e o escritório local (Claude Code) usemos o vault com a MESMA organização. Precisamos definir boundaries claras pra não pisar no pé um do outro.
PRIORITY: alta
CREATED: 2026-04-30 17:22

STATUS: PENDING
FROM: openclaw
TO: executor
TASK: Após pesquisador responder sobre as ferramentas, criar um documento comparativo em 00 - Jarvis/shared/ferramentas-multiagentes.md com tabela comparativa entre Pixel Agents, CrewAI, AutoGen, n8n AI agents, e outras encontradas pela pesquisa. Incluir: preço, 24/7, visibilidade de conversa, open source, facilidade de setup. Incluir também recomendação do que faz sentido pra Nicholas agora vs futuro.
CONTEXT: Nicholas quer decidir qual plataforma usar pra evoluir o escritório. Precisamos de dados concretos.
PRIORITY: alta
CREATED: 2026-04-30 17:22
