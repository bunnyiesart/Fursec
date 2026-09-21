---
name: Fursec
description: Catálogo de cibersegurança que se declara pela dimensão — dez caixas contadas, cinco cores, fonte de sistema.
colors:
  bg: "#ffffff"
  fg: "#16171a"
  muted: "#6e7178"
  line: "#e6e7e9"
  accent: "#1a4fd6"
  realce: "color-mix(in srgb, var(--accent) 12%, transparent)"
typography:
  display:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "2.125rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-.03em"
    fontVariant: "tabular-nums"
  displayCompact:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.875rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-.03em"
    fontVariant: "tabular-nums"
  headline:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "normal"
  title:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 600
    lineHeight: 1.6
    letterSpacing: ".14em"
  body:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  campo:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  label:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: ".7rem"
    fontWeight: 600
    lineHeight: 1.6
    letterSpacing: ".12em"
  meta:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: ".8125rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  arte:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "clamp(5.5px, 2.2vw, 11px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "normal"
  prompt:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: ".875rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  avisoRotulo:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: ".75rem"
    fontWeight: 600
    lineHeight: 1.55
    letterSpacing: ".06em"
  tag:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: ".625rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: ".06em"
  micro:
    fontFamily: "ui-sans-serif, -apple-system, \"Segoe UI\", Roboto, Helvetica, Arial, sans-serif"
    fontSize: ".75rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: ".04em"
rounded:
  nenhum: "0"
  foco: "2px"
  micro: "3px"
  bloco: "5px"
  barra: "6px"
spacing:
  "2xs": ".35rem"
  xs: ".5rem"
  sm: ".75rem"
  md: "1.25rem"
  lg: "2rem"
  xl: "2.5rem"
  "2xl": "4rem"
components:
  caixa:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.fg}"
    rounded: "{rounded.nenhum}"
    padding: "1.25rem 1.25rem 1.5rem"
  caixa-rotulo:
    textColor: "{colors.muted}"
    typography: "{typography.label}"
  caixa-rotulo-hover:
    textColor: "{colors.accent}"
  caixa-contagem:
    textColor: "{colors.fg}"
    typography: "{typography.display}"
  caixa-item:
    textColor: "{colors.fg}"
    typography: "{typography.body}"
    width: "fit-content"
  caixa-item-hover:
    textColor: "{colors.accent}"
  caixa-item-descricao:
    textColor: "{colors.muted}"
    typography: "{typography.meta}"
  faixa-boot:
    textColor: "{colors.fg}"
    typography: "{typography.arte}"
    padding: "0 0 1rem"
    width: "100%"
  busca-campo:
    backgroundColor: "transparent"
    textColor: "{colors.fg}"
    typography: "{typography.campo}"
    rounded: "{rounded.nenhum}"
    padding: ".7rem 0"
  busca-prompt:
    textColor: "{colors.muted}"
    typography: "{typography.prompt}"
  busca-prompt-focus:
    textColor: "{colors.accent}"
  aviso:
    textColor: "{colors.muted}"
    typography: "{typography.meta}"
    rounded: "{rounded.nenhum}"
    padding: ".7rem 0 .7rem .9rem"
  aviso-rotulo:
    textColor: "{colors.fg}"
    typography: "{typography.avisoRotulo}"
  atalho-tecla:
    textColor: "{colors.muted}"
    rounded: "{rounded.micro}"
    padding: ".1rem .35rem"
    size: ".6875rem"
  secao-summary:
    textColor: "{colors.muted}"
    typography: "{typography.micro}"
    width: "fit-content"
  secao-summary-hover:
    textColor: "{colors.accent}"
  documento-link:
    textColor: "{colors.accent}"
    typography: "{typography.body}"
  documento-tag:
    textColor: "{colors.muted}"
    typography: "{typography.tag}"
    rounded: "{rounded.micro}"
    padding: ".1em .4em"
---

# Design System: Fursec

## Overview

**Creative North Star: "O Acervo Medido"**

Este sistema não tem cor nem face para gastar. A paleta de cinco tokens e a pilha de fonte de sistema estão fixadas pelo usuário como intocáveis, e é dessa restrição que todo o resto nasce: a hierarquia é carregada por **escala, peso, espaço e área**, e o acento existe só em hover, foco e estado. Onde outro sistema pintaria uma seção de destaque, este a faz maior; onde outro trocaria de face, este muda o corpo do numeral.

A personalidade é de catálogo conferido, não de brochura. A página se declara pela dimensão antes de se declarar pelo conteúdo: cada caixa abre com sua contagem real em numeral tabular de corpo grande, e é a contagem que o olho pega primeiro — o rótulo vem acima dela, menor. Recusa explícita, confirmada no build: a lista corrida de links anotados que trata 172 cursos e 2 arquivos de progresso como se pesassem igual, e a grade de cartões idênticos de ícone-título-texto. A caixa tem o tamanho do que carrega.

