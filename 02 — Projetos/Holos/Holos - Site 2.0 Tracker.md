---
created: 2026-04-20
updated: 2026-04-22
type: recurso
status: ativo
prioridade: alta
quando_ler: "tracker Site 2.0 Holos (Elementor HTML widget), status por página (blog pendente, 9 cursos a criar), bloqueadores externos (mãe/tia), sistema de design, decisões de arquitetura tomadas"
tags: [projeto, holos, site, tracker, wordpress]
---
# Holos — Site 2.0 · Tracker de Progresso

> **Abordagem atual:** HTML/CSS puro colado no **Elementor Custom HTML widget** com layout **"Tela do Elementor" (Canvas)**. Sem tema filho, sem PHP, sem ACF Pro. Mais rápido de entregar, visual idêntico.
>
> **Arquivos:** `C:\Users\lugzi\dev\holos-site\wordpress\`
> **Site:** holoscursoseterapias.com.br

---

## 📊 Status atual — Abril 2026

| Página | Arquivo local | Status no WP | URL |
|--------|--------------|-------------|-----|
| Homepage | `elementor-html.html` | ✅ No ar | /homepage/ (ou similar) |
| Curso Massoterapia Presencial | `elementor-curso.html` | ✅ No ar | /forma-masso90/ |
| Portal de Cursos | `elementor-portal.html` | ✅ No ar | /agenda-de-cursos |
| Blog listagem | `elementor-blog.html` | ⏳ Pronto, aguarda upload | — |
| Blog post individual | `elementor-post.html` | ⏳ Pronto, aguarda upload | — |
| 9 páginas de cursos | — | ❌ Não criadas ainda | — |

---

## ⏳ Próximos passos (em ordem)

### 1. Upload das páginas prontas (2 páginas)
Para cada uma: WP Admin → Páginas → Nova → título → Elementor → ⚙️ → Layout → **Tela do Elementor** → Custom HTML widget → colar arquivo → Salvar

- [ ] Blog listagem → `elementor-blog.html`
- [ ] Blog post template → `elementor-post.html` → título: "Como ganhar R$6.000 por mês como massoterapeuta"

### 2. Criar 9 páginas de cursos (via script Python)
Script em planejamento: `generate_cursos.py` — gera todos os 9 arquivos de uma vez a partir do template `elementor-curso.html`.

| Curso | Preço | Arquivo alvo |
|-------|-------|-------------|
| Massoterapia EAD | Consulte | `elementor-curso-masso-ead.html` |
| Acupuntura | R$7.920 | `elementor-curso-acupuntura.html` |
| Auriculoterapia | R$620 | `elementor-curso-auriculoterapia.html` |
| Aromaterapia | R$450 | `elementor-curso-aromaterapia.html` |
| Bambuterapia | R$305 | `elementor-curso-bambuterapia.html` |
| Reiki | R$380 | `elementor-curso-reiki.html` |
| Candle Massage | R$360 | `elementor-curso-candle.html` |
| Craniosacral Yamamoto | R$820 | `elementor-curso-craniosacral.html` |
| Baralho Cigano | R$440 | `elementor-curso-baralho.html` |

### 3. Conteúdo real (depende da mãe/tia)
- [ ] Depoimentos reais (mínimo 3): nome, curso, ano, texto
- [ ] Foto + nome dos professores reais
- [ ] Carga horária Massoterapia Presencial (atual: 1.200h — não confirmado)
- [ ] Horários de turmas reais
- [ ] Ranking dos top 10 cursos mais vendidos

### 4. Fase 2 — depois do MVP
- [ ] Conectar Bumblebee 2.0 ao WordPress (2 posts/dia automáticos)
- [ ] N8N → WP REST API: atualizar preços e turmas
- [ ] Substituir fotos Unsplash por fotos reais da escola

---

## 🏗️ Como funciona o deploy

```
1. Abrir página no WP Admin
2. Editar com Elementor
3. ⚙️ Configurações → Layout da Página → "Tela do Elementor" (Canvas)
4. Adicionar widget "HTML Personalizado"
5. Colar conteúdo do arquivo .html (sem DOCTYPE/html/head)
6. Salvar e publicar
```

> Cada arquivo HTML começa com `<link rel="preconnect" href="https://fonts.googleapis.com"...` — isso é o início correto, sem tags de documento.

---

## 🎨 Sistema de design (compartilhado por todas as páginas)

```css
--verde: #6B4A9E          /* cor principal */
--verde-escuro: #4A2E80   /* escuro, fundo dark */
--terracota: #E8621A      /* destaque/CTA */
--dourado: #F5B800        /* urgência/estrelas */
--bege: #FAF8FD           /* background */
footer: #160A30           /* footer */
```

- **Fontes:** Playfair Display (títulos) + Inter (corpo) via Google Fonts
- **Logo HTML/CSS:** H∞s com gotas e símbolo infinito gradiente — sem arquivo de imagem
- **WhatsApp:** +55 11 99316-4769

---

## 🔑 Decisões tomadas

| Decisão | Motivo |
|---------|--------|
| Elementor HTML widget (não PHP custom theme) | PHP exigiria FTP + tema filho + ACF Pro — complexidade desnecessária agora |
| Canvas layout ("Tela do Elementor") | Remove header/footer do tema, dá controle total do visual |
| HTML/CSS logo (sem imagem) | Zero dependência de arquivo, idêntico em todas as páginas |
| CTAs via WhatsApp (não formulário) | Resposta em 10 min, mais conversão, menos fricção |
| Urgency bar + sticky mobile CTA | Padrão de alta conversão em landing pages de cursos |
| Script Python para gerar 9 páginas | Mais eficiente que criar 9 arquivos manualmente |

---

## ⚠️ Bloqueadores externos

| Bloqueio | Quem resolve | Impacto |
|----------|-------------|---------|
| Depoimentos reais | Mãe | Seção de prova social com placeholder |
| Fotos professores | Tia/Mãe | Imagem Unsplash no lugar |
| Horários reais das turmas | Mãe | "Consulte via WhatsApp" como fallback |
| Ranking top 10 confirmado | Mãe | Ordem dos cursos no portal |

---

Cursos → [[01 - Profissional/Projetos/Holos/Holos - Cursos]] · Sistema Técnico → [[01 - Profissional/Projetos/Holos/Holos - Sistema Técnico]] · Modelo Negócio → [[01 - Profissional/Projetos/Holos/Holos - Modelo de Negócio]] · Funil → [[01 - Profissional/Projetos/Holos/Holos - Funil Digital]]

---
[[01 - Profissional/Projetos/Holos/Holos]] | [[01 - Profissional/Projetos/Holos/Holos - Site 2.0]] | [[_INDEX]]
