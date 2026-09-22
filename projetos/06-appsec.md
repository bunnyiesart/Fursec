# Projetos AppSec / DevSecOps (P31–P33)

[← Voltar ao índice](../README.md)

---

Três projetos de segurança de aplicação. Da trilha [AppSec / DevSecOps](../trilhas/appsec.md), fase 2 em diante.

São poucos porque nesta área **profundidade vale mais que quantidade**: os três juntos cobrem o ciclo inteiro — pensar a ameaça antes de codar, barrar no pipeline, corrigir no código de outra pessoa.

**Se fizer só um, faça o [P33](#p33--code-review-de-segurança-com-pr-real).** É o único do catálogo cuja validação vem de fora, de um mantenedor que não te conhece.

> Leia [`00-regras.md`](./00-regras.md) antes de começar qualquer um. Analisar código aberto é legítimo; testar a instância **hospedada** de um projeto sem autorização não é. Rode tudo na sua cópia local.

---

### P31 — Threat model de um projeto open source

**Prova que:** você pensa em segurança antes do código existir, que é onde ela custa barato.
**Tempo:** 10–15h · **Precisa de:** um projeto real, de porte médio, que você consiga entender

**Passos:**
1. Escolha um projeto de tamanho médio — grande demais não termina, pequeno demais não ensina.
2. Desenhe o diagrama de fluxo de dados e **marque as fronteiras de confiança**. É o passo que define tudo o resto.
3. Aplique STRIDE em cada fronteira, não no sistema inteiro de uma vez.
4. Priorize as ameaças por impacto e por esforço de exploração.
5. Proponha mitigação concreta para as principais, e **ofereça ao mantenedor** — muitos aceitam de bom grado.

**Entregável:** diagrama de fluxo, ameaças priorizadas por STRIDE e as mitigações propostas.
**Pronto quando:** você aponta, no diagrama, onde o dado atravessa fronteira de confiança sem validação.
**Armadilha:** listar ameaça genérica que serve para qualquer software. Ameaça útil aponta componente, fluxo e o que o atacante ganha.
**Apoio:** [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) · [STRIDE](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)

---

### P32 — Pipeline CI/CD com segurança embutida

**Prova que:** você automatiza segurança onde ela precisa estar — no caminho do deploy.
**Tempo:** 12–20h · **Precisa de:** um repositório seu com GitHub Actions

**Passos:**
1. Ponha SAST com [Semgrep](https://github.com/semgrep/semgrep), SCA com [Trivy](https://github.com/aquasecurity/trivy) e varredura de segredo com [Gitleaks](https://github.com/gitleaks/gitleaks).
2. Defina a política de bloqueio por severidade — e escreva por que aquele limiar, não outro.
3. Trabalhe o falso positivo: sem isso, o time desliga a verificação na segunda semana.
4. Faça o resultado aparecer **no PR**, não em uma aba de log que ninguém abre.
5. Meça quanto tempo o pipeline ganhou de duração. Se passar de poucos minutos, ninguém espera.

**Entregável:** o pipeline funcionando, a política de limiar documentada e o tempo medido.
**Pronto quando:** um PR com vulnerabilidade real é barrado, e um PR limpo passa sem ruído.
**Armadilha:** bloquear tudo que é HIGH desde o primeiro dia. O time contorna a verificação, e você perde o controle inteiro em vez de ganhar parte dele.
**Apoio:** [Semgrep](https://github.com/semgrep/semgrep) · [Trivy](https://github.com/aquasecurity/trivy) · [Gitleaks](https://github.com/gitleaks/gitleaks) · [`cursos/06-appsec-devsecops.md`](../cursos/06-appsec-devsecops.md)

---

### P33 — Code review de segurança com PR real

**Prova que:** acha falha em código de verdade e sabe reportar. **Um PR de segurança aceito é currículo puro.**
**Tempo:** 8–15h · **Precisa de:** o [P31](#p31--threat-model-de-um-projeto-open-source) ou o [P32](#p32--pipeline-cicd-com-segurança-embutida) feito antes

**Passos:**
1. Escolha um projeto ativo, com mantenedor que responde, e leia o `SECURITY.md` dele antes de tudo.
2. Revise à mão as partes que importam: autenticação, autorização, tratamento de entrada, desserialização, upload de arquivo.
3. Confirme o achado na **sua cópia local**, com prova de conceito — nunca na instância hospedada de terceiro.
4. Reporte pelo canal privado que o projeto indica, e **espere a resposta** antes de publicar qualquer coisa.
5. Mande o PR de correção, com teste que falha antes e passa depois.

**Entregável:** o report responsável, o PR de correção e o writeup depois do disclosure autorizado.
**Pronto quando:** o mantenedor respondeu. Recusa também conta, desde que você entenda o motivo dela.
**Armadilha:** abrir issue pública com o detalhe da falha. Isso expõe todos os usuários do projeto antes de existir correção, e queima a sua reputação com o mantenedor.
**Apoio:** [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/) · [Semgrep](https://github.com/semgrep/semgrep) para achar o ponto, revisão à mão para confirmar

---

[← Voltar ao índice](../README.md)
