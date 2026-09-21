---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["assets/site.css"]
---

## Scope and mode

Surface: `index.html` (índice do sítio) e `assets/site.css` (folha única, compartilhada com as páginas geradas de `.md` pelo `tools/build-site.py`). Modo: **Read** — o visitante vem entender o que existe e achar seu caminho.

Duas entradas de peso igual, e o índice serve as duas sem penalizar nenhuma: primeira visita ("isso é pra mim? por onde começo?") e retorno ("onde estava aquele lab?"). A busca client-side atende a segunda; a dimensão declarada do acervo atende a primeira.

## Constraints

- Paleta e tipografia **fixadas pelo usuário**: os cinco tokens com seus valores atuais e a pilha de fonte de sistema. Tons derivados por `color-mix` dos mesmos tokens são permitidos; face nova ou cor nova não. Isto conflita de frente com o piso de qualidade, que pede face própria self-hosted para superfície de mundo próprio — o brief vence, e a hierarquia passa a ser carregada por escala, peso, espaço e contagem em vez de cor.
- Nome "Fursec", mascote raposa e logo ASCII do README preservados.
- Markdown é fonte única. O índice não pode mostrar nada que não exista no `.md`.
- Sem etapa de build de CSS/JS. O que está em `assets/` é o que é servido.
- `tools/check-site.py` roda no CI e quebra em link interno morto, âncora inexistente e página órfã. As sublistas `.sec` do índice apontam para âncoras derivadas de heading: mexer em heading exige reescrever o link junto.
- Tema claro e escuro obrigatórios. `prefers-reduced-motion` já desliga o parallax e qualquer movimento novo respeita a mesma consulta.
- O mascote de fundo é decorativo por definição: `background` em CSS, nunca `<img>`.

## Direction contract

**THESIS.** O catálogo se declara pela dimensão antes de se declarar pelo conteúdo: dez caixas contadas, cada uma com sua quantidade real e as primeiras entradas à mostra. Recusa o arranjo-padrão do ramo — lista corrida de links anotados que trata os 172 cursos e os 2 arquivos de progresso como se pesassem igual — e recusa também a grade de cartões idênticos de ícone-título-texto, que é a resposta preguiçosa à mesma pergunta. Aqui a caixa tem o tamanho do que carrega.

**OWN-WORLD.** Os cinco tokens e a fonte de sistema, sem adição. Hierarquia por escala, peso, espaço e contagem, nunca por cor: o único acento existe em link ativo, foco e estado, e nada mais. Linguagem de componente: a caixa rotulada — rótulo em caixa alta com tracking largo, contagem em numeral tabular de corpo grande, três entradas reais como amostra, e a borda de 1px do token `--line` como única moldura. A **ordem** das caixas é a contagem do acervo; a **largura** é quantos documentos a caixa tem para dispor. São dois sinais de propósito diferente: LIVROS declara 45 no acervo mas dispõe 3 documentos, e dar-lhe meia página abria um vão que lia como conteúdo que não carregou. Nunca a posição na grade. Numeral tabular em toda contagem. Nenhum emoji na cromia da interface: ícone é desenhado ou não existe. Superfícies do navegador — seleção, caret, barra de rolagem, anel de foco, deslocamento de sublinhado — puxadas dos mesmos tokens, porque com paleta fixa é ali que se lê que a página foi construída e não montada.

**STORY.** O visitante entende em um viewport que isto é um acervo grande, gratuito e ordenado, e que a dimensão é verificável — 172 cursos, 33 projetos, 80 repositórios. Passa a acreditar que a curadoria é real porque vê contagem e não adjetivo. E age de um de dois jeitos: quem chega abre "Comece aqui" e cai no método de estudo; quem volta digita na busca e a página filtra sob o dedo.

