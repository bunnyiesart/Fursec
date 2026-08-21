# 🗺️ Roadmap — Fursec

> O **quando**. Fases medidas em horas de estudo, não em datas.
> Catálogo completo do que existe: [`cursos/`](./cursos/) · Certificações: [`docs/certificacoes.md`](./docs/certificacoes.md)

---

## Como ler este roadmap

Cada fase tem um **orçamento de horas**. Converta em tempo de calendário usando o seu próprio ritmo:

| Seu ritmo | Fases 0+1 (~180h) | Até a Fase 3 (~450h) | Roadmap completo (~650h) |
|---|---|---|---|
| 5 h/semana | ~9 meses | ~21 meses | ~30 meses |
| 10 h/semana | ~4,5 meses | ~11 meses | ~15 meses |
| 20 h/semana | ~2 meses | ~5,5 meses | ~8 meses |

Duas faixas paralelas atravessam o roadmap inteiro:

- 🟢 **FAIXA GRATUITA** — nunca custa nada. Todo mundo faz esta faixa.
- 💳 **FAIXA PAGA** — vouchers de exame, opcionais. Nunca pague pelo *aprendizado*; pague só pelo *exame* que o comprova. Guia completo em [`docs/certificacoes.md`](./docs/certificacoes.md).

**Regra de bolso:** não compre um exame antes de já acertar 85% num simulado gratuito.

---

## Fase 0 — Fundamentos (~70h)

Você não protege o que não entende. Pule esta fase só se você já administra Linux e sabe explicar um handshake TCP.

