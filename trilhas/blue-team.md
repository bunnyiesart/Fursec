# Blue Team / SOC

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)

---

Defesa: detectar, investigar e responder. É a trilha com mais vaga de entrada no Brasil e a que exige menos investimento em hardware.

## O que a função faz de fato

Um analista de SOC nível 1 passa o dia numa fila de alertas. O trabalho real é:

- Abrir o alerta e decidir em minutos se é falso positivo, ruído ou incidente
- Buscar contexto: esse IP já apareceu? esse usuário costuma logar desse país? esse hash é conhecido?
- Escalar com um resumo que a pessoa do nível 2 consiga usar
- Escrever o que foi feito, para o próximo turno entender

Não é ficar olhando gráfico bonito. É triagem, e a habilidade central é **saber o que é normal** no ambiente — porque só assim o anormal aparece.

### Esta trilha é para você se

Você gosta de investigar, tem paciência com detalhe, e não se incomoda em escrever. Boa parte do valor de um analista está no texto que ele deixa.

### Não é, se

Você quer só "hackear". A rotina é repetitiva por natureza, e o turno pode ser noturno no começo.

---

## Pré-requisito

Fases 0 e 1 do [roadmap](../ROADMAP.md), ~180h. Sem redes e sistemas você não interpreta alerta — decora procedimento.

O que mais pesa aqui: **log** (onde nasce, o que registra), **rede** (TCP/IP, DNS, HTTP) e **Windows** (Active Directory, Event Log), porque é de onde vem quase todo alerta corporativo.

---

## O caminho, em ordem

Fase 2A do roadmap, ~120h.

| # | O que fazer | Onde |
|---|---|---|
| 1 | Fundamentos de SOC, SIEM e detecção | [`cursos/02-blue-team.md`](../cursos/02-blue-team.md) |
| 2 | Montar seu SIEM e mandar log de verdade para ele | [Wazuh](https://github.com/wazuh/wazuh) no [home lab](../labs/home-lab.md) |
| 3 | Triagem em SOC simulado, todo dia | [LetsDefend](https://letsdefend.io/), [CyberDefenders](https://cyberdefenders.org/) |
| 4 | Análise de PCAP e de e-mail de phishing | [Malware-Traffic-Analysis](https://www.malware-traffic-analysis.net/) |
| 5 | Escrever regra de detecção própria | [Sigma](https://github.com/SigmaHQ/sigma) |
| 6 | Forense e resposta a incidente | [`labs/blue-team.md`](../labs/blue-team.md) |

Plataformas completas: [`labs/blue-team.md`](../labs/blue-team.md). Ferramentas: [`repositorios/ferramentas-blue.md`](../repositorios/ferramentas-blue.md).

---

## Os projetos desta trilha

P5–P12, em [`projetos/02-blue-team.md`](../projetos/02-blue-team.md). Os três que mais aparecem em entrevista:

| Projeto | Por que importa |
|---|---|
| [P5 — SIEM próprio com Wazuh](../projetos/02-blue-team.md#p5--siem-próprio-com-wazuh) | Prova que você entende de onde o log vem, não só como consultá-lo |
| [P6 — Lab de detecção: ataque → detecção](../projetos/02-blue-team.md#p6--lab-de-detecção-ataque--detecção) | O ciclo completo: você ataca, você detecta, você documenta |
| [P7 — Pacote de regras Sigma](../projetos/02-blue-team.md#p7--pacote-de-regras-sigma-e-contribua-upstream) | Contribuição upstream é a evidência mais forte que existe |

Se fizer só um: **P6**. Ele mostra as duas metades do problema na mesma pessoa.

---

## Ferramentas que você vai usar de verdade

| Categoria | Ferramentas |
|---|---|
| SIEM | [Wazuh](https://github.com/wazuh/wazuh), Splunk, Elastic, Microsoft Sentinel |
| Detecção como código | [Sigma](https://github.com/SigmaHQ/sigma), [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) |
| Endpoint e resposta | [Velociraptor](https://github.com/Velocidex/velociraptor), [osquery](https://github.com/osquery/osquery) |
| Rede | Wireshark, [Zeek](https://github.com/zeek/zeek), [Suricata](https://github.com/OISF/suricata) |
| Forense | [Volatility](https://github.com/volatilityfoundation/volatility3), Autopsy, [KAPE](https://www.kroll.com/kape) |
| Inteligência | [MISP](https://github.com/MISP/MISP), [OpenCTI](https://github.com/OpenCTI-Platform/opencti) |
| Enquadramento | [MITRE ATT&CK](https://attack.mitre.org/) — o vocabulário obrigatório |

---

## Certificações

Ordem e o que é gratuito estão em [`docs/certificacoes.md`](../docs/certificacoes.md). Para esta trilha:

- **Gratuito primeiro:** trilhas da [TryHackMe](https://tryhackme.com/) e o certificado do [Google Cybersecurity](https://www.coursera.org/professional-certificates/google-cybersecurity) via Financial Aid
- **Primeiro exame que vale pagar:** Security+, se o RH da sua região filtra por ele
- **Depois, se a empresa paga:** Blue Team Level 1, GCIH, ou a certificação do SIEM que você usa no trabalho

Certificado passa pelo RH. O writeup do P6 passa pela entrevista técnica.

---

## Teste de saída

Você terminou esta trilha quando consegue, **sem consultar nada**:

- [ ] Explicar a diferença entre falso positivo, verdadeiro positivo e falso negativo, com exemplo do seu lab
- [ ] Receber um alerta de login suspeito e listar as cinco primeiras coisas que você checa
- [ ] Escrever uma regra Sigma para uma técnica do ATT&CK e explicar o que ela não pega
- [ ] Ler um PCAP e dizer o que aconteceu
- [ ] Contar a linha de tempo de um incidente do seu lab, do primeiro sinal à contenção
- [ ] Dizer onde o log de autenticação do Windows e do Linux fica, e o que cada um registra

Se travar em algum, o buraco está ali.

---

## O que perguntam em entrevista

- "Como você investiga um alerta de PowerShell suspeito?" — quer ver seu processo, não a resposta certa
- "Chega um phishing. Quais são seus passos?" — cabeçalho, anexo, URL, indicador, contenção
- "O que é pass-the-hash e como você detectaria?" — testa se você entende o mecanismo
- "Diferença entre IDS e IPS, EDR e antivírus" — vocabulário
- "Conta um incidente que você investigou" — **é aqui que o projeto P6 paga o investimento**

Quem não tem experiência profissional responde a última com o lab. Funciona, se estiver documentado.

---

## Próximos passos

Depois desta trilha, as duas continuações naturais:

- **[Cloud Security](./cloud.md)** — porque o log que você vai triar está cada vez mais na nuvem
- **[Malware / Engenharia reversa](./malware-re.md)** — a profundidade técnica do lado defensivo

E a fase 3 do [roadmap](../ROADMAP.md#fase-3--profundidade-e-prova-150h), que é a que torna o trabalho visível.

---

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)