O mascote não entra mais como imagem. A expressão de marca do índice é a **faixa de boot**: um `<pre aria-hidden>` com a cabeça de raposa desenhada em caracteres de bloco cheio ao lado do logotipo FURSEC em ASCII de bloco, o mesmo do `README.md`. A folha shipped não tem **nenhum** `url()`; a camada de fundo fotográfica, o parallax de rolagem e o script que o movia foram removidos. O que sobrou de movimento persistente é só a divisa do `<details>` girando em 180ms, desligada por `prefers-reduced-motion`. Densidade alta, moldura mínima, movimento quase nulo: a única moldura é a borda de 1px de `--line`. A folha é única e serve duas superfícies: o índice (grade de caixas, 64rem) e as 48 páginas de documento geradas dos `.md` (coluna de leitura, 46rem).

**Key Characteristics:**
- Cinco tokens de cor, um derivado por `color-mix`, nenhum sexto — em claro e escuro.
- Uma face de leitura só: a pilha sans do sistema. A mono é pilha do sistema e funcional, não segunda voz de display.
- Zero raster: nenhum `url()` na folha. Marca desenhada em caractere, borda CSS ou `path` autoral.
- Contagem em numeral tabular como primeiro elemento de leitura de cada caixa.
- Rótulo de seção em corpo fixo nas dez caixas; a diferença entre elas é área.
- Borda de 1px e régua de 1px como único recurso de separação. Zero sombra.
- Ícone é desenhado (borda CSS, `path` autoral) ou substituído por texto; nunca glifo decorativo nem emoji na cromia da interface.
- Superfícies do navegador — seleção, caret, barra de rolagem, anel de foco — puxadas dos mesmos tokens.

## Colors

Paleta de cinco tokens em `:root`, com contrapartes completas no tema escuro por `prefers-color-scheme`. Nenhum valor novo entra; o único tom derivado sai de `color-mix` sobre os mesmos tokens.

### Primary
- **Azul de Estado** (`--accent`, `#1a4fd6` claro / `#8fb0ff` escuro): o único acento. Aparece **exclusivamente** em resposta: link em hover, `:focus-visible`, `caret-color`, borda de foco da linha de busca, o prompt `fursec#` quando a linha tem foco, `accent-color` de checkbox, e a cor de corpo dos links dentro das páginas de documento (`.md a`). Em repouso, no índice, ele não aparece em lugar nenhum.
- **Realce de Seleção** (`--realce`, `color-mix` do acento a 12% sobre transparente): fundo de `::selection`. Existe para que a seleção de texto pertença à paleta em vez de chegar com o azul de fábrica do navegador.

### Neutral
- **Branco de Papel** (`--bg`, `#ffffff` claro / `#131417` escuro): fundo do documento e da caixa. A caixa repinta o fundo em cima de si mesma, e a borda interna de 3px do polegar da barra de rolagem sai desta cor.
- **Grafite de Texto** (`--fg`, `#16171a` claro / `#e7e8ea` escuro): texto corrido, numeral da contagem, título de item em repouso, a arte da faixa de boot, o rótulo `WARNING:` e a régua esquerda de 1px do aviso — o único filete da folha que usa a cor do texto em vez de `--line`, porque um aviso não negociável precisa de mais presença que uma divisa e a paleta não tem cor de alerta. Também aparece diluído por `color-mix` como fundo de `code` (8%) e de `pre` (4%) e como borda das etiquetas de peso alto (22%) nas páginas de documento.
- **Cinza de Apoio** (`--muted`, `#6e7178` claro / `#8b8f97` escuro): tudo que é segundo plano de leitura — rótulo da caixa, unidade da contagem, descrição de item, `summary`, migalha, rodapé, placeholder, prompt em repouso, corpo do aviso, etiqueta de catálogo, e o polegar da barra de rolagem em hover.
- **Linha de Divisa** (`--line`, `#e6e7e9` claro / `#26282d` escuro): borda da caixa, régua entre entradas (a 60% via `color-mix`), sublinhado da linha de busca, borda da tecla de atalho, borda da etiqueta, filete de tabela e de bloco de código, topo do rodapé, polegar da barra de rolagem em repouso.

### Named Rules

**A Regra dos Cinco.** A paleta é fechada em cinco tokens mais derivados por `color-mix` dos mesmos tokens. Uma sexta cor é proibida, em claro e em escuro. Precisar de uma cor nova significa que a hierarquia foi resolvida errada: resolva por escala, peso, espaço ou área.

**A Regra do Acento Reativo.** O acento não decora: ele responde. Só pode aparecer em hover, `:focus-visible`, caret, estado ativo e corpo de link de documento. Um acento em repouso na superfície do índice é violação.

