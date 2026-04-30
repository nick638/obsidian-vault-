---
created: 2026-04-29
type: heartbeat
---

# HEARTBEAT.md — Checklist Proativo

> Executado como cron `sessionTarget: isolated` a cada 4h.
> Máximo 2-4 itens por batida — custo controlado (Haiku).

## Checks (rotacionar, 2-4 por batida)

### 🔴 Gate 42 — fechamento forçado
- Algum projeto está nos 90% parado? → identificar e cobrar próximo step concreto
- Mapa da Alma: 1ª venda até 15/maio — qual o próximo passo **comercial** (não de build)?
- Lara Comercial 2: conversa com Elisangela aconteceu? Se não → lembrar Nicholas

### 🟡 Projetos ativos
- Revisar `shared/pending.md` — item novo ou expirado?
- Revisar `shared/project-state.md` — status mudou?
- Holos Natureza: tia Lu aprovou? Se não → quantos dias sem feedback?

### 📬 Notificações (quando canal configurado)
- Email urgente não lido?
- Evento no calendário nas próximas 2h?
- Última mensagem do Senhor foi há >8h → mandar sinal proativo

### 🛡️ Infra (1x/dia, batida matinal)
- `sudo ufw status` — firewall ativo?
- `docker ps` — todos serviços rodando?
- `openclaw cron list` — algum cron com erro?

## Regras de saída

**HEARTBEAT_OK** → nada urgente, tudo normal
**Mensagem pro Senhor** → só se: gate crítico detectado, serviço caído, email urgente, >8h sem contato

## Estado das últimas checagens
> Atualizar após cada batida

```json
{
  "lastChecks": {
    "gate42": null,
    "pending": null,
    "infra": null,
    "email": null
  }
}
```
