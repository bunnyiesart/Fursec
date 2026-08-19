# ☁️ Projetos Cloud Security (P20–P24)

[⬅️ Voltar ao índice](../README.md)

---

### P20 — Baseline seguro em Terraform
**Prova que:** security as code — a skill mais pedida em cloud hoje.
**Tempo:** 15–25h
**Entregável:** módulo Terraform de VPC/conta segura, escaneado por [Checkov](https://github.com/bridgecrewio/checkov) e [tfsec/Trivy](https://github.com/aquasecurity/trivy), com pipeline que bloqueia deploy inseguro.

### P21 — flaws.cloud com plano de remediação
**Prova que:** ataca *e* corrige.
**Tempo:** 10–15h
**Diferencial:** todo mundo publica o writeup do ataque. Publique também a política IAM corrigida de cada nível.

### P22 — Detecção em CloudTrail
**Prova que:** blue team + cloud, combinação rara e bem paga.
**Tempo:** 12–18h
**Entregável:** alertas para ações IAM suspeitas (criação de chave, escalada de privilégio, desligamento de log), testados contra ataques reais do [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat).

### P23 — Auditoria multi-cloud automatizada
**Tempo:** 10–15h · **Repos:** [Prowler](https://github.com/prowler-cloud/prowler) · [ScoutSuite](https://github.com/nccgroup/ScoutSuite) · [CloudFox](https://github.com/BishopFox/cloudfox)
**Entregável:** relatório executivo de postura da sua própria conta free-tier, com plano de correção priorizado por risco.

### P24 — Hardening de Kubernetes
**Tempo:** 15–20h · **Repos:** [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) · [Trivy](https://github.com/aquasecurity/trivy)
**Entregável:** cluster explorado, depois endurecido com NetworkPolicies, PSA, RBAC mínimo — com evidência antes/depois.

---

---

[⬅️ Voltar ao índice](../README.md)