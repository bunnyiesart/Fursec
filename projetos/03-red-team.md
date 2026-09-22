# Projetos Red Team (P13–P19)

[← Voltar ao índice](../README.md)

---

Sete projetos ofensivos. Da trilha [Red Team / Pentest](../trilhas/red-team.md), fase 2 em diante.

**Se fizer só um, faça o [P13](#p13--relatório-de-pentest-profissional).** Nesta área o relatório é o produto, e é o artefato que prova que você é contratável.

> **Leia [`00-regras.md`](./00-regras.md) antes de tocar em qualquer coisa.** Todo alvo aqui é máquina sua ou plataforma que autoriza por escrito. Testar terceiro sem autorização é crime — Lei 12.737/2012, Art. 154-A. O passo a passo completo está em [`docs/pentest-completo.md`](../docs/pentest-completo.md).

---

### P13 — Relatório de pentest profissional

**Prova que:** você escreve como consultor, não como script kiddie. **Diferencial gigante.**
**Tempo:** 10–15h por relatório · **Precisa de:** uma máquina *retired* do HTB ou uma VM do VulnHub

**Passos:**
1. Ataque o alvo **anotando tudo enquanto faz** — comando, saída, horário. Reconstruir depois nunca sai igual.
2. Escreva o sumário executivo em uma página, sem jargão, para quem decide orçamento.
3. Documente escopo e metodologia: o que foi e o que não foi testado.
4. Um achado por vulnerabilidade, com severidade justificada por [CVSS](https://www.first.org/cvss/calculator/3.1) e o vetor à mostra.
5. Escreva a remediação concreta — arquivo e linha quando possível, não "validar entrada".

**Entregável:** o relatório completo no formato de consultoria, usando [`templates/relatorio-pentest.md`](./templates/relatorio-pentest.md).
**Pronto quando:** outra pessoa reproduz um achado seu seguindo só o passo a passo que você escreveu.
**Armadilha:** despejar saída de ferramenta como se fosse achado. Dez achados verificados à mão valem mais que 200 páginas de scanner com falso positivo.
**Apoio:** [PTES](http://www.pentest-standard.org/) · [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/)

---

### P14 — Ferramenta de automação de recon

**Prova que:** programa e entende o fluxo ofensivo.
**Tempo:** 12–20h · **Precisa de:** Python ou Go

**Passos:**
1. Encadeie as etapas: subdomínio → resolução → porta → tecnologia → captura de tela.
2. Saída em JSON, para encadear com outra ferramenta.
3. Trate a parte chata: limite de taxa, tempo esgotado, execução parcial que pode continuar.
4. Estude o código do [ProjectDiscovery](https://github.com/projectdiscovery) e veja como eles resolveram concorrência.

**Entregável:** a ferramenta, o README e a saída de uma execução contra alvo autorizado.
**Pronto quando:** ela roda contra um domínio novo sem você editar nada, e você consegue interrompê-la e retomar.
**Armadilha:** disparar tudo em paralelo sem limite. Derruba o alvo, o que conta como negação de serviço, e queima seu IP nos serviços de consulta.
**Apoio:** [ProjectDiscovery](https://github.com/projectdiscovery) · alvos autorizados em [`labs/red-team-ctf.md`](../labs/red-team-ctf.md)

---

### P15 — Pentest completo do OWASP Juice Shop

**Prova que:** domina o OWASP Top 10 na prática.
**Tempo:** 15–25h · **Precisa de:** Docker e o Burp Suite Community

**Passos:**
1. Suba o Juice Shop localmente, nunca ataque uma instância pública de terceiro.
2. Resolva os desafios, do fácil ao difícil, anotando a mecânica de cada um.
3. Escreva o relatório no formato do [P13](#p13--relatório-de-pentest-profissional).
4. **Corrija o código** de pelo menos três vulnerabilidades e mostre o diff — quase ninguém faz isso.

**Entregável:** desafios resolvidos, relatório e os três patches com explicação.
**Pronto quando:** você explica **por que** cada correção resolve, e que classe de bypass ela ainda deixa aberta.
**Armadilha:** caçar a flag sem entender. O objetivo é a mecânica da falha, não o placar.
**Apoio:** [juice-shop](https://github.com/juice-shop/juice-shop) · [PortSwigger Web Security Academy](https://portswigger.net/web-security) para a teoria de cada classe

---

### P16 — Attack path em Active Directory

**Prova que:** entende o ambiente corporativo real, que é onde o dinheiro está.
**Tempo:** 25–40h · **Precisa de:** 16 GB de RAM ([nível 1 do home lab](../labs/home-lab.md))

**Passos:**
1. Suba o GOAD e deixe quebrado de propósito, como ele vem.
2. Comece de um usuário sem privilégio, como um atacante que entrou por phishing.
3. Colete com BloodHound e **leia o grafo** — o caminho está ali.
4. Execute cada passo até Domain Admin, registrando comando e resultado.
5. Para cada passo, escreva **como detectar e como bloquear**. Esta é a metade que valoriza o projeto.

**Entregável:** caminho completo com diagrama do BloodHound, mais a tabela de detecção e mitigação por passo.
**Pronto quando:** você refaz o caminho do zero, sem consultar suas anotações, e explica por que cada passo funciona.
**Armadilha:** entregar só o ataque. Quem contrata quer saber se você sabe fechar, não só abrir.
**Apoio:** [GOAD](https://github.com/Orange-Cyberdefense/GOAD) · [BloodHound](https://github.com/SpecterOps/BloodHound) · [Impacket](https://github.com/fortra/impacket)

---

### P17 — Lab de quebra de senhas

**Prova que:** entende hashing e política de senha na prática, com dado medido.
**Tempo:** 6–10h · **Precisa de:** hashcat, e GPU ajuda mas não é obrigatória

**Passos:**
1. Gere **seus próprios** hashes — nunca use vazamento real de terceiros.
2. Meça a taxa do hashcat para MD5, SHA-256, bcrypt e Argon2 no seu hardware.
3. Compare ataque de dicionário, com regra e por força bruta.
4. Converta a medição em tempo de quebra por tamanho de senha.
5. Escreva a recomendação de política **baseada nos seus números**.

**Entregável:** tabela de medições e a recomendação de política derivada dela.
**Pronto quando:** sua recomendação tem número atrás, e você explica por que bcrypt muda a conta em ordens de grandeza.
**Armadilha:** baixar vazamento real para "testar". É dado pessoal de outras pessoas, e usar isso tem implicação de LGPD além da ética.
**Apoio:** [hashcat](https://github.com/hashcat/hashcat) · [John the Ripper](https://github.com/openwall/john)

---

### P18 — Primeiro report válido de bug bounty

**Prova que:** encontra bug real em alvo autorizado. Vale mais que 10 CTFs.
**Tempo:** indefinido — é persistência, não cronograma · **Precisa de:** o [P15](#p15--pentest-completo-do-owasp-juice-shop) feito antes

**Passos:**
1. Leia o escopo do programa **inteiro** antes de testar qualquer coisa. Fora do escopo é acesso não autorizado.
2. Escolha alvo com escopo amplo e menos concorrência, não o programa da moda.
3. Procure lógica de negócio, não o que o scanner acha — isso já foi reportado.
4. Escreva o report com impacto e passo de reprodução mínimo.
5. Espere o disclosure autorizado **antes** de publicar qualquer coisa.

**Entregável:** o report aceito, e o writeup público depois da autorização.
**Pronto quando:** um triador aceitou. Duplicata também ensina — mostra que você achou algo real.
**Armadilha:** publicar antes do disclosure. Queima o programa, pode te tirar da plataforma, e em alguns casos tem consequência legal.
**Apoio:** [HackerOne](https://hackerone.com/) · [Bugcrowd](https://www.bugcrowd.com/) · [Bugcrowd University](https://www.bugcrowd.com/hackers/bugcrowd-university/)

---

### P19 — Pentest de aplicação mobile

**Prova que:** cobre uma área com pouca concorrência.
**Tempo:** 15–20h · **Precisa de:** Android Studio com emulador, ou aparelho antigo com root

**Passos:**
1. Comece por Android: ferramental aberto e APK fácil de obter legalmente.
2. Análise estática: descompile, procure segredo embutido, endpoint e chave de API.
3. Intercepte o tráfego, o que exige lidar com fixação de certificado.
4. Análise dinâmica com Frida: instrumente e contorne verificação local.
5. Siga o [OWASP MASTG](https://mas.owasp.org/) como lista de cobertura, para não testar só o que é fácil.

**Entregável:** relatório no formato do [P13](#p13--relatório-de-pentest-profissional), sobre app propositalmente vulnerável ou app seu.
**Pronto quando:** você contorna fixação de certificado e explica por que aquela defesa não é suficiente sozinha.
**Armadilha:** testar app de terceiro sem autorização. Estar na loja não é autorização — use alvo propositalmente vulnerável.
**Apoio:** [OWASP MASTG](https://mas.owasp.org/) · [Mobile Hacking Lab](https://www.mobilehackinglab.com/) · a seção completa em [`cursos/10-mobile.md`](../cursos/10-mobile.md)

---

[← Voltar ao índice](../README.md)
