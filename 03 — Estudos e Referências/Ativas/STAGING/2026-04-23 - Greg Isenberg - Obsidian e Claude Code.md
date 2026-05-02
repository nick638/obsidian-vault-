---
created: 2026-04-23
updated: 2026-04-23
area: pesquisa
type: staging
status: rascunho
tags: [obsidian, claude-code, segundo-cerebro, automacao, greg-isenberg, commands]
---
# Greg Isenberg (Vin) — How I Use Obsidian + Claude Code to Run My Life

> **Fonte:** [How I Use Obsidian + Claude Code to Run My Life](https://www.youtube.com/watch?v=6MBq1paspVU)
> **Data de Captura:** 2026-04-23

## 1. Tese Central (A Essência)
Os tokens de IA são a **energia**. Os arquivos Markdown interconectados do Obsidian são as **memórias**. Sem memória, a energia é desperdiçada a cada sessão (o problema da amnésia). A solução não é usar mais IAs — é construir uma rede de atalhos de terminal que usam a CLI do Obsidian + Claude Code para executar análises complexas e persistentes, sem precisar reexplicar o contexto toda vez.

## 2. Os 11 Comandos (Skills do Thinking Partner)

### `/context`
Carrega o contexto completo sobre a vida, trabalho e estado atual do usuário. Lê as notas diárias e segue os backlinks para construir um quadro holístico. Elimina a necessidade de reexplicar quem você é à IA a cada nova sessão.

### `/today`
Revisão matinal. Puxa tarefas do calendário, mensagens e notas diárias da última semana para criar um plano priorizado do dia. Como lê as anotações, a IA entende o que o usuário está de fato refletindo — decisões de agenda muito mais inteligentes.

### `/close day`
Processamento do fim do dia. Extrai itens de ação, traz conexões soltas à superfície e verifica "marcadores de confiança" (o quão seguro o usuário está sobre certas hipóteses de trabalho).

### `/ghost`
Reflexão no estilo do próprio usuário. Responde a uma pergunta exatamente como o usuário responderia — constrói um perfil de voz a partir de todas as anotações e avalia a fidelidade do resultado gerado.

### `/challenge`
Testa as crenças atuais. Usa o histórico do vault para encontrar contradições, contra-evidências e mudanças de pensamento. Garante desenvolvimento de ideias sem viés ou pontos de vista limitados.

### `/emerge`
Traz à superfície ideias que o vault "sugere" mas que nunca foram ditas explicitamente. Tira conclusões de premissas espalhadas pelas anotações e nomeia padrões que ainda não tinham nome.

### `/trace`
Rastreia como a relação com uma ideia, conceito ou ferramenta evoluiu ao longo do tempo. Constrói um mapa de vocabulário, pesquisa por todo o cofre e cria um histórico completo da evolução daquele pensamento.

### `/schedule`
Ao agendar algo, a IA não olha apenas a disponibilidade no calendário — lê as notas diárias para entender as prioridades mentais do momento. Pode recomendar cancelar uma reunião porque o assunto já está sendo resolvido de outra forma nas notas.

### `/connect [A] e [B]`
Pega dois domínios completamente diferentes e os conecta usando a rede de links do Obsidian. Analisa as "vizinhanças" de notas de cada conceito e gera pontes e interseções originais.

### `/ideas`
Gera um relatório de ideias de negócios e ferramentas prontas para construir. Lê arquivos órfãos, analisa padrões isolados e dá sugestões de ação práticas — move da reflexão passiva para a execução.

### `/graduate`
Criado pela própria IA durante uma execução do `/ideas`. Escaneia notas diárias recentes buscando pensamentos interessantes não desenvolvidos e ajuda a decidir se uma anotação solta deve ser "promovida" a um mini-ensaio ou documento independente.

## 3. Quote Cirúrgica
> "Os tokens de IA são a energia, mas os arquivos Markdown com links são as memórias. Sem memória, a energia é desperdiçada."

## 4. O que isso reforça ou contradiz no nosso Vault?
- **Reforça:** Toda a arquitetura do Jarvis OS. Nós já implementamos o `/context`, `/today`, `/close day`, `/challenge`, `/trace`, `/connect`, `/ideas` e `/graduate` como Skills nativas no `CLAUDE.md`.
- **Novidade:** `/ghost` e `/emerge` ainda não implementados. `/ghost` é particularmente poderoso para o Nicolas como Projetor 6/2 — escrever como você mesmo, mas usando o cofre como espelho.
- `/schedule` requer integração com calendário (Google Calendar ou Notion) — próximo nível da automação.

## 5. Teste de Aplicação
*Os 11 comandos já foram inseridos no `CLAUDE.md`. Qual quer testar primeiro além do `/ideas` que rodamos agora? Sugiro o `/emerge` — provavelmente revelará padrões que você não nomeou mas que já estão latentes no seu vault.*

---

Jarvis OS → [[00 — Quem Sou Nicolas/Como trabalho com IA]] · Pesquisa complementar → [[03 — Estudos e Referências/Arquivadas/Curado/2026-04-19 - Claude + Obsidian]] · Perfil → [[00 — Quem Sou Nicolas/Diagnóstico Real]]
