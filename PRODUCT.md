# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Sítio estático sem framework, já estabelecido pelo código existente:

- `index.html` — índice de navegação escrito à mão, com filtro client-side em JS puro.
- `assets/site.css` — folha única, tokens em `:root`, tema escuro por `prefers-color-scheme`.
- `tools/build-site.py` — gera `_site/`. Cada `.md` versionado vira uma página HTML; a conversão de markdown **não** é local: o HTML vem da API do GitHub (`Accept: application/vnd.github.html`), para que tabela, checkbox, emoji e âncora saiam idênticos ao que se vê no repositório.
- `tools/check-site.py` — confere links internos, âncoras mortas e páginas órfãs no site gerado.
- Publicação em GitHub Pages (`.github/workflows/pages.yml`), com `.nojekyll`.

## Users

Pessoas no Brasil que querem entrar em cibersegurança e estão estudando sozinhas, sem verba: sem curso pago, sem faculdade da área, sem mentoria. Chegam de dois estados, em proporção parecida:

- **Primeira visita** — não sabe se a trilha serve para ela. Precisa responder "isso é para mim?", "quanto tempo leva?", "é de graça mesmo?" e "por onde começo agora?".
- **Retorno** — já estuda pela trilha e volta para localizar um curso, lab ou projeto específico. Aqui só velocidade de busca importa.

Público secundário: quem contribui com o catálogo (critérios em `CONTRIBUTING.md`).

## Product Purpose

Catálogo curado de material gratuito de cibersegurança, ordenado em uma trilha executável. O valor está tanto no que **não** entra quanto no que entra.

O produto separa três perguntas que a maioria das listas mistura, cada uma com seu lugar no repositório:

| Pergunta | Responde | Onde |
|---|---|---|
| **Quando** estudo cada coisa? | Sequência e pré-requisitos | `ROADMAP.md` |
| **O que** existe de material? | Catálogo por área | `cursos/`, `livros/`, `labs/` |
| **Como** provo que aprendi? | Projetos e documentação | `projetos/`, `docs/` |

Essa separação é o que deixa o catálogo crescer sem virar bagunça: curso novo entra em `cursos/` sem tocar no roadmap.

Sucesso é a pessoa concluir uma fase e ter um artefato publicado que sirva em entrevista — não terminar o catálogo. O repositório é um menu; ninguém termina tudo.

## Positioning

Trilha medida em **horas de estudo**, não em semanas de calendário, com **teste de saída objetivo** por fase: não "terminei o curso", mas "consigo fazer X sem consultar nada". A conversão para calendário é do leitor (5h/semana ≈ 30 meses; 20h/semana ≈ 8 meses).

Somado a isso, e raro no conjunto: cobertura real em português, camada gratuita e paga sempre separadas (nunca na mesma lista), e projeto tratado como entregável com formato definido, não como sugestão.

## Operating Context

- Leitura em duas portas de igual peso: o sítio publicado e o repositório no GitHub. São o mesmo sistema, sem conteúdo exclusivo de nenhum dos dois — o markdown é a fonte única e o texto é idêntico nos dois lugares.
- Navegação por hierarquia de pastas. Toda pasta tem `README.md` de índice; todo arquivo tem volta ao índice no topo e no rodapé.
- Estudo intercalado com lab prático: metade do tempo deveria ser lab, não aula.
- Acompanhamento em `progresso/checklist.md` (por fase, com campo de data) e `progresso/log-semanal.md` (três minutos por semana).
- Consulta pontual é comum: a pessoa chega procurando um item nomeado, não navegando a trilha.

## Capabilities and Constraints

Conteúdo, nos números atuais:

- 172 cursos (171 gratuitos), em 8 arquivos por área
- 33 projetos (P1–P33) + 3 templates: README de projeto, writeup de CTF, relatório de pentest
- 80 repositórios, organizados por função, não por popularidade
- 45 livros, 20 plataformas de lab, 27 recursos (canais, podcasts, comunidades)
- 5 fases de roadmap, 6 trilhas de especialização
- 48 arquivos de conteúdo, 324 links externos, ~17.700 palavras
- Índice do sítio: ~48 links de primeiro nível em 10 seções, mais sublistas de âncoras

Restrições técnicas:

