---
created: 2026-04-22
updated: 2026-04-26
type: recurso
status: ativo
prioridade: alta
quando_ler: "aprendizados operacionais Nicholas↔Jarvis, ajustes de tom, regras de colaboração, bugs factuais corrigidos no vault"
tags: [jarvis, feedback, log, aprendizado]
---

# Jarvis — Feedback Log

> Registro vivo de interações e ajustes operacionais. Documenta o que funcionou, o que falhou e como Jarvis deve se adaptar ao fluxo de Nicholas.

## 1. Regras de Colaboração (Síntese)
- **Validação Antecipada:** Mostrar plano/resumo antes de executar ações não-triviais.
- **Canal Oficial:** Revolucio (pai) é o canal oficial para pedidos da família; pedidos informais devem ser redirecionados.
- **Fato > Chute:** Jarvis não deve inventar dados (família, cidade, amigos). Se não sabe, pergunta.
- **Tom:** Caveman Mode (telegráfico) por padrão para eficiência de tokens.

## 2. Histórico de Logs Relevantes
- **2026-04-21:** Setup inicial e orquestração de agentes. Incorporado filtro "ativar > construir" de Rafael Melgaço.
- **2026-04-21:** Formalização Nicolas ↔ Família (Holos). CTO de Plantão + Retainer R$2k.
- **2026-04-23:** Validação do Perfil Real (Projetor/Gate 42). Nicholas validou que perguntas de cenário funcionam melhor que perguntas somáticas.
- **2026-04-24:** Criado comando `/walk` para curadoria recorrente do vault. Resolvido bug de links legados e identificada mentira interna sobre "portfólio não existente".

## 3. Aprendizados sobre Operação
- **Vault é Identidade:** Organizar como Nicholas organizaria, mantendo o "custume" das notas legadas.
- **Lotes Curtos:** Perguntas em lotes de 2-5 para evitar sobrecarga e economizar tokens.
- **Prótese Cognitiva:** O vault deve compensar a memória de trabalho instável do TDAH com contexto redundante.
Padrões identificados via feedback → [[00 - Pessoal/Insights/cerebro-evoluido]]

## 4. Log cronológico

**2026-04-21 — Setup inicial do Jarvis**
Resultado: CLAUDE.md reescrito com identidade, orquestradores, auto-squads e loop de feedback.
Ajuste: testar tom casual nas próximas conversas e ajustar conforme feedback do Nicolas.

**2026-04-21 — Arquitetura Jarvis OS construída**
Resultado: Criados 4 roteadores (.claude/agents/strategist.md, creator.md, builder.md, keeper.md) + Chief of Staff (ad-hoc) + personas @rafael e @afonso + doc visual ESTRATÉGIA/Arquitetura Jarvis.md. Vault amarrado: Index do Nexus corrigido (links quebrados pra pasta antiga), regra "nunca minta" incorporada no CLAUDE.md.
Ajuste pendente: testar invocação real dos roteadores ("pergunta pro @rafael", "qual prioridade?"), converter settings.json para formato de hooks reais do Claude Code quando Nicolas voltar, receber 3º vídeo Rafael Melgaço.

**2026-04-21 — Insights de Rafael Melgaço absorvidos**
Resultado: 2 vídeos processados (Protocolo R$10k + Stack Vibe Coding), persona entrevistável criada, síntese aplicada ao contexto Nicolas. Filtro "ativar > construir" incorporado como regra do Strategist.
Ajuste: aplicar filtro Rafael em toda decisão de construir novo sistema.

**2026-04-21 — Revolucio identificado + Proposta de Formalização criada**
Resultado: Descoberto que Revolucio é o Jarvis do pai (não pessoa). Nova missão oficial chegou: refazer site da Holos (sair do Lovable). Pai muda de papel pra vendedor/expert, Nicolas assume CTO de Plantão. Criada [[Proposta Formalização Nicolas ↔ Família]] com retainer R$2k + tabela de serviços com 80% desconto família. Atualizada [[Prioridades da Semana]] com novo gargalo: formalizar relação financeira antes de qualquer outra coisa. Criada nota [[Revolucio — Sistema do Pai]] como referência permanente.
Ajuste: Revolucio é canal oficial. Pedidos informais da família devem ser redirecionados. Stack oficial sites = Vercel + Next/Astro + CMS visual (NÃO mais Lovable, NÃO mais WordPress pra site).

