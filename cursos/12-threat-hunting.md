# Caça a ameaças e engenharia de detecção

[← Voltar ao índice](../README.md)

---

Caça é disciplina própria, não apêndice de SOC: em vez de esperar o alerta, você formula hipótese e vai procurar. Detecção como código é o que transforma o achado em regra que não se perde.

Pré-requisito honesto: faça [`02-blue-team.md`](./02-blue-team.md) antes. Sem saber o que é normal, não há como caçar o anormal.

<sub>🇧🇷 português · 🇺🇸 inglês · 🆓 gratuito · 💸 pago · 🎓 emite certificado · 🧪 prático · ⭐ prioridade alta · *parcial / tier / audit / Financial Aid* = gratuito com ressalva</sub>

<sub>Esta página usa uma quinta coluna, **Nota**, que os arquivos 00–07 não têm. É
deliberado: são áreas de nicho em que o nome do item não diz o que ele é. O
formato segue o de [`labs/`](../labs/), que já usa nota.</sub>

| Curso / material | Fonte | Lang | Tags | Nota |
|---|---|---|---|---|
| ⭐ Foundations of Threat Hunting | [academy.picussecurity.com](https://academy.picussecurity.com/course/foundations-of-threat-hunting-training-free-course-certification) | 🇺🇸 | 🆓 🎓 | Ponto de partida conceitual: define caça, os quatro passos do ciclo de hunting e os frameworks, com exemplos reais e certificado no fim |
| ⭐ SC-200 — Executar a caça de ameaças no Microsoft Sentinel | [learn.microsoft.com](https://learn.microsoft.com/pt-br/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) | 🇧🇷🇺🇸 | 🆓 🧪 | A única trilha de caça que achei em português: formular hipótese, consultar, usar marcadores e stream ao vivo no Sentinel |
| Adversary Emulation Library | [github.com](https://github.com/center-for-threat-informed-defense/adversary_emulation_library) | 🇺🇸 | 🆓 🧪 | Planos de emulação completos por grupo de adversário (APT3, FIN6, menuPass), o insumo que falta para o exercício purple team ter roteiro |
| Detection Management — From Entropy to Evidence | [academy.attackiq.com](https://www.academy.attackiq.com/courses/detection-management-from-entropy-to-evidence) | 🇺🇸 | 🆓 🎓 | Engenharia de detecção baseada em evidência: validar regra, cortar ruído e reportar cobertura real com ATT&CK, Sigma e o 4D score |
| Emulation Planning for Purple Teams | [academy.attackiq.com](https://www.academy.attackiq.com/courses/emulation-planning-for-purple-teams) | 🇺🇸 | 🆓 🎓 | Como planejar a emulação que vira exercício purple team, o passo seguinte ao Foundations of Purple Teaming que já está no catálogo |
| Hunt Evil — baseline de processos do Windows (pôster) | [sans.org](https://www.sans.org/posters/hunt-evil/) | 🇺🇸 | 🆓 | Referência de qual processo do Windows é normal, pai, caminho e usuário esperados, o que transforma ruído em outlier caçável |
| Must Learn KQL (livro-curso) | [github.com](https://github.com/rod-trent/MustLearnKQL) | 🇺🇸 | 🆓 🧪 | Vinte e uma partes de KQL do zero até escrever a primeira regra de análise no Sentinel, com datasets e app interativo |
| PEAK Threat Hunting Framework | [splunk.com](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html) | 🇺🇸 | 🆓 | Framework que separa caça baseada em hipótese, caça baseada em baseline e caça exploratória por modelo, e fecha o ciclo entregando detecção |
| SC-200 — Criar consultas para o Microsoft Sentinel usando KQL | [learn.microsoft.com](https://learn.microsoft.com/pt-br/training/paths/sc-200-utilize-kql-for-azure-sentinel/) | 🇧🇷🇺🇸 | 🆓 🧪 | A linguagem de consulta é o alicerce da caça em SIEM, e aqui está em português com exercícios interativos |
| Security Datasets (ex-Mordor) — datasets para treinar caça | [github.com](https://github.com/OTRF/Security-Datasets) | 🇺🇸 | 🆓 🧪 | Telemetria pré-gravada de ataques reais para caçar sem precisar montar laboratório nem atacar nada |
| TaHiTI — metodologia de caça integrada a threat intelligence (whitepaper) | [betaalvereniging.nl](https://www.betaalvereniging.nl/wp-content/uploads/2026/03/TaHiTI-Threat-Hunting-Methodology-whitepaper.pdf) | 🇺🇸 | 🆓 | Metodologia de caça em três fases com backlog de hipóteses e métricas, a resposta para quem já sabe consultar mas não sabe o que caçar |
| Threat Hunter Playbook | [threathunterplaybook.com](https://threathunterplaybook.com/) | 🇺🇸 | 🆓 🧪 | Caças documentadas como notebooks executáveis: hipótese, consulta, lógica de detecção e validação, o modelo de detection-as-code |

---

[← Voltar ao índice](../README.md)
