<div align="center">

<pre align="center">
🦊

███████╗██╗   ██╗██████╗ ███████╗███████╗ ██████╗
██╔════╝██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗  ██║   ██║██████╔╝███████╗█████╗  ██║&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
██╔══╝  ██║   ██║██╔══██╗╚════██║██╔══╝  ██║&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
██║     ╚██████╔╝██║  ██║███████║███████╗╚██████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝
</pre>

# Fursec

**Trilha completa de cibersegurança com material gratuito.**

Cursos · Labs · Livros · Projetos · Repositórios · Método de estudo

🇧🇷 Português · 🇺🇸 English · 100% material gratuito (com camada paga opcional e claramente marcada)

</div>

---

## 🚀 Começar agora

**Nunca estudou segurança?** Faça exatamente isto, nesta ordem:

1. Leia o [método de estudo](./docs/metodo-de-estudo.md) — 10 minutos que economizam meses
2. Abra o [roadmap](./ROADMAP.md) e comece pela **Fase 0**
3. Pegue **um** curso: [`cursos/00-fundamentos.md`](./cursos/00-fundamentos.md) se você é novo em TI, ou [`cursos/01-introducao-seguranca.md`](./cursos/01-introducao-seguranca.md) se já sabe o básico
4. Monte seu [home lab](./labs/home-lab.md) — dá para começar com R$ 0. Documentá-lo **é** o [projeto P1](./projetos/01-fundamentais.md), não a preparação para ele
5. Registre no [checklist](./progresso/checklist.md)

> Não tente ler tudo. Este repositório é um **menu**, não uma lista de tarefas. Ninguém termina tudo, nem deveria.

**Não é o seu caso?** Escolha o atalho:

| Se você… | Vá direto para |
|---|---|
| Já sabe o básico e quer especializar | [`ROADMAP.md`](./ROADMAP.md) Fase 2 → escolha a trilha → `cursos/` + `labs/` + `projetos/` da trilha |
| Quer montar portfólio agora | [`projetos/00-regras.md`](./projetos/00-regras.md) → 3 projetos de trilhas diferentes → [`templates/`](./projetos/templates/) → [`docs/como-documentar.md`](./docs/como-documentar.md) |
| Só quer material em português | [`docs/trilha-pt-br.md`](./docs/trilha-pt-br.md) — é a trilha inteira, do zero, sem inglês |
| Quer saber o que vale pagar | [`docs/certificacoes.md`](./docs/certificacoes.md) — camada gratuita e ordem de compra dos exames |

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

| Pasta | O que é — e o detalhe que importa | Quantidade | Comece por |
|---|---|---|---|
| 📍 [`ROADMAP.md`](./ROADMAP.md) | O **quando**. Cinco fases (0 a 4), medidas em **horas, não em datas** — 5h/semana ≈ 30 meses, 20h/semana ≈ 8 meses. Cada fase tem um **teste de saída** objetivo: não é "terminei o curso", é "consigo fazer X sem consultar nada". | 5 fases | Aqui |
| 📚 [`cursos/`](./cursos/) | O catálogo: oito arquivos, um por área. Todo curso vem marcado com idioma, gratuidade, certificado e prioridade. | **155 cursos** (154 gratuitos) | [Introdução](./cursos/01-introducao-seguranca.md) |
| 🧪 [`labs/`](./labs/) | Onde você realmente aprende — **50% do seu tempo deveria estar aqui**, não assistindo aula. Traz o "loop correto" de resolver um lab, cujo passo mais importante é o 4: *refazer do zero no dia seguinte, sem consultar nada*. | **20 plataformas** | [Home lab](./labs/home-lab.md) · [Blue](./labs/blue-team.md) · [Red](./labs/red-team-ctf.md) |
| 🏗️ [`projetos/`](./projetos/) | O que gera entrevista. P1–P33, cada um com: o que prova, tempo estimado, entregável e repositórios de apoio. `templates/` tem 3 modelos prontos: README de projeto, writeup de CTF e relatório de pentest no formato de consultoria. Começa por [`00-regras.md`](./projetos/00-regras.md): testar sistema de terceiros sem autorização é crime, e publicar isso é red flag, não portfólio. | **33 projetos + 3 templates** | [Regras](./projetos/00-regras.md) — **obrigatório** |
| 🔧 [`repositorios/`](./repositorios/) | Ferramentas organizadas por **função, não por popularidade**: índices mestres, consulta diária, labs para atacar, blue team, appsec/cloud, e exemplos de portfólio alheio. | **51 repositórios** | [Awesome lists](./repositorios/awesome-lists.md) |
| 📖 [`livros/`](./livros/) | Gratuitos-EN, gratuitos-PT e pagos, separados. Todo link gratuito é **distribuição autorizada** pelo autor ou instituição. | **45 livros** | [Gratuitos 🇧🇷](./livros/gratuitos-pt.md) |
| 📄 [`docs/`](./docs/) | O método. [`metodo-de-estudo.md`](./docs/metodo-de-estudo.md) é o arquivo mais importante do repositório: por que vídeo retém ~29% e testar-se retém ~57%, como configurar Anki, e as 7 armadilhas que travam quase todo mundo. | 4 documentos | [Método](./docs/metodo-de-estudo.md) |
| 🎧 [`recursos/`](./recursos/) | Canais, podcasts e comunidades. | **27 recursos** | [YouTube](./recursos/youtube.md) |
| 📈 [`progresso/`](./progresso/) | Checklist por fase com campo de data, e um log semanal de 3 minutos. Parece bobo, mas é o que mostra seu ritmo real em vez do ritmo que você imagina ter. | 2 ferramentas | [Checklist](./progresso/checklist.md) |

