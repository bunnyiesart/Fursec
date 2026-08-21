# 🧠 Método de Estudo

[⬅️ Voltar ao índice](../README.md)

---

Não é opinião. É o que a pesquisa de aprendizagem mostra:

| Método | Retenção aproximada |
|---|---|
| Ler/assistir passivamente | ~29% |
| **Active recall** (se testar sem olhar) | ~57% |
| Active recall + spaced repetition | até **70% melhor** que método passivo |

**Tradução prática:** assistir vídeo de curso é a parte *menos* importante do seu estudo. Sério. O vídeo é o começo, não o fim.

## O método das 3 camadas

Todo tópico que você estudar passa por três camadas. Se pular alguma, você esquece.

```
CAMADA 1 — APRENDER      (30% do tempo)  → vídeo, leitura, curso
CAMADA 2 — FAZER         (50% do tempo)  → lab, CTF, quebrar e consertar
CAMADA 3 — DOCUMENTAR    (20% do tempo)  → escrever o que aprendeu
```

A camada 3 é a que quase todo mundo pula — e é a que mais ensina. Escrever força você a descobrir o que **não** entendeu. Bônus: vira portfólio automaticamente.

> **Regra de ouro:** se você não consegue explicar por escrito, você não aprendeu. Você reconheceu.

## Spaced repetition (Anki) — configuração para segurança

Anki é obrigatório para conteúdo de certificação (portas, protocolos, siglas, frameworks, comandos).

**Setup recomendado:**

| Parâmetro | Valor | Por quê |
|---|---|---|
| Novos cards por dia | **20–30 máximo** | Mais que isso vira dívida impagável em 2 semanas |
| Horário da revisão | **Antes** do conteúdo novo | Cérebro mais fresco |
| Primeira revisão | 24h após aprender | Corta a queda da curva do esquecimento |
| Segunda revisão | 3 dias depois | Consolida no curto prazo |
| Duração da sessão | 15–20 min | Se passar disso, você fez cards demais |

**O que vira card (e o que NÃO vira):**

✅ Vira card: portas (22=SSH), siglas (CIA, AAA), fases do ATT&CK, flags de comando (`nmap -sV`), definições de controle NIST, códigos HTTP, tipos de ataque.
❌ NÃO vira card: conceitos que exigem raciocínio ("como funciona um ataque de pass-the-hash") — isso vai para lab e writeup, não para flashcard.

**Dica:** crie os cards **você mesmo** enquanto estuda. Deck pronto baixado da internet tem ~1/3 da eficácia, porque o ato de formular a pergunta já é aprendizado.

## Sistema de notas

Use um só lugar. Recomendação: **Obsidian** (grátis, local, markdown, funciona offline).

Estrutura sugerida:

```
📁 vault/
├── 00-inbox/           ← joga tudo aqui primeiro, organiza depois
├── 01-fundamentos/     ← redes, linux, windows, cripto
├── 02-blue-team/
├── 03-red-team/
├── 04-cloud/
├── 05-grc/
├── 06-labs/            ← 1 nota por lab/CTF resolvido
├── 07-writeups/        ← versão pública, vira portfólio
├── 08-comandos/        ← seu cheatsheet pessoal (o mais usado de todos)
└── 99-carreira/        ← vagas, contatos, currículo
```

**A nota mais valiosa que você vai ter:** `08-comandos/`. Todo comando que você usou e funcionou, cole ali com uma linha de contexto. Em 6 meses isso vale mais que qualquer cheatsheet da internet, porque é do *seu* jeito de trabalhar.

## Ritmo semanal

Independente de quantas horas você tem:

| Fatia | % do tempo | O que é |
|---|---|---|
| Conteúdo novo | 30% | Curso, vídeo, livro |
| Mão na massa | 50% | Lab, CTF, home lab |
| Documentação | 15% | Notas, writeup, Anki |
| Comunidade/notícias | 5% | Newsletter, Discord, LinkedIn |

**Consistência > intensidade.** 5h/semana toda semana bate 20h numa semana e zero nas três seguintes. O cérebro consolida no intervalo, não no esforço.

## As 7 armadilhas (todas comuns, todas evitáveis)

| Armadilha | Sintoma | Antídoto |
|---|---|---|
| **Tutorial hell** | Você assiste, entende tudo, e não consegue fazer sozinho | Sempre refazer o lab do zero, sem o vídeo, 24h depois |
| **Colecionador de certificados** | 8 certificados, 0 projetos, 0 entrevistas | 1 projeto documentado > 3 certificados básicos |
| **Paralisia de trilha** | 3 meses escolhendo entre blue e red | Escolha qualquer uma. Os fundamentos são 70% iguais |
| **Ferramenta como muleta** | Sabe rodar o Nmap, não sabe o que é um SYN | Sempre pergunte "o que essa ferramenta está fazendo por baixo?" |
| **Anotação passiva** | Notas lindas, memória zero | Feche o material e escreva de memória. Depois confira |
| **Comparação com sênior** | "Nunca vou saber tudo isso" | Ninguém sabe. A área é grande demais. Compare com você de 3 meses atrás |
| **Burnout de 20h/semana** | 6 semanas ótimas, depois 2 meses parado | Planeje 70% da sua capacidade máxima. Sobra folga para a vida |

## Como estudar para prova de certificação

1. **Cobertura primeiro** — assista/leia o material completo uma vez, rápido, sem tentar decorar.
2. **Anki durante** — crie cards a partir da segunda passada.
3. **Simulados como diagnóstico, não como treino** — faça um simulado, e para cada erro, volte ao conteúdo. Errar e só olhar a resposta não ensina nada.
4. **Gatilho de marcar a prova:** acerto consistente de **85%+** em simulados que você nunca viu antes.
5. **Última semana:** só revisão de Anki + 2 simulados completos cronometrados. Nada de conteúdo novo.

## Como estudar um lab / CTF (o loop correto)

```
1. Tente sozinho          → mínimo 30–45 min antes de olhar dica
2. Travou? Dica pequena   → nunca pule direto para o writeup completo
3. Resolveu               → ANOTE cada comando e por que funcionou
4. Refaça do zero         → no dia seguinte, sem consultar nada
5. Escreva o writeup      → explicando para alguém que não sabe nada
6. Card no Anki           → só as partes memorizáveis
```

O passo 4 é o que separa quem aprendeu de quem copiou.

## Regra dos 30 dias

Se você estudar algo e não usar em 30 dias, você perde. Por isso o home lab importa tanto: ele é o lugar onde você **reencontra** os conceitos naturalmente, sem precisar "revisar".

---

---

[⬅️ Voltar ao índice](../README.md)