**A Regra de Estado é Marca, Não Matiz.** Com um acento só, o que diferencia uma caixa da outra nunca é cor. Diferença se expressa por área, ordem e peso. Vale inclusive para severidade: o aviso de ética é marcado por filete e caixa alta, não por vermelho.

## Typography

**Face de leitura (única):** pilha de sistema — `ui-sans-serif, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`. Não há face de display e não há face self-hosted.

**Pilha monoespaçada (funcional, não segunda voz):** `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`. Entrou no sistema por requisito de largura fixa e vive em exatamente três lugares: a arte da faixa de boot (`.arte`, onde sem avanço constante o desenho desalinha), o prompt `fursec#` da busca (`.busca .prompt`) e o rótulo `WARNING:` do aviso (`.aviso b`). Não é uma voz de display e não deve ser usada para título, corpo, rótulo de seção nem etiqueta.

**Character:** neutra por imposição e usada como instrumento de medida, não de voz. Toda a expressão vem de três alavancas: corpo, peso (400 / 600) e tracking (de `-.03em` no numeral grande a `.14em` no título em caixa alta). `font-variant-numeric: tabular-nums` em toda contagem, para que os dígitos alinhem em coluna e a comparação entre caixas seja visual.

### Hierarchy
- **Display** (600, 2.125rem, line-height 1, tracking `-.03em`, tabular): a contagem dentro da caixa. É o maior corpo da página e o primeiro elemento de leitura de cada seção. Cai para 1.875rem abaixo de 40rem (`displayCompact`).
- **Headline** (600, 1.5rem, 1.25, tracking normal, `text-wrap: balance`): o `h1` das páginas de documento. Deliberadamente **não** é caixa alta — o tracking largo é assinatura do índice, não de título de documento.
- **Title** (600, 1.05rem, tracking `.14em`, caixa alta): o `h1` "Fursec". No índice ele está **visualmente oculto** (`clip-path: inset(50%)`) e serve como nome acessível, porque a faixa de boot já grafa o logotipo; o mesmo corpo, sem tracking e sem caixa alta, serve o `h2` das páginas de documento, que ainda ganha um filete inferior de 1px.
- **Body** (400, 15px, 1.6): texto corrido e título de item de catálogo. Nas páginas de documento, `p` e `li` sobem para 1.65 dentro de uma coluna de 46rem.
- **Campo** (400, 1.0625rem): o input de busca, um corpo acima do texto corrido, sem moldura — lê como linha de prosa, não como widget.
- **Label** (600, .7rem, tracking `.12em`, caixa alta): o rótulo de seção. **O mesmo corpo nas dez caixas.**
- **Meta** (400, .8125rem): descrição de item, unidade da contagem, contagem de resultados, links de sublista, endereço do repositório, corpo do aviso (1.55 de entrelinha).
- **Arte** (mono, 400, `clamp(5.5px, 2.2vw, 11px)`, line-height 1): a faixa de boot. O corpo escala com a viewport para as 64 colunas caberem em 390px sem estourar nem inflar no desktop; a entrelinha 1 é requisito, não descuido (ver "Exceção conhecida do detector").
- **Prompt** (mono, 400, .875rem): `fursec#` à esquerda do campo de busca. Carrega identidade num lugar onde antes havia um ícone.
- **Rótulo de aviso** (mono, .75rem, tracking `.06em`, caixa alta): `WARNING:`. No shipped ele sai em **700**, o bold nativo do `<b>`, sem declaração de peso.
- **Etiqueta** (400, .625rem, tracking `.06em`, caixa alta): as etiquetas escritas das tabelas de catálogo (`GRÁTIS`, `PAGO`, `CERT`, `LAB`, `PT`, `EN`, nível de risco), na sans e não na mono.
- **Micro** (400, .75rem, tracking `.04em`, tabular): o `summary` de "N seções". A tecla de atalho `/` desce a .6875rem; a migalha vai a .8rem em caixa alta com tracking `.1em`.

### Named Rules

**A Regra do Rótulo Fixo.** Os dez rótulos de seção saem todos no mesmo corpo (.7rem). Hierarquia entre seções se lê pela área que a caixa ocupa e pela ordem em que aparece — nunca pelo tamanho da letra. Teste: se dois rótulos de seção têm corpos diferentes, a composição falhou.

**A Regra do Numeral Tabular.** Todo número que o leitor possa comparar — contagem da caixa, resultado do filtro, "N seções", coluna de horas e de preço nas tabelas — sai com `font-variant-numeric: tabular-nums`.

**A Regra dos Dois Pesos.** 400 e 600 são os pesos do sistema. O peso 600 é reservado a título, rótulo, contagem, `th`, etiqueta de peso alto, nome com prioridade (`.prio`) e à única caixa de entrada ("Comece aqui"), que é a ação primária de quem chega. O `700` do `<b>` de `WARNING:` é o único valor fora dessa dupla no shipped e é desvio herdado, não licença: peso novo se declara em 600.

**A Regra da Mono Funcional.** A monoespaçada só entra onde a largura fixa do caractere é o requisito — grade de caracteres, prompt, rótulo curto de máquina. Nunca como face de voz, nunca em texto corrido, e sempre da pilha do sistema: nenhuma face self-hosted entra neste sistema.

## Layout

Duas larguras de contêiner, uma por superfície: `body` a **46rem** para as páginas de documento (a medida de leitura manda) e `body.inicio` a **64rem** para o índice (a grade de caixas pede largura). Respiro vertical de `4rem 1.5rem 6rem`, caindo para `2.5rem 1rem 4rem` abaixo de 40rem.

A página do índice abre por uma **faixa de boot de largura inteira** dentro do cabeçalho flex (`flex: 0 0 100%`), com 1rem de folga abaixo (`.75rem` abaixo de 62rem) e `overflow: hidden`, para que a arte nunca empurre a largura da página. Abaixo dela vem o cabeçalho de linha (frase + endereço do repositório), depois o aviso de ética, depois a linha de busca, depois a grade.

O índice é uma grade de **12 colunas** (`repeat(12, minmax(0, 1fr))`) com `gap: 1.25rem` e `align-items: start`, para que cada caixa termine onde seu conteúdo termina — sem isso a linha da grade estica a caixa curta até a altura da vizinha alta e abre um vão que desmente a regra da página.

**Três faixas de largura**, e dois eixos de significado independentes:
- **Banda** (`span 12`): as duas bandas de orientação — "Comece aqui" no topo e "Roadmap" depois dos catálogos grandes. A banda deita seu conteúdo em colunas (`auto-fit, minmax(12rem, 1fr)`) e não leva régua entre os itens.
- **Larga** (`span 6`): catálogos com muitos documentos a dispor (Cursos, Repositórios, Projetos).
- **Estreita** (`span 3`): seções com poucos documentos (Livros, Recursos, Labs, Documentação, Progresso). O `span 4` de base do `.caixa` é o padrão da classe; no shipped nenhuma caixa roda sem uma das três faixas.

**A ordem é a contagem do acervo; a largura é quantos documentos a caixa tem para dispor.** São dois sinais de propósito diferente. Livros declara 45 no acervo mas dispõe 3 documentos: dar-lhe meia página abria um vão que lia como conteúdo que não carregou. Consequência assumida: Projetos (33) ocupa cerca do dobro da área de Livros (45), e **posto se lê pela ordem de leitura, não pela área**. A ordem dos catálogos é estritamente decrescente pela contagem — 172, 80, 45, 33, 26, 22, 4, 2 — e as duas bandas saem dessa fila porque "5 fases" e "172 cursos" não medem a mesma coisa.

**Breakpoints: 62rem e 40rem.**
- Abaixo de 62rem a grade vira duas colunas (`span 6` para base, larga e estreita); o Roadmap passa de 5 para 3 colunas de fase, a banda de entrada trava em 2 colunas, para não deixar o quarto passo órfão numa linha só, e a faixa de boot encurta a folga inferior.
- Abaixo de 40rem tudo empilha (`span 12`), o cabeçalho passa a `display: block`, a tecla de atalho desaparece (não serve num telefone), a contagem desce para a própria linha, e as grades internas das bandas viram uma coluna.
- A caixa mantém o corpo da letra e perde colunas, nunca o contrário. A exceção é a arte: ela **precisa** escalar o corpo com a viewport, porque é uma grade de 64 colunas de caractere, não texto.

**Armadilha de cascata registrada.** `.caixa` dentro de uma media query posterior casa a banda também (ela é `.caixa`) e, vindo depois no arquivo, vence o `span 12` de `.caixa--banda`. Toda media query que reescreva o span de `.caixa` **precisa restaurar `.caixa--banda { grid-column: span 12; }` dentro dela**. Foi esse o defeito que colapsou as bandas na faixa 40–62rem.

**Ritmo de espaço.** Passos efetivamente usados: `.35rem` / `.5rem` / `.75rem` (régua entre entradas, folga da arte em tela média) / `.9rem` (recuo interno do aviso) / `1rem` (folga da arte) / `1.25rem` (padding da caixa e gap da grade) / `2rem` (gap entre colunas da banda, início da busca) / `2.5rem` (início da grade, `h2` de documento) / `3rem` (rodapé) / `4rem` (topo da página).

### Named Rules

**A Regra da Caixa Medida.** A caixa tem o tamanho do que carrega: `align-items: start` no eixo vertical e a faixa de largura pelo volume de documentos no horizontal. Nenhuma caixa é esticada para casar com a vizinha.

**A Regra da Banda Restaurada.** Reescrever o span de `.caixa` numa media query obriga a reafirmar o span 12 das bandas na mesma query.