| # | O que | Onde | Horas | Certificado grátis? |
|---|---|---|---|---|
| 0.1 | Redes básicas (OSI, TCP/IP, DNS, DHCP, roteamento) | [Cisco Networking Basics](https://www.netacad.com/courses/networking-basics) | 20 | ✅ Badge |
| 0.2 | Introdução à cibersegurança | [Cisco Intro to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity) | 6 | ✅ Badge |
| 0.3 | Linha de comando Linux | [TryHackMe Pre-Security path](https://tryhackme.com/path/outline/presecurity) (salas gratuitas) + [Linux Journey](https://labex.io/linuxjourney) | 20 | ⚪ |
| 0.4 | Internals do Windows + noções de AD | [Microsoft Learn — Windows Server fundamentals](https://learn.microsoft.com/training/) | 12 | ⚪ |
| 0.5 | Panorama de ameaças | [Fortinet NSE 1 + 2 + 3](https://training.fortinet.com/) | 6 | ✅ 3 badges |
| 0.6 | Montar um home lab | VirtualBox/Proxmox + Kali + Ubuntu + VMs de avaliação do Windows | 6 | ⚪ |

**Teste de saída:** você consegue subir uma VM, ler `ip a`, capturar tráfego no Wireshark e explicar o que uma regra de firewall faz.

---

## Fase 1 — Núcleo de segurança (~110h)

Tudo aqui é comum às quatro trilhas. **Não se especialize ainda.**

| # | O que | Onde | Horas |
|---|---|---|---|
| 1.1 | Fundamentos de segurança (CID, AAA, controles, noções de cripto) | [Professor Messer Security+](https://www.professormesser.com/) — vídeo 100% gratuito | 35 |
| 1.2 | Base de analista de cibersegurança | [IBM SkillsBuild — Cybersecurity Fundamentals](https://skillsbuild.org/) | 15 |
| 1.3 | Google Cybersecurity Certificate (audit / ajuda financeira) | [Coursera](https://www.coursera.org/professional-certificates/google-cybersecurity) — audit gratuito, ou peça Financial Aid para o certificado | 25 |
| 1.4 | Fundamentos de segurança, compliance e identidade da Microsoft | [Trilha SC-900 no Microsoft Learn](https://learn.microsoft.com/training/) | 12 |
| 1.5 | Fluência em MITRE ATT&CK | [Treinamento oficial MITRE ATT&CK](https://attack.mitre.org/resources/training/) | 10 |
| 1.6 | Scripting: Python + Bash para segurança | [Automate the Boring Stuff](https://automatetheboringstuff.com/) | 13 |

**Teste de saída:** você tira mais de 80% num simulado gratuito de Security+ e escreve um script Python que parseia um arquivo de log.

💳 *Este é o primeiro momento em que faz sentido pagar por algo — veja [`docs/certificacoes.md`](./docs/certificacoes.md).*

---

## Fase 2 — A bifurcação: prática por trilha (~120h cada)

Escolha **uma** trilha principal agora. Se todas te interessam, tudo bem — mas faça **em sequência**, não em paralelo. Ordem que eu recomendo: **Blue Team → Cloud → Red Team → GRC** (blue team contrata mais rápido, cloud paga melhor, red team é a entrada mais concorrida, e GRC premia experiência que você ainda não tem).

### 🔵 2A — Blue Team / Analista de SOC (~120h)

| O que | Onde | Horas | Gratuito? |
|---|---|---|---|
| Trilha SOC Level 1 | [TryHackMe SOC Level 1](https://tryhackme.com/path/outline/soclevel1) | 45 | Parcial; ~US$ 14/mês para tudo |
| Splunk fundamentals + datasets BOTS | [Splunk Free Training](https://www.splunk.com/en_us/training/free-courses/overview.html) + [BOTS](https://bots.splunk.com/) | 20 | ✅ Grátis |
| Triagem de alertas numa UI real de SOC | [LetsDefend — tier gratuito](https://letsdefend.io/) | 20 | ✅ Tier grátis |
| Desafios de DFIR / blue team | [CyberDefenders](https://cyberdefenders.org/) — labs gratuitos generosos | 20 | ✅ Tier grátis |
| Profundidade de investigação | [Blue Team Labs Online](https://blueteamlabs.online/) — desafios gratuitos | 15 | ✅ Parcial |

### 🔴 2B — Red Team / Pentest (~120h)

| O que | Onde | Horas | Gratuito? |
|---|---|---|---|
| Vulns web — o padrão-ouro | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | 45 | ✅ 100% grátis |
| Trilha Jr Penetration Tester | [TryHackMe](https://tryhackme.com/path/outline/jrpenetrationtester) | 35 | Parcial |
| Wargames de privesc em Linux | [OverTheWire Bandit → Natas](https://overthewire.org/wargames/) | 15 | ✅ Grátis |
| Hacking ético prático | [TCM Security no YouTube](https://www.youtube.com/@TCMSecurityAcademy) — cursos completos | 15 | ✅ Grátis |
| Músculo de CTF | [picoCTF](https://picoctf.org/) | 10 | ✅ Grátis |

### ☁️ 2C — Cloud Security (~120h)

| O que | Onde | Horas | Gratuito? |
|---|---|---|---|
| Operações de segurança no Azure (trilha SC-200) | [Microsoft Learn](https://learn.microsoft.com/training/) | 35 | ✅ Grátis |
| Fundamentos de segurança AWS + labs | [AWS Skill Builder](https://skillbuilder.aws/) — tier gratuito + Builder Labs | 30 | ✅ Tier grátis |
| Badges de segurança no GCP | [Google Skills](https://www.skills.google/) — cursos gratuitos | 25 | ✅ Tier grátis |
| Prática de ataque/defesa em nuvem | [flaws.cloud](http://flaws.cloud/) + [flaws2.cloud](http://flaws2.cloud/) + [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | 20 | ✅ Grátis |
| Segurança de IaC e contêineres | [Kubernetes Goat](https://madhuakula.com/kubernetes-goat/) | 10 | ✅ Grátis |

### 📋 2D — GRC / Compliance (~90h)

| O que | Onde | Horas | Gratuito? |
|---|---|---|---|
| NIST Cybersecurity Framework 2.0 | [Material oficial do NIST CSF](https://www.nist.gov/cyberframework) | 20 | ✅ Grátis |
| NIST RMF + SP 800-53 | [Treinamento NIST RMF](https://csrc.nist.gov/projects/risk-management/rmf-courses) | 20 | ✅ Grátis |
| Cursos federais / infra crítica | [CISA free training](https://www.cisa.gov/resources-tools/training) + [FEMA IS courses](https://training.fema.gov/programs/independent-study/) | 20 | ✅ Grátis + certificados |
| Estrutura da ISO 27001 | [Visão geral da ISO 27001](https://www.iso.org/standard/27001) + webinars gratuitos de fornecedores | 15 | ✅ Grátis |
| Prática de risco e auditoria | Monte um risk register e uma matriz de controles reais para uma empresa fictícia | 15 | ✅ Grátis |

---

## Fase 3 — Profundidade e prova (~150h)

Agora você se especializa *e* torna isso visível. Divida mais ou menos 60/40 entre aprender e produzir artefatos.

| # | O que | Horas |
|---|---|---|
| 3.1 | Trilha avançada na sua área (módulos gratuitos da HTB Academy, cursos pay-what-you-can da Antisyphon, OpenSecurityTraining2) | 60 |
| 3.2 | **Projeto de home lab** — monte um lab de detecção (Security Onion / Wazuh / ELK), ataque-o e detecte a si mesmo | 40 |
| 3.3 | **Escreva** — 6 a 10 posts ou writeups no GitHub documentando labs, CTFs e detecções que você construiu | 30 |
| 3.4 | Segunda trilha da Fase 2 (amplitude) | 20 |

**É esta fase que realmente te contrata.** Certificado passa pelo RH; os writeups de lab passam pela entrevista técnica.

---

## Fase 4 — Pronto para o mercado (~100h, contínuo)

| # | O que | Horas |
|---|---|---|
| 4.1 | Currículo + LinkedIn reescritos em torno de projetos, não de cursos | 10 |
| 4.2 | Preparo para entrevista — treine explicar seus labs em voz alta | 20 |
| 4.3 | Contribua: regras de detecção open source (Sigma), writeups de CTF, bug bounty em programas gratuitos do [HackerOne](https://hackerone.com/) | 40 |
| 4.4 | Contínuo: [webcasts gratuitos da SANS](https://www.sans.org/webcasts/), newsletters de threat intel, briefings diários do Simply Cyber | 30+ |

---

## Ordem sequencial condensada

Se você quiser apenas **uma lista sequencial** sem pensar muito:

1. Cisco *Introdução à Cibersegurança* 🇧🇷 → 2. Cisco *Conceitos Básicos de Redes* 🇧🇷 → 3. Fundação Bradesco *Segurança em TI* 🇧🇷 → 4. CC50/CS50 → 5. TCM *Linux 100* → 6. Fortinet FCF+FCA → 7. Professor Messer Security+ 🇺🇸 → 8. Google Cybersecurity Certificate → 9. **ESCOLHA A TRILHA** → 10a. Blue: THM SOC L1 + Splunk + LetsDefend + CyberDefenders · 10b. Red: PortSwigger + Solyd Intro + THM Jr Pentester + picoCTF · 10c. Cloud: SC-200 + AWS Skill Builder + flaws.cloud · 10d. GRC: LGPD EV.gov + CIS Controls + NIST CSF → 11. Home lab + writeups → 12. Certificação paga (ver [`docs/certificacoes.md`](./docs/certificacoes.md)).

> **Meta-conselho:** você não vai terminar tudo aqui — e nem deve. Este catálogo é um **menu**, não uma lista de tarefas. Escolha 1 curso por vez, termine, documente, e só então pegue o próximo.

---

## Próximos passos

- Projetos para provar cada fase → [`projetos/`](./projetos/)
- Como estudar de forma eficiente → [`docs/metodo-de-estudo.md`](./docs/metodo-de-estudo.md)
- Acompanhar progresso → [`progresso/checklist.md`](./progresso/checklist.md)

