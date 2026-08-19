# 📝 Como Documentar (o que vira portfólio)

[⬅️ Voltar ao índice](../README.md)

---

```
github.com/seu-usuario/
├── 📌 cybersecurity-portfolio      ← repo FIXADO (pinned). Índice de tudo.
├── homelab-build
├── wazuh-siem-detection-lab
├── sigma-detection-rules
├── pentest-report-vulnhub-kioptrix
├── aws-security-baseline-terraform
└── grc-isms-policy-set
```

O repo `cybersecurity-portfolio` é só um README que aponta para os outros, com **uma frase por projeto explicando o que ele prova**. É a primeira coisa que o recrutador abre.

## Template de README de projeto

```markdown
# [Nome do Projeto]

**O que este projeto prova:** [uma frase — a skill demonstrada]

## Problema
Que situação real isso resolve ou simula.

## Ambiente
- SO / versões / ferramentas
- Diagrama de rede (imagem)

## Metodologia
Passo a passo do que foi feito e **por quê** cada escolha.

## Resultados
Achados, alertas gerados, evidências. Screenshots com dados anonimizados.

## Remediação / Recomendações
O que você faria para corrigir. **Esta seção é a que mais impressiona.**

## Problemas encontrados
O que quebrou e como você resolveu. Mostra raciocínio real, não roteiro.

## O que eu aprendi
Honesto e específico. Inclusive o que você faria diferente.

## Referências
```

## Template de writeup de CTF/lab

```markdown
# [Máquina/Desafio] — Writeup

**Dificuldade:** | **Plataforma:** | **Data:**

## Resumo executivo
3 linhas: qual foi a falha, qual o impacto, como corrigir.

## Reconhecimento
Comandos + saída relevante (recortada, não colada inteira).

## Exploração
O raciocínio antes do comando. Por que você tentou isso?

## Pós-exploração / escalada
## Correção
Como o administrador teria evitado. **Não pule esta parte.**
## Lições
```

## Checklist antes de publicar

- [ ] Nenhum IP, hostname, credencial ou nome real de terceiro
- [ ] Nenhum payload funcional contra sistema real
- [ ] Screenshots com dados sensíveis borrados
- [ ] README explica em 1 frase o que o projeto prova
- [ ] Tem seção de remediação
- [ ] Alguém de fora da área entenderia o resumo executivo
- [ ] Commits com mensagens decentes (o recrutador técnico olha)

## Ritmo de publicação

| Fase do roadmap | Meta de projetos |
|---|---|
| Fim da Fase 1 | 2 projetos (P1 + um de código) |
| Fim da Fase 2 | 4–5 projetos (2+ da sua trilha) |
| Fim da Fase 3 | 8–10 projetos + 6 writeups |
| Fase 4 | 1 contribuição open source aceita |

> **Meta realista:** 1 projeto documentado a cada 3–4 semanas. Em um ano você tem 12–15 — mais que a maioria dos candidatos júnior tem.

---

---

[⬅️ Voltar ao índice](../README.md)