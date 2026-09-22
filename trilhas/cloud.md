# Cloud Security

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)

---

Segurança de AWS, Azure, GCP e Kubernetes. É a trilha com melhor relação entre demanda e quantidade de gente qualificada.

## O que a função faz de fato

O trabalho quase nunca é "hackear a nuvem". É:

- Revisar permissão de identidade — **o IAM é onde os incidentes de nuvem realmente começam**
- Achar recurso exposto: bucket público, banco sem rede privada, painel sem autenticação
- Escrever infraestrutura como código com baseline seguro, e impedir que o inseguro passe no pipeline
- Configurar e ler log de plano de controle: CloudTrail, Azure Activity Log, GCP Audit Logs
- Responder quando uma credencial vaza, o que é o incidente mais comum

### Esta trilha é para você se

Você já mexe com infraestrutura, gosta de automatizar e não se incomoda em ler documentação longa. Aqui documentação de fornecedor é a fonte primária.

### Não é, se

Você não tem paciência com console de nuvem e com nome de serviço mudando. E atenção ao custo: é a única trilha em que **estudar pode gerar fatura** se você esquecer um recurso ligado.

---

## Pré-requisito

Fases 0 e 1 do [roadmap](../ROADMAP.md), ~180h. Além disso, aqui é obrigatório:

- **Rede** de verdade: VPC, sub-rede, roteamento, grupo de segurança
- **Linux e contêiner**, porque quase tudo roda em contêiner
- **Um pouco de IaC**, Terraform de preferência

Vir de [Blue Team](./blue-team.md) ajuda muito: você já sabe ler log, e aqui o log só muda de lugar.

---

## O caminho, em ordem

Fase 2C do roadmap, ~120h.

| # | O que fazer | Onde |
|---|---|---|
| 1 | Fundamentos de um provedor — **escolha UM** | [`cursos/04-cloud-security.md`](../cursos/04-cloud-security.md) |
| 2 | IAM a fundo, antes de qualquer outra coisa | Documentação do provedor + lab |
| 3 | Quebrar ambiente vulnerável de propósito | [flaws.cloud](http://flaws.cloud/), [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) |
| 4 | Baseline seguro em Terraform, com varredura no pipeline | [Checkov](https://github.com/bridgecrewio/checkov), [tfsec](https://github.com/aquasecurity/tfsec) |
| 5 | Auditoria automatizada da sua própria conta | [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite) |
| 6 | Kubernetes: RBAC, política, hardening | [kube-bench](https://github.com/aquasecurity/kube-bench), [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) |

**Escolha um provedor e vá fundo.** Saber 30% de AWS, Azure e GCP é pior que saber 90% de um. Os conceitos transferem; os nomes dos serviços, não.

Ferramentas completas: [`repositorios/ferramentas-appsec-cloud.md`](../repositorios/ferramentas-appsec-cloud.md). Labs: [`repositorios/labs-vulneraveis.md`](../repositorios/labs-vulneraveis.md).

> **Sobre custo:** use sempre a camada gratuita, ligue alerta de orçamento **no primeiro dia**, e destrua o que criou com `terraform destroy`. Recurso esquecido ligado é a forma mais comum de tomar susto na fatura.

---

## Os projetos desta trilha

P20–P24, em [`projetos/04-cloud.md`](../projetos/04-cloud.md).

| Projeto | Por que importa |
|---|---|
| [P20 — Baseline seguro em Terraform](../projetos/04-cloud.md#p20--baseline-seguro-em-terraform) | Mostra que você previne, não só encontra |
| [P21 — flaws.cloud com plano de remediação](../projetos/04-cloud.md#p21--flawscloud-com-plano-de-remediação) | O plano de remediação é o que diferencia do writeup comum |
| [P22 — Detecção em CloudTrail](../projetos/04-cloud.md#p22--detecção-em-cloudtrail) | Junta nuvem com a habilidade de Blue Team |
| [P24 — Hardening de Kubernetes](../projetos/04-cloud.md#p24--hardening-de-kubernetes) | K8s é onde mais falta gente |

Se fizer só um: **P20**. Infraestrutura como código com controle embutido é exatamente o que a vaga pede.

---

## Ferramentas que você vai usar de verdade

| Categoria | Ferramentas |
|---|---|
| Postura e auditoria | [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite), [CloudSploit](https://github.com/aquasecurity/cloudsploit) |
| IaC | Terraform, [Checkov](https://github.com/bridgecrewio/checkov), [tfsec](https://github.com/aquasecurity/tfsec), [Terrascan](https://github.com/tenable/terrascan) |
| Contêiner e imagem | [Trivy](https://github.com/aquasecurity/trivy), [Grype](https://github.com/anchore/grype), [Docker Bench](https://github.com/docker/docker-bench-security) |
| Kubernetes | [kube-bench](https://github.com/aquasecurity/kube-bench), [kubescape](https://github.com/kubescape/kubescape), [Falco](https://github.com/falcosecurity/falco) |
| IAM | [Cloudsplaining](https://github.com/salesforce/cloudsplaining), [PMapper](https://github.com/nccgroup/PMapper), IAM Access Analyzer |
| Ofensivo | [Pacu](https://github.com/RhinoSecurityLabs/pacu), [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) |
| Enquadramento | [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) do provedor |

---

## Certificações

- **Gratuito:** os badges do tier gratuito de [AWS Skill Builder](https://skillbuilder.aws/) e [Microsoft Learn](https://learn.microsoft.com/training/), e as conquistas do [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- **Primeiro exame que vale:** o de **associate** do seu provedor (AWS Solutions Architect Associate, AZ-104 ou equivalente) — porque contexto de nuvem vem antes de segurança de nuvem
- **Depois:** a de especialidade em segurança (AWS Security Specialty, AZ-500, GCP Professional Cloud Security Engineer)

Aqui certificação pesa mais que na média, porque os fornecedores treinam o mercado a olhar para elas.

---

## Teste de saída

Você terminou esta trilha quando consegue, **sem consultar nada**:

- [ ] Explicar a diferença entre política de identidade e política de recurso, com exemplo
- [ ] Achar todo recurso exposto publicamente numa conta, e dizer como achou
- [ ] Escrever política IAM de menor privilégio para um caso concreto
- [ ] Explicar como uma credencial vazada vira comprometimento de conta, passo a passo
- [ ] Dizer o que CloudTrail registra e o que **não** registra
- [ ] Subir um cluster Kubernetes minimamente endurecido e justificar cada controle
- [ ] Rodar Prowler e explicar por que três achados dele são falso positivo no seu contexto

---

## O que perguntam em entrevista

- "Como você garante menor privilégio na prática?" — quer ver processo, não teoria
- "Um bucket está público. Como você descobre e como impede que aconteça de novo?" — detecção **e** prevenção
- "O que você monitora no plano de controle?" — CloudTrail, criação de usuário, mudança de política
- "Como você trata segredo em pipeline?" — cofre, rotação, nunca no repositório
- "Diferença entre segurança **da** nuvem e segurança **na** nuvem" — modelo de responsabilidade compartilhada

---

## Próximos passos

- **[AppSec / DevSecOps](./appsec.md)** — o pipeline é o vizinho natural
- **[Blue Team](./blue-team.md)** — se você quer aprofundar detecção sobre o log que já sabe coletar

---

[← Voltar às trilhas](./README.md) · [← Voltar ao índice](../README.md)
