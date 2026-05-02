---
created: 2026-04-27
updated: 2026-04-27
type: conhecimento
status: ativo
area: profissional
tags: [afonso-lopes, youtube, crm, sistema, produto, aprendizado]
---

# Afonso Lopes — Ensinamentos YouTube

> Registro acumulativo de insights extraídos dos vídeos do canal do Afonso Lopes.
> Cada entrada = 1 vídeo. Adicionar na ordem que assistir.

---

## Sobre Afonso Lopes

- **Posicionamento:** Criador de sistemas com Claude Code / no-code → vende como produto recorrente
- **Modelo de negócio:** CRM vertical (nicho específico) + setup + mensalidade
- **Princípio central:** "Específico demais pra comparar" — sem competição por preço
- **Público-alvo dos sistemas:** Clínicas, estética, salões, advocacia, barbearia
- **Replicabilidade:** Sistema construído uma vez → vendido para múltiplos clientes do mesmo nicho

---

## Vídeos

---

### 2026-04-26 — CHOCANTE! Criei um CRM profissional com CLAUDE CODE em menos de 1 HORA
> URL: https://www.youtube.com/watch?v=g9Mhkda65ic
> Tema: CRM vertical para clínica de estética — construção, funcionalidades e modelo de venda

#### Funcionalidades do CRM demonstrado
- **Login + Dashboard** — faturamento, agendamentos, gráficos por período
- **Clientes** — cadastro completo + ficha clínica (alergias, tipo de pele, gestante, medicamentos, restrições)
- **Histórico de atendimentos** — cada cliente tem registro de todos os procedimentos, profissional, valor e data
- **Profissionais** — cadastro com dias e horários individuais por profissional → agenda gerada automaticamente
- **Agendamentos** — bloqueio automático de horários fora do expediente do profissional, sem conflito
- **Serviços** — categorias + variações de preço por tipo (ex: limpeza facial R$250 vs corporal R$400)
- **Dashboard gerencial** — receita por categoria, agendamentos por profissional, clientes novos vs recorrentes, variação diária

#### Modelo de negócio (valores benchmark)
| Item | Valor |
|------|-------|
| Setup (implementação) | R$800 – R$1.500 |
| Mensalidade | R$200 – R$400/mês |
| 5 clínicas | R$1k – R$2k/mês recorrente |
| 10 clínicas | R$2k – R$4k/mês recorrente |
| 20 clínicas | R$4k – R$8k/mês recorrente |

Setup inclui: configuração inicial + cadastro de serviços + **treinamento da equipe** (secretária) + personalização básica.

#### Frameworks / Modelos mentais

**"Você não vende tecnologia — vende organização, controle e tranquilidade"**
→ Reframing de valor. Não compete com SaaS genérico. Compete com planilha + caderno + WhatsApp.

**CRM Vertical > CRM Genérico**
→ Genérico resolve tudo mais ou menos. Vertical resolve UM problema com precisão.
→ Cliente sente que "foi feito para ela" → justifica preço maior + elimina comparação.
→ Sem guerra de preço. Valor definido pela dor resolvida, não pelo concorrente.

**Replicabilidade = ativo, não hora**
→ Trabalho pesado feito 1 vez. Nova clínica = configurar serviços + personalizar visual + colocar no ar.
→ Carteira cresce sem esforço de entrega crescer na mesma proporção = margem aumenta.

**CRM é porta de entrada, não produto final**
→ Depois de ganhar confiança: oferecer agente WhatsApp, reativação de inativos, agendamento automático.
→ Receita por cliente: R$300/mês (só CRM) → R$800-1.000/mês (CRM + agente IA).

**Mercado: 1 milhão+ estabelecimentos, poucos fornecedores verticais**
→ Maioria usa sistema genérico com 2 funcionalidades de 300.
→ Menos concorrência direta = mais fácil posicionar como referência no nicho.

#### Processo de criação (método dele)
- Cria por etapas: 1) banco de dados → 2) autenticação → 3) layout/design → 4+ funcionalidades
- Testa cada etapa antes de avançar
- Documentação = prompts organizados por etapa
- Ferramenta: **Claude Code** (sem escrever linha de código, só prompt)
- Hospedagem barata (Vercel + GitHub gratuito para começar, mas recomenda pago ao vender)

#### Aplicar no Jarvis / projetos
- **Unimasso** = exatamente esse modelo → CRM vertical para massoterapeutas → R$400-800/mês por cliente
- Setup Unimasso incluir treinamento → aumenta valor percebido sem custo extra
- Após CRM Unimasso estabilizar → oferecer Lara (agente WhatsApp) como upsell natural
- Replicar estrutura: massoterapeuta 1 = trabalho pesado → massoterapeuta 2+ = só configurar
- Nicho estética tem dor real documentada: planilha + caderno + WhatsApp ainda dominam