**FIRST VIEWPORT.** Faixa de topo curta: "Fursec" em caixa alta com tracking, uma linha dizendo o que é, e o link do repositório. A raposa continua atrás de tudo em opacidade baixa. Imediatamente abaixo, o campo de busca ocupando a largura, com lupa desenhada à esquerda, o atalho `/` à mostra e a contagem de entradas à direita. Então a grade das caixas começa **dentro** do primeiro viewport, liderada pela banda "Comece aqui" em largura inteira — porque é a ação primária para quem chega — seguida por CURSOS 172 e REPOSITÓRIOS 80, cujos números caem bem dentro da dobra. A contagem é o que o olho pega primeiro dentro de cada caixa; o rótulo vem acima dela, menor. Ação primária: o campo de busca tem o foco visível, e "Comece aqui" é a única caixa com peso de fonte elevado.

Duas decisões de ordem, corrigidas depois da revisão de fecho e registradas aqui porque o build as entrega e a versão anterior deste bloco não as nomeava:

- **Ordem estritamente decrescente pela contagem do acervo:** 172, 80, 45, 33, 26, depois 22, 4, 2. A redação anterior deste bloco listava "CURSOS 172, PROJETOS 33 e REPOSITÓRIOS 80", que punha 33 antes de 80 e contradizia a própria cláusula que a governa ("larguras que caem com o peso"). O erro era do contrato, não do render.
- **Segunda banda, ROADMAP, em largura inteira, depois dos catálogos grandes.** Não estava prometida. Entrou porque "5 fases", "4 documentos" e "172 cursos" não medem a mesma coisa: ranquear as dez caixas por número era erro de categoria. A banda tira o Roadmap da fila de contagem e põe as cinco fases numa linha só, lidas da esquerda para a direita, que é o que um roadmap é; os três itens que não são fase vão para um rodapé próprio dentro da banda. Quem chega não perde nada com a descida, porque o passo 2 da banda de entrada é o link do roadmap.

**FORM.** Estrutura escolhida: "Dez caixas contadas", posição 7 da minha lista ordenada por ressonância, assinalada pelo dado (índices 7, 5, 2; 7 lidera) e travada pelo usuário na página de decisão. Seed key `b41a4499`, escopo surface, modo read, caminho code-led.

Elevação doada pelos desafiantes do catálogo, que não podiam vencer aqui porque a paleta está fixada: da bancada de montagem de filme (`operate-a-cutting-bench-select-rail`), a disciplina de que **estado é marca, não matiz** — com um acento só, o que diferencia uma caixa não pode ser cor. A outra metade dessa doação, "posto é contagem de células", foi revista depois da revisão de fecho e **não descreve mais a página**: com a largura atrelada ao volume de documentos, PROJETOS (33) ocupa cerca do dobro da área de LIVROS (45). O posto passou a ser lido pela **ordem de leitura**, e a **área** lê quanto a caixa tem para dispor. São dois eixos, e nenhum deles é o tamanho da letra, que continua fixo nos dez rótulos. Do diagrama de transporte (`wayfinding-cartography-signage-midnight-transit-diagram`), a disciplina de que **rótulo tem tamanho fixo e a composição é que carrega a hierarquia** — os dez rótulos de seção saem todos no mesmo corpo, e a diferença entre eles é a área, não a tipografia.

**FINISH.** unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Copy pass (escopo combinado com o usuário)

Além da composição, o texto do produto inteiro é reescrito para ir direto ao ponto: `index.html`, `README.md`, `ROADMAP.md` e os 45 `.md`. Alvos medidos: 20 antíteses "X, não Y" (8 só no README), 91 headings com emoji decorativo (🧪 ×44, 🚀 ×35, 🔵 ×12), em-dash em excesso (60 em `labs/home-lab.md`).

Preservado: a **legenda de tags** (🇧🇷 🇺🇸 🆓 💸 🎓 🧪 ⭐) nas tabelas dos catálogos. É dado funcional que o leitor filtra, não decoração — distinto do emoji de heading. Remover emoji de heading muda o id da âncora, então todo link `.sec` do índice que aponta para heading alterado é reescrito no mesmo lote, e `check-site.py` é o portão.

## Unresolved

- Nada pendente com o usuário. Escopo de texto (45 arquivos) e liberdade visual (redesenho, com paleta e tipografia fixas) confirmados na entrada.