- Markdown é a fonte única. Qualquer coisa que o sítio mostre tem de existir no `.md`.
- O HTML das páginas de conteúdo vem da API do GitHub, não de um renderizador local. O layout controla o envelope e o CSS; não controla a marcação interna do conteúdo.
- Âncoras de heading são derivadas do texto do heading. Mudar um heading muda o id e quebra quem aponta para ele — inclusive as sublistas do índice.
- Sem etapa de build de CSS/JS: o que está em `assets/` é o que é servido.
- `check-site.py` roda no CI e falha em link interno quebrado, âncora inexistente e página órfã.
- Links externos verificados por lychee toda segunda-feira. 403/429/307 são aceitos (runner de datacenter apanha de WAF); 404 falha.

Critérios de entrada no catálogo, que restringem o conteúdo:

- Gratuito de verdade, ou com camada gratuita substancial e marcada. "Grátis por 7 dias" não conta.
- Nada de material pirateado: todo link gratuito precisa ser distribuição autorizada pelo autor ou instituição.
- Link aponta para a página do item, nunca para a home do provedor. Sem texto de link genérico (`[aqui]`, `[link]`).

## Brand Commitments

Fixados pelo usuário como intocáveis:

- **Nome "Fursec" e o mascote raposa.** `assets/mascote.jpg` e o favicon 🦊. Como e onde a raposa aparece é livre; descartá-la não é.
- **Logo ASCII.** O bloco `<pre>` com FURSEC em arte ASCII no topo do `README.md`.
- **Paleta e tipografia atuais.** Os cinco tokens e seus valores — `--bg #ffffff`, `--fg #16171a`, `--muted #6e7178`, `--line #e6e7e9`, `--accent #1a4fd6`, com as contrapartes do tema escuro — e a pilha de fonte de sistema (`ui-sans-serif, -apple-system, "Segoe UI", Roboto…`). Tons derivados desses mesmos tokens são permitidos; paleta nova não.

Outras marcas do produto:

- **Legenda de tags.** 🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva. Isto é **dado funcional** nas tabelas dos catálogos, não decoração: o leitor filtra por ele. Distinto dos emoji decorativos de heading, que não são compromisso nenhum.
- **Voz.** Direta, sem entusiasmo de brochura. Diz o que o produto não faz: não garante emprego, não é atalho, não substitui prática. Avisa que preço e disponibilidade mudam.
- Licença MIT. Repositório `github.com/bunnyiesart/Fursec`.

## Evidence on Hand

Real, no repositório:

- O catálogo inteiro, com contagens verificáveis e links verificados semanalmente no CI.
- Números de retenção citados em `docs/metodo-de-estudo.md`: vídeo passivo ~29%, testar-se ~57%.
- Base legal citada em `projetos/00-regras.md` e no aviso do README: Lei 12.737/2012 e Art. 154-A do Código Penal.
- `assets/mascote.jpg` — única imagem do projeto.

Não existe e não deve ser inventado: depoimento, número de usuários, estrela de repositório, caso de pessoa contratada, parceria, patrocínio, métrica de tráfego.

## Product Principles

1. **Gratuito primeiro.** Nunca pagar pelo aprendizado; no máximo pelo exame. Gratuito e pago são camadas separadas, nunca misturadas na mesma lista.
2. **Fazer vale mais que assistir.** Metade do tempo tem de ser lab. O catálogo existe para levar ao terminal, não para ser lido.
3. **Documentar é aprender.** Quem não consegue explicar por escrito reconheceu o assunto, não aprendeu. Projeto documentado vale mais que certificado básico.
4. **Curadoria é subtração.** O valor está no que fica de fora. Se tudo é prioridade alta, nada é.
5. **Ética não é negociável.** Só se testa o que é seu ou o que se tem autorização escrita para testar.
6. **Honestidade sobre o custo.** A trilha leva de 8 a 30 meses e o produto diz isso em vez de prometer atalho.

## Accessibility & Inclusion

- O mascote de fundo é decorativo por definição: entra como `background` em CSS, não como `<img>`, para que leitor de tela o ignore em vez de anunciar descrição no meio da navegação.
- `prefers-reduced-motion: reduce` já desliga o parallax do fundo. Movimento novo tem de respeitar a mesma consulta.
- Tema claro e escuro por `prefers-color-scheme`, ambos obrigatórios.
- Barreira de idioma é a exclusão que o produto ataca de frente: existe uma trilha só em português (`docs/trilha-pt-br.md`) porque inglês é o filtro que trava a maioria das pessoas na entrada.
- Barreira de custo: o nível 0 do home lab é R$ 0 e está documentado como caminho de primeira classe, não como consolo.