## Elevation & Depth

**Este sistema não usa sombra.** Não há um único `box-shadow` de elevação na folha, e desde a remoção da camada fotográfica não há **nenhuma** camada de fundo: a página shipped não tem `url()`, nem `z-index` negativo, nem parallax. Profundidade é feita por dois recursos, ambos de um pixel ou de opacidade:

1. **Borda e régua de 1px** em `--line`: a caixa se separa do fundo por contorno, não por levantamento. A régua entre entradas sai a 60% do token (`color-mix`), um degrau abaixo da moldura, para que a divisão interna leia como mais fraca que a externa. O aviso de ética sobe um degrau na direção oposta: sua régua esquerda usa `--fg`, o valor mais forte da folha.
2. **Preenchimento tonal por `color-mix` do próprio texto**: `code` a 8% e `pre` a 4% de `--fg` sobre transparente, nas páginas de documento.

O único `box-shadow` da folha não é elevação: `0 1px 0 var(--accent)` na linha de busca em foco, usado para **engrossar a régua sem mexer na borda**, que deslocaria o layout. É um recurso de desenho de 1px, não uma sombra.

### Named Rules

**A Regra de Zero Sombra.** Nenhuma superfície levanta. Se um elemento precisa se destacar, ele ganha contorno, área ou espaço — não sombra, não gradiente, não deslocamento.

**A Regra do Fundo Vazio.** O fundo é chapado em `--bg`. Sem imagem, sem gradiente, sem camada atmosférica: a folha shipped tem zero `url()` e a atmosfera, quando a marca precisa dela, é grafada em primeiro plano como caractere.

## Shapes

Forma retangular, de canto vivo. A caixa, o campo de busca, a linha da busca, a tabela, o aviso e o filete têm **raio 0**. O raio existe só em quatro lugares funcionais e é sempre micro: o anel de `:focus-visible` (2px, para acompanhar a caixa do link), a tecla de atalho, o `code` inline e a etiqueta de catálogo (3px), o bloco `pre` (5px) e o polegar da barra de rolagem (6px).

A geometria recorrente é a **linha**: borda de 1px fecha a caixa; régua de 1px separa entradas; um filete inferior de 1px marca a linha de busca e o `h2` de documento; uma borda esquerda de 1px indenta a sublista `.sec`, o `blockquote` e o aviso. Onde outro sistema usaria fundo ou pílula, este usa um traço.

A segunda geometria, nova no shipped, é a **grade de caractere**: a raposa e o logotipo da faixa de boot são desenhados em bloco cheio (`█`) e meio-bloco de moldura, num `<pre>` de 64 colunas com entrelinha 1. É desenho, mas o material é texto: escala por `font-size`, herda `--fg` e não carrega um único byte de imagem.

**Marcas desenhadas:** a divisa do `<details>` é feita de duas bordas CSS de 1.5px giradas em -45° (e 45° quando aberto); o favicon do índice é um `path` autoral de raposa num data URI que carrega seu próprio bloco `prefers-color-scheme`. O ícone de lupa da busca não existe mais — foi substituído por texto (`fursec#`).

### Named Rules

**A Regra do Ícone Desenhado.** Ícone é desenhado, escrito ou não existe. Borda CSS, SVG inline a 1.5px em `currentColor`, `path` autoral, ou uma palavra em mono no lugar do pictograma. Glifo tipográfico decorativo, fonte de ícone e emoji na cromia da interface são proibidos.

**A Regra do Canto Vivo.** Contêiner não arredonda. O raio é reservado a superfície de navegador, marcação de código e etiqueta.

## Components

### Caixa rotulada (componente-assinatura)

A linguagem de componente inteira do índice. Caráter: ficha de acervo conferida.
- **Forma:** retângulo de canto vivo, borda de 1px `--line`, fundo `--bg`, padding `1.25rem 1.25rem 1.5rem`.
- **Anatomia, nesta ordem:** rótulo em caixa alta com tracking `.12em` a .7rem em `--muted` → contagem (numeral 2.125rem/600 tabular + unidade a .8125rem em `--muted`, alinhados por baseline) → lista de entradas, cada uma com título em `--fg` e descrição a .8125rem em `--muted`, separadas por régua de 1px a 60% do token.
- **Faixas:** `banda` (span 12, conteúdo em colunas, sem régua), `larga` (span 6), `estreita` (span 3). Na estreita e acima de 62rem a unidade da contagem quebra para a linha inteira, porque não cabe ao lado do numeral — a regra está atada à **largura**, não à classe.
- **Variante de entrada:** a caixa "Comece aqui" é a única com peso de fonte elevado nos itens (600). É a ação primária de quem chega.
- **Estados:** o rótulo, quando é link, e todo item ganham `color: --accent` + `border-bottom-color: --accent` em `:hover` e em `:focus-visible`. O sublinhado existe desde o repouso como borda transparente, para que acender não mexa no layout. O link tem `width: fit-content`, para que a linha acenda só sob o texto.

