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

## Os templates

Não recrie do zero — copie o arquivo pronto:

| Template | Quando usar | O que ele força você a preencher |
|---|---|---|
| [`README-projeto.md`](../projetos/templates/README-projeto.md) | Todo projeto que você publicar | Problema, ambiente, metodologia, resultados, **remediação**, o que quebrou, o que aprendeu |
| [`writeup-ctf.md`](../projetos/templates/writeup-ctf.md) | Cada máquina / CTF resolvido | Resumo executivo, recon, exploração, **correção**, lições |
| [`relatorio-pentest.md`](../projetos/templates/relatorio-pentest.md) | Quando quiser o formato de consultoria | Sumário executivo, escopo e regras de engajamento, achados com severidade, apêndices |

As duas seções que quase todo mundo pula — e que são exatamente as que impressionam — são **remediação** ("o que eu faria para corrigir") e **problemas encontrados** ("o que quebrou e como resolvi"). A primeira mostra que você pensa como defensor; a segunda mostra raciocínio real em vez de roteiro decorado.

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