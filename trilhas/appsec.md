# AppSec / DevSecOps

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)

---

Segurança de aplicação e de pipeline. A trilha mais direta para quem **já programa** — e a que aproveita mais uma carreira anterior em desenvolvimento.

> **Lacuna declarada:** o [`ROADMAP.md`](../ROADMAP.md) mapeia fase 2 para Blue (2A), Red (2B), Cloud (2C) e GRC (2D). **AppSec não tem fase 2 própria ainda.** A sequência abaixo foi montada a partir dos cursos e projetos que existem, sem carga horária oficial do roadmap.

## O que a função faz de fato

- Revisar código procurando classe de falha, não erro de estilo
- Fazer *threat model*: sentar com quem desenvolve e perguntar o que pode dar errado
- Colocar verificação no pipeline sem parar a entrega — e essa é a parte difícil
- Triar o que a ferramenta cospe: SAST gera muito falso positivo, e alguém precisa separar
- Ensinar. Boa parte do trabalho é fazer o time desenvolver melhor sem virar obstáculo

A tensão central da função: **segurança que atrasa demais é contornada**. Quem não resolve isso não é eficaz.

### Esta trilha é para você se

Você programa, entende como aplicação é construída, e prefere prevenir a encontrar. Se você já é desenvolvedor, é de longe seu caminho mais curto.

### Não é, se

Você não gosta de ler código alheio, ou não tem paciência para negociar com time de produto.

---

## Pré-requisito

Fases 0 e 1 do [roadmap](../ROADMAP.md), mais uma coisa que as outras trilhas não exigem: **saber programar de verdade**, em pelo menos uma linguagem, o suficiente para ler o código de outra pessoa e entender a arquitetura.

Se você não programa, faça [`cursos/00-fundamentos.md`](../cursos/00-fundamentos.md) na parte de programação antes. Não dá para pular.

O que mais pesa: **HTTP e web** a fundo, **Git e CI/CD**, e a lógica de autenticação e autorização.

---

## O caminho, em ordem

