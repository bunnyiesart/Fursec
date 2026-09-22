# Projetos Blue Team (P5–P12)

[← Voltar ao índice](../README.md)

---

Oito projetos de defesa. Da trilha [Blue Team / SOC](../trilhas/blue-team.md), fase 2 em diante.

**Se fizer só um, faça o [P6](#p6--lab-de-detecção-ataque--detecção).** Ele mostra as duas metades do problema na mesma pessoa, e é o que responde a pergunta de entrevista "conta um incidente que você investigou".

> Leia [`00-regras.md`](./00-regras.md) antes de começar qualquer um.

---

### P5 — SIEM próprio com Wazuh

**Prova que:** monta e opera detecção, não só usa a ferramenta do empregador.
**Tempo:** 12–20h · **Precisa de:** 8 GB de RAM livres e o lab do [P1](./01-fundamentais.md#p1--home-lab-documentado)

**Passos:**
1. Suba o servidor Wazuh e conecte agentes em **Windows e Linux** — os dois, porque o log de cada um é diferente.
2. Confirme que o log está chegando de fato: autenticação, processo, alteração de arquivo.
3. Escreva 5 ou mais regras próprias para o seu ambiente.
4. Simule um incidente e leve do alerta até o fechamento, registrando cada passo.

**Entregável:** agentes nos dois sistemas, 5+ regras customizadas, dashboard e o registro do incidente simulado.
**Pronto quando:** você explica **de onde vem** cada campo de um alerta — qual log, qual evento, qual decodificador — sem abrir a documentação.
**Armadilha:** parar quando o dashboard fica bonito. Dashboard não detecta nada; regra detecta.
**Apoio:** [wazuh/wazuh](https://github.com/wazuh/wazuh)

---

### P6 — Lab de detecção: ataque → detecção

**Prova que:** entende os dois lados. **O projeto mais valioso desta lista.**
**Tempo:** 20–30h · **Precisa de:** o [P5](#p5--siem-próprio-com-wazuh) funcionando

**Passos:**
1. Escolha 10 técnicas do [ATT&CK](https://attack.mitre.org/) que façam sentido no seu ambiente.
2. Execute cada uma com o [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) contra o seu lab.
3. Anote o que o SIEM pegou, o que pegou **tarde** e o que não pegou.
4. **Escreva detecção para o que ele não pegou** — é aqui que está o valor.
5. Execute de novo e confirme que a nova regra dispara.

**Entregável:** tabela de técnica × detectou/não detectou, as regras novas, e o antes/depois.
**Pronto quando:** você consegue dizer, para cada regra que escreveu, **o que ela não pega** — a variação da técnica que passa batido.
**Armadilha:** testar só o caminho feliz da técnica. O atacante usa a variante, não o exemplo da documentação.
**Apoio:** [atomic-red-team](https://github.com/redcanaryco/atomic-red-team) · [MITRE Caldera](https://github.com/mitre/caldera) · [Splunk Attack Range](https://github.com/splunk/attack_range)

---

### P7 — Pacote de regras Sigma (e contribua upstream)

**Prova que:** faz engenharia de detecção de verdade — e tem PR aceito em projeto público.
**Tempo:** 10–15h · **Precisa de:** o [P6](#p6--lab-de-detecção-ataque--detecção), que é de onde saem as regras

**Passos:**
1. Leia o guia de contribuição do SigmaHQ **antes** de escrever, para não refazer tudo.
2. Escreva 10 regras, cada uma mapeada a uma técnica do ATT&CK.
3. Teste cada uma contra tráfego real do seu lab e **documente o falso positivo** que ela gera.
4. Verifique se já não existe regra equivalente no repositório.
5. Mande PR e responda à revisão.

**Entregável:** 10 regras testadas, com falso positivo documentado, e pelo menos um PR aberto.
**Pronto quando:** um mantenedor revisou sua regra — mesmo que peça mudança. A revisão é o aprendizado.
**Armadilha:** regra que só funciona no seu ambiente. Regra boa é genérica o suficiente para servir a outros e específica o suficiente para não afogar em ruído.
**Apoio:** [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) — um PR aceito ali vale mais que um certificado básico

---

### P8 — Honeypot com relatório de 30 dias

**Prova que:** paciência, análise de dado real e inteligência de ameaça.
**Tempo:** 5h de montagem + 30 dias coletando · **Precisa de:** um VPS barato ou a camada gratuita de uma nuvem

**Passos:**
1. Suba o honeypot **isolado** — nunca na sua rede doméstica.
2. Deixe coletando 30 dias, sem mexer.
3. Analise: IPs mais ativos, credenciais mais tentadas, geolocalização, binário capturado.
4. Escreva o que os dados dizem sobre o cenário de ameaça — não só os números.

**Entregável:** relatório de 30 dias com dados, gráficos e conclusão.
**Pronto quando:** o relatório responde "e daí?" — o que alguém defendendo uma rede deveria fazer diferente por causa do que você observou.
**Armadilha:** expor o honeypot na rede onde estão suas máquinas reais. Ele **vai** ser comprometido; é para isso que existe. Isole de verdade.
**Apoio:** [T-Pot](https://github.com/telekom-security/tpotce) · [Cowrie](https://github.com/cowrie/cowrie)

---

### P9 — Análise de phishing (série de writeups)

**Prova que:** habilidade número 1 do SOC júnior no dia a dia.
**Tempo:** 2h por análise, faça de 5 a 10 · **Precisa de:** VM descartável para abrir anexo

**Passos:**
1. Pegue phishing real — a sua própria caixa de spam serve.
2. Analise os cabeçalhos: origem real, SPF, DKIM, DMARC, cadeia de repasse.
3. Extraia indicadores: URL, domínio, IP, hash de anexo.
4. Detone URL e anexo **em sandbox**, nunca na sua máquina.
5. Escreva o veredito: é phishing, o que ele queria, o que fazer.

**Entregável:** de 5 a 10 writeups no mesmo formato, com indicadores em lista reutilizável.
**Pronto quando:** você analisa um e-mail novo em menos de 30 minutos e chega ao veredito com confiança.
**Armadilha:** clicar no link para "ver o que é". Use sandbox — e nunca reencaminhe a amostra para serviço público se ela contiver dado de outra pessoa.
**Apoio:** [CyberChef](https://github.com/gchq/CyberChef) · [Any.Run](https://any.run/) · [URLScan](https://urlscan.io/)

---

### P10 — Playbook de resposta a incidentes + tabletop

**Prova que:** pensa em processo, não só em ferramenta. Vale para blue **e** para [GRC](../trilhas/grc.md).
**Tempo:** 8–12h · **Precisa de:** nada além de texto

**Passos:**
1. Escolha um cenário concreto: ransomware numa empresa fictícia que você descreve.
2. Escreva as cinco fases: detecção → contenção → erradicação → recuperação → lições.
3. Para cada fase, defina **quem decide o quê** e em quanto tempo.
4. Conduza um exercício de mesa seguindo o playbook, mesmo sozinho.
5. Registre onde o playbook falhou durante o exercício e corrija.

**Entregável:** o playbook e a ata do exercício, com as correções que ele provocou.
**Pronto quando:** o exercício encontrou pelo menos um buraco no seu próprio playbook. Se não encontrou, o exercício foi fácil demais.
**Armadilha:** playbook que só descreve o caminho técnico. A pergunta que trava resposta real é "quem autoriza desligar o servidor?".
**Apoio:** [NIST SP 800-61r2](https://csrc.nist.gov/pubs/sp/800/61/r2/final), o guia de referência de resposta a incidentes

---

### P11 — Forense de memória

**Prova que:** DFIR de verdade — achar o que não está no disco.
**Tempo:** 10–15h · **Precisa de:** Volatility 3 e imagens públicas de memória

**Passos:**
1. Baixe uma imagem pública já analisada, para poder conferir o seu resultado depois.
2. Liste processos e procure o que não devia estar ali: nome estranho, pai errado, caminho fora do padrão.
3. Extraia conexões de rede, DLLs injetadas e comandos executados.
4. Reconstrua a linha do tempo: o que aconteceu, em que ordem.
5. Só então compare com a análise publicada.

**Entregável:** relatório com processo malicioso identificado, indicadores e linha do tempo.
**Pronto quando:** você chega à mesma conclusão da análise publicada **antes** de lê-la.
**Armadilha:** rodar todos os plugins e despejar a saída. Forense é hipótese e verificação, não varredura.
**Apoio:** [Volatility 3](https://github.com/volatilityfoundation/volatility3)

---

### P12 — Relatório de threat intel sobre um grupo APT

**Prova que:** lê, sintetiza e mapeia para ATT&CK.
**Tempo:** 8–12h · **Precisa de:** só leitura e escrita

**Passos:**
1. Escolha um grupo com relatório público farto e com alvo relevante para o Brasil.
2. Levante o perfil: alvos, motivação, período de atividade, atribuição e quão confiável ela é.
3. Mapeie as TTPs no [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/).
4. Para **cada** TTP, escreva a detecção recomendada — é o que separa este relatório de um resumo.
5. Feche com o que uma empresa do porte da sua deveria priorizar.

**Entregável:** perfil do grupo, camada do Navigator e a lista de detecções por TTP.
**Pronto quando:** alguém de blue team consegue pegar seu relatório e transformar em regra sem pesquisar mais nada.
**Armadilha:** repetir o relatório do fornecedor. O valor está na síntese de várias fontes e na parte de detecção, que quase nenhum relatório público traz.
**Apoio:** [MITRE ATT&CK](https://attack.mitre.org/groups/) · [MISP](https://github.com/MISP/MISP) · o [guia de CVE](../docs/guia-cve.md) para a parte de vulnerabilidade explorada

---

[← Voltar ao índice](../README.md)
