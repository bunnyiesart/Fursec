# 🔵 Projetos Blue Team (P5–P12)

[⬅️ Voltar ao índice](../README.md)

---

### P5 — SIEM próprio com Wazuh
**Prova que:** monta e opera detecção, não só usa a ferramenta do empregador.
**Tempo:** 12–20h · **Repo:** [wazuh/wazuh](https://github.com/wazuh/wazuh)
**Entregável:** agentes em Windows e Linux, 5+ regras customizadas, dashboard, e um incidente simulado do alerta até o fechamento.

### P6 — Lab de detecção: ataque → detecção
**Prova que:** entende os dois lados. **O projeto mais valioso desta lista.**
**Tempo:** 20–30h
**Como:** execute técnicas do [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) contra seu lab, veja o que o SIEM pegou, e **escreva detecção para o que ele não pegou**.
**Repos:** [atomic-red-team](https://github.com/redcanaryco/atomic-red-team) · [MITRE Caldera](https://github.com/mitre/caldera) · [Splunk Attack Range](https://github.com/splunk/attack_range)

### P7 — Pacote de regras Sigma (e contribua upstream)
**Prova que:** faz detection engineering de verdade — e tem PR aceito em projeto público.
**Tempo:** 10–15h · **Repo:** [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma)
**Entregável:** 10 regras suas, testadas, com falso-positivo documentado. Mande PR para o repo oficial. Um PR aceito no SigmaHQ vale mais que um certificado.

### P8 — Honeypot com relatório de 30 dias
**Prova que:** paciência, análise de dados reais, threat intel.
**Tempo:** 5h setup + 30 dias coletando · **Repos:** [T-Pot](https://github.com/telekom-security/tpotce) · [Cowrie](https://github.com/cowrie/cowrie)
**Entregável:** relatório com top IPs, credenciais mais tentadas, geolocalização, malware capturado, e o que isso diz sobre o cenário de ameaças.

### P9 — Análise de phishing (série de writeups)
**Prova que:** habilidade nº1 do SOC júnior no dia a dia.
**Tempo:** 2h por análise
**Faça:** pegue e-mails de phishing reais (a própria caixa serve), analise cabeçalhos, extraia IOCs, detone URLs em sandbox, escreva o veredito. Faça 5–10.
**Ferramentas:** [CyberChef](https://github.com/gchq/CyberChef) · [Any.Run](https://any.run/) · [URLScan](https://urlscan.io/)

### P10 — Playbook de resposta a incidentes + tabletop
**Prova que:** pensa em processo, não só em ferramenta. Ótimo para blue + GRC.
**Tempo:** 8–12h
**Entregável:** playbook de ransomware (detecção → contenção → erradicação → recuperação → lições), e a ata de um exercício tabletop que você conduziu (mesmo que sozinho).

### P11 — Forense de memória
**Prova que:** DFIR de verdade.
**Tempo:** 10–15h · **Repo:** [Volatility 3](https://github.com/volatilityfoundation/volatility3)
**Use:** imagens públicas de memória, ache o processo malicioso, reconstrua a timeline.

### P12 — Relatório de threat intel sobre um grupo APT
**Prova que:** lê, sintetiza e mapeia para ATT&CK.
**Tempo:** 8–12h
**Entregável:** perfil de um grupo, TTPs mapeados no ATT&CK Navigator, e **detecções recomendadas** para cada TTP.

---

---

[⬅️ Voltar ao índice](../README.md)