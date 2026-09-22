# Projetos Cloud Security (P20–P24)

[← Voltar ao índice](../README.md)

---

Cinco projetos de nuvem. Da trilha [Cloud Security](../trilhas/cloud.md), fase 2 em diante.

**Se fizer só um, faça o [P20](#p20--baseline-seguro-em-terraform).** Infraestrutura como código com verificação no pipeline é o que a vaga de cloud security pede hoje, e é verificável por qualquer pessoa que abra o seu repositório.

> Leia [`00-regras.md`](./00-regras.md) antes de começar qualquer um. E aqui há uma regra a mais: **conta de nuvem custa dinheiro de verdade.** Configure limite de gasto e alerta de faturamento antes do primeiro `terraform apply`, e destrua o que subir quando terminar.

---

### P20 — Baseline seguro em Terraform

**Prova que:** você faz segurança como código — a habilidade mais pedida em nuvem hoje.
**Tempo:** 15–25h · **Precisa de:** uma conta de camada gratuita e Terraform instalado

**Passos:**
1. Escreva um módulo de VPC e conta: rede segmentada, log ativado, raiz protegida, IAM sem curinga.
2. Rode o [Checkov](https://github.com/bridgecrewio/checkov) e o [Trivy](https://github.com/aquasecurity/trivy) contra o seu próprio código e corrija o que eles acharem.
3. Para cada regra que você **suprimir**, escreva o motivo no código — supressão sem justificativa é dívida escondida.
4. Monte o pipeline que **bloqueia** o deploy quando a varredura falha, não só avisa.
5. Prove o bloqueio: abra um PR com um bucket público de propósito e mostre o pipeline vermelho.

**Entregável:** o módulo, o pipeline e a captura do PR reprovado pela verificação.
**Pronto quando:** alguém clona o repositório, roda `terraform apply` na conta dele e recebe uma base segura sem editar nada.
**Armadilha:** deixar a varredura em modo aviso. Pipeline que não quebra é documentação, não controle.
**Apoio:** [Checkov](https://github.com/bridgecrewio/checkov) · [Trivy](https://github.com/aquasecurity/trivy) · [`cursos/04-cloud-security.md`](../cursos/04-cloud-security.md)

---

### P21 — flaws.cloud com plano de remediação

**Prova que:** você ataca **e** corrige.
**Tempo:** 10–15h · **Precisa de:** AWS CLI configurada

**Passos:**
1. Resolva os níveis do flaws.cloud, que é um alvo feito para ser atacado — sem sair dele.
2. Para cada nível, escreva qual configuração errada permitiu o acesso.
3. **Escreva a política IAM corrigida** de cada nível, em JSON, que fecharia aquele caminho.
4. Diga também como você **detectaria** aquele acesso no CloudTrail — liga direto no [P22](#p22--detecção-em-cloudtrail).

**Entregável:** writeup por nível, com a política corrigida e a detecção proposta.
**Pronto quando:** cada nível tem as três partes: como entrou, o JSON que fecha, o alerta que pegaria.
**Armadilha:** publicar só o writeup do ataque. Todo mundo faz isso; a metade da correção é o que te diferencia.
**Apoio:** [flaws.cloud](http://flaws.cloud/) · [flaws2.cloud](http://flaws2.cloud/) · [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat)

---

### P22 — Detecção em CloudTrail

**Prova que:** blue team mais nuvem — combinação rara e bem paga.
**Tempo:** 12–18h · **Precisa de:** CloudTrail ativado numa conta sua

**Passos:**
1. Ative o log em todas as regiões e confirme que o evento chega ao destino.
2. Escreva detecção para ações de IAM que importam: chave de acesso nova, política anexada, usuário criado, MFA removido.
3. Detecte também o que o atacante faz **antes**: enumerar permissão, assumir papel, e **desligar o próprio log**.
4. Suba o [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat), execute os cenários e confira quais alertas dispararam.
5. Meça o atraso entre a ação e o alerta — em nuvem, a entrega do log não é instantânea.

**Entregável:** as regras, a tabela de cenário × alerta disparado e o atraso medido.
**Pronto quando:** você mostra um cenário do CloudGoat ponta a ponta: ação, evento bruto no log, alerta.
**Armadilha:** confiar que o log existe. Atacante desliga CloudTrail, e o alerta que mais importa é justamente o de desligamento do log.
**Apoio:** [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) · [Stratus Red Team](https://github.com/DataDog/stratus-red-team)

---

### P23 — Auditoria multi-cloud automatizada

**Prova que:** você avalia postura e prioriza, em vez de despejar achado.
**Tempo:** 10–15h · **Precisa de:** uma conta de camada gratuita, sua

**Passos:**
1. Rode o [Prowler](https://github.com/prowler-cloud/prowler) e o [ScoutSuite](https://github.com/nccgroup/ScoutSuite) na **sua própria** conta — nunca em conta de terceiro.
2. Compare os dois: onde discordam, e por quê.
3. Triagem manual: separe o achado real do ruído de configuração padrão.
4. Priorize por risco de verdade — exposição à internet e permissão excessiva primeiro.
5. Escreva o sumário executivo com o plano de correção em ordem.

**Entregável:** relatório de postura com achados triados e plano de correção priorizado.
**Pronto quando:** seu relatório cabe em uma página de decisão, com o detalhamento em anexo.
**Armadilha:** entregar as 400 linhas de saída da ferramenta. Ninguém lê, e priorização é exatamente o trabalho que se espera de você.
**Apoio:** [Prowler](https://github.com/prowler-cloud/prowler) · [ScoutSuite](https://github.com/nccgroup/ScoutSuite) · [CloudFox](https://github.com/BishopFox/cloudfox)

---

### P24 — Hardening de Kubernetes

**Prova que:** entende contêiner do ponto de vista de segurança, não só de deploy.
**Tempo:** 15–20h · **Precisa de:** um cluster local (kind ou minikube) e 8 GB de RAM

**Passos:**
1. Suba o [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) localmente e explore cada cenário.
2. Anote o que cada cenário quebra: fuga de contêiner, segredo exposto, RBAC frouxo, rede chapada.
3. Endureça: NetworkPolicy, Pod Security Admission, RBAC mínimo, sem contêiner privilegiado.
4. **Refaça cada ataque** e mostre onde ele para agora.
5. Varra as imagens com [Trivy](https://github.com/aquasecurity/trivy) e coloque isso no pipeline.

**Entregável:** manifestos de hardening e a evidência antes/depois de cada cenário.
**Pronto quando:** cada controle que você aplicou está ligado ao ataque específico que ele impede.
**Armadilha:** colar um YAML de hardening pronto da internet. Sem o antes/depois, você não sabe — nem prova — o que ele bloqueou.
**Apoio:** [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) · [Trivy](https://github.com/aquasecurity/trivy) · [kube-bench](https://github.com/aquasecurity/kube-bench)

---

[← Voltar ao índice](../README.md)
