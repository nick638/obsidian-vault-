---
created: 2026-04-20
updated: 2026-04-26
type: recurso
status: ativo
prioridade: media
quando_ler: "stack frontend autônomo (Nano Banana Pro text-to-image, AOS/GSAP/Locomotive, WP Custom CPT mínimo), pipeline para vender site por R$3k-10k"
tags: [claude, nano-banana, sites, wp]
---

# Claude Code — Sites e Design

> Stack de Frontend autônomo. HTML/CSS estrutural + Geração Imagem On-the-fly.
> Output simula projeto de R$ 10.000 de agência.

## 1. Ferramentas da Esteira
- **Claude Code CLI:** Backend / Frontend. (Refs: Anthropic Cookbook, Oliur).
- **Nano Banana Pro:** Gemini 3 Pro MCP. Text-to-image com typography accuracy.
  - Repos: `github.com/kkoppenhaver/cc-nano-banana`, `github.com/Ibrahim-3d/nano-banana-claude-plugin` (13 modos, 4k inpainting).

## 2. Tech Stack Visual
| Lib / Feature | Descrição | Peso | Status |
| :--- | :--- | :--- | :--- |
| **AOS** | Elementos on-scroll. | Leve | ✅ Ativo na Holos. |
| **GSAP + ScrollTrigger**| Complexidade alta. Padrão Awwwards. | ~50kb| ⏳ Upgrades MVP. |
| **Locomotive Scroll** | Smooth Scroll + Parallax. | ~9kb | ⏳ Backlog. |

## 3. Estrutura WP Custom (Referência CPT)
Arquitetura mínima para CMS além-MVP.
```text
wp-content/themes/nome-do-tema/
├── style.css          
├── index.php
├── functions.php      
├── header.php
├── footer.php
└── single-curso.php   
```

## 4. Pipeline Prático
1. Instalar Nano Banana no Claude Code.
2. Trocar assets unbranded (Unsplash) por assets text-to-image nichados.
3. Vender por R$ 3k-10k.

Sandbox → [[Projetos/Holos/Holos - Site 2.0 Tracker]] · WebApps → [[03 — Estudos e Referências/Memoria Antiga/Referencias/Vibe Coding]]

---
[[03 — Estudos e Referências/Memoria Antiga/Referencias/Vibe Coding]] | [[Projetos/Holos/Holos - Site 2.0 Tracker]] | [[_INDEX]]
