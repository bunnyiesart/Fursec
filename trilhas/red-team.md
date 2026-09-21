# Red Team / Pentest

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)

---

Ofensiva: encontrar a falha antes de quem tem má intenção, e explicar de um jeito que o time consiga corrigir.

> **Leia [`projetos/00-regras.md`](../projetos/00-regras.md) antes de qualquer coisa.** Testar sistema de terceiros sem autorização escrita é crime — Lei 12.737/2012 e Art. 154-A. Nesta trilha isso não é detalhe burocrático: é a diferença entre profissão e processo criminal.

## O que a função faz de fato

Ao contrário da imagem, a maior parte do tempo não é explorar. Num teste real:

- **Escopo e autorização** vêm primeiro, sempre por escrito
- **Enumeração** é a fase mais longa, e é ela que decide o resultado
- **Exploração** é a menor fatia do tempo
- **Relatório** é o entregável — o único artefato que o cliente lê

O guia completo, fase a fase, está em [`docs/pentest-completo.md`](../docs/pentest-completo.md).

### Esta trilha é para você se

Você é teimoso de um jeito produtivo, gosta de entender como as coisas funcionam por dentro, e **aceita escrever**. Pentester que não escreve relatório bom não é contratado duas vezes.

### Não é, se

Você quer só o acesso e não a explicação. Ou se espera mercado de entrada fácil: há menos vaga júnior aqui que em Blue Team, e quase toda vaga pede portfólio.

---

## Pré-requisito

Fases 0 e 1 do [roadmap](../ROADMAP.md), ~180h. E aqui o pré-requisito é mais rígido que nas outras trilhas: **sem Linux, redes e um pouco de programação, você só roda ferramenta sem entender a saída**.

O que mais pesa: **HTTP** (porque a maior parte do trabalho é web), **Active Directory** (porque é o alvo corporativo padrão) e **linha de comando**.

---

## O caminho, em ordem

Fase 2B do roadmap, ~120h.