### Faixa de boot (componente-assinatura)

Caráter: a máquina se apresentando antes do catálogo. Substitui a camada fotográfica de mascote que existia antes.
- **Estrutura:** `<pre class="arte" aria-hidden="true">` de largura inteira no topo do `<header class="topo">`, com a cabeça de raposa em bloco cheio à esquerda e o logotipo FURSEC em ASCII de bloco à direita — o mesmo desenho do `README.md`, uma marca em dois suportes.
- **Tipo:** pilha mono do sistema, `clamp(5.5px, 2.2vw, 11px)`, `line-height: 1`, `white-space: pre`, `overflow: hidden`, cor `--fg`. Nenhum peso, nenhuma cor própria.
- **Acessibilidade:** a arte é decoração por definição, então sai do alcance do leitor de tela por `aria-hidden` e o `<h1>Fursec</h1>` fica visualmente oculto (`clip-path: inset(50%)`, 1×1px) carregando o nome acessível. O nome nunca desaparece da árvore; só sai da tela.
- **Regra de manutenção:** o desenho só se mantém com entrelinha 1 e largura de caractere fixa. Mexer em qualquer dos dois esfarrapa o logotipo.

### Aviso de ética (`p.aviso`)

Caráter: aviso de máquina, não banner de alerta.
- **Estilo:** régua esquerda de 1px em `--fg` com `.9rem` de recuo interno, corpo a .8125rem/1.55 em `--muted`, rótulo `WARNING:` em mono .75rem caixa alta com tracking `.06em` em `--fg`. Sem fundo, sem raio, sem cor de severidade — a paleta não tem uma e severidade se marca por contraste de filete e por caixa alta.
- **Link:** herda a cor do corpo, sublinhado por borda de 1px `--line`, acendendo em `--accent` no hover e no `:focus-visible`. Aponta para `projetos/00-regras.md`.
- **Posição:** entre o cabeçalho e a busca, ou seja, antes de qualquer caminho de navegação.

### Linha de busca

Caráter: linha de prosa que aceita digitação, não widget.
- **Estilo:** fila flex com o prompt `fursec#` à esquerda (mono .875rem em `--muted`, `user-select: none`, `aria-hidden`), campo transparente sem borda própria, tecla de atalho `/` e contagem de entradas à direita. A **única** moldura é o filete inferior de 1px de toda a linha.
- **Foco:** `:focus-within` acende o filete inteiro em `--accent` e o engrossa com `0 1px 0` — o foco é da linha, não um anel em volta do campo. O prompt também vira `--accent`. É o único lugar da folha autorizado a usar `outline: none`, porque o estado de foco é mais legível que o anel padrão e está desenhado no filete.
- **Estado com texto:** a tecla de atalho fica `visibility: hidden` (mantém o espaço, não salta) quando a linha tem foco ou texto.
- **Estreito:** abaixo de 40rem a tecla sai de cena e a contagem desce para a própria linha.

### Seção recolhida (`<details>`)

Caráter: nativo primeiro — teclado e leitor de tela funcionam sem script.
- `summary` a .75rem em `--muted`, tracking `.04em`, tabular, `width: fit-content`, marcador nativo suprimido, divisa de borda CSS a 1.5px girando 180ms com `cubic-bezier(.2,.8,.2,1)`.
- Hover leva o `summary` a `--accent`. A sublista interna indenta por borda esquerda de 1px e usa links a .8125rem em `--muted`.

### Cabeçalho e rodapé do índice

- **Cabeçalho:** a faixa de boot em linha própria, e abaixo dela uma fila flex de baseline comum: a frase do que é em `--muted` e o endereço do repositório empurrado para a direita por `margin-left: auto`, a .8125rem com filete inferior de 1px que acende em `--accent`. O `h1` está na árvore mas fora da tela. Abaixo de 40rem empilha em bloco.
- **Rodapé:** topo de 1px, texto a .8125rem em `--muted`, links herdando a cor e acendendo em `--accent`.

### Página de documento (segunda superfície da mesma folha)

Caráter: coluna de leitura sóbria dentro do mesmo mundo. Marcação gerada pela API do GitHub; a folha controla o envelope.
- **Migalha:** `.8rem` em caixa alta com tracking `.1em`, em `--muted`, com 2.5rem de folga antes do título.
- **Hierarquia:** `h1` a 1.5rem/600 sem caixa alta; `h2` a 1.05rem com filete inferior de 1px e 2.5rem de folga acima; `h3` a .95rem. Todos com `text-wrap: balance`.
- **Link de corpo:** este é o único lugar onde o acento aparece em repouso — `color: --accent` com sublinhado a 35% do acento, que fecha em 100% no hover.
- **Código:** `code` inline com fundo a 8% de `--fg` e raio 3px; `pre` com borda de 1px, fundo a 4%, raio 5px e rolagem horizontal própria.
- **Tabela:** embrulhada em um contêiner de `overflow-x: auto` para rolar em tela estreita em vez de estourar a página; células com filete de 1px, `th` em 600 e `td` em numeral tabular.
- **Listas de tarefa:** marcador removido, checkbox com `accent-color: --accent`.

