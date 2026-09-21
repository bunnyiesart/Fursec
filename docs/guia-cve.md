# Guia de CVE — ler, pontuar e priorizar vulnerabilidade

[← Voltar ao índice](../README.md)

---

Todo mundo aprende a rodar scanner. Pouca gente aprende a olhar o resultado e decidir **o que corrigir primeiro**. Este guia é sobre isso.

> **Uma CVE não é uma nota de gravidade.** É um identificador, só isso: `CVE-2021-44228` quer dizer "a quarenta e quatro mil duzentos e vigésima oitava vulnerabilidade catalogada em 2021". Quem dá nota é o CVSS, e quem diz se importa para você é outra coisa ainda.

---

## Quem é quem no ecossistema

Confundir essas cinco coisas é o erro mais comum de quem começa.

| Sigla | Quem mantém | O que é | O que **não** é |
|---|---|---|---|
| **CVE** | [MITRE](https://www.cve.org/) | O identificador único da vulnerabilidade | Não é gravidade nem prioridade |
| **NVD** | [NIST](https://nvd.nist.gov/) | Base que enriquece a CVE com CVSS, CWE e produtos afetados | Não é a fonte primária do ID |
| **CVSS** | [FIRST](https://www.first.org/cvss/) | Nota de 0 a 10 da gravidade **técnica** | Não mede risco no seu ambiente |
| **CWE** | [MITRE](https://cwe.mitre.org/) | A **classe** do defeito (ex.: CWE-89, injeção SQL) | Não é uma vulnerabilidade específica |
| **EPSS** | [FIRST](https://www.first.org/epss/) | Probabilidade de exploração nos próximos 30 dias | Não diz se já foi explorada |
| **KEV** | [CISA](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Catálogo do que **comprovadamente** está sendo explorado | Não é exaustivo |

A relação entre elas: uma **CVE** é uma instância de uma **CWE**, recebe nota **CVSS** na **NVD**, tem probabilidade **EPSS** de ser explorada, e se já estiver sendo explorada entra no **KEV**.

---

## Como ler um registro de CVE

Pegue `CVE-2021-44228` (Log4Shell) como exemplo e abra os dois lados:

- **Fonte do identificador:** [cve.org/CVERecord?id=CVE-2021-44228](https://www.cve.org/CVERecord?id=CVE-2021-44228)
- **Enriquecido:** [nvd.nist.gov/vuln/detail/CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)

### Os campos que importam

| Campo | O que você tira dele |
|---|---|
| **Description** | O mecanismo da falha, em uma frase. Leia isto antes da nota |
| **CVSS vector** | Como a nota foi montada. Vale mais que o número |
| **CWE** | A classe do defeito — diz se o problema é sistêmico no seu código |
| **CPE / Known Affected** | As versões exatas afetadas. É aqui que você descobre se te atinge |
| **References** | Avisos do fabricante, patch, análise técnica, prova de conceito |

**O campo mais ignorado é o CPE.** Ele lista produto, fornecedor e faixa de versão. Sem ler isso você corrige o que não precisava, ou pior, acha que está seguro porque a versão "parece" diferente.

### Decorar o vetor CVSS vale a pena

`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` — nota 10.0. Traduzido:

| Sigla | Valor | Significado |
|---|---|---|
| `AV:N` | Network | Explorável pela rede, sem estar na máquina |
| `AC:L` | Low | Não precisa de condição especial |
| `PR:N` | None | **Não precisa de privilégio nenhum** |
| `UI:N` | None | Não precisa de usuário clicar em nada |
| `S:C` | Changed | Escapa do componente e afeta outros |
| `C/I/A:H` | High | Compromete confidencialidade, integridade e disponibilidade |

Compare com `AV:L/AC:H/PR:H/UI:R` — precisa de acesso local, condição difícil, privilégio alto e um usuário cooperando. Mesmo que a nota base seja 7.0, é um problema completamente diferente.

Calculadora oficial: [first.org/cvss/calculator/3.1](https://www.first.org/cvss/calculator/3.1). Rode o vetor de três CVEs reais nela e o formato deixa de ser sopa de letra.

---

## As três perguntas da priorização

CVSS sozinho é um péssimo critério de prioridade, porque metade das CVEs recebe nota alta. Use três eixos:

### 1. Está sendo explorada? → KEV

O [catálogo KEV da CISA](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) lista o que tem exploração confirmada no mundo real. Se a sua CVE está lá, **ela sobe ao topo**, independentemente da nota.

```bash
# baixar o catálogo e procurar uma CVE
curl -s https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json \
  | jq -r '.vulnerabilities[] | select(.cveID=="CVE-2021-44228") | .cveID, .dateAdded, .requiredAction'
```

### 2. Qual a chance de ser explorada? → EPSS

O [EPSS](https://www.first.org/epss/) dá uma probabilidade de 0 a 1 de exploração nos próximos 30 dias, baseada em dados observados.

```bash
# consultar o EPSS de uma CVE
curl -s "https://api.first.org/data/v1/epss?cve=CVE-2021-44228" \
  | jq -r '.data[] | "\(.cve)  epss=\(.epss)  percentil=\(.percentile)"'
```

Na prática: uma CVE com CVSS 9.8 e EPSS 0.0004 é menos urgente que uma CVSS 7.5 com EPSS 0.87.

### 3. Te atinge de verdade? → o seu inventário

A pergunta que nenhuma base responde. Depende de:

- Você **usa** o produto e a versão afetada?
- O componente está **exposto** à rede, ou atrás de autenticação e segmentação?
- Existe **mitigação** já aplicada que quebra a condição de exploração?
- O que roda ali é **crítico** para o negócio?

Uma CVSS 10.0 num serviço interno, desligado, sem dado, atrás de firewall, perde para uma CVSS 6.5 no seu portal público de clientes.

> **A regra prática:** `KEV` → corrija agora. `EPSS alto + exposto` → corrija esta semana. `CVSS alto, EPSS baixo, não exposto` → entra na fila normal de correção.

---

## Como descobrir se você é afetado

```bash
# o que está instalado, com versão
dpkg -l | grep -i openssl              # Debian/Ubuntu
rpm -qa | grep -i openssl              # RHEL/Fedora

# dependências de aplicação
npm audit                              # Node
pip-audit                              # Python
composer audit                         # PHP

# imagem de contêiner e sistema de arquivos
trivy image minha-imagem:tag
grype dir:.
```

**Ferramentas:** [Trivy](https://github.com/aquasecurity/trivy) · [Grype](https://github.com/anchore/grype) · [pip-audit](https://github.com/pypa/pip-audit) · [OSV-Scanner](https://github.com/google/osv-scanner)

Para vulnerabilidade em dependência de código, a base mais precisa é a [OSV](https://osv.dev/), porque ela trabalha por versão de pacote em vez de CPE — e CPE erra muito em ecossistema de linguagem.

---

## Achar prova de conceito sem se machucar

| Fonte | Observação |
|---|---|
| [Exploit-DB](https://www.exploit-db.com/) | Curada, acessível offline por `searchsploit` |
| [GitHub](https://github.com/) | Onde aparece primeiro, e onde tem mais armadilha |
| [Nuclei templates](https://github.com/projectdiscovery/nuclei-templates) | Detecção, não exploração — ideal para confirmar exposição |
| [Metasploit](https://github.com/rapid7/metasploit-framework) | Quando existe módulo, é a opção mais segura |

**Três regras, sempre:**

1. **Leia o código antes de executar.** PoC público com backdoor é comum, especialmente em repositório novo com CVE da moda.
2. **Rode em lab isolado**, nunca contra produção, nunca da sua máquina principal.
3. **Desconfie de binário.** Se o "exploit" é um `.exe` ou um script obfuscado, não é exploit, é malware.

Detectar exposição sem explorar é quase sempre suficiente e sempre mais seguro:

```bash
nuclei -u https://example.com -t http/cves/2021/CVE-2021-44228.yaml
```

---

## Acompanhar CVE nova

| Fonte | Para quê |
|---|---|
| [NVD — feed de dados](https://nvd.nist.gov/vuln/data-feeds) | Tudo, em JSON, para automatizar |
| [KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | O que virou urgência |
| [CISA Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) | Aviso e análise oficial |
| [OSV](https://osv.dev/) | Vulnerabilidade em dependência, por ecossistema |
| [GitHub Advisory Database](https://github.com/advisories) | Boa cobertura de biblioteca |
| Aviso do próprio fabricante | A fonte da verdade sobre patch |
| [SANS Internet Storm Center](https://isc.sans.edu/) | Leitura diária curta do que está acontecendo |

Assine o do fabricante do que **você** usa. Acompanhar tudo é impossível e inútil.

---

## Os erros mais comuns

| Erro | Por que é errado |
|---|---|
| Tratar CVSS como prioridade | Mede gravidade técnica, não risco seu. Metade das CVEs é "alta" |
| Ignorar o vetor e olhar só a nota | `PR:H/UI:R` e `PR:N/UI:N` com a mesma nota são problemas diferentes |
| Não ler o CPE | Você corrige versão que não era afetada e deixa a que era |
| Rodar PoC do GitHub sem ler | Backdoor, ou serviço derrubado |
| Achar que "sem CVE" é "sem vulnerabilidade" | Muita falha nunca recebe CVE, e configuração errada nunca recebe |
| Confiar só no scanner | Falso positivo é a regra; achado precisa de confirmação manual |
| Corrigir sem registrar | Sem data e responsável, ninguém sabe se foi corrigido |

---

## Transforme isto em portfólio

Escrever uma análise própria de CVE é um dos artefatos que mais mostra maturidade, e ninguém precisa de autorização para fazer.

**Escolha uma CVE recente e relevante, e escreva:**

1. O que é o produto, e quem o usa
2. O mecanismo da falha, na sua palavra, com o trecho de código quando o patch é público
3. A leitura do vetor CVSS, e se você concorda com a nota
4. CWE e se o defeito é sistêmico naquele projeto
5. Como detectar exposição no seu ambiente, com comando
6. A mitigação, e a correção definitiva
7. O que o diff do patch mudou

Comparar o commit de correção com a versão vulnerável é o exercício que mais ensina. É um passo do [projeto P12](../projetos/02-blue-team.md) e casa direto com [`docs/como-documentar.md`](./como-documentar.md).

---

## Fontes

- [CVE Program](https://www.cve.org/) — a fonte do identificador
- [NVD](https://nvd.nist.gov/) — registro enriquecido, CVSS e CPE
- [Especificação do CVSS 3.1](https://www.first.org/cvss/v3.1/specification-document) — o que cada métrica significa
- [EPSS](https://www.first.org/epss/) — modelo e API de probabilidade de exploração
- [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — exploração confirmada
- [CWE](https://cwe.mitre.org/) — classes de defeito
- [OSV](https://osv.dev/) — vulnerabilidade por versão de pacote

---

[← Voltar ao índice](../README.md)
