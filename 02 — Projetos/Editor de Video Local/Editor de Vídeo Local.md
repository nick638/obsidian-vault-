---
created: 2026-04-12
updated: 2026-04-26
type: arquitetura
status: ativo
tags: [video, remotion, ia, automacao, local]
---

# Editor de Vídeo Local — Claude + Remotion

> Substituição do Lovable para UI/Vídeo. Arquitetura 100% local, orquestrada por Claude Code.

## 1. Arquitetura do Sistema
Sistema que substitui editores cloud (Opus Clip, Descript) gerando margem de 99% (Custo: ~$0.25/vídeo de 10 min).
- **Engine Visual:** Remotion 4.0 (Componentes React viram frames MP4).
- **Engine Analítica:** Claude API (Sonnet 4.6) analisa contexto + Whisper API extrai *timestamps* reais.
- **Engine Imagem:** NanoBanana (Google Imagen via Gemini API, ~R$0,20/img).

## 2. Schema de Comunicação (Literal)
JSON estruturado retornado pela Claude API para montagem no Remotion:
```json
{
  "cenas": [
    { "inicio": "00:00", "fim": "00:12", "descricao": "...", "prompt_imagem": "..." }
  ]
}
```

## 3. Comandos de Instalação (Remotion)
```bash
node -v
npm create video@latest
cd meu-video-editor
npm install
npx remotion dev
npx remotion render src/index.ts MinhaComposicao out/video.mp4
```

## 4. O Diferencial Competitivo
- Não há limite de minutos (Cloud).
- Não há dependência de internet para render.
- Claude Code escreve e altera as transições via CLI (ex: "adiciona transição fade entre as cenas").

Orquestrador → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Claude Code - Como Usar]] · Implementação real → [[Content Agent Holos/Content Agent Holos]]

---