| # | O que fazer | Onde |
|---|---|---|
| 1 | Fundamentos de pentest e metodologia | [`cursos/03-red-team.md`](../cursos/03-red-team.md) |
| 2 | **Web, a fundo** — é onde está o trabalho | [PortSwigger Web Security Academy](https://portswigger.net/web-security) |
| 3 | Máquinas guiadas, para pegar o loop | [TryHackMe](https://tryhackme.com/) |
| 4 | Máquinas sem guia, para aprender a travar | [Hack The Box](https://www.hackthebox.com/), [VulnHub](https://www.vulnhub.com/) |
| 5 | Active Directory no seu lab | [GOAD](https://github.com/Orange-Cyberdefense/GOAD) |
| 6 | Escrever relatório de verdade | [`projetos/templates/relatorio-pentest.md`](../projetos/templates/relatorio-pentest.md) |

**Sobre o passo 2:** a Web Security Academy do PortSwigger é gratuita e é o melhor material de segurança web que existe, pago ou não. Se você fizer só uma coisa desta lista, faça ela inteira.

Plataformas completas: [`labs/red-team-ctf.md`](../labs/red-team-ctf.md). Ambientes para atacar: [`repositorios/labs-vulneraveis.md`](../repositorios/labs-vulneraveis.md).

### O loop correto de um lab

Está em [`docs/metodo-de-estudo.md`](../docs/metodo-de-estudo.md), e o passo que todo mundo pula é o 4: **refazer do zero no dia seguinte, sem consultar nada.** Resolver com walkthrough e seguir em frente não ensina.

---

## Os projetos desta trilha

P13–P19, em [`projetos/03-red-team.md`](../projetos/03-red-team.md).

| Projeto | Por que importa |
|---|---|
| [P13 — Relatório de pentest profissional](../projetos/03-red-team.md#p13--relatório-de-pentest-profissional) | O artefato que prova que você é contratável |
| [P15 — Pentest do OWASP Juice Shop](../projetos/03-red-team.md#p15--pentest-completo-do-owasp-juice-shop) | Cobertura web completa, num alvo que autoriza |
| [P16 — Attack path em Active Directory](../projetos/03-red-team.md#p16--attack-path-em-active-directory) | O cenário corporativo real |
| [P18 — Primeiro report válido de bug bounty](../projetos/03-red-team.md#p18--primeiro-report-válido-de-bug-bounty) | Validação externa, de terceiro |

Se fizer só um: **P13**. E faça sobre um alvo de CTF, escrevendo como se fosse cliente pagante — formato de consultoria, sumário executivo, severidade justificada por [CVSS](https://www.first.org/cvss/calculator/3.1).

---

## Ferramentas que você vai usar de verdade

| Categoria | Ferramentas |
|---|---|
| Interceptação web | [Burp Suite](https://portswigger.net/burp/communitydownload) (a Community basta para aprender) |
| Varredura | [nmap](https://nmap.org/), [naabu](https://github.com/projectdiscovery/naabu) |
| Recon | [subfinder](https://github.com/projectdiscovery/subfinder), [amass](https://github.com/owasp-amass/amass), [httpx](https://github.com/projectdiscovery/httpx) |
| Conteúdo e fuzzing | [ffuf](https://github.com/ffuf/ffuf), [feroxbuster](https://github.com/epi052/feroxbuster), [SecLists](https://github.com/danielmiessler/SecLists) |
| Active Directory | [BloodHound](https://github.com/SpecterOps/BloodHound), [Impacket](https://github.com/fortra/impacket), [NetExec](https://github.com/Pennyw0rth/NetExec) |
| Exploração | [Metasploit](https://github.com/rapid7/metasploit-framework), [sqlmap](https://github.com/sqlmapproject/sqlmap) |
| Escalada | [PEASS-ng](https://github.com/peass-ng/PEASS-ng), [GTFOBins](https://gtfobins.github.io/), [LOLBAS](https://lolbas-project.github.io/) |
| Senhas | [hashcat](https://github.com/hashcat/hashcat), [John](https://github.com/openwall/john) |
| Consulta diária | [HackTricks](https://book.hacktricks.wiki/), [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) |

---

## Certificações

Ordem e faixa gratuita em [`docs/certificacoes.md`](../docs/certificacoes.md). Para esta trilha:

- **Gratuito:** trilhas da TryHackMe, [Bugcrowd University](https://www.bugcrowd.com/hackers/bugcrowd-university/), [PortSwigger](https://portswigger.net/web-security) (o conteúdo, não certificado)
- **O primeiro exame que muda entrevista:** um prático e hands-on. PNPT ou CPTS custam menos que OSCP e são igualmente respeitados tecnicamente
- **OSCP:** ainda é o nome que o RH reconhece, mas é caro. Não é porta de entrada, é investimento de fase 3

Nesta trilha, portfólio pesa mais que sigla. Um P13 bem escrito abre mais porta que um certificado básico.

---

## Teste de saída

Você terminou esta trilha quando consegue, **sem consultar nada**:

- [ ] Explicar o que precisa estar no documento de autorização antes de um teste
- [ ] Enumerar um host do zero e justificar cada comando que rodou
- [ ] Explicar e demonstrar as classes do [OWASP Top 10](https://owasp.org/www-project-top-ten/) num alvo de lab
- [ ] Fazer Kerberoasting num AD e explicar por que funciona
- [ ] Escalar privilégio em Linux e em Windows, por caminhos diferentes
- [ ] Escrever um achado com impacto de negócio, passo de reprodução e severidade justificada
- [ ] Dizer por que você **não** rodaria um exploit específico num ambiente de produção

O último é o que separa profissional de entusiasta.

---

## O que perguntam em entrevista

- "Descreva sua metodologia num teste externo" — quer ver processo, não ferramenta
- "Achou uma SQLi. E agora?" — testa se você pensa em impacto e em limite de escopo
- "Como você explica risco para quem não é técnico?" — o sumário executivo virou pergunta
- "Qual foi a falha mais interessante que você achou?" — traga uma do lab, com detalhe
- "O cliente diz que o achado é falso positivo. Como você responde?" — evidência, reprodução, calma

---

## Próximos passos

- **[AppSec / DevSecOps](./appsec.md)** — se o que te prendeu foi a parte web e de código
- **[Cloud Security](./cloud.md)** — porque o alvo corporativo está migrando para lá
- **[Malware / Engenharia reversa](./malware-re.md)** — se o que te prendeu foi o baixo nível

E o [guia de pentest completo](../docs/pentest-completo.md), que é a referência para consultar durante o trabalho, não para ler uma vez.

---

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)