| # | O que fazer | Onde |
|---|---|---|
| 1 | **Web a fundo, primeiro** — não dá para fazer AppSec sem isso | [PortSwigger Web Security Academy](https://portswigger.net/web-security) |
| 2 | OWASP Top 10 e API Security Top 10, com exemplo em código | [`cursos/06-appsec-devsecops.md`](../cursos/06-appsec-devsecops.md) |
| 3 | Praticar em aplicação vulnerável, lendo o código-fonte dela | [Juice Shop](https://owasp.org/www-project-juice-shop/), [DVWA](https://github.com/digininja/DVWA) |
| 4 | Threat modeling, de verdade | [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/), STRIDE |
| 5 | Montar pipeline com SAST, SCA e varredura de segredo | [Semgrep](https://github.com/semgrep/semgrep), [Trivy](https://github.com/aquasecurity/trivy), [gitleaks](https://github.com/gitleaks/gitleaks) |
| 6 | Revisão de código de segurança em projeto open source real | Qualquer repositório que você use |
| 7 | Modelo de maturidade, para saber onde o programa está | [OWASP SAMM](https://owaspsamm.org/) |

**Sobre o passo 1:** a Web Security Academy é gratuita e é o melhor material de segurança web que existe. Faça a trilha inteira; ela ensina a mecânica, não a lista.

Ferramentas completas: [`repositorios/ferramentas-appsec-cloud.md`](../repositorios/ferramentas-appsec-cloud.md).

---

## Os projetos desta trilha

P31–P33, em [`projetos/06-appsec.md`](../projetos/06-appsec.md). São só três — a trilha com menos projeto do catálogo.

| Projeto | Por que importa |
|---|---|
| [P31 — Threat model de projeto open source](../projetos/06-appsec.md#p31--threat-model-de-um-projeto-open-source) | Mostra que você pensa em arquitetura, não em sintoma |
| [P32 — Pipeline CI/CD com segurança embutida](../projetos/06-appsec.md#p32--pipeline-cicd-com-segurança-embutida) | É literalmente a descrição da vaga de DevSecOps |
| [P33 — Code review de segurança com PR real](../projetos/06-appsec.md#p33--code-review-de-segurança-com-pr-real) | Validação externa: alguém aceitou sua correção |

Se fizer só um: **P33**. Um PR aceito num projeto que outras pessoas usam é a evidência mais difícil de fabricar.

**Como escolher o alvo do P31 e P33:** um projeto que você já usa e cuja linguagem você conhece. Familiaridade com o domínio vale mais que fama do repositório.

---

## Ferramentas que você vai usar de verdade

| Categoria | Ferramentas |
|---|---|
| SAST | [Semgrep](https://github.com/semgrep/semgrep), [CodeQL](https://codeql.github.com/), [Bandit](https://github.com/PyCQA/bandit) (Python) |
| SCA / dependência | [Trivy](https://github.com/aquasecurity/trivy), [OSV-Scanner](https://github.com/google/osv-scanner), [Dependency-Check](https://github.com/jeremylong/DependencyCheck) |
| Segredo | [gitleaks](https://github.com/gitleaks/gitleaks), [trufflehog](https://github.com/trufflesecurity/trufflehog) |
| DAST | [OWASP ZAP](https://github.com/zaproxy/zaproxy), [Nuclei](https://github.com/projectdiscovery/nuclei) |
| Teste manual | [Burp Suite](https://portswigger.net/burp/communitydownload) |
| Threat modeling | [Threat Dragon](https://owasp.org/www-project-threat-dragon/), [pytm](https://github.com/OWASP/pytm) |
| Contêiner | [Trivy](https://github.com/aquasecurity/trivy), [Grype](https://github.com/anchore/grype), [Hadolint](https://github.com/hadolint/hadolint) |
| Referência | [OWASP ASVS](https://owasp.org/ASVS/), [Cheat Sheet Series](https://cheatsheetseries.owasp.org/) |

O [ASVS](https://owasp.org/ASVS/) é subestimado: é uma lista de requisitos verificáveis, e serve tanto para testar quanto para especificar.

---

## Certificações

- **Gratuito:** [API Security Fundamentals](https://au.apisec.ai/courses/api-security-fundamentals) e os outros da APIsec University, e o conteúdo do PortSwigger
- **Primeiro exame que vale:** aqui certificação pesa **menos** que nas outras trilhas. Um PR de segurança aceito vale mais
- **Se quiser sigla:** Burp Suite Certified Practitioner é prático e respeitado; CSSLP se o seu contexto é corporativo

Esta é a trilha em que portfólio de código supera credencial com mais folga.

---

## Teste de saída

Você terminou esta trilha quando consegue, **sem consultar nada**:

- [ ] Achar e explicar, em código, cada classe do OWASP Top 10
- [ ] Fazer um threat model de um serviço em uma hora, com quem desenvolve na sala
- [ ] Configurar SAST num pipeline e **justificar cada regra que você desligou**
- [ ] Olhar 20 achados de SAST e separar real de falso positivo, com argumento
- [ ] Explicar por que uma correção proposta não resolve o problema de raiz
- [ ] Escrever correção segura, não só apontar a falha
- [ ] Dizer onde você colocaria um controle sem parar a entrega do time

O quarto item é o trabalho do dia a dia, e quase ninguém treina.

---

## O que perguntam em entrevista

- "Como você impede que uma classe de falha volte?" — controle sistêmico, não correção pontual
- "SAST acusou 400 achados. E agora?" — triagem, priorização, ajuste de regra
- "O time diz que a verificação atrasa o deploy. O que você faz?" — a tensão central da função
- "Explique SSRF e como corrigir" — quer mecanismo e mitigação em profundidade
- "Como você faria threat model deste sistema?" — normalmente com um diagrama na lousa

---

## Próximos passos

- **[Cloud Security](./cloud.md)** — pipeline e nuvem são a mesma conversa hoje
- **[Red Team](./red-team.md)** — se você quer atacar o que aprendeu a defender

---

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)
