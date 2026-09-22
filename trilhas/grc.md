# GRC / LGPD

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)

---

Governança, risco e conformidade. É a única trilha que **não precisa de home lab** — e a que tem mais material bom em português, porque a LGPD é lei brasileira.

## O que a função faz de fato

- Escrever e manter política de segurança que as pessoas realmente consigam seguir
- Medir a distância entre o que a norma pede e o que a empresa faz — o *gap assessment*
- Manter registro de risco: identificar, avaliar, tratar, aceitar, revisar
- Avaliar fornecedor antes de contratar, e reavaliar depois
- Preparar e conduzir auditoria
- Na LGPD: mapear dado pessoal, base legal, atender titular, responder incidente

O trabalho é **escrita e conversa**, não ferramenta. Quem não gosta de escrever não dura.

### Esta trilha é para você se

Você escreve bem, tem paciência com processo, consegue traduzir técnico para executivo e vice-versa. Vem bem de área jurídica, auditoria, qualidade ou administração.

### Não é, se

Você quer trabalho técnico. É a trilha mais distante do terminal — e isso é uma característica, não um defeito.

---

## Pré-requisito

Fases 0 e 1 do [roadmap](../ROADMAP.md) continuam valendo, mas com peso diferente: você precisa **entender** o controle técnico para exigi-lo, não precisa implementá-lo.

O que mais pesa aqui: vocabulário técnico correto (para não escrever política impossível de cumprir) e noção de como a empresa funciona.

> **Vantagem real desta trilha:** sem lab, sem hardware, sem custo de nuvem. Você precisa de um editor de texto e de leitura. É a trilha mais acessível para quem não tem máquina boa.

---

## O caminho, em ordem

Fase 2D do roadmap, ~90h — a mais curta das quatro mapeadas.

| # | O que fazer | Onde |
|---|---|---|
| 1 | Fundamentos de GRC e os frameworks | [`cursos/05-grc-compliance.md`](../cursos/05-grc-compliance.md) |
| 2 | Ler a LGPD inteira, uma vez, do começo ao fim | [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) |
| 3 | Material oficial da autoridade brasileira | [Guias e estudos da ANPD](https://www.gov.br/anpd/pt-br/centrais-de-conteudo) |
| 4 | NIST CSF 2.0, e fazer um gap assessment de verdade | [NIST CSF](https://www.nist.gov/cyberframework) |
| 5 | CIS Controls IG1, controle por controle | [CIS Controls](https://www.cisecurity.org/controls) |
| 6 | ISO/IEC 27001 e 27002: estrutura e Anexo A | [`cursos/05-grc-compliance.md`](../cursos/05-grc-compliance.md) |

**Ordem importa aqui:** LGPD primeiro se você está no Brasil, porque é lei e cria obrigação. Framework depois, porque é escolha.

---

## Os projetos desta trilha

P25–P30, em [`projetos/05-grc.md`](../projetos/05-grc.md). São os projetos mais fáceis de fazer sem infraestrutura e os mais fáceis de fazer mal — texto genérico não prova nada.

| Projeto | Por que importa |
|---|---|
| [P26 — Gap assessment NIST CSF 2.0](../projetos/05-grc.md#p26--gap-assessment-nist-csf-20) | O artefato central da função |
| [P27 — Registro de riscos + metodologia](../projetos/05-grc.md#p27--registro-de-riscos--metodologia) | A **metodologia** é o que separa do amador |
| [P28 — Programa LGPD completo 🇧🇷](../projetos/05-grc.md#p28--programa-lgpd-completo-) | Diferencial claro no mercado brasileiro |
| [P30 — CIS Controls IG1](../projetos/05-grc.md#p30--implementação-de-cis-controls-ig1) | Mostra que você sai do papel |

Se fizer só um: **P28**. É específico do Brasil, tem demanda real e pouca gente faz bem.

**Como não fazer mal:** invente uma empresa fictícia com detalhe — setor, tamanho, o que ela coleta, que sistema usa — e escreva para ela. Política genérica que serviria para qualquer empresa não serve para nenhuma.

---

## O que você vai usar de verdade

| Categoria | O que é |
|---|---|
| Frameworks | [NIST CSF 2.0](https://www.nist.gov/cyberframework), ISO/IEC 27001 e 27002, [CIS Controls](https://www.cisecurity.org/controls) |
| Lei brasileira | [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), regulamentação e guias da [ANPD](https://www.gov.br/anpd/pt-br/centrais-de-conteudo) |
| Maturidade | [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [SAMM](https://owaspsamm.org/) para desenvolvimento |
| Risco | ISO/IEC 27005, [NIST SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final), FAIR |
| Privacidade | ISO/IEC 27701, avaliação de impacto (DPIA/RIPD) |
| Ferramenta | Planilha, editor de texto e um controle de versão. Sério |

Boa parte do valor está em saber **qual** framework aplicar e até onde, não em decorar todos.

---

## Certificações

- **Gratuito:** os cursos da faixa gratuita em [`docs/certificacoes.md`](../docs/certificacoes.md), e o material da ANPD
- **Primeiro exame que vale:** ISO 27001 Lead Implementer ou Foundation, se a sua empresa segue ISO
- **No Brasil, especificamente:** certificação em LGPD/DPO tem procura real
- **Longo prazo:** CISA (auditoria) ou CISM (gestão) — as duas pedem experiência comprovada

Nesta trilha, certificação pesa mais que em Red Team, porque auditoria valoriza credencial formal.

---

## Teste de saída

Você terminou esta trilha quando consegue, **sem consultar nada**:

- [ ] Explicar a diferença entre política, norma, procedimento e diretriz
- [ ] Citar as bases legais da LGPD e dar um exemplo de uso de cada
- [ ] Conduzir um gap assessment e apresentar o resultado para diretoria em uma página
- [ ] Montar registro de risco com metodologia explícita de probabilidade e impacto
- [ ] Dizer a diferença entre risco inerente e risco residual, com exemplo
- [ ] Explicar o que fazer nas primeiras 24h de um incidente com dado pessoal
- [ ] Escrever uma política que alguém consiga cumprir sem parar de trabalhar

O último é o mais difícil e o mais raro.

---

## O que perguntam em entrevista

- "Como você prioriza controle com orçamento limitado?" — risco sobre esforço
- "A área de negócio recusa um controle. O que você faz?" — negociação, risco aceito formalmente
- "Explique LGPD para quem nunca ouviu falar" — tradução, em dois minutos
- "Diferença entre conformidade e segurança" — conformidade é piso, não teto
- "Como você mede se o programa está funcionando?" — indicador, não sensação

---

## Próximos passos

- **[Blue Team](./blue-team.md)** — se você quiser a base técnica para exigir controle com autoridade
- **[Cloud Security](./cloud.md)** — conformidade em nuvem é onde mais falta gente que entenda as duas partes

---

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)