### Etiqueta de catálogo e a transformação de build

O sistema chega às 48 páginas geradas por uma camada de build, não só por CSS: `tools/build-site.py` converte o emoji da legenda do markdown em etiqueta escrita antes de a página existir.
- **Etiqueta (`.md .tag`):** `inline-block`, borda de 1px `--line`, raio 3px, .625rem em caixa alta com tracking `.06em`, cor `--muted`, `white-space: nowrap`. Diferenciação por **peso**, nunca por matiz: `tag--gratis` e `tag--prioridade` sobem para `--fg` com borda a 22% de `--fg`, porque "gratuito primeiro" é princípio do produto.
- **Transformação:** `etiquetar()` troca 🆓/💸/💳/🎓/🧪/bandeiras/bolas de risco pelas palavras `grátis`, `pago`, `cert`, `lab`, `PT`, `EN` e níveis de risco (`crítico`, `alto`, `médio`, `baixo`, `a fazer`); `destaca_prioridade()` transforma `⭐` em `<strong class="prio">` no nome do item, porque como etiqueta a estrela pesava mais que o curso que qualificava; e `REMOVER` apaga o emoji que só repetia a palavra ao lado.
- **Limite deliberado:** `fora_de_pre()` não aplica nada dentro de `<pre>` — emoji em bloco de código é conteúdo (as árvores de diretório de `docs/` desenham com 📁 e 📌) e trocá-lo quebraria o exemplo.
- **Fonte intacta:** o markdown continua com emoji, para ler bem no GitHub. A remoção do emoji da cromia é uma regra da **superfície**, aplicada na geração, não uma edição do acervo.

### Filtro ao vivo (interação-assinatura)

Digitar recalcula a contagem de entradas ao vivo (`N de M entradas`), esconde as entradas que não casam, **abre à força** o `<details>` cujo conteúdo casa (senão o resultado ficaria atrás de um resumo fechado) e esconde por inteiro a caixa que ficou sem nenhum acerto. `/` foca o campo de qualquer lugar da página; `Esc` limpa. O estado vazio diz o que foi buscado, o que o filtro lê e como sair. Nenhum número é fixo no HTML: a contagem inicial é escrita pelo script no carregamento.

### Superfícies do navegador

Com paleta fixa, é aqui que se lê que a página foi construída e não montada. Todas puxadas dos tokens: `::selection` no realce derivado, `caret-color` no acento, polegar da barra de rolagem em `--line` com borda interna de 3px na cor do fundo (o que o faz parecer mais fino do que é), `:focus-visible` como anel de 2px do acento com 2px de deslocamento e raio 2px, `text-underline-offset: .2em`, `font-variant-numeric: tabular-nums` nas contagens.

## Exceção conhecida do detector

`tight-leading` dispara em `.arte` e **fica disparando de propósito**. A regra
existe para texto corrido de várias linhas; a arte ASCII não é texto para ler,
é um desenho feito de caracteres, e as fileiras de bloco só se encostam com
`line-height: 1`. Com 1.25 o logotipo FURSEC ganha faixas brancas horizontais
e se esfarrapa — foi o defeito corrigido no commit que introduziu a faixa.

Não suprima a regra por glob de arquivo: isso a apagaria para a folha inteira
e perderíamos a cobertura de entrelinha em texto corrido, que é onde ela vale.
E não "conserte" a arte afrouxando a entrelinha.

**Estado atual, registrado como é.** Existe hoje em `.impeccable/config.json` um
`ignoreValues` com `rule: tight-leading`, `value: "*"`, escopado ao arquivo
`index.html`. Ele foi criado **por decisão do assistente, não confirmada pelo
usuário**, e o custo está assumido no próprio registro: a entrelinha de prosa do
`index.html` deixa de ser coberta. Isso é mais largo do que o parágrafo acima
recomenda — o ideal continua sendo uma exceção por valor e por seletor, não um
curinga por arquivo. Fica aqui como pendência conhecida, para quem revisar
decidir; não é um padrão a copiar para outro arquivo.

## Do's and Don'ts

