---
assunto: Escritório Virtual de Agentes de IA com Claude Code
data: 2026-05-01
status: staging
fontes:
  - https://www.youtube.com/watch?v=4uGQMkiWzMc
conflito: verificar
tags: [claude-code, multiagentes, escritório-virtual, monetização, obsidian, nano-banana]
---

# Escritório Virtual de Agentes de IA com Claude Code

## Síntese

**O que é:** Dashboard visual (web app local) que representa múltiplos agentes de Claude Code como "funcionários" com avatars/animações. Cada agente = instância separada de Claude Code com seu próprio workspace/VAULT. O app chama-se "Pixel Agents" — feito via vibe coding, sem programar.

**Como funciona:** Cada agente tem uma pasta de vault (Obsidian) onde armazena memória, briefings e outputs em markdown. Agentes comunicam entre si escrevendo/lendo arquivos no vault do outro. Um "CEO agent" pode contratar e demitir outros agentes (cria novos prompts/instâncias). O dashboard mostra quem está trabalhando, histórico de contratações, kanban de tarefas, docs/sumários.

**5 agentes padrão mostrados:**
- **Criativos** — extrai brand de imagens de referência, gera imagens via nano-banana, segue guia de marca
- **Landing Pages** — cria quizzes/LPs, extrai branding do Obsidian, sobe localmente para teste
- **Campanhas** — analisa biblioteca de anúncios Meta (URL → extrai criativos, copies, LPs, competitive analysis completa)
- **Proposta** — recebe transcrição de reunião → gera proposta comercial completa com site HTML
- **Suporte** — integra WhatsApp para atender leads sem resposta

**Fluxo de trabalho demo (ao vivo):**
1. CEO preenche onboarding via outro Claude Code que já tem contexto do dono
2. Criativo agent extrai 9 imagens de referência → gera brand guide .md
3. Copy agent raspa landing page do produto → escreve 5 copies para criativos estáticos
4. Copy passa briefing para Criativo via vault → Criativo gera 5 imagens com nano-banana
5. Campanhas agent recebe URL da biblioteca de anúncios → entrega: 79 ads analisados, deep dive de 5, criativos baixados, estratégia de campanha
6. Proposta agent recebe transcrição → gera proposta + site HTML com brand

**Skills/tools usados pelos agentes:**
- nano-banana (geração de imagens)
- Kling AI (animação de vídeos — via API token)
- Meta Ads Library (acesso via browser/MCP)
- Obsidian como vault/memória persistente
- MCP para browser

## Aplicações práticas

**Para Nicholas diretamente:**
- Modelo de monetização validado: R$15k–60k implementação + R$3k/mês manutenção
- Agente de campanhas que analisa biblioteca Meta é imediatamente útil para Holos/clientes
- CEO agent que auto-contrata é padrão que Jarvis já usa — validação do approach
- Quiz + LP gerado em minutos via agente = direto aplicável no Mapa da Alma / Holos

**Para vender como produto:**
- Nichos compradores validados: e-commerce, agências, infoprodutores
- Pitch: "economizar 4 funcionários por R$15k" — empresário paga sem questionar
- Um-shot prompt = produto escalável (cliente copia e personaliza)

## Fontes principais

- [Live completa (2h11)](https://www.youtube.com/watch?v=4uGQMkiWzMc) — demonstração ao vivo, código do Pixel Agents prometido como open source para membros da Coda
- Canal: MGTInc | AI Economy (Marcelo) — [@mgtincexe](http://www.youtube.com/@mgtincexe)
- Comunidade Coda: comunidadecoda.com (plataforma Gather + Claude Code + Obsidian)

## YouTube relevante

- [Este vídeo](https://www.youtube.com/watch?v=4uGQMkiWzMc) — é a fonte primária, live de 2h com demo completa

## ⚠️ Conflitos detectados

**conflito: verificar** — pontos de atenção:

1. **Obsidian como vault de agentes** — Nicholas já usa Obsidian como vault do Jarvis. Compatível. Porém Marcelo usa Obsidian local como memória por agente (pasta separada por funcionário). Verificar se Nicholas quer esse pattern vs. vault centralizado.

2. **nano-banana** — skill já listada no Jarvis. Compatível.

3. **WhatsApp integration** — Marcelo usa "API direta do WhatsApp". Nicholas usa Evolution API + Chatwoot. Abordagem diferente mas objetivo igual. Sem conflito real.

4. **"Escritório virtual" overlap com Jarvis** — o que Marcelo chama de "escritório virtual" é exatamente o que Nicholas está construindo com Jarvis. Diferença: Marcelo foca em UI visual (avatar de funcionários), Nicholas foca em orquestração via CLAUDE.md + squads. Ambos usam Obsidian + Claude Code.

5. **CEO agent auto-hiring** — pattern idêntico ao jarvis-ceo que já existe no vault. Validação externa.

## Próximo passo sugerido

- Arquivos de destino no vault: `01 - Profissional/Areas/Estrategia/` (modelo de monetização) + `03 - Memoria da IA/Agentes/` (padrões de arquitetura)
- Ação imediata de alto valor: implementar o agente de campanhas (análise Meta Ads Library) para uso próprio no Holos/Lara
- Considerar: pegar o código do Pixel Agents (GitHub do Marcelo) para adaptar dashboard visual
