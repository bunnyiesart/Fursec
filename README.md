<div align="center">

# 🦊 Fursec

**Trilha completa de cibersegurança com material gratuito.**

Cursos · Labs · Livros · Projetos · Repositórios · Método de estudo

🇧🇷 Português · 🇺🇸 English · 100% material gratuito (com camada paga opcional e claramente marcada)

</div>

---

## 🚀 Começar agora

**Nunca estudou segurança?** Faça exatamente isto, nesta ordem:

1. Leia o [método de estudo](./docs/metodo-de-estudo.md) — 10 minutos que economizam meses
2. Abra o [roadmap](./ROADMAP.md) e descubra em que fase você está
3. Pegue **um** curso em [`cursos/01-introducao-seguranca.md`](./cursos/01-introducao-seguranca.md)
4. Monte seu [home lab](./labs/home-lab.md) — dá para começar com R$ 0
5. Registre no [checklist](./progresso/checklist.md)

> Não tente ler tudo. Este repositório é um **menu**, não uma lista de tarefas.

---

## 🧭 A ideia central

A maioria das listas de cibersegurança falha por dois motivos: ou é um monte de link sem ordem, ou é uma trilha rígida que não serve para quem tem uma rotina real. O Fursec separa isso em **três perguntas diferentes**, cada uma com seu lugar:

| Pergunta | Responde | Onde fica |
|---|---|---|
| **Quando** eu estudo cada coisa? | Sequência e pré-requisitos | [`ROADMAP.md`](./ROADMAP.md) |
| **O que** existe de material? | Catálogo por área | [`cursos/`](./cursos/), [`livros/`](./livros/), [`labs/`](./labs/) |
| **Como** eu provo que aprendi? | Projetos e documentação | [`projetos/`](./projetos/), [`docs/`](./docs/) |

Separar essas três coisas é o que permite o repositório crescer sem virar bagunça: um curso novo entra em `cursos/`, sem mexer no roadmap. Uma mudança de método entra em `docs/`, sem mexer nos projetos.

---

## 🗺️ Mapa do repositório

| Pasta | Conteúdo | Quantidade | Comece por |
|---|---|---|---|
| 📍 [`ROADMAP.md`](./ROADMAP.md) | O **quando** — fases em horas de estudo | 5 fases | Aqui |
| 📚 [`cursos/`](./cursos/) | Cursos gratuitos em 8 áreas | **154 cursos** | [Introdução](./cursos/01-introducao-seguranca.md) |
| 🧪 [`labs/`](./labs/) | Home lab + plataformas práticas, CTFs, wargames | **20 plataformas** | [Home lab](./labs/home-lab.md) · [Blue](./labs/blue-team.md) · [Red](./labs/red-team-ctf.md) |
| 🏗️ [`projetos/`](./projetos/) | Projetos de portfólio (P1–P33) | **33 projetos + 3 templates** | [Regras](./projetos/00-regras.md) |
| 🔧 [`repositorios/`](./repositorios/) | Ferramentas, labs vulneráveis, awesome lists | **51 repositórios** | [Awesome lists](./repositorios/awesome-lists.md) |
| 📖 [`livros/`](./livros/) | Gratuitos (legais) e pagos recomendados | **44 livros** | [Gratuitos 🇧🇷](./livros/gratuitos-pt.md) |
| 📄 [`docs/`](./docs/) | Método, certificações, trilha PT-BR | 4 documentos | [Método](./docs/metodo-de-estudo.md) |
| 🎧 [`recursos/`](./recursos/) | Canais, podcasts, comunidades | **27 recursos** | [YouTube](./recursos/youtube.md) |
| 📈 [`progresso/`](./progresso/) | Checklist e log semanal | 2 ferramentas | [Checklist](./progresso/checklist.md) |

**Total:** 47 arquivos markdown · ~260 links externos · ~12.600 palavras.

---

## 🎯 Trilhas

Escolha **uma** por vez. Os fundamentos são ~70% comuns entre elas.

| Trilha | Cursos | Labs | Projetos | Boa para |
|---|---|---|---|---|
| 🔵 **Blue Team / SOC** | [ver](./cursos/02-blue-team.md) | [ver](./labs/blue-team.md) | [P5–P12](./projetos/02-blue-team.md) | Quem quer contratar rápido |
| 🔴 **Red Team / Pentest** | [ver](./cursos/03-red-team.md) | [ver](./labs/red-team-ctf.md) | [P13–P19](./projetos/03-red-team.md) | Quem gosta de quebrar coisas |
| ☁️ **Cloud Security** | [ver](./cursos/04-cloud-security.md) | — | [P20–P24](./projetos/04-cloud.md) | Melhor salário |
| 📋 **GRC / LGPD** | [ver](./cursos/05-grc-compliance.md) | — | [P25–P30](./projetos/05-grc.md) | Menos concorrência, sem lab |
| 🛡️ **AppSec** | [ver](./cursos/06-appsec-devsecops.md) | — | [P31–P33](./projetos/06-appsec.md) | Quem já programa |
| 🟣 **Malware / RE** | [ver](./cursos/07-malware-re-intel.md) | — | P11, P12 | Quem curte baixo nível |

**Ordem sugerida se todas interessam:** Blue Team → Cloud → Red Team → GRC.

---

## 📂 Como cada pasta funciona

### 📍 `ROADMAP.md` — o esqueleto

