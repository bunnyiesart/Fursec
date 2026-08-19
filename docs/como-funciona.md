# 🧭 Como Funciona o Fursec

[⬅️ Voltar ao índice](../README.md)

---

Este arquivo explica **a lógica do repositório**: por que ele é dividido assim, o que tem em cada pasta e como usar no dia a dia. Se você só quer começar a estudar, vá direto para o [README](../README.md).

---

## A ideia central

A maioria das listas de cibersegurança falha por dois motivos: ou é um monte de link sem ordem, ou é uma trilha rígida que não serve para quem tem uma rotina real. O Fursec separa isso em **três perguntas diferentes**, cada uma com seu lugar:

| Pergunta | Responde | Onde fica |
|---|---|---|
| **Quando** eu estudo cada coisa? | Sequência e pré-requisitos | [`ROADMAP.md`](../ROADMAP.md) |
| **O que** existe de material? | Catálogo por área | [`cursos/`](../cursos/), [`livros/`](../livros/), [`labs/`](../labs/) |
| **Como** eu provo que aprendi? | Projetos e documentação | [`projetos/`](../projetos/), [`docs/`](./) |

Separar essas três coisas é o que permite o repositório crescer sem virar bagunça: um curso novo entra em `cursos/`, sem mexer no roadmap. Uma mudança de método entra em `docs/`, sem mexer nos projetos.

---

## O que tem dentro (inventário conferido)

| Pasta | Conteúdo | Quantidade |
|---|---|---|
| [`cursos/`](../cursos/) | Cursos gratuitos em 8 áreas | **154 cursos** |
| [`labs/`](../labs/) | Plataformas práticas, CTFs, wargames | **20 plataformas** |
| [`projetos/`](../projetos/) | Projetos de portfólio (P1–P33) | **33 projetos + 3 templates** |
| [`repositorios/`](../repositorios/) | Ferramentas, labs vulneráveis, awesome lists | **51 repositórios** |
| [`livros/`](../livros/) | Gratuitos (legais) e pagos recomendados | **44 livros** |
| [`recursos/`](../recursos/) | Canais, podcasts, newsletters, comunidades | **27 recursos** |
| [`docs/`](./) | Método de estudo, certificações, trilha PT-BR | 5 documentos |
| [`progresso/`](../progresso/) | Checklist e log semanal | 2 ferramentas de acompanhamento |

**Total:** 48 arquivos markdown · ~260 links externos · ~12.600 palavras.

---

## Como cada pasta funciona

### 📍 `ROADMAP.md` — o esqueleto

Cinco fases (0 a 4) medidas em **horas de estudo, não em datas**. Existe uma tabela de conversão: 5h/semana = ~30 meses; 20h/semana = ~8 meses. Você escolhe seu ritmo e o roadmap se ajusta.

Cada fase tem um **teste de saída** — a condição objetiva para avançar. Não é "terminei o curso", é "consigo fazer X sem consultar nada".

### 📚 `cursos/` — o catálogo

Oito arquivos, um por área. Todo curso vem marcado com:

`🇧🇷` português · `🇺🇸` inglês · `🆓` gratuito · `🎓` emite certificado · `🧪` prático · `⭐` prioridade alta

Se você quer só material em português, existe um atalho: [`docs/trilha-pt-br.md`](./trilha-pt-br.md).

### 🧪 `labs/` — onde você realmente aprende

Separado dos cursos de propósito, porque **50% do seu tempo deveria estar aqui**, não assistindo aula. Contém o "loop correto" de resolver um lab — cujo passo mais importante é o 4: *refazer do zero no dia seguinte, sem consultar nada*.

### 🏗️ `projetos/` — o que gera entrevista

33 projetos numerados P1–P33, cada um com: o que prova, tempo estimado, entregável e repositórios de apoio.

Começa obrigatoriamente por [`00-regras.md`](../projetos/00-regras.md) — ética e legalidade. Testar sistema de terceiros sem autorização é crime, e publicar isso é red flag, não portfólio.

A pasta `templates/` tem três modelos prontos para copiar: README de projeto, writeup de CTF e relatório de pentest no formato de consultoria.

### 🔧 `repositorios/` — as ferramentas

Organizado por **função**, não por popularidade: índices mestres, consulta diária, labs para atacar, ferramentas blue team, ferramentas appsec/cloud, e exemplos de portfólio alheio.

### 📖 `livros/` — leitura

Separado em gratuitos-EN, gratuitos-PT e pagos. Todo link gratuito é **distribuição autorizada** pelo autor ou instituição — nada de site pirata.

### 📄 `docs/` — o método

O arquivo mais importante do repositório inteiro é [`metodo-de-estudo.md`](./metodo-de-estudo.md). Ele responde por que assistir vídeo retém ~29% e testar-se retém ~57%, como configurar Anki, e as 7 armadilhas que travam quase todo mundo.

Também aqui: [`certificacoes.md`](./certificacoes.md) (o que é gratuito de verdade e em que ordem comprar exame) e [`como-documentar.md`](./como-documentar.md).

### 📈 `progresso/` — o acompanhamento

Checklist por fase com campo de data, e um log semanal de 3 minutos. Parece bobo, mas é o que mostra seu ritmo real em vez do ritmo que você imagina ter.

---

## Fluxos de uso

### 🌱 Nunca estudei segurança

```
docs/metodo-de-estudo.md  →  ROADMAP.md (Fase 0)
   →  cursos/00-fundamentos.md  →  cursos/01-introducao-seguranca.md
   →  projetos/01-fundamentais.md (P1: home lab)
   →  progresso/checklist.md
```

### 🎯 Já sei o básico, quero especializar

```
ROADMAP.md (Fase 2, escolha a trilha)
   →  cursos/0X-<trilha>.md  →  labs/<trilha>.md
   →  projetos/0X-<trilha>.md  →  templates/
```

### 💼 Quero montar portfólio agora

```
projetos/00-regras.md  →  escolha 3 projetos de trilhas diferentes
   →  projetos/templates/README-projeto.md
   →  docs/como-documentar.md
```

### 🇧🇷 Só quero material em português

```
docs/trilha-pt-br.md  →  é a trilha inteira, do zero, sem inglês
```

### 💳 Quero saber o que vale pagar

```
docs/certificacoes.md  →  camada gratuita e ordem de compra dos exames
```

---

## Convenções do repositório

- **Toda pasta tem um `README.md`** que serve de índice
- **Todo arquivo tem navegação** de volta ao índice, no topo e no rodapé
- **Nada de link pirata** — se é gratuito, é porque o autor liberou
- **Preço e disponibilidade mudam** — confira antes de se inscrever; o repositório marca a data da última verificação
- **Gratuito e pago são camadas separadas**, nunca misturadas na mesma lista

---

## O que o repositório NÃO é

- ❌ Não é uma lista de tarefas — é um **menu**. Ninguém termina tudo, nem deveria.
- ❌ Não é garantia de emprego — é material organizado. O trabalho continua sendo seu.
- ❌ Não é atalho — a trilha completa é de 8 a 30 meses, dependendo do seu ritmo.
- ❌ Não substitui prática — se você só ler este repositório e não abrir um terminal, não aprendeu nada.

---

## Como contribuir

Curso gratuito faltando, link quebrado, projeto novo: abra issue ou PR. Critérios em [`README.md`](../README.md#-contribuindo). Material em português é especialmente bem-vindo — é onde a área tem menos conteúdo bom e organizado.

---

[⬅️ Voltar ao índice](../README.md)