### Do:
- **Do** resolver hierarquia por escala, peso (400/600), espaço e área. A paleta e a face são intocáveis; toda diferenciação nova sai dessas quatro alavancas.
- **Do** usar o acento só em hover, `:focus-visible`, caret, estado ativo e corpo de link de documento.
- **Do** manter o rótulo de seção no mesmo corpo (.7rem, `.12em`, caixa alta) em toda caixa nova.
- **Do** abrir toda caixa pela contagem real em numeral tabular, com a unidade em `--muted` ao lado.
- **Do** ordenar caixas de catálogo de forma estritamente decrescente pela contagem do acervo, e dimensionar a largura pelo volume de documentos que a caixa dispõe. Ordem é posto; área é volume.
- **Do** restaurar `.caixa--banda { grid-column: span 12; }` dentro de qualquer media query que reescreva o span de `.caixa`.
- **Do** desenhar todo ícone — borda CSS, SVG inline ou `path` autoral — a 1.5px em `currentColor`, ou substituí-lo por uma palavra, como o prompt `fursec#` fez com a lupa.
- **Do** usar a mono do sistema só onde a largura fixa do caractere é requisito: grade de caracteres, prompt, rótulo curto de máquina.
- **Do** manter a arte em `<pre aria-hidden>` com o nome acessível num `<h1>` visualmente oculto, sempre que a marca aparecer como desenho.
- **Do** derivar tons novos com `color-mix` sobre os cinco tokens existentes, como já fazem o realce da seleção, a régua a 60%, os fundos de código e a borda da etiqueta de peso alto.
- **Do** dar contraparte escura a todo token e a todo valor de opacidade; ambos os temas são obrigatórios.
- **Do** submeter qualquer movimento novo a `prefers-reduced-motion: reduce`, como já faz a transição da divisa do `<details>` — o único movimento persistente que restou na página.
- **Do** converter emoji de conteúdo em etiqueta escrita na camada de build, deixando o markdown intacto e pulando `<pre>`.
- **Do** capturar 1440, **768** e 390 em claro e escuro ao revisar. A faixa 40–62rem não é interpolável pelos extremos: foi ali que a banda colapsada passou por várias rodadas de revisão sem ser vista.

### Don't:
- **Don't** introduzir uma sexta cor, um gradiente ou uma face tipográfica nova. Nem no claro, nem no escuro, nem "só para este componente".
- **Don't** trazer face self-hosted, nem promover a mono a segunda voz de display. Ela é pilha do sistema e é funcional.
- **Don't** reintroduzir imagem de fundo, `url()`, camada atmosférica ou parallax de rolagem. O fundo é chapado; a folha shipped tem zero `url()`.
- **Don't** usar emoji na cromia da interface. (Nas tabelas dos catálogos o dado permanece, mas escrito: o build o converte em etiqueta.)
- **Don't** usar glifo tipográfico ou fonte de ícone onde cabe um traço desenhado ou uma palavra.
- **Don't** adicionar `box-shadow` de elevação, nem gradiente, nem deslocamento de profundidade. O sistema é plano por contorno.
- **Don't** diferenciar uma caixa por cor de fundo, cor de borda ou tamanho de rótulo.
- **Don't** marcar severidade por cor. Aviso se marca por filete em `--fg` e rótulo em caixa alta; não há cor de alerta na paleta.
- **Don't** arredondar contêiner. O raio pertence a anel de foco, marcação de código, etiqueta e superfície de navegador.
- **Don't** escrever `outline: none` num link. O único `outline: none` autorizado da folha é o do campo de busca, cujo foco está desenhado no filete da linha inteira.
- **Don't** trazer o mascote como `<img>` nem como `background`. Ele entra grafado em caractere, decorativo e `aria-hidden`, para que o leitor de tela o ignore em vez de anunciar descrição no meio da navegação.
- **Don't** esticar uma caixa para casar com a altura da vizinha, nem remover `align-items: start`.
- **Don't** fixar contagem em HTML. Número que o leitor confere é escrito pelo script ou vem do `.md`.
- **Don't** reduzir o corpo do texto para ganhar colunas em tela estreita. A caixa perde colunas, nunca corpo de letra. A arte é a única exceção: ela escala porque é grade de caractere, não texto.

<!--
Cobertura de revisão, registrada honestamente: a revisão de fecho (três rodadas, veredito "ship")
cobriu o índice em 1440, 768 e 390, em claro e escuro, e explicitamente NÃO cobriu as páginas de
documento geradas dos `.md` — a metade `.md` deste sistema está documentada a partir do código,
não verificada visualmente. Desde aquele veredito o índice MUDOU outra vez: a camada fotográfica
de fundo e o parallax saíram, e entraram a faixa de boot em ASCII, o aviso de ética e o prompt
`fursec#`. Essas mudanças NÃO passaram por revisão de fecho nova. O veredito antigo não cobre o
índice atual.

Raster: `assets/mascote.jpg` continua no repositório e hoje não é referenciado por nada — nem pela
folha (zero `url()`), nem pelo `index.html`. É ativo de marca pré-existente, retido de propósito;
não é dependência viva desta superfície e não foi gerado por este trabalho.
-->