Cinco fases (0 a 4) medidas em **horas de estudo, não em datas**. Existe uma tabela de conversão: 5h/semana = ~30 meses; 20h/semana = ~8 meses. Você escolhe seu ritmo e o roadmap se ajusta.

Cada fase tem um **teste de saída** — a condição objetiva para avançar. Não é "terminei o curso", é "consigo fazer X sem consultar nada".

### 📚 `cursos/` — o catálogo

Oito arquivos, um por área. Todo curso vem marcado com:

`🇧🇷` português · `🇺🇸` inglês · `🆓` gratuito · `💸` pago · `🎓` emite certificado · `🧪` prático · `⭐` prioridade alta

Se você quer só material em português, existe um atalho: [`docs/trilha-pt-br.md`](./docs/trilha-pt-br.md).

### 🧪 `labs/` — onde você realmente aprende

Separado dos cursos de propósito, porque **50% do seu tempo deveria estar aqui**, não assistindo aula. Contém o "loop correto" de resolver um lab — cujo passo mais importante é o 4: *refazer do zero no dia seguinte, sem consultar nada*.

### 🏗️ `projetos/` — o que gera entrevista

33 projetos numerados P1–P33, cada um com: o que prova, tempo estimado, entregável e repositórios de apoio.

Começa obrigatoriamente por [`00-regras.md`](./projetos/00-regras.md) — ética e legalidade. Testar sistema de terceiros sem autorização é crime, e publicar isso é red flag, não portfólio.

A pasta `templates/` tem três modelos prontos para copiar: README de projeto, writeup de CTF e relatório de pentest no formato de consultoria.

### 🔧 `repositorios/` — as ferramentas

Organizado por **função**, não por popularidade: índices mestres, consulta diária, labs para atacar, ferramentas blue team, ferramentas appsec/cloud, e exemplos de portfólio alheio.

### 📖 `livros/` — leitura

Separado em gratuitos-EN, gratuitos-PT e pagos. Todo link gratuito é **distribuição autorizada** pelo autor ou instituição — nada de site pirata.

### 📄 `docs/` — o método

O arquivo mais importante do repositório inteiro é [`metodo-de-estudo.md`](./docs/metodo-de-estudo.md). Ele responde por que assistir vídeo retém ~29% e testar-se retém ~57%, como configurar Anki, e as 7 armadilhas que travam quase todo mundo.

Também aqui: [`certificacoes.md`](./docs/certificacoes.md) (o que é gratuito de verdade e em que ordem comprar exame) e [`como-documentar.md`](./docs/como-documentar.md).

### 📈 `progresso/` — o acompanhamento

Checklist por fase com campo de data, e um log semanal de 3 minutos. Parece bobo, mas é o que mostra seu ritmo real em vez do ritmo que você imagina ter.

---

## 🔀 Fluxos de uso

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

## 💡 Os 5 princípios do Fursec

1. **Fazer > assistir.** Vídeo passivo retém ~29%. Testar-se retém ~57%. 50% do seu tempo tem que ser lab.
2. **Documentar é aprender.** Se você não consegue explicar por escrito, você reconheceu — não aprendeu.
3. **Projeto > certificado.** Um projeto bem documentado vale mais que três certificados básicos.
4. **Gratuito primeiro.** Nunca pague pelo aprendizado; pague no máximo pelo **exame**. Ver [certificações](./docs/certificacoes.md).
5. **Ética não é negociável.** Só teste o que é seu ou o que você tem autorização escrita para testar.

---

## 📐 Convenções do repositório

- **Toda pasta tem um `README.md`** que serve de índice
- **Todo arquivo tem navegação** de volta ao índice, no topo e no rodapé
- **Nada de link pirata** — se é gratuito, é porque o autor liberou
- **Preço e disponibilidade mudam** — confira antes de se inscrever
- **Gratuito e pago são camadas separadas**, nunca misturadas na mesma lista

---

## 🚫 O que o Fursec NÃO é

- ❌ Não é uma lista de tarefas — é um **menu**. Ninguém termina tudo, nem deveria.
- ❌ Não é garantia de emprego — é material organizado. O trabalho continua sendo seu.
- ❌ Não é atalho — a trilha completa é de 8 a 30 meses, dependendo do seu ritmo.
- ❌ Não substitui prática — se você só ler este repositório e não abrir um terminal, não aprendeu nada.

---

## ⚖️ Aviso legal

Todo o conteúdo aqui é para **fins educacionais e defensivos**. Testar sistemas sem autorização explícita é crime — no Brasil, Lei 12.737/2012 e Código Penal Art. 154-A. Use seu próprio laboratório, plataformas que autorizam explicitamente (TryHackMe, HTB, VulnHub), ou programas de bug bounty dentro do escopo publicado.

## 🤝 Contribuindo

Achou um curso gratuito que não está aqui? Um link quebrado? Abra uma issue ou um PR. Critérios:

- Precisa ser **gratuito de verdade** (ou ter uma camada gratuita substancial — e marcada como tal)
- Nada de link para material pirateado
- Cursos em português são especialmente bem-vindos — é onde a área tem menos conteúdo bom e organizado

## 📄 Licença

[MIT](./LICENSE) — use, copie, adapte à vontade.

---

<div align="center">
<sub>Última atualização: agosto de 2026 · Verifique preços e disponibilidade antes de se inscrever — ofertas gratuitas mudam.</sub>
</div>