---

### 2026-04-27 — Criei um AGENTE de IA no Whatsapp para CLINICAS: atende, agenda e faz follow-up
> URL: https://www.youtube.com/watch?v=sCEIyXbo9PY
> Tema: Agente IA WhatsApp para clínica de cirurgia plástica — ecossistema N8N + Claude Code + Chatwoot + Supabase

#### Stack do sistema completo
- **N8N** — agente IA + 3 flows de follow-up (20min, 24h, 36h)
- **Chatwoot** — CRM WhatsApp centralizado para secretária + dono visualizarem atendimento em tempo real
- **Claude Code** — frontend/dashboard + CRM com kanban
- **Supabase** — banco de dados (conta gratuita)
- **WaAPI** (R$29/mês) — API não-oficial WhatsApp. **NÃO usar Evolution API** — dá muito problema
- **Google Calendar** — agenda integrada (agente agenda diretamente)

#### Funcionalidades do ecossistema
- **Agente humanizado** — simula secretária real, sem cara de chatbot
- **Interpreta áudio** — transcreve e responde áudio no WhatsApp
- **Qualificação de lead** — pergunta se é paciente novo/antigo (apenas uma vez — tem contexto de conversa)
- **Quebra de objeção** — "está caro" → agente argumenta valor e faz CTA
- **Agendamento direto no Google Calendar** — verifica horários disponíveis, respeita expediente, sugere alternativas
- **Envio de link Google Meet + instrução de pagamento PIX** — automático ao agendar
- **Follow-up automático** — 3 níveis: 20min, 24h, 36h sem resposta → kanban atualiza automaticamente
- **Etiqueta "humano" no Chatwoot** — quando assunto é delicado (efeitos colaterais, dores), agente para e secretária assume
- **Dashboard em tempo real** — contatos hoje, consultas agendadas, taxa de conversão, horários de pico, lides fora do expediente
- **Comparativo mensal** — mês atual vs anterior, dias da semana com mais movimento

#### Modelo de negócio (nicho cirurgia plástica = ticket alto)
| Item | Valor |
|------|-------|
| Setup | R$5.000 |
| Mensalidade (até 1.000 leads/mês) | R$1.500/mês |
| Contrato mínimo | 6 meses |
| 5 clínicas | R$7.500/mês recorrente |
| 10 clínicas | R$15.000/mês recorrente |

**Por que cobrar mais:** médico já investe pesado em tráfego pago → mentalidade de investimento já formada. Nicho premium = preço premium.

#### Frameworks / Modelos mentais

**Agente = prova de ROI automática**
→ Dashboard mostra "27 leads atendidos fora do expediente" → dono vê na tela o que perderia sem o agente
→ Você entra como parceiro estratégico, não como fornecedor de software

**Lock-in pelo dado**
→ Dados de atendimento ficam no sistema → cliente dificilmente sai → churn baixíssimo

**Nicho premium = abertura para preço premium**
→ Cirurgia plástica: procedimento mínimo R$10k → R$1.500/mês de recorrência é insignificante pro médico

**CRM é porta de entrada (confirmado novamente)**
→ Ordem natural: CRM básico → agente WhatsApp → pacote completo → mais caro, mais preso

#### Aplicar no Jarvis / projetos
- **Lara Comercial 2** = exatamente esse modelo — agente humanizado + follow-up + qualificação
- Stack confirmada: N8N + Evolution API (mas Afonso usa WaAPI — considerar trocar se der problema)
- Chatwoot já está na stack do Jarvis → usar como ele usa: supervisão em tempo real + etiqueta humano
- Dashboard integrado = upsell natural após estabilizar agente básico
- Follow-up 3 níveis (20min/24h/36h) → implementar na Lara se ainda não tem
- **Nunca usar Evolution API segundo Afonso** — WaAPI R$29/mês como alternativa

---

---
[[02 - Pesquisas e Estudos/Ativas/Experts/Afonso Lopes/Protocolo CRM Clínica Estética]] | [[01 - Profissional/Areas/Negocios]] | [[01 - Profissional/Projetos/Lara Comercial/instrucoes-ia]]

<!-- Template para novos vídeos:

### YYYY-MM-DD — [Título do Vídeo]
> URL: 
> Tema: 

#### Principais ensinamentos
- 

#### Frameworks / Modelos mentais
- 

#### O que aplicar no Jarvis / projetos
- 

---
-->