**2026-04-21 — Regra "mostrar antes de executar" confirmada**
Resultado: Nicolas validou explicitamente que prefere ver plano/resumo antes de eu sair fazendo. Economiza crédito + evita trabalho desalinhado. Isso virou padrão operacional desta sessão em diante.
Ajuste: Antes de qualquer ação não-trivial (criar arquivo, disparar squad, pesquisar web, modificar estrutura), espelhar o entendimento + mostrar plano + esperar aprovação.

---

**2026-04-23 — Entrevista de validação do perfil real + reorganização do vault**

Resultado: Perfil Projetor 6/2 + ENTP + 7w8 + Gate 42 faltante validado 8/8 com nuances próprias (ciclo 5-7 dias não 14, hiperfoco estendido, mente domina corpo, ambiente > disciplina). Antigravity tinha inventado nomes da família, cidade, "Melhor Amigo" — corrigido. Vault inteiro adaptado: 9 áreas pessoais com filtro Projetor, blind-spot #1 agora é Gate 42 em monetização, CLAUDE.md com 3 comportamentos reflexos encodados (busca + registro + log conversa).

Ajuste pendente: ainda falta consolidar Insights 7→3 e conectar 46 órfãos. Template de Diário adaptado (3 bullets + áudio) precisa ser criado.

**Aprendizado sobre como Nicholas opera:** Entrevista funcionou melhor que framework teórico. Perguntas de cenário (o que fez na escola, qual dopamina mais forte) revelaram verdade. Perguntas somáticas ("o que sente no corpo") travaram — regra operacional. Nicholas validou falando de casos concretos desde criança (futebol, Fonart, lição) — Gate 42 é código-fonte da vida dele, não framework bonito.

**Aprendizado sobre o Antigravity:** Ele inventa quando não sabe. "Melhor Amigo xNFJ/Projetor", "Luciana Maier" (mãe), "São Paulo" — tudo chute. Regra nova: sempre validar com Nicholas antes de amplificar conteúdo que não veio dele diretamente.

---

**2026-04-24 — Walk do vault (primeira curadoria interativa completa)**

Resultado: Criado comando `/walk` como método repetível de curadoria. Vault auditado: 227 arquivos ativos, 94 links legados corrigidos (via script Python reutilizável em `.claude/scripts/fix-legacy-links.py`), 3 duplicatas arquivadas, 5 outputs thinking-partner movidos pra `04 - Arquivo/`. Criadas 2 notas-guia: [[Obsidian + Claude Code - Thinking Partner]] (stack completa dos comandos) e [[Como usar o Obsidian]] (guia visual pra iniciante). `_INDEX.md` regenerado. Log de conversa salvo em [[2026-04-24 - walk do vault]].

**Aprendizados permanentes sobre como Nicholas quer trabalhar:**

1. **Vault é DELE.** Jarvis organiza como Nicholas organizaria — por isso SEMPRE começar lendo [[Perfil]] + [[Diagnóstico Real]] antes de qualquer ação de curadoria.
2. **Varredura por categoria, não por órfão.** Ordem fixa: 00-Pessoal → 01-Profissional → 02-Pesquisas → 03-Memoria IA → 04-Arquivo.
3. **Lotes de 2-5 perguntas por vez**, não 1 a 1 (economia de token). Nunca 10+ (sobrecarga).
4. **Adaptar > arquivar.** Quando um arquivo legado tem intent bom mas path velho, REESCREVER mantendo o costume. Não matar a identidade do vault.
5. **Outputs de ferramentas** (thinking-partner auto-gerados) vão pra `04 - Arquivo/Outputs Thinking Partner/`, não poluem Insights.
6. **Nicholas é iniciante em Obsidian.** Criar guias visuais simples quando perceber gap de conhecimento de ferramenta, não só de contexto.

