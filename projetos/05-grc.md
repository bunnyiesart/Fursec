# Projetos GRC (P25–P30)

[← Voltar ao índice](../README.md)

---

Seis projetos de governança, risco e conformidade. Da trilha [GRC](../trilhas/grc.md), fase 2 em diante.

> GRC tem uma vantagem: os projetos são 100% documentais, não precisam de lab. E quase ninguém faz portfólio de GRC — então o seu se destaca.

**Se fizer só um, faça o [P28](#p28--programa-lgpd-completo-).** LGPD é obrigação de toda empresa brasileira, há pouca gente que sabe operacionalizar, e o entregável é imediatamente reconhecível por quem contrata aqui.

**Use a mesma empresa fictícia nos seis.** Descreva-a uma vez — setor, porte, o que ela trata de dado pessoal, o que é crítico para o negócio — e reaproveite. Seis documentos sobre a mesma empresa formam um programa; seis sobre empresas diferentes formam uma pasta de exercícios.

> Leia [`00-regras.md`](./00-regras.md) antes de começar qualquer um. E nunca use dado real de empresa onde você trabalha ou trabalhou: política interna costuma ser confidencial, e publicar isso é quebra de contrato.

---

### P25 — Conjunto completo de políticas (SGSI fictício)

**Prova que:** você escreve política que dá para cumprir, não texto copiado de modelo.
**Tempo:** 20–30h · **Precisa de:** só escrita, e a empresa fictícia definida

**Passos:**
1. Descreva a empresa em uma página: setor, porte, dados que trata, o que não pode parar.
2. Escreva as seis políticas: segurança da informação, controle de acesso, resposta a incidentes, uso aceitável, gestão de fornecedores, classificação de dados.
3. Mapeie cada política aos controles do Anexo A da ISO 27001 que ela cobre.
4. Em cada uma, defina **dono, prazo de revisão e o que acontece em caso de descumprimento**.
5. Corte tudo que a empresa fictícia não teria como cumprir.

**Entregável:** as seis políticas, com a tabela de mapeamento para o Anexo A.
**Pronto quando:** para cada política, você aponta quem a cumpre no dia a dia e como alguém verifica que foi cumprida.
**Armadilha:** política que exige o impossível para o porte da empresa. Política descumprida é pior que política ausente, porque vira achado de auditoria.
**Apoio:** [`cursos/05-grc-compliance.md`](../cursos/05-grc-compliance.md) · [`docs/certificacoes.md`](../docs/certificacoes.md) para a ordem das siglas da área

---

### P26 — Gap assessment NIST CSF 2.0

**Prova que:** avalia maturidade e transforma isso em plano com ordem e custo.
**Tempo:** 15–20h · **Precisa de:** o [P25](#p25--conjunto-completo-de-políticas-sgsi-fictício), que é a base avaliada

**Passos:**
1. Avalie a empresa fictícia contra as seis funções do CSF 2.0 — Govern entrou na 2.0 e quase ninguém cobre.
2. Para cada categoria, registre o nível atual, o alvo e **a evidência** que sustenta a nota.
3. Calcule a distância e classifique o esforço de fechar cada lacuna.
4. Monte o roadmap de 12 meses, priorizado por risco contra custo.
5. Escreva o sumário de uma página para a diretoria, sem sigla.

**Entregável:** planilha de avaliação com evidência, e o roadmap de 12 meses.
**Pronto quando:** cada nota tem evidência atrás, e o roadmap explica **por que** o item 1 vem antes do item 2.
**Armadilha:** dar nota sem evidência. Vira opinião, e é o primeiro ponto que um auditor derruba.
**Apoio:** [NIST CSF 2.0](https://www.nist.gov/cyberframework)

---

### P27 — Registro de riscos + metodologia

**Prova que:** você tem método, e não classifica risco por instinto.
**Tempo:** 12–18h · **Precisa de:** só escrita

**Passos:**
1. Escreva a metodologia **antes** dos riscos: escala, critério de probabilidade e de impacto, apetite ao risco.
2. Registre 20 riscos ou mais, cada um com causa, evento e consequência — não só um rótulo.
3. Classifique com a sua escala e monte a matriz.
4. Defina o tratamento de cada um: mitigar, transferir, aceitar ou evitar — com dono e prazo.
5. Faça uma avaliação quantitativa em pelo menos três, para exercitar [FAIR](https://www.fairinstitute.org/).

**Entregável:** o documento de metodologia e o registro com 20+ riscos tratados.
**Pronto quando:** duas pessoas diferentes, seguindo a sua metodologia, classificariam o mesmo risco no mesmo nível.
**Armadilha:** "risco: ransomware". Isso é evento, não risco. Risco tem causa, evento e consequência para o negócio, e é isso que permite priorizar.
**Apoio:** [FAIR Institute](https://www.fairinstitute.org/) · [ISO 31000](https://www.iso.org/standard/65694.html)

---

### P28 — Programa LGPD completo 🇧🇷

**Prova que:** domina o contexto brasileiro — vantagem local enorme.
**Tempo:** 20–30h · **Precisa de:** o texto da [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) lido, não resumido

**Passos:**
1. Faça o mapeamento de dados: o que a empresa coleta, por quê, onde guarda, por quanto tempo, com quem compartilha.
2. Defina a **base legal** de cada tratamento — consentimento é a exceção, não o padrão.
3. Escreva o RIPD para os tratamentos de maior risco.
4. Desenhe o fluxo de atendimento ao titular, com os prazos da lei.
5. Escreva o plano de resposta a incidente com dado pessoal, incluindo a comunicação à ANPD.

**Entregável:** mapeamento, bases legais, RIPD, fluxo do titular e o plano de incidente.
**Pronto quando:** você responde, para qualquer dado do mapeamento, qual a base legal e o que acontece se o titular pedir exclusão amanhã.
**Armadilha:** marcar consentimento como base legal de tudo. Consentimento pode ser revogado a qualquer momento — e um programa construído sobre ele desmonta na primeira revogação.
**Apoio:** [Guias e estudos técnicos da ANPD](https://www.gov.br/anpd/pt-br/centrais-de-conteudo) · [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)

---

### P29 — Programa de gestão de fornecedores

**Prova que:** cobre risco de terceiro, que é por onde a maior parte dos incidentes grandes entra.
**Tempo:** 10–15h · **Precisa de:** o [P27](#p27--registro-de-riscos--metodologia), para reusar a escala de risco

**Passos:**
1. Classifique fornecedor por criticidade: acesso a dado, acesso a rede, indisponibilidade tolerada.
2. Monte o questionário, com profundidade diferente por faixa de criticidade.
3. Defina o que é aceite, o que é ressalva e o que é bloqueio.
4. Escreva as cláusulas de segurança que vão para o contrato, incluindo prazo de notificação de incidente.
5. Defina a reavaliação periódica e o processo de saída — encerrar acesso quando o contrato acaba.

**Entregável:** critérios de classificação, questionário por faixa, cláusulas e o processo de reavaliação.
**Pronto quando:** você aplica o programa a um fornecedor real e conhecido, e chega a uma decisão justificada.
**Armadilha:** um questionário de 200 perguntas para todo mundo. Ninguém responde, e o fornecedor pequeno e crítico é o que passa direto.
**Apoio:** [`cursos/05-grc-compliance.md`](../cursos/05-grc-compliance.md)

---

### P30 — Implementação de CIS Controls IG1

**Prova que:** junta GRC com técnico — combinação forte e incomum.
**Tempo:** 15–20h · **Precisa de:** o home lab do [P1](./01-fundamentais.md#p1--home-lab-documentado)

**Passos:**
1. Baixe os CIS Controls v8.1 e separe os safeguards do Implementation Group 1.
2. Aplique cada um ao seu lab de verdade — inventário, configuração, log, backup, controle de acesso.
3. Registre a **evidência** de cada safeguard: captura, arquivo de configuração, saída de comando.
4. Para o que não se aplica ao lab, escreva por que não se aplica.
5. Meça o antes e o depois com uma ferramenta de postura, como no [P4](./01-fundamentais.md#p4--hardening-baseline-aplicado).

**Entregável:** a planilha de safeguards com evidência por linha, e o delta antes/depois.
**Pronto quando:** um auditor conseguiria conferir cada linha sem te perguntar nada.
**Armadilha:** marcar "implementado" sem evidência. Evidência é o produto deste projeto; a marcação é só o índice dela.
**Apoio:** [CIS Controls](https://www.cisecurity.org/controls) · [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)

---

[← Voltar ao índice](../README.md)
