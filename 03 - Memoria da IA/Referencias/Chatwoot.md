---
created: 2026-04-13
updated: 2026-04-26
type: recurso
status: rascunho
prioridade: alta
quando_ler: "inbox WhatsApp Holos (Comercial 1/2/EAD), IDs que alimentam CRM_HOLOS, papel na arquitetura (Evolution→Chatwoot→N8N)"
tags: [recurso, tecnico, whatsapp, chatwoot]
---
# Chatwoot

> **A inbox que organiza o caos do WhatsApp.** Centraliza todas as conversas, gera os IDs que o N8N usa, e é onde a Lara Comercial 2 recebe e envia mensagens. Sem Chatwoot, o sistema não tem inbox estruturada.

---

## O que é

Plataforma open-source de atendimento ao cliente. É o "painel" que recebe as mensagens do WhatsApp (via Evolution API) e as encaminha para o N8N processar.

Sem o Chatwoot, as mensagens do WhatsApp chegam direto na Evolution API mas não têm organização por conversa, por inbox, por agente — e não têm os IDs que o CRM precisa para funcionar.

---

## Como se encaixa na arquitetura

```
WhatsApp do lead
      ↓
Evolution API (recebe a mensagem)
      ↓
Chatwoot (organiza por inbox, cria conversa, atribui IDs)
      ↓
N8N (webhook do Chatwoot → processa com IA)
      ↓
Resposta → Evolution API → WhatsApp do lead
```

---

## Por que o Chatwoot é crítico

- Gera os **IDs de conversa** que o CRM usa para rastrear cada lead
- Permite ter **múltiplas inboxes** (Comercial 1, Comercial 2, EAD) num único painel
- Guarda o **histórico de conversa** visível para humanos (Giovanna, tia)
- Permite que humanos **assumam a conversa** quando a IA não consegue resolver
- Os campos `IDConta`, `IDConversa`, `IDLead`, `InboxID` no `CRM_HOLOS` vêm daqui

---

## Inboxes ativas (Holos)

| Inbox | Número | Responsável | Função |
|-------|--------|-------------|--------|
| Comercial 1 | Número da equipe | Equipe da tia | Massoterapia + imersões |
| Comercial 2 | Número do disparo | Lara (IA) | Cursos livres + geral |
| EAD | Número do Nicolas | Nicolas | Testes apenas |

---

## Onde está hospedado

**EasyPanel** — mesma VPS Hetzner do N8N e Evolution API

---

## Configuração relevante

- Webhook configurado no Chatwoot → dispara para o N8N quando mensagem chega
- Token de autenticação necessário nos requests do N8N para Chatwoot
- Permite criar etiquetas por conversa (funil: novo → em_conversa → aula_agendada → matriculado)

---

## Para aprofundar

- [ ] Documentar credenciais e URL da instância
- [ ] Mapear todas as inboxes ativas (Holos + Unimasso)
- [ ] Documentar o webhook URL e configuração no N8N

---

Evolution API → [[03 - Memoria da IA/Referencias/Evolution API]] · N8N → [[03 - Memoria da IA/Referencias/N8N]] · CRM IDs → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] · Unimasso → [[01 - Profissional/Projetos/Unimasso/Unimasso]]

---
[[03 - Memoria da IA/Referencias/Evolution API]] | [[03 - Memoria da IA/Referencias/N8N]] | [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]]