**Total:** 48 arquivos de conteúdo · 276 links externos · ~17.000 palavras.

<sub>**Legenda usada nos catálogos:** 🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva</sub>

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

## 💡 Como este repositório pensa

Cinco princípios, e o que cada um implica na prática:

| Princípio | Na prática |
|---|---|
| **Fazer > assistir** | Vídeo passivo retém ~29%; testar-se retém ~57%. Metade do seu tempo tem que ser lab. |
| **Documentar é aprender** | Se você não consegue explicar por escrito, você reconheceu — não aprendeu. |
| **Projeto > certificado** | Um projeto bem documentado vale mais que três certificados básicos. Certificado passa pelo RH; o writeup passa pela entrevista técnica. |
| **Gratuito primeiro** | Nunca pague pelo aprendizado; pague no máximo pelo **exame**. Gratuito e pago são camadas separadas, nunca misturadas na mesma lista. Ver [certificações](./docs/certificacoes.md). |
| **Ética não é negociável** | Só teste o que é seu ou o que você tem autorização escrita para testar. |

E o que ele **não** é: não garante emprego (é material organizado — o trabalho continua seu), não é atalho (a trilha completa leva de 8 a 30 meses), e não substitui prática — se você só ler isto e não abrir um terminal, não aprendeu nada.

**Convenções:** toda pasta tem um `README.md` de índice · todo arquivo tem navegação de volta ao índice, no topo e no rodapé · nada de link pirata · preço e disponibilidade mudam, confira antes de se inscrever.

---

## ⚖️ Aviso legal

Todo o conteúdo aqui é para **fins educacionais e defensivos**. Testar sistemas sem autorização explícita é crime — no Brasil, Lei 12.737/2012 e Código Penal Art. 154-A. Use seu próprio laboratório, plataformas que autorizam explicitamente (TryHackMe, HTB, VulnHub), ou programas de bug bounty dentro do escopo publicado.

## 🤝 Contribuindo

Achou um curso gratuito que não está aqui? Um link quebrado? Abra uma issue ou um PR — o [`CONTRIBUTING.md`](./CONTRIBUTING.md) tem os critérios e o formato das tabelas. Em resumo:

- Precisa ser **gratuito de verdade** (ou ter uma camada gratuita substancial — e marcada como tal)
- Nada de link para material pirateado
- Cursos em português são especialmente bem-vindos — é onde a área tem menos conteúdo bom e organizado

Os links do repositório são [verificados automaticamente](./.github/workflows/link-check.yml) toda semana.

## 📄 Licença

[MIT](./LICENSE) — use, copie, adapte à vontade.

---

<div align="center">
<sub>Última atualização: agosto de 2026 · Verifique preços e disponibilidade antes de se inscrever — ofertas gratuitas mudam.</sub>
</div>