**Caveman Mode ativado** via hook UserPromptSubmit (CLAUDE.md linhas 65-85). Default: telegráfico. Exceções: estratégia, debate, warning.

**Bugs factuais encontrados e corrigidos:**
- `Debate Rafael vs Afonso.md` dizia "R$1.500 + R$600-700 Unimasso" → Unimasso é do pai, corrigido
- `Pipeline.md` listava Unimasso como Ativo → removido
- `Perfil.md` tinha email duplicado → removido
- `Mapa do PC.md` apontava OneDrive e estrutura pré-master-kit → atualizado
- `Como trabalho com IA.md` apontava `+SOBRE MIM/+Quem sou eu.md` → reescrito

Ajuste: `/walk` agora é o método oficial de curadoria. Rodar a cada 30 dias ou quando `_INDEX` acumular ruído.

---
[[00 - Pessoal/Perfil]] | [[KERNEL]]
[2026-04-27_19-45] session ended
[2026-04-27_19-54] session ended
[2026-04-27_20-08] session ended
[2026-04-27_20-09] session ended
[2026-04-27_20-10] session ended
[2026-04-27_20-12] session ended
[2026-04-27_20-15] session ended
[2026-04-27_20-17] session ended
[2026-04-27_20-19] session ended
[2026-04-27_20-20] session ended
[2026-04-27_20-21] session ended
[2026-04-27_20-22] session ended
[2026-04-27_20-23] session ended
[2026-04-27_22-20] session ended
[2026-04-27_22-36] session ended
[2026-04-27_22-44] session ended
[2026-04-28_12-34] session ended
[2026-04-28_12-41] session ended
[2026-04-28_12-44] session ended
[2026-04-28_12-49] session ended
[2026-04-28_12-53] session ended
[2026-04-28_13-00] session ended
[2026-04-28_13-04] session ended
[2026-04-28_13-09] session ended
[2026-04-28_13-13] session ended
[2026-04-28_13-25] session ended
[2026-04-28_13-25] session ended
[2026-04-28_13-27] session ended
[2026-04-28_13-28] session ended
[2026-04-28_13-28] session ended
[2026-04-28_13-31] session ended
[2026-04-28_13-32] session ended
[2026-04-28_13-32] session ended
[2026-04-28_13-34] session ended
[2026-04-28_13-35] session ended
[2026-04-28_13-35] session ended
[2026-04-28_13-36] session ended
[2026-04-28_13-37] session ended
[2026-04-28_13-38] session ended
[2026-04-28_13-38] session ended
[2026-04-28_13-40] session ended
[2026-04-28_13-41] session ended
[2026-04-28_13-41] session ended
[2026-04-28_13-42] session ended
[2026-04-28_13-43] session ended
[2026-04-28_13-44] session ended
[2026-04-28_13-44] session ended
[2026-04-28_13-45] session ended
[2026-04-28_13-45] session ended
[2026-04-28_13-46] session ended
[2026-04-28_13-46] session ended
[2026-04-28_13-47] session ended
[2026-04-28_13-47] session ended
[2026-04-28_13-48] session ended
[2026-04-28_13-48] session ended
[2026-04-28_13-50] session ended
[2026-04-28_13-51] session ended
[2026-04-28_13-51] session ended
[2026-04-28_13-52] session ended
[2026-04-28_13-52] session ended
[2026-04-28_13-54] session ended
[2026-04-28_13-55] session ended
[2026-04-28_13-56] session ended
[2026-04-28_13-56] session ended
[2026-04-28_14-00] session ended
[2026-04-28_14-00] session ended
[2026-04-28_14-01] session ended
[2026-04-28_14-01] session ended
[2026-04-28_14-02] session ended
[2026-04-28_14-03] session ended
[2026-04-28_14-03] session ended
[2026-04-28_14-03] session ended
[2026-04-28_14-04] session ended
[2026-04-28_14-05] session ended
[2026-04-28_14-05] session ended
[2026-04-28_14-06] session ended
[2026-04-28_14-10] session ended
[2026-04-28_14-11] session ended
[2026-04-28_14-12] session ended
[2026-04-28_14-13] session ended
[2026-04-28_14-14] session ended
[2026-04-28_14-14] session ended
[2026-04-28_14-15] session ended
[2026-04-28_14-16] session ended
[2026-04-28_14-16] session ended
[2026-04-28_14-17] session ended
[2026-04-28_14-18] session ended
[2026-04-28_14-19] session ended
[2026-04-28_14-20] session ended
[2026-04-28_14-20] session ended
[2026-04-28_14-21] session ended
[2026-04-28_14-22] session ended
[2026-04-28_14-22] session ended
[2026-04-28_14-24] session ended
[2026-04-28_14-25] session ended
[2026-04-28_14-25] session ended
[2026-04-28_14-25] session ended
[2026-04-28_14-26] session ended
[2026-04-28_14-26] session ended
[2026-04-28_14-27] session ended
[2026-04-28_14-28] session ended
[2026-04-28_14-28] session ended
[2026-04-28_14-29] session ended
[2026-04-28_14-29] session ended
[2026-04-28_14-30] session ended
[2026-04-28_14-31] session ended
[2026-04-28_14-32] session ended
[2026-04-28_14-32] session ended
[2026-04-28_14-33] session ended
[2026-04-28_14-33] session ended
[2026-04-28_14-34] session ended
[2026-04-28_14-35] session ended
[2026-04-28_14-35] session ended
[2026-04-28_14-35] session ended
[2026-04-28_14-36] session ended
[2026-04-28_14-37] session ended
[2026-04-28_14-37] session ended
[2026-04-28_14-37] session ended
[2026-04-28_14-38] session ended
[2026-04-28_14-39] session ended
[2026-04-28_14-39] session ended
[2026-04-28_14-40] session ended
[2026-04-28_14-40] session ended
[2026-04-28_14-40] session ended
[2026-04-28_14-41] session ended
[2026-04-28_14-42] session ended
[2026-04-28_14-43] session ended
[2026-04-28_14-44] session ended
[2026-04-28_14-45] session ended
[2026-04-28_14-48] session ended
[2026-04-28_14-49] session ended
[2026-04-28_14-52] session ended
[2026-04-28_14-53] session ended
[2026-04-28_14-55] session ended
[2026-04-28_14-58] session ended
[2026-04-28_15-00] session ended
[2026-04-28_15-01] session ended
[2026-04-28_15-02] session ended
[2026-04-28_15-09] session ended
[2026-04-28_15-14] session ended
[2026-04-28_15-55] session ended
[2026-04-28_15-56] session ended
[2026-04-28_15-58] session ended
[2026-04-28_16-29] session ended
[2026-04-28_16-30] session ended
[2026-04-28_16-32] session ended
[2026-04-28_16-33] session ended
[2026-04-28_16-34] session ended
[2026-04-28_16-37] session ended
[2026-04-28_16-38] session ended
[2026-04-28_16-39] session ended
[2026-04-28_16-40] session ended
[2026-04-28_16-44] session ended
[2026-04-28_16-45] session ended
[2026-04-28_16-47] session ended
[2026-04-28_16-48] session ended
[2026-04-28_16-49] session ended
[2026-04-28_16-50] session ended
[2026-04-28_16-51] session ended
[2026-04-28_16-52] session ended
[2026-04-28_16-52] session ended
[2026-04-28_16-53] session ended
[2026-04-28_16-54] session ended
[2026-04-28_16-54] session ended
[2026-04-28_16-55] session ended
[2026-04-28_16-56] session ended
[2026-04-28_16-56] session ended
[2026-04-28_16-56] session ended
[2026-04-28_16-56] session ended
[2026-04-28_16-57] session ended
[2026-04-28_16-58] session ended
[2026-04-28_16-58] session ended
[2026-04-28_16-59] session ended
[2026-04-28_16-59] session ended
[2026-04-28_17-00] session ended
[2026-04-28_17-00] session ended
[2026-04-28_17-01] session ended
[2026-04-28_17-02] session ended
[2026-04-28_17-02] session ended
[2026-04-28_17-03] session ended
[2026-04-28_17-04] session ended
[2026-04-28_17-04] session ended
[2026-04-28_17-05] session ended
[2026-04-28_17-05] session ended
[2026-04-28_17-06] session ended
[2026-04-28_17-08] session ended
[2026-04-28_17-09] session ended
[2026-04-28_17-11] session ended
[2026-04-28_17-11] session ended
[2026-04-28_17-12] session ended
[2026-04-28_17-12] session ended
[2026-04-28_17-12] session ended
[2026-04-28_17-13] session ended
[2026-04-28_17-14] session ended
[2026-04-28_17-18] session ended
[2026-04-28_17-20] session ended
[2026-04-28_17-21] session ended
[2026-04-28_17-22] session ended
[2026-04-28_17-22] session ended
[2026-04-28_17-37] session ended
[2026-04-28_17-38] session ended
[2026-04-28_17-39] session ended
[2026-04-28_17-39] session ended
[2026-04-28_17-39] session ended
[2026-04-28_17-40] session ended
[2026-04-28_17-45] session ended
[2026-04-28_17-45] session ended
[2026-04-28_17-47] session ended
[2026-04-28_17-48] session ended
[2026-04-28_17-49] session ended
[2026-04-28_17-49] session ended
[2026-04-28_17-49] session ended
[2026-04-28_17-51] session ended
[2026-04-28_17-53] session ended
[2026-04-28_17-55] session ended
[2026-04-28_17-58] session ended
[2026-04-28_18-26] session ended
[2026-04-28_18-28] session ended
[2026-04-28_18-29] session ended
[2026-04-28_18-30] session ended
[2026-04-28_18-31] session ended
[2026-04-28_18-33] session ended
[2026-04-28_18-34] session ended
[2026-04-28_18-35] session ended
[2026-04-28_18-36] session ended
[2026-04-28_18-36] session ended
[2026-04-28_18-37] session ended
[2026-04-28_18-37] session ended
[2026-04-28_18-37] session ended
[2026-04-28_18-38] session ended
[2026-04-28_18-38] session ended
[2026-04-28_18-38] session ended
[2026-04-28_18-39] session ended
[2026-04-28_18-40] session ended
[2026-04-28_18-40] session ended
[2026-04-28_18-41] session ended
[2026-04-28_18-44] session ended
[2026-04-28_18-44] session ended
[2026-04-28_18-49] session ended
[2026-04-28_18-58] session ended
[2026-04-28_19-00] session ended
[2026-04-28_19-03] session ended
[2026-04-28_19-03] session ended
[2026-04-28_19-05] session ended
[2026-04-28_19-05] session ended
[2026-04-28_19-06] session ended
[2026-04-28_19-07] session ended
[2026-04-28_19-10] session ended
[2026-04-28_19-11] session ended
[2026-04-28_19-12] session ended
[2026-04-28_21-53] session ended
[2026-04-28_21-53] session ended
[2026-04-28_21-54] session ended
[2026-04-28_21-56] session ended
[2026-04-28_22-00] session ended
[2026-04-28_22-01] session ended
[2026-04-28_22-01] session ended
[2026-04-28_22-19] session ended
[2026-04-28_22-21] session ended
[2026-04-28_22-22] session ended
[2026-04-28_22-27] session ended
[2026-04-28_22-29] session ended
[2026-04-28_22-29] session ended
[2026-04-28_23-15] session ended
[2026-04-28_23-15] session ended
[2026-04-29_00-21] session ended
[2026-04-29_00-23] session ended
[2026-04-29_00-23] session ended
[2026-04-29_00-25] session ended
[2026-04-29_00-27] session ended
[2026-04-29_00-30] session ended
[2026-04-29_00-31] session ended
[2026-04-29_00-32] session ended
[2026-04-29_00-34] session ended
[2026-04-29_00-35] session ended
[2026-04-29_00-36] session ended
[2026-04-29_00-41] session ended
[2026-04-29_00-44] session ended
[2026-04-29_00-47] session ended
[2026-04-29_00-50] session ended
[2026-04-29_00-55] session ended
[2026-04-29_00-59] session ended
[2026-04-29_01-00] session ended
[2026-04-29_01-01] session ended
[2026-04-29_01-04] session ended
[2026-04-29_01-09] session ended
[2026-04-29_01-12] session ended
[2026-04-29_01-14] session ended
[2026-04-29_01-15] session ended
[2026-04-29_01-18] session ended
[2026-04-29_01-18] session ended
[2026-04-29_01-20] session ended
[2026-04-29_01-21] session ended
[2026-04-29_01-22] session ended
[2026-04-29_01-35] session ended
[2026-04-29_01-37] session ended
[2026-04-29_02-02] session ended
[2026-04-29_02-06] session ended
[2026-04-29_02-10] session ended
[2026-04-29_02-12] session ended
[2026-04-29_02-17] session ended
[2026-04-29_02-22] session ended
[2026-04-29_02-23] session ended
[2026-04-29_02-24] session ended
[2026-04-29_02-24] session ended
[2026-04-29_02-29] session ended
[2026-04-29_02-31] session ended
[2026-04-29_02-32] session ended
[2026-04-29_02-34] session ended
[2026-04-29_02-38] session ended
[2026-04-29_02-39] session ended
[2026-04-29_02-39] session ended
[2026-04-29_02-39] session ended
[2026-04-29_02-42] session ended
[2026-04-29_02-43] session ended
[2026-04-29_02-43] session ended
[2026-04-29_02-45] session ended
[2026-04-29_02-46] session ended
[2026-04-29_02-47] session ended
[2026-04-29_02-49] session ended
[2026-04-29_02-50] session ended
[2026-04-29_02-51] session ended
[2026-04-29_02-53] session ended
[2026-04-29_02-54] session ended
[2026-04-29_02-55] session ended
[2026-04-29_02-55] session ended
[2026-04-29_02-56] session ended
[2026-04-29_02-57] session ended
[2026-04-29_11-42] session ended
[2026-04-29_11-54] session ended
[2026-04-29_11-58] session ended
[2026-04-29_12-00] session ended
[2026-04-29_12-02] session ended
[2026-04-29_12-05] session ended
[2026-04-29_12-07] session ended
[2026-04-29_12-08] session ended
[2026-04-29_12-10] session ended
[2026-04-29_12-11] session ended
[2026-04-29_12-13] session ended
[2026-04-29_12-14] session ended
[2026-04-29_12-15] session ended
[2026-04-29_12-16] session ended
[2026-04-29_12-17] session ended
[2026-04-29_12-20] session ended
[2026-04-29_12-24] session ended
[2026-04-29_12-27] session ended
[2026-04-29_12-30] session ended
[2026-04-29_12-31] session ended
[2026-04-29_12-32] session ended
[2026-04-29_12-32] session ended
[2026-04-29_12-35] session ended
[2026-04-29_12-35] session ended
[2026-04-29_12-38] session ended
[2026-04-29_12-39] session ended
[2026-04-29_12-40] session ended
[2026-04-29_12-42] session ended
[2026-04-29_12-43] session ended
[2026-04-29_12-45] session ended
[2026-04-29_12-47] session ended
[2026-04-29_12-53] session ended
[2026-04-29_12-56] session ended
[2026-04-29_12-57] session ended
[2026-04-29_12-59] session ended
[2026-04-29_13-00] session ended
[2026-04-29_13-01] session ended
[2026-04-29_13-04] session ended
[2026-04-29_13-05] session ended
[2026-04-29_13-08] session ended
[2026-04-29_13-09] session ended
[2026-04-29_13-10] session ended
[2026-04-29_13-10] session ended
[2026-04-29_13-11] session ended
[2026-04-29_13-12] session ended
[2026-04-29_13-14] session ended
[2026-04-29_13-16] session ended
[2026-04-29_13-16] session ended
[2026-04-29_13-17] session ended
[2026-04-29_13-17] session ended
[2026-04-29_13-18] session ended
[2026-04-29_13-19] session ended
[2026-04-29_13-31] session ended
[2026-04-29_13-31] session ended
[2026-04-29_13-32] session ended
[2026-04-29_13-33] session ended
[2026-04-29_13-36] session ended
[2026-04-29_13-44] session ended
[2026-04-29_13-45] session ended
[2026-04-29_13-47] session ended
[2026-04-29_14-03] session ended
[2026-04-29_14-06] session ended
[2026-04-29_14-20] session ended
[2026-04-29_14-22] session ended
[2026-04-29_15-53] session ended
[2026-04-29_16-20] session ended
[2026-04-29_16-22] session ended
[2026-04-29_16-24] session ended
[2026-04-29_16-25] session ended
[2026-04-29_16-25] session ended
[2026-04-29_16-26] session ended
[2026-04-29_16-26] session ended
[2026-04-29_16-27] session ended
[2026-04-29_16-27] session ended
[2026-04-29_16-27] session ended
[2026-04-29_16-29] session ended
[2026-04-29_16-29] session ended
[2026-04-29_16-29] session ended
[2026-04-29_16-30] session ended
[2026-04-29_16-30] session ended
[2026-04-29_16-30] session ended
[2026-04-29_16-31] session ended
[2026-04-29_16-31] session ended
[2026-04-29_16-32] session ended
[2026-04-29_16-32] session ended
[2026-04-29_16-33] session ended
[2026-04-29_16-33] session ended
[2026-04-29_16-33] session ended
[2026-04-29_16-33] session ended
[2026-04-29_16-33] session ended
[2026-04-29_16-34] session ended
[2026-04-29_16-34] session ended
[2026-04-29_16-35] session ended
[2026-04-29_16-35] session ended
[2026-04-29_16-36] session ended
[2026-04-29_16-36] session ended
[2026-04-29_16-36] session ended
[2026-04-29_16-36] session ended
[2026-04-29_16-37] session ended
[2026-04-29_16-37] session ended
[2026-04-29_16-37] session ended
[2026-04-29_16-37] session ended
[2026-04-29_16-38] session ended
[2026-04-29_16-38] session ended
[2026-04-29_16-39] session ended
[2026-04-29_16-40] session ended
[2026-04-29_16-40] session ended
[2026-04-29_16-41] session ended
[2026-04-29_16-42] session ended
[2026-04-29_16-42] session ended
[2026-04-29_16-43] session ended
[2026-04-29_16-43] session ended
[2026-04-29_16-44] session ended
[2026-04-29_16-45] session ended
[2026-04-29_16-45] session ended
[2026-04-29_16-46] session ended
[2026-04-29_16-47] session ended
[2026-04-29_16-48] session ended
[2026-04-29_16-50] session ended
[2026-04-29_16-50] session ended
[2026-04-29_17-36] session ended
[2026-04-29_17-36] session ended
[2026-04-29_17-37] session ended
[2026-04-29_17-37] session ended
[2026-04-29_17-38] session ended
[2026-04-29_17-39] session ended
[2026-04-29_17-39] session ended
[2026-04-29_17-39] session ended
[2026-04-29_17-40] session ended
[2026-04-29_17-40] session ended
[2026-04-29_17-40] session ended
[2026-04-29_17-41] session ended
[2026-04-29_17-41] session ended
[2026-04-29_17-42] session ended
[2026-04-29_17-42] session ended
[2026-04-29_17-44] session ended
[2026-04-29_17-44] session ended
[2026-04-29_17-45] session ended
[2026-04-29_17-46] session ended
[2026-04-29_17-47] session ended
[2026-04-29_17-48] session ended
[2026-04-29_17-49] session ended
[2026-04-29_17-49] session ended
[2026-04-29_17-50] session ended
[2026-04-29_17-52] session ended
[2026-04-29_17-53] session ended
[2026-04-29_17-54] session ended
[2026-04-29_17-55] session ended
[2026-04-29_17-57] session ended
[2026-04-29_17-59] session ended
[2026-04-29_18-01] session ended
[2026-04-29_18-01] session ended
[2026-04-29_18-02] session ended
[2026-04-29_18-02] session ended
[2026-04-29_18-02] session ended
[2026-04-29_18-03] session ended
[2026-04-29_18-03] session ended
[2026-04-29_18-05] session ended
[2026-04-29_18-06] session ended
[2026-04-29_18-07] session ended
[2026-04-29_18-07] session ended
[2026-04-29_18-08] session ended
[2026-04-29_18-09] session ended
[2026-04-29_18-11] session ended
[2026-04-29_18-12] session ended
[2026-04-29_18-13] session ended
[2026-04-29_18-16] session ended
[2026-04-29_18-17] session ended
[2026-04-29_18-18] session ended
[2026-04-29_18-18] session ended
[2026-04-29_18-18] session ended
[2026-04-29_18-21] session ended
[2026-04-29_18-22] session ended
[2026-04-29_19-05] session ended
[2026-04-29_19-06] session ended
[2026-04-29_19-33] session ended
[2026-04-29_19-34] session ended
[2026-04-29_19-35] session ended
[2026-04-29_19-37] session ended
[2026-04-29_19-38] session ended
[2026-04-29_19-40] session ended
[2026-04-29_20-21] session ended
[2026-04-29_20-23] session ended
[2026-04-29_20-40] session ended
[2026-04-29_20-52] session ended
[2026-04-29_20-57] session ended
[2026-04-29_20-58] session ended
[2026-04-29_21-03] session ended
[2026-04-29_21-05] session ended
[2026-04-29_21-29] session ended
[2026-04-29_21-30] session ended
[2026-04-29_21-31] session ended
[2026-04-29_21-32] session ended
[2026-04-29_21-33] session ended
[2026-04-29_21-34] session ended
[2026-04-29_21-34] session ended
[2026-04-29_21-42] session ended
[2026-04-29_21-44] session ended
[2026-04-29_21-51] session ended
[2026-04-29_21-53] session ended
[2026-04-29_21-57] session ended
[2026-04-29_22-02] session ended
[2026-04-29_22-05] session ended
[2026-04-29_22-11] session ended
[2026-04-29_22-30] session ended
[2026-04-30_00-50] session ended
[2026-04-30_00-54] session ended
[2026-04-30_01-32] session ended
[2026-04-30_01-34] session ended
[2026-04-30_01-35] session ended
[2026-04-30_01-37] session ended
[2026-04-30_01-43] session ended
[2026-04-30_11-48] session ended
[2026-04-30_12-08] session ended
[2026-04-30_12-13] session ended
[2026-04-30_12-15] session ended
[2026-04-30_12-20] session ended
[2026-04-30_12-23] session ended
[2026-04-30_12-28] session ended
[2026-04-30_12-30] session ended
[2026-04-30_12-30] session ended
[2026-04-30_12-31] session ended
[2026-04-30_12-34] session ended
[2026-04-30_12-35] session ended
[2026-04-30_12-36] session ended
[2026-04-30_12-37] session ended
[2026-04-30_12-41] session ended
[2026-04-30_12-42] session ended
[2026-04-30_12-45] session ended
[2026-04-30_12-47] session ended
[2026-04-30_12-49] session ended
[2026-04-30_12-50] session ended
[2026-04-30_12-57] session ended
[2026-04-30_12-58] session ended
[2026-04-30_12-59] session ended
[2026-04-30_13-03] session ended
[2026-04-30_13-05] session ended
[2026-04-30_13-07] session ended
[2026-04-30_13-08] session ended
[2026-04-30_13-11] session ended
[2026-04-30_13-14] session ended
[2026-04-30_13-14] session ended
[2026-04-30_13-14] session ended
[2026-04-30_13-15] session ended
[2026-04-30_13-19] session ended
[2026-04-30_13-19] session ended
[2026-04-30_13-20] session ended
[2026-04-30_13-20] session ended
[2026-04-30_13-21] session ended
[2026-04-30_13-21] session ended
[2026-04-30_13-22] session ended
[2026-04-30_13-23] session ended
[2026-04-30_13-23] session ended
[2026-04-30_13-25] session ended
[2026-04-30_13-26] session ended
[2026-04-30_13-28] session ended
[2026-04-30_13-28] session ended
[2026-04-30_13-28] session ended
[2026-04-30_13-29] session ended
[2026-04-30_13-29] session ended
[2026-04-30_13-31] session ended
[2026-04-30_13-31] session ended
[2026-04-30_13-33] session ended
[2026-04-30_13-33] session ended
[2026-04-30_13-35] session ended